sudo docker run -it --rm \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v /root/.Xauthority:/root/.Xauthority \
  -v `pwd`:/opt/screen-recorder \
  -e DISPLAY=unix${DISPLAY} \
  --name screen-recorder \
  screen-recorder python run.py
