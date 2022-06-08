sudo docker run -it --rm --privileged \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v /root/.Xauthority:/root/.Xauthority \
#  -v `pwd`/blackbox:/opt/screen-recorder/blackbox \
  -v `pwd`:/opt/screen-recorder \
  -e DISPLAY=unix${DISPLAY} \
  --name screen-recorder \
  screen-recorder python run.py
