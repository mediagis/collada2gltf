# Supported tags and respective `Dockerfile` links #

- [`v1.0-draft2`, `default` (*/Dockerfile*)](https://bitbucket.org/ololoteam/collada_converter/src/default)

Web service to convert 3D models from COLLADA to glTF using [COLLADA2GLTF](https://github.com/KhronosGroup/glTF). This is analog the [convertmodel](https://cesiumjs.org/convertmodel.html) without 10 Mb file size limit.

![gltf.png](https://github.com/KhronosGroup/glTF/raw/master/specification/figures/gltf.png)

# How to use this image #
## Run a collada2gltf instance ##

```
$ docker run -d winsent/collada2gltf

```
You can test it by visiting http://container-ip:80


## License ##
COLLADA2GLTF [license](https://github.com/KhronosGroup/glTF/blob/v1.0-draft2/LICENSE.md).

# Other GIS containers

* Geoserver on Alpine Linux ([link](https://hub.docker.com/r/winsent/geoserver-alpine/))
* OSM tools ([link](https://hub.docker.com/r/cartography/osmtools/))
* Nominatim ([link](https://hub.docker.com/r/cartography/nominatim-docker/))
* OSRM backend ([link](https://hub.docker.com/r/cartography/osrm-backend-docker/))
* OSRM frontend ([link](https://hub.docker.com/r/cartography/osrm-frontend-docker/))


# User Feedback

## Issues

If you have any problems or questions about this image, please contact me through a [Bitbucket issue](https://bitbucket.org/ololoteam/collada_converter/issues) or email [pipetc@gmail.com](mailto:pipetc@gmail.com).