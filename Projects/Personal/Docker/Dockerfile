FROM python:alpine3.10
WORKDIR /app
COPY lib.txt /app
RUN pip install -r lib.txt
COPY . /app
CMD python ./hello_world.py
