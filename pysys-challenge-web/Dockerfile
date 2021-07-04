FROM node:14.17.1

#COPY docker-entrypoint.sh /usr/local/bin/
#ENTRYPOINT ["docker-entrypoint.sh"]

RUN mkdir -p /opt/pysys-challenge-web

RUN chmod +x /opt/pysys-challenge-web

COPY . /opt/pysys-challenge-web

WORKDIR /opt/pysys-challenge-web

RUN npm install -g @angular/cli@9.1.9

RUN npm update

RUN ng update

EXPOSE 4200
