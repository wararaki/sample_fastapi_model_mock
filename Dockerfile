FROM python:3.7

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt && rm -rf requirements.txt ~/.cache

COPY src /work/src
COPY tests /work/tests

WORKDIR /work
CMD [ "pytest" ]
