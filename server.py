import os
import re
import tempfile
import subprocess

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    file_field = 'file'
    output_extension = '.gltf'
    
    def get_file_data(self):
        files = self.request.files.get(self.file_field, None)
        return files[0].filename, files[0].body, files[0].content_type
    
    def change_extension(self, filename):
        return re.sub('\.[\w]+$', self.output_extension, filename)
    
    def convert_file(self, in_name, out_name):
        out_name = os.path.join(tempfile.gettempdir(), out_name)
        subprocess.call(['collada2gltf', '-f', in_name, '-o', out_name])
        return out_name
    
    def read_file(self, file_path):
        with open(file_path, 'rb') as f:
            content = f.read()
        return content
    
    def write_file(self, content):
        temp_file = tempfile.NamedTemporaryFile()
        with open(temp_file.name, 'w+b') as f:
            f.write(content)
            f.flush()
        return temp_file
    
    def post(self, *args, **kwargs):
        if not self.request.files:
            raise tornado.web.HTTPError(400, reason='Bad request')
        filename, file_content, _ = self.get_file_data()
        
        in_file = self.write_file(file_content)
        out_file = self.convert_file(in_file.name, self.change_extension(filename))
        
        response_content = self.read_file(out_file)
        
        self.set_header('Content-Type', 'application/octet-stream')
        self.write(response_content)
    
def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(80)
    tornado.ioloop.IOLoop.current().start()
