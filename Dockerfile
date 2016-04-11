FROM python:2.7
MAINTAINER gneroks@gmail.com

RUN pip install tornado

ADD server.py /server.py

RUN apt-get update && apt-get install -y --no-install-recommends cmake \
	&& rm -rf /var/lib/apt/lists/* \
	&& git clone --recurse-submodules https://github.com/KhronosGroup/glTF.git \
	&& cd glTF/COLLADA2GLTF \
	&& git checkout 1.0-final \
	&& cmake . \
	&& make install \
	&& cp ./bin/collada2gltf /usr/local/bin/ \
	&& rm -rf /glTF/

EXPOSE 80

CMD python /server.py
