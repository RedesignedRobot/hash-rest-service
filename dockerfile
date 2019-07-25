FROM ubuntu:18.04
LABEL maintainer="Amir Ayub, dev.amirayub@gmail.com"
COPY . /app
WORKDIR /app
RUN apt-get update
RUN apt-get install python3 -y
RUN pip install -r requirements.txt
EXPOSE 80
ENTRYPOINT [ "python3" ]
CMD [ "core.py" ]