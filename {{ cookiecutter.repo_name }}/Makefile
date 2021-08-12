
PROJECT_NAME = {{ cookiecutter.repo_name }}

ifndef DS_VOLUME
	DS_VOLUME=/scratch
endif

ifndef NB_PORT
	NB_PORT=8888
endif

ifndef MLF_PORT
	MLF_PORT=5000
endif

help:
	@echo "build -- builds the docker image"

build:
	docker build -t $(PROJECT_NAME) .
	chmod 775 ./download.sh
	./download.sh

dockershell:
	docker run --rm --name $(PROJECT_NAME) --gpus all -p 9197:9197 \
	-v $(shell pwd):/iqf -v $(DS_VOLUME):/ds_volume \
	-it $(PROJECT_NAME)

notebookshell:
	docker run --gpus all --privileged -itd --rm -p ${NB_PORT}:${NB_PORT} \
	-v $(shell pwd):/iqf -v $(DS_VOLUME):/ds_volume \
	$(PROJECT_NAME) \
	jupyter notebook \
	--NotebookApp.token='IQF' \
	--no-browser \
	--ip=0.0.0.0 \
	--allow-root \
	--port=${NB_PORT}

mlflow:
	docker run --privileged -itd --rm -p ${MLF_PORT}:${MLF_PORT} \
	-v $(shell pwd):/iqf -v $(DS_VOLUME):/ds_volume \
	$(PROJECT_NAME) \
	mlflow ui --host 0.0.0.0:$(MLF_PORT)
