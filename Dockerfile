FROM python:3.8

RUN apt-get update && apt-get -y install ffmpeg libgl1-mesa-glx

RUN echo "ForwardX11 yes" >> /etc/ssh/ssh_config

RUN mkdir /opt/screen-recorder
WORKDIR /opt/screen-recorder
ADD . /opt/screen-recorder
RUN pip install -r requirements.txt
