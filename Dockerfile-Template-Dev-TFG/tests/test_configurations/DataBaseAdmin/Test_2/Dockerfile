FROM phpmyadmin:latest

COPY ./config.user.inc.php /etc/phpmyadmin/config.inc.php

ENV PMA_ARBITRARY=1
ENV PMA_HOST=host
ENV PMA_PORT=port

EXPOSE 80
