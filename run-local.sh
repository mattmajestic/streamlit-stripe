#!/bin/bash

docker build -t bramble-beachhouse .
docker run -p 8501:8501 bramble-beachhouse