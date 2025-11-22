FROM python:3.14.0-alpine3.22
WORKDIR /src
COPY . .
RUN pip install -r requirements.txt
EXPOSE 4000
CMD python3 server.py
