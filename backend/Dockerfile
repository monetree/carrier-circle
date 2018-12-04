FROM python:3.6
ENV PYTHONUNBUFFERED 1
WORKDIR /usr/src/govtcareer_api

COPY ./ /usr/src/govtcareer_api

RUN pip install -r requirements.txt

CMD ["/bin/bash"]
