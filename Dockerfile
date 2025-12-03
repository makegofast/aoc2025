FROM python:latest
RUN pip3 install numpy
CMD tail -f /dev/null
