# Admin

## Add user with home directory and with group

`sudo adduser -m -d <home directory> -s /bin/bash -U <user name>`

## Set user's password

`sudo passwd <username>`

## Add user to sudoers

`sudo usermod -aG sudo <user name>`



# Conda

## List environments

`conda env list` or `conda info -e`

## List packages in environment

`conda list`

## Add kernels to Jupyter

`conda install nb_conda_kernels`



# Docker

## Create Docker container from image and use volume

`docker run -v <local-path>:<new-path-on-docker> -it <image-id> /bin/bash`

## Run docker container

`docker start <container-id>`

`docker exec -it <container-id> /bin/bash`



# Document

## PDF compress

* `ps2pdf input.pdf output.pdf`
* `gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook -dNOPAUSE -dQUIET -dBATCH -sOutputFile=output.pdf input.pdf`
* `gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/screen -dNOPAUSE -dQUIET -dBATCH -sOutputFile=output.pdf input.pdf`  ## even smaller

## md to pdf

`pandoc  <md-file> -s -o <pdf-file>`

## Scanning

### List devices

`scanimage -L`

### Scan

`scanimage -d "<device-name>" --format tiff > <scanned_doc.tiff>`



# Files

## Replace space with underscore

`for f in *; do mv "$f" ${f// _/}; done`

## Remove parantheses (left and right))

`for f in *; do mv "$f" "${f/\(/}"; done`

`for f in *; do mv "$f" "${f/\)/}"; done`



# Gcloud

## List accounts

`gcloud auth list`

## Set account

`gcloud config set account <ACCOUNT>`

## List projects

`gcloud projects list`

## Set project 

`gcloud config set project <PROJECT_NAME>`

## List files in the bucket

`gsutil ls gs://<BUCKET_NAME>`

## Copy files to bucket

`gsutil cp -r <FILES> gs://<BUCKET_NAME>`



# Git

## Recover deleted branch

1. `git reflog`
2. Take the deleted branch log id
3. `git checkout <id>`
4. `git branch <branch-name>`

## Git pull-push with specific ssh-key

`ssh-agent bash -c 'ssh-add ~/.ssh/azmi; git pull'`

## Remove unnecessary objects from .git

1. Find the biggest 10 objects with `git verify-pack -v .git/objects/pack/pack-ebdff2509d4fab153db9a62ea7764875873d827f.idx | sort -k 3 -n | tail -10`
2. Get object name with `git rev-list --objects --all | grep <sha1 code from the 1st command>`
3. Remove objects with `git filter-branch --index-filter 'git rm --cached --ignore-unmatch <filename-pattern>' -- --all`
4. `rm -Rf .git/refs/original/`
5. `rm -Rf .git/logs`
6. Continue step 3. by removing other filename-patterns.
7. If done with 6. prune with `git gc --prune=now --aggressive`



# Image

## Convert to gray

`convert <img_in> -set colorspace Gray -separate -average <img_out>`

## Convert to RGB

`convert <img_in> -set colorspace sRGB -type truecolor <img_out>`



# OS

## Stop-Run CPU cores

1. Go root
2. Stop: `echo 0> /sys/devices/system/cpu/cpu<X>/online` ## X is cpu index
3. Run:  `echo 1> /sys/devices/system/cpu/cpu<X>/online`

## See process start time

`ps -eo pid,lstart,cmd | grep <process_name e.g. python>`



# Privacy

## ssh-key generation

`ssh-keygen -t rsa -b 4096 -o -a 100`



# Screen

## Get screen size

`xrandr | grep ' connected'`


