FROM ubuntu:20.04

ARG DEBIAN_FRONTEND="noninteractive"

# Install python and deps for gdal
RUN apt-get update
RUN apt-get install -y python3 python3-pip build-essential gdal-bin python3-gdal libgdal-dev wget
RUN echo 'PATH="$HOME/.local/bin/:$PATH"' >>~/.bashrc
RUN pip install "GDAL<=$(gdal-config --version)"

# Install deps for tippecanoe
RUN apt-get -y install build-essential libsqlite3-dev zlib1g-dev git
RUN git clone https://github.com/mapbox/tippecanoe.git
WORKDIR /tippecanoe

# Build tippecanoe
RUN make \
  && make install

# Run the tippecanoe tests
CMD make test

# Add other python deps
RUN pip install click

COPY . /app

WORKDIR /app
