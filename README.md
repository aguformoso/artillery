# artillery
Dockerized @shoreditch-ops's artillery, with @matplotlib load charts

## Requirements

The usage of [multi-stage builds](https://docs.docker.com/engine/userguide/eng-image/multistage-build/#use-multi-stage-builds) requires running docker >= 17.05.

## Usage

Build

`./build.sh`

Stress a service

`./stress /data/<my_artillery_conf>.yaml --target <my_target>  --output /data/<my_artillery_output>.json`

Draw the plots

`./draw.sh -i <my_artillery_output> [-i <my_other_artillery_output>] [-o <my_plot>.png]`

## Example (Docker for Mac)

`./build.sh`

Stressing my service at port `8080`

`$(ipconfig getifaddr en0)` will get you your host's address

`./stress /data/artillery.conf.yaml --target http://$(ipconfig getifaddr en0):8080 --output /data/service1.json`

`./stress /data/artillery.conf.yaml --target http://$(ipconfig getifaddr en0):8080 --output /data/service2.json`

`./draw.sh -i service1.json -i service2.json -o my_plot.png`

