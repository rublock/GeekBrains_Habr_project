FROM python:3.10-alpine3.15 as builder

COPY /requirements.txt .

RUN apk add --no-cache jpeg-dev \
    postgresql-libs \
    gcc \
    musl-dev \
    postgresql-dev \
    g++ \
    python3-dev \
    zlib-dev \
    libxml2-dev \
    libffi-dev \
    openssl-dev \
    cargo \
    build-base \
    && mkdir build \
    && python -m pip --no-cache-dir install --upgrade pip \
    && python -m pip --no-cache-dir install --prefix build/ --no-warn-script-location --requirement requirements.txt


FROM python:3.10-alpine3.15

RUN apk add --no-cache libpq \
    libjpeg \
    tzdata \
    poppler-utils \
    && ln -snf /usr/share/zoneinfo/Europe/Moscow /etc/localtime \
    && echo Europe/Moscow > /etc/timezone

ENV PYTHONUNBUFFERED=1

COPY --from=builder /build /usr/local

WORKDIR /app
COPY /app .
