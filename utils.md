# Utilities

## Admin

### Add user with home directory and with group

`sudo adduser --home <home directory> --shell /bin/bash <user_name>`

### Set user's password

`sudo passwd <username>`

### See sudoers

`grep "sudo" /etc/group`

### Add user to sudoers

1. `sudo usermod -aG sudo <user name>`
2. Logout and login



## Conda

### List environments

`conda env list` or `conda info -e`

### List packages in environment

`conda list`

### Add kernels to Jupyter

1. `conda install nb_conda_kernels`
2. `python -m ipykernel install --user --name <env_name>`



## Docker

### Create Docker container from image and use volume

`docker run -v <local-path>:<new-path-on-docker> -it <image-id> /bin/bash`

### Run docker container

1. `docker start <container-id>`
2. `docker exec -it <container-id> /bin/bash`



## Document

### Separate pdf pages

`pdftk <input_pdf> cat <page_number> output <output_pdf>`

### PDF compress

* `ps2pdf input.pdf output.pdf`
* `gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook -dNOPAUSE -dQUIET -dBATCH -sOutputFile=output.pdf input.pdf`
* Even smaller: `gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/screen -dNOPAUSE -dQUIET -dBATCH -sOutputFile=output.pdf input.pdf`

### Markdown to pdf

`pandoc  <md-file> -s -o <pdf-file>`

### Scanning

#### List devices

`scanimage -L`

#### Scan

`scanimage -d "<device-name>" --format tiff > <scanned_doc.tiff>`



## Files

### Replace space with underscore

`for f in *; do mv "$f" ${f// _/}; done`

### Remove parantheses (left and right))

`for f in *; do mv "$f" "${f/\(/}"; done`

`for f in *; do mv "$f" "${f/\)/}"; done`

### Find all unique characters in a file

* `fold -w1 <input_file> | sort -u -o <output_file>`           <!-- Problematic with non-printable characters -->
* `sed 's/./&\n/g' <input_file> | sort -u -o <output_file>`


## Gcloud

### List accounts

`gcloud auth list`

### Set account

`gcloud config set account <ACCOUNT>`

### List projects

`gcloud projects list`

### Set project 

`gcloud config set project <PROJECT_NAME>`

### List files in the bucket

`gsutil ls gs://<BUCKET_NAME>`

### Copy files to bucket

`gsutil cp -r <FILES> gs://<BUCKET_NAME>`



## Git

### Recover deleted branch

1. `git reflog`
2. Take the deleted branch log id
3. `git checkout <id>`
4. `git branch <branch-name>`

### Git pull-push with specific ssh-key

`ssh-agent bash -c 'ssh-add ~/.ssh/azmi; git pull'`

### Remove unnecessary objects from .git

1. Find the biggest 10 objects with `git verify-pack -v .git/objects/pack/pack-*.idx | sort -k 3 -n | tail -10`
2. Get object name with `git rev-list --objects --all | grep <sha1 code from the 1st command>`
3. Remove objects with `git filter-branch --index-filter 'git rm --cached --ignore-unmatch <filename-pattern>' -- --all`
4. `rm -Rf .git/refs/original/`
5. `rm -Rf .git/logs`
6. Continue step 3. by removing other filename-patterns.
7. If done with 6. prune with `git gc --prune=now --aggressive`
8. `git push --force`

### Submodules

### Clone with submodules

* `git clone --recursive <URL to Git repo>`
* `git submodule update --init --recursive` (Already cloned repository)

#### Pull with submodules

* `git pull --recurse-submodules`

#### Add submodule

* `git submodule add <URL to Git repo>`
* `git submodule init`


## Image

### Convert to gray

`convert <img_in> -set colorspace Gray -separate -average <img_out>`

### Convert to RGB

`convert <img_in> -set colorspace sRGB -type truecolor <img_out>`

### Check if image is valid

`identify <img_in> &> /dev/null; echo $?`  (0 if valid, else 1)



## OS

### Stop-Run CPU cores

1. Go root
2. Stop: `echo 0> /sys/devices/system/cpu/cpu<cpu_index>/online`
3. Run:  `echo 1> /sys/devices/system/cpu/cpu<cpu_index>/online`

### See process start time

`ps -eo pid,lstart,cmd | grep <process_name e.g. python>`



## Privacy

### ssh-key generation

`ssh-keygen -t rsa -b 4096 -o -a 100`



## Screen

### Get screen size

`xrandr | grep ' connected'`


### Add new resolution(1920x1080)

1. `sudo xrandr --newmode "1920x1080_60.00"  173.00  1920 2048 2248 2576  1080 1083 1088 1120 -hsync +vsync`
2. Get display port name with `sudo xrandr`
2. `sudo xrandr --addmode eDP-1-1 "1920x1080_60.00"` (eDP-1-1 is embedded display port namely laptop screen)



## Sed

### Substitute (Replace)

* In the entire file for all occurrences in place `sed -i 's/<old_pattern>/<new_pattern>/g' <file_name>`



## Valgrind

### For analyze with GUI Valkyrie

* `valgrind --tool=memcheck --leak-check=full --track-origins=yes --xml=yes --xml-file=valgrind_output.xml <binary_file>`



## Tesseract

### Standard OCR

* `tesseract --psm 1 --oem 1 -l eng text.txt text`

#### psm (Page Segmentation Modes)

* 0 Orientation and script detection (OSD) only.
* 1 Automatic page segmentation with OSD.
* 2 Automatic page segmentation, but no OSD, or OCR.
* 3 Fully automatic page segmentation, but no OSD. (Default)
* 4 Assume a single column of text of variable sizes.
* 5 Assume a single uniform block of vertically aligned text.
* 6 Assume a single uniform block of text.
* 7 Treat the image as a single text line.
* 8 Treat the image as a single word.
* 9 Treat the image as a single word in a circle.
* 10 Treat the image as a single character.
* 11 Sparse text. Find as much text as possible in no particular order.
* 12 Sparse text with OSD.
* 13 Raw line. Treat the image as a single text line, bypassing hacks that are Tesseract-specific.

#### oem (OCR Engine Modes)

* 0 Legacy engine only
* 1 Neural nets LSTM only
* 2 Legacy + LSTM engines
* 3 Default, based on what is available

### Get character box coordinates in a file with extension '.box'

* `tesseract --psm 1 --oem 2 <input_image_file> <output_file_wo_extension> makebox`



## Vim

### Set commands

* Paste mode on-off `:set paste` - `set nopaste`
* Numbered line mode on-off `:set nu` - `set nonu`

### Substitute (Replace)

* In the current line `:s/<old_pattern>/<new_pattern>`
* In the current line for all occurences `:s/<old_pattern>/<new_pattern>/g`
* In the entire file for all occurences `:%s/<old_pattern>/<new_pattern>/g`
* In the specific lines for all occurences `:<line1>,<line2>s/<old_pattern>/<new_pattern>/g`
* In the entire file for all occurences case insensitively `:%s/<old_pattern>/<new_pattern>/gi`
* In the entire file for all occurences case sensitively `:%s/<old_pattern>/<new_pattern>/gI`
* In the entire file for all occurences by confirming each `:%s/<old_pattern>/<new_pattern>/gc`
