FROM ubuntu:18.04
LABEL maintainer="Amir Ayub, dev.amirayub@gmail.com"
RUN apt-get update
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN pip3 install -r requirements.txt
EXPOSE 80
COPY . /app
WORKDIR /app
ENTRYPOINT [ "python3" ]
CMD [ "core.py" ]