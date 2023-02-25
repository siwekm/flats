FROM python:3.9

RUN mkdir -p /var/app

WORKDIR /var/app

COPY requirements.txt ./

RUN pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt

COPY . /var/app