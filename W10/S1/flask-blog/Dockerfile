FROM python:3.7-alpine
RUN mkdir /blog
WORKDIR /blog
ADD requirements.txt .
RUN pip3 install -r requirements.txt
COPY app/ .
ENTRYPOINT ["sh"]