FROM python:3.7.7

COPY /requirements.txt /app/
WORKDIR /app

RUN pip3 install --no-cache-dir -i https://mirrors.aliyun.com/pypi/simple/ -r requirements.txt

COPY / /app

EXPOSE 7002

ENTRYPOINT sh /app/start.sh
