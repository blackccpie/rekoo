#!/bin/bash
say() { curl -s -A Mozilla "http://translate.google.com/translate_tts?tl=en&q=$*&client=t" > output.mp3; afplay output.mp3; }
say $*

# old commandline using mplayer
# say() { local IFS=+;/usr/bin/mplayer -ao alsa -really-quiet -noconsolecontrols "http://translate.google.com/translate_tts?tl=en&q=$*&client=t"; }
