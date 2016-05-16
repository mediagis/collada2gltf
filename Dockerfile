FROM python:2.7
MAINTAINER gneroks@gmail.com

WORKDIR /app

ADD ./collada_converter .

RUN apt-get update && apt-get install -y --no-install-recommends cmake \
	nginx \
	&& rm -r /etc/nginx/sites-enabled \
	&& rm -rf /var/lib/apt/lists/* \
	&& git clone --recurse-submodules https://github.com/KhronosGroup/glTF.git \
	&& cd glTF/COLLADA2GLTF \
	&& git checkout v1.0-draft2 \
	&& cmake . \
	&& make install \
	&& cp ./bin/collada2gltf /usr/local/bin/ \
	&& rm -rf ./glTF/ \
	&& pip install tornado

COPY ./nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD python ./server.py

CMD ["nginx", "-g", "daemon off;"]
