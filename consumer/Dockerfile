FROM python:3.9-alpine3.17

COPY ./consumer /hover/receiver
WORKDIR /home/consumer/

COPY .requirements.txt /tmp/requirements.txt
RUN python3 -m pip install -r /tmp/requirements.txt

CMD [ "python", "consumer.py" ]