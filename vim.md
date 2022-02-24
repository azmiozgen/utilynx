# Vim commands

# Set commands

* Paste mode on-off `:set paste` - `set nopaste`
* Numbered line mode on-off `:set nu` - `set nonu`

# Substitute (Replace)

* In the current line `:s/<old_pattern>/<new_pattern>`
* In the current line for all occurences `:s/<old_pattern>/<new_pattern>/g`
* In the entire file for all occurences `:%s/<old_pattern>/<new_pattern>/g`
* In the specific lines for all occurences `:<line1>,<line2>s/<old_pattern>/<new_pattern>/g`
* In the entire file for all occurences case insensitively `:%s/<old_pattern>/<new_pattern>/gi`
* In the entire file for all occurences case sensitively `:%s/<old_pattern>/<new_pattern>/gI`
* In the entire file for all occurences by confirming each `:%s/<old_pattern>/<new_pattern>/gc`