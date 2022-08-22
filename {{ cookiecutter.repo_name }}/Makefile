PROJ_NAME={{ cookiecutter.repo_name }}
CONTAINER_NAME="${PROJ_NAME}-${USER}"


ifndef DS_VOLUME
	DS_VOLUME=/scratch
endif

ifndef GEN_PORT
	GEN_PORT=9197
endif

ifndef NB_PORT
	NB_PORT=8888
endif

ifndef MLF_PORT
	MLF_PORT=5000
endif

help:
	@echo "build -- builds the docker image"
	@echo "container -- runs a container in the background"
	@echo "nb -- launches a notebook server"
	@echo "nbstop -- Stops the notebook server"
	@echo "mlf -- launches an mlflow server"
	@echo "execsh -- raises an interactive shell docker from a running container"
	@echo "test -- run tests"
	@echo "stop -- Stop the docker container and everything that is running within it"
	@echo "downloads course materials"

build:
	docker build -t $(PROJ_NAME) --no-cache .
	chmod 775 ./download.sh
	./download.sh

container:
	docker run --rm -itd --name $(CONTAINER_NAME) --gpus all --privileged \
	-v $(DS_VOLUME):/ds_volume \
	-p $(GEN_PORT):$(GEN_PORT) \
	-p $(NB_PORT):$(NB_PORT) \
	-p $(MLF_PORT):$(MLF_PORT) \
	-v $(shell pwd):$(shell pwd) \
	-w $(shell pwd) \
	${PROJ_NAME} /bin/bash

nb:
	docker exec -d --privileged $(CONTAINER_NAME) \
	jupyter lab \
	--NotebookApp.token='iqf' \
	--no-browser \
	--ip=0.0.0.0 \
	--allow-root \
	--port=$(NB_PORT)

nbstop:
	docker exec -d --privileged $(CONTAINER_NAME) \
	jupyter lab stop ${NB_PORT}

mlf:
	docker exec -d $(CONTAINER_NAME) mlflow ui --host 0.0.0.0:$(MLF_PORT)

execsh:
	docker exec -it ${CONTAINER_NAME} /bin/bash

test:
	docker exec -it -w $(shell pwd) ${CONTAINER_NAME} pip3 install pytest flake8
	docker exec -it -w $(shell pwd) ${CONTAINER_NAME} pytest tests/

stop:
	docker stop $(CONTAINER_NAME)

course:
	wget https://image-quality-framework.s3.eu-west-1.amazonaws.com/iq-tool-box/datasets/course.zip
	chmod 775 ./course.zip && unzip -o ./course.zip && rm ./course.zip
