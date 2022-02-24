# ImageMagick commands

## Check if image is valid
`identify <img_in> &> /dev/null; echo $?`  (0 if valid, else 1)

## Convert to gray
`convert <img_in> -set colorspace Gray -separate -average <img_out>`

## Convert to RGB
`convert <img_in> -set colorspace sRGB -type truecolor <img_out>`

## Get image format (JPEG, PNG etc.)
`identify <image_file> | cut -d ' ' -f 2`

## Get image dimensions
`identify <image_file> | cut -d ' ' -f 3`

## Get image width
`identify -format "%w" <image_file>`

## Get image height
`identify -format "%h" <image_file>`

## Get maximum image dimension
```
a=$(identify -format "%w" <image_file>)
b=$(identify -format "%h" <image_file>)
echo $(( a > b ? a : b ))
```

## Get minimum image dimension
```
a=$(identify -format "%w" <image_file>)
b=$(identify -format "%h" <image_file>)
echo $(( a < b ? a : b ))
```

## Get minimum image dimension for jpg files
```
for f in *jpg
do
    a=$(identify -format "%w" $f)
    b=$(identify -format "%h" $f)
    echo $(( a < b ? a : b ))
done
```

## Negate image
`convert <image_file> -negate <output_file>`

## Resize ignoring aspect ratio
`convert <image_file> -resize WxH! <output_file>`

## Resize keeping aspect ratio
`convert <image_file> -resize WxH <output_file>`
`convert <image_file> -resize 50% <output_file>`
