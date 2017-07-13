# artillery
Dockerized @shoreditch-ops's artillery, with @matplotlib load charts

## Usage

Build

`./build.sh`

Stress a service

`./run.sh artillery run --target <my_target> /data/<my_artillery_conf>.yaml --output /data/<my_artillery_output>.json`

Draw the plots

`./run.sh python /bin/process.py -i <my_artillery_output> [-i <my_other_artillery_output>] [-o <my_plot>.png]`

