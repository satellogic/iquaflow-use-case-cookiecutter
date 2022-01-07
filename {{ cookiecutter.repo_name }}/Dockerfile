FROM nvidia/cuda:11.0.3-cudnn8-runtime-ubuntu20.04

ENV DEBIAN_FRONTEND=noninteractive
ENV LD_LIBRARY_PATH=/usr/local/nvidia/lib64:$LD_LIBRARY_PATH
ENV PATH=/usr/local/nvidia/bin:$PATH
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV CONDA_DIR $HOME/miniconda3
ENV PATH=$CONDA_DIR/bin:$PATH

RUN apt-get update && apt-get install -y --no-install-recommends software-properties-common \
    libsm6 libxext6 libxrender-dev curl \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update &&  \
    apt-get install -y \
    curl unzip wget git \
    ffmpeg libsm6 libxext6 libglib2.0-0 libgl1-mesa-glx

RUN echo ". $CONDA_DIR/etc/profile.d/conda.sh" >> ~/.profile
RUN apt update
RUN apt -y install gcc
RUN apt -y install wget 
RUN apt -y install git
RUN apt install libglib2.0-0 -y 
RUN apt install libgl1-mesa-glx -y 
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh 
RUN chmod 775 Miniconda3-latest-Linux-x86_64.sh 
RUN bash Miniconda3-latest-Linux-x86_64.sh -b -p $CONDA_DIR 
RUN rm Miniconda3-latest-Linux-x86_64.sh 
RUN export PATH="$HOME/miniconda3/bin:$PATH" 
RUN conda create -n satellogic python=3.6 -q -y 
RUN conda install -n satellogic pytorch=0.4.0 cuda90 -c pytorch -y 
RUN conda install -n satellogic torchvision -c soumith -y
RUN conda run -n satellogic pip3 install pip --upgrade

WORKDIR /iqf
COPY ./requirements.txt ./requirements.txt

RUN  conda run -n satellogic pip install -r requirements.txt

### Install IQF in the project
RUN conda run -n satellogic pip3 install git+https://gitlab+deploy-token-45:FKSA3HpmgUoxa5RZ69Cf@publicgitlab.satellogic.com/iqf/iq_tool_box-

RUN conda run -n satellogic pip3 install torch==1.7.1+cu110 torchvision==0.8.2+cu110 -f https://download.pytorch.org/whl/torch_stable.html

RUN conda run -n satellogic pip3 install notebook
RUN conda run -n satellogic pip3 install jupyterlab
RUN conda run -n satellogic pip3 install mlflow

CMD ["/bin/bash", "-c", "source activate satellogic && /bin/bash"]


