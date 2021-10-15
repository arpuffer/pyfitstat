# pyfitstat
python wrapper for USB fit-stat indicator LED

from the fitStat itself:
```
HELP
*******************************************************

?                       - Return device UUID #

#RRGGBB                 - Set LED color according to Hex color code

F                       - Set Fade transition Time in ms 'F1000'

G                       - Return current color, (rr,gg,bb)

B                       - Set Fade transition Colors B#RRGGBB-tttt#RRGGBB....

                         Fade transition after each color


Firmware Revision: V0.9.6
```

## Development
```
pip install poetry

# Unless specified with --no-dev, poetry installs all dev dependencies
poetry install
```
