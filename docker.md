# Docker commands

## Build

`docker build -f <Dockerfile> -t <image_name> .`
`docker build -f docker/services/labeling.Dockerfile -t dev-labeling:latest .`

## Create Docker container from image and use volume

`docker run -v <local-path>:<new-path-on-docker> -it <image-id> /bin/bash`

## Run docker container

1. `docker start <container-id>`
2. `docker exec -it <container-id> /bin/bash`

## Stop docker container

`docker stop <container-id>`

## Docker Compose commands

`docker-compose up --build` Start all services

`docker-compose up serving` Start specific service

`docker-compose logs -f` View logs

`docker-compose down` Stop all services

`sudo systemctl restart docker.socket docker.service` Restart Docker if needed

## Clean

`docker image prune` Remove unused images

`docker builder prune` Clean up build cache
