FROM nginx:1.17.9

LABEL maintainer="Paulo Francesco Pacheco <pfpacheco@gmail.com>"

RUN rm -rf /etc/nginx/nginx.conf

RUN mkdir -p /var/www \
    && mkdir -p /var/www/html

COPY ./html /var/www/html

ADD ./conf/nginx.conf /etc/nginx/
