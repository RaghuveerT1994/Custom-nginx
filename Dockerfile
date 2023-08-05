FROM nginx
WORKDIR /
COPY ./python.py /
COPY ./docker-entrypoint.sh /
RUN chmod 777 /docker-entrypoint.sh
RUN apt-get update && apt-get install python3 -y && apt-get install vim -y
EXPOSE 80

