# diagramascode
Drawing diagram as code


# Setup
## Virtual Environment
- create a python virtual enviroment
- activate pthon enviroment
- install the requirements

```shell
python -m venv venv_diagramascode
venv_diagramascode\Scripts\activate
pip install -r requirements.txt
```

## Docker dev container
	"name": "Alpine",
	// Or use a Dockerfile or Docker Compose file. More info: https://containers.dev/guide/dockerfile
	"image": "mcr.microsoft.com/devcontainers/base:alpine-3.17"

```shell
# within alphine linux container
sudo apk add graphviz
sudo apk add py3-pip
sudo apk add terminus-font font-inconsolata font-dejavu font-noto font-noto-cjk font-awesome font-noto-extra

# create python virtual environment and install requirements

```

# how to run
Examples given in https://diagrams.mingrammer.com/docs/getting-started/examples

```shell
python diagram.py
```