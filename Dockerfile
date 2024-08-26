FROM python:3.11-slim as build

# Install packages
COPY ./requirements.txt requirements.txt
RUN pip3 install --no-cache-dir --target=packages -r requirements.txt


FROM python:3.11-slim as runtime

# Copy packages from build
COPY --from=build packages /usr/lib/python3.11/site-packages
ENV PYTHONPATH=/usr/lib/python3.11/site-packages

# Setup /app
WORKDIR /app
COPY . .