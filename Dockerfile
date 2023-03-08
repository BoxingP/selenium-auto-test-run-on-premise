FROM python:3.8-slim
RUN apt-get update && apt-get install -y --no-install-recommends cron tzdata lsb-release build-essential wget unzip
RUN apt-get update && apt-get install -y --no-install-recommends python3-dev python3-virtualenv
RUN apt-get update && apt-get install -y --no-install-recommends libpq-dev
WORKDIR /tmp
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install -y ./google-chrome-stable_current_amd64.deb
RUN chrome_version="$(google-chrome --version | grep -o -E '[0-9.]+' | cut -d '.' -f1)" \
    && chromedriver_version=$(wget https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$chrome_version -q -O -) \
    && wget -q https://chromedriver.storage.googleapis.com/$chromedriver_version/chromedriver_linux64.zip
RUN unzip -o chromedriver_linux64.zip -d /usr/bin
RUN chmod 755 /usr/bin/chromedriver
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