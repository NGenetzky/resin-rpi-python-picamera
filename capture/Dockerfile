FROM resin/nuc-python

ENV READTHEDOCS True

# pip install python deps from requirements.txt
# For caching until requirements.txt changes
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY ./picamera_capture.py /usr/bin/
WORKDIR /data/

CMD ["picamera_capture.py"]

