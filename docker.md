# Docker commands

## Create Docker container from image and use volume
`docker run -v <local-path>:<new-path-on-docker> -it <image-id> /bin/bash`

## Run docker container
1. `docker start <container-id>`
2. `docker exec -it <container-id> /bin/bash`
