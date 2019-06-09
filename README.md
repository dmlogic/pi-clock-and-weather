# Clock and weather display for Raspberry Pi & touchscreen

This project uses a Raspberry PI with touch screen to provide time, date and weather information

<img alt="Main screen" src="https://user-images.githubusercontent.com/1250252/59160300-4493a900-8acc-11e9-9ac9-21d3a6f2715c.png">

Main features:

* Time and date update from the PI timezone
* Weather data is from UK MetOffice [DataPoint API](https://www.metoffice.gov.uk/datapoint) based on GPS coordinates. The seven most relevant forecasts from the 3 hourly service are displayed
* Display is off most of the time and is turned on using the touchscreen
* Alert icons are displayed beneath the date if thresholds for "Apply sunscreen", "Dress for rain" or "Dress for cold" are met

<img alt="Main screen" src="https://user-images.githubusercontent.com/1250252/59160304-4b222080-8acc-11e9-8096-fec14519525f.png">

## Requirements

* A recent Raspberry PI
* Official LCD Touchscreen (others probably work)
* [PyGame](https://www.pygame.org) installed
* An API key for MetOffice DataPoint

This project makes use of the [Metoffer](https://github.com/sludgedesk/metoffer) library with some slight tweaks

## Installation

* Put your PI and screen together with a case if needed
* Set the PI to [boot in CLI mode](https://www.digikey.com/en/maker/blogs/2018/how-to-boot-to-command-line-and-ssh-on-raspberry-pi) if it isn't already
* Adjust the [backlight brightness](https://raspberrypi.stackexchange.com/questions/46225/adjusting-the-brightness-of-the-official-touchscreen-display) to a suitable setting for your location
* Ensure PyGame is installed
* Clone this repo (or your version of it) onto the PI
* Copy `config.py.sample` to `config.py` and set values to suit you
* Adjust `~/.bashrc` to include the following line at the end `cd /full/path/to/project/folder && python3 clock.py`. Adjust for the actual project path
* Reboot the Pi

On boot you should now see the clock. The backlight timer does not automatically start on boot so you need to touch the screen to turn it off. Subsequently it will turn off after the timeout interval.

## Future considerations

* Make the first forecast tile show recent, observed weather instead of the preceeding forecast period
* Convert all the display images, fonts, colours and coordinates into a theme file
* Introduce an alarm clock. This would need sound hardware in addition to much increased use of the touchscreen to turn the alarm on and off and set the alarm time(s)
* Ability to adjust backlight brightness via a settings interface

<img alt="In use" src="https://user-images.githubusercontent.com/1250252/59160305-52492e80-8acc-11e9-808a-044dcb590d6e.jpg">
