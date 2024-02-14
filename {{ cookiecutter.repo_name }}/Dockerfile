FROM nvidia/cuda:11.0.3-cudnn8-runtime-ubuntu20.04

# This prevents interactive region dialoge
ENV DEBIAN_FRONTEND=noninteractive
ENV LD_LIBRARY_PATH=/usr/local/nvidia/lib64:$LD_LIBRARY_PATH
ENV PATH=/usr/local/nvidia/bin:$PATH
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# https://developer.nvidia.com/blog/updating-the-cuda-linux-gpg-repository-key/
RUN apt-key del 7fa2af80 && \
    rm /etc/apt/sources.list.d/cuda.list && \
    rm /etc/apt/sources.list.d/nvidia-ml.list && \
    apt-get update -y && apt-get install wget -y && \
    wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/$(uname -m)/cuda-keyring_1.0-1_all.deb && \
    dpkg -i cuda-keyring_1.0-1_all.deb && \
    apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/7fa2af80.pub && \
    apt-get update -y

RUN apt update && apt install -y --no-install-recommends software-properties-common \
    libsm6 libxext6 libxrender-dev curl \
    && rm -rf /var/lib/apt/lists/*
    
RUN echo "**** Installing Python ****" && \
    add-apt-repository -y ppa:deadsnakes/ppa &&  \
    apt install -y build-essential python3.6 python3.6-dev python3-pip python3.6-distutils python3-apt && \
    curl -O https://bootstrap.pypa.io/pip/3.6/get-pip.py && \
    python3.6 get-pip.py && \
    rm -rf /var/lib/apt/lists/*

RUN apt update
RUN apt install -y wget unzip git
RUN apt install -y ffmpeg libglib2.0-0 libgl1-mesa-glx

RUN echo 'alias pip=pip3.6' >> ~/.bashrc
RUN echo 'alias pip3=pip3.6' >> ~/.bashrc

RUN ln -sf /bin/python3.6 /bin/python
RUN ln -sf /bin/python3.6 /bin/python3

RUN pip3 install pip --upgrade

WORKDIR /iqf
COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

# Install IQF in the project# git clone https://github.com/satellogic/iquaflow.git && \
RUN pip install iquaflow

# Force a suitable torch version given your hardware
# RUN pip3 install torch==1.7.1+cu110 torchvision==0.8.2+cu110 -f https://download.pytorch.org/whl/torch_stable.html

RUN pip3 install notebook
RUN pip3 install jupyterlab

CMD ["/bin/bash"]
