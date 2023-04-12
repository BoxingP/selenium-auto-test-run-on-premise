FROM python:3.8-slim
RUN apt-get update && apt-get install -y --no-install-recommends cron tzdata lsb-release build-essential wget unzip libdbus-glib-1-2 gpg
RUN apt-get update && apt-get install -y --no-install-recommends python3-dev python3-virtualenv
RUN apt-get update && apt-get install -y --no-install-recommends libpq-dev
RUN apt-get update && apt-get install -y --no-install-recommends libaio1
WORKDIR /opt/oracle
RUN wget -q https://download.oracle.com/otn_software/linux/instantclient/instantclient-basiclite-linuxx64.zip \
    && unzip instantclient-basiclite-linuxx64.zip && rm -f instantclient-basiclite-linuxx64.zip \
    && cd /opt/oracle/instantclient* && rm -f *jdbc* *occi* *mysql* *README *jar uidrvci genezi adrci \
    && echo /opt/oracle/instantclient* > /etc/ld.so.conf.d/oracle-instantclient.conf && ldconfig
WORKDIR /tmp
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && apt-get install -y ./google-chrome-stable_current_amd64.deb \
    && rm -f ./google-chrome-stable_current_amd64.deb
RUN wget -O firefox-latest-linux64.tar.bz2 "https://download.mozilla.org/?product=firefox-latest&os=linux64" \
    && tar xjf ./firefox-latest-linux64.tar.bz2 -C /opt/ \
    && ln -s /opt/firefox/firefox /usr/bin/firefox \
    && rm -f ./firefox-latest-linux64.tar.bz2
RUN wget -q -O- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg \
    && install -o root -g root -m 644 microsoft.gpg /etc/apt/trusted.gpg.d/ \
    && sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/edge stable main" > /etc/apt/sources.list.d/microsoft-edge.list' \
    && rm -f ./microsoft.gpg \
    && apt-get update \
    && apt-get install microsoft-edge-stable
WORKDIR /usr/src/selenium_auto_test
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m pip install virtualenv
RUN python3 -m virtualenv --python=/usr/bin/python3 $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
COPY . ./
RUN pip install -r requirements.txt
RUN mv ./crontab /etc/cron.d/cron-jobs && sed -i -e 's/\r/\n/g' /etc/cron.d/cron-jobs && chmod 0644 /etc/cron.d/cron-jobs
RUN chmod +x cron.sh
RUN mkdir -p /var/log/cron && touch /var/log/cron/cron.log
ENV TZ="Asia/Shanghai"
ENTRYPOINT ["/bin/sh", "/usr/src/selenium_auto_test/cron.sh"]