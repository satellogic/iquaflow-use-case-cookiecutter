FROM nvidia/cuda:11.0.3-cudnn8-runtime-ubuntu20.04

ENV DEBIAN_FRONTEND=noninteractive
ENV LD_LIBRARY_PATH=/usr/local/nvidia/lib64:$LD_LIBRARY_PATH
ENV PATH=/usr/local/nvidia/bin:$PATH
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV CONDA_DIR $HOME/miniconda3
ENV PATH=$CONDA_DIR/bin:$PATH

RUN echo ". $CONDA_DIR/etc/profile.d/conda.sh" >> ~/.profile
RUN apt update 
RUN apt install wget 
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

WORKDIR /iqf
COPY ./requirements.txt ./requirements.txt

RUN  conda run -n satellogic pip install -r requirements.txt

### Install IQF in the project
RUN conda run -n satellogic pip install git+https://gitlab+deploy-token-28:xkxRsx2anp-u3_V4aAK9@publicgitlab.satellogic.com/iqf/iq_tool_box-

RUN pip3 install torch==1.7.0+cu110 torchvision==0.8.1+cu110 -f https://download.pytorch.org/whl/torch_stable.html

CMD ["/bin/bash", "-c", "source activate satellogic && /bin/bash"]


