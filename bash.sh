sudo docker run -it --rm -v /tmp/.X11-unix:/tmp/.X11-unix -v ${HOME}/.Xauthority:/root/.Xauthority -e DISPLAY=unix${DISPLAY} --name screen-recorder screen-recorder bash