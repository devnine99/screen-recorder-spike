FROM python:3.8

RUN apt update && apt -y install ffmpeg libgl1-mesa-glx

RUN mkdir /opt/screen_recorder
WORKDIR /opt/screen_recorder
ADD . /opt/screen_recorder
RUN pip install -r requirements.txt