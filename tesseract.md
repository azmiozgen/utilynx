# Tesseract

## Standard OCR
* `tesseract -l eng --oem 2 --psm 8 -c tessedit_char_whitelist=0123456789., <image-file> stdout`

### psm (Page Segmentation Modes)
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

### oem (OCR Engine Modes)
* 0 Legacy engine only
* 1 Neural nets LSTM only
* 2 Legacy + LSTM engines
* 3 Default, based on what is available

## Get character box coordinates in a file with extension '.box'
* `tesseract --psm 1 --oem 2 <input_image_file> <output_file_wo_extension> makebox`

## Limit characters
* `tesseract <image_file> stdout -c tessedit_char_whitelist=0123456789.,`

## List all available languages
* `tesseract --list-langs`

## List all parameters
* `tesseract --print-parameters`

## Print output to standard out
* `tesseract <image_file> stdout`

## Use multiple languages together
* `tesseract -l eng+deu+fra+ita+spa+por <image_file> <output_file>`

## Write output to text file
* `tesseract <image_file> <text_file>`
