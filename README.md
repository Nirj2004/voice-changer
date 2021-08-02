# VoiceChanger

![Status:Archived](https://img.shields.io/badge/Status-Archived-inactive)

GUI for Sox and pulseaudio allowing for real time voice distortion

## Requirements
- Python 3.5 or later
- Python's TkInter module (Usually part of the standard library, besides on Ubuntu and derivatives)
- SoX
- PulseAudio

## Known issues
- This is just a GUI that runs and stops Pulseaudio and SoX commands, don't expect a fully-fledged package
- The load and save features use Python's Pickle, which is weak to arbitrary code execution.
