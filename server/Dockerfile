FROM python:3.10

WORKDIR /usr/src/app

ENV PYTHONBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV PATH="/root/.cargo/bin:${PATH}"
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
RUN cargo install beacon-verifier