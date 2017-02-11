#!/bin/bash
say() { curl -s -A Mozilla "http://translate.google.com/translate_tts?tl=en&q=$*&client=t" > output.mp3; omxplayer -I -o local  output.mp3; }
say $*

