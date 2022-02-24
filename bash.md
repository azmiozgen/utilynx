# Bash commands

## Add new resolution(1920x1080)
1. `sudo xrandr --newmode "1920x1080_60.00"  173.00  1920 2048 2248 2576  1080 1083 1088 1120 -hsync +vsync`
2. Get display port name with `sudo xrandr`
3. `sudo xrandr --addmode eDP-1-1 "1920x1080_60.00"` (eDP-1-1 is embedded display port namely laptop screen)

## Add new user with home directory and with group
1. `sudo adduser --home <home_directory> --shell /bin/bash <user_name>`
2. `sudo passwd <user_name>`

## Add user to sudoers
`sudo usermod -aG sudo <user_name>`

## Compress pdf
* `ps2pdf input.pdf output.pdf`
* `gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook -dNOPAUSE -dQUIET -dBATCH -sOutputFile=output.pdf input.pdf`
* Even smaller: `gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/screen -dNOPAUSE -dQUIET -dBATCH -sOutputFile=output.pdf input.pdf`

## Convert markdown to pdf
`pandoc  <md-file> -s -o <pdf-file>`

## Find all unique characters in a file
* `fold -w1 <input_file> | sort -u -o <output_file>`    <!-- Problematic with non-printable characters -->
* `sed 's/./&\n/g' <input_file> | sort -u -o <output_file>`

## Generate ssh key
`ssh-keygen -t rsa -b 4096 -o -a 100`

## Get process start time
`ps -eo pid,lstart,cmd | grep <process_name e.g. python>`

## Get screen size
`xrandr | grep ' connected'`

### Get sudoers
`grep "sudo" /etc/group`

### List scanners
`scanimage -L`

## Remove all invalid characters
`for f in *; do mv ${f} $(echo ${f} | sed -e 's/[^A-Za-z0-9._-]//g'); done`

## Replace space with underscore
`for f in *; do mv "$f" "${f// /_}"; done`

## Remove parantheses (left and right))
`for f in *; do mv "$f" "${f/\(/}"; done`
`for f in *; do mv "$f" "${f/\)/}"; done`

## Separate pdf pages
`pdftk <input_pdf> cat <page_number> output <output_pdf>`

## Set graphics tablet screen
1. See tablet ids with `xsetwacom list`
2. See screen outputs with `xrandr`
3. For the first screen e.g. `xsetwacom --set <id> MapToOutput HEAD-0` or for the second screen `xsetwacom --set <id> MapToOutput HEAD-1` where <id> is the tablet id

### Scan
`scanimage -d "<device-name>" --format tiff > <scanned_doc.tiff>`

## Stop-Run CPU cores
1. Go root
2. Stop: `echo 0> /sys/devices/system/cpu/cpu<cpu_index>/online`
3. Run:  `echo 1> /sys/devices/system/cpu/cpu<cpu_index>/online`

### Substitute (Replace)
* In the entire file for all occurrences in place `sed -i 's/<old_pattern>/<new_pattern>/g' <file_name>`

## Sum numbers in the file
`awk '{ sum += 1 } END { print sum }' <file>`
