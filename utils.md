# Privacy

## ssh-key generation

`ssh-keygen -t rsa -b 4096 -o -a 100`

# Image

## Convert to gray

`convert <img_in> -set colorspace Gray -separate -average <img_out>`

## Convert to RGB

`convert <img_in> -set colorspace sRGB -type truecolor <img_out>`

# Document

## PDF compress

1. `ps2pdf input.pdf output.pdf`
2. `gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook -dNOPAUSE -dQUIET -dBATCH -sOutputFile=output.pdf input.pdf`
3. `gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/screen -dNOPAUSE -dQUIET -dBATCH -sOutputFile=output.pdf input.pdf`  ## even smaller