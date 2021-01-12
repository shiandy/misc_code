# Merge multiple ics files into one ics file

This Python script merges multiple ics files into one ics file.

## Motivation

When I sign up for Zoom seminars, there is sometimes a link to add the Zoom
event to my calendar. I use Google Calendar, but to add the Zoom event directly
to Google Calendar, I need to give Zoom permission to read my Google Calendar,
which I don't want to do. Instead, I download the ics file, which I can then
import into Google Calendar (Gear Icon > Settings > Import & export). If I sign
up for multiple seminars, I need to import each ics file one at a time. Using
this script, I can merge all the ics files into one big ics file and just import
one ics file.

## Installation

This Python script requires the
[ics.py](https://github.com/C4ptainCrunch/ics.py) library, which can be
installed from pip:

```
pip install ics
```

## Usage

```
python merge_ics.py --output merged.ics cal1.ics cal2.ics cal3.ics ...
```

+ Specify the output file using the `--output` flag. If not specified, the
  default is `merged.ics`.

+ Use positional arguments to add ics files. If you don't add any, by default
  all the `.ics` files in your current working directory will be merged.
