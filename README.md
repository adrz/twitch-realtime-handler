[![Build
Status](https://travis-ci.org/adrz/twitch-realtime-handler.svg?branch=master)](https://travis-ci.org/adrz/twitch-realtime-handler)
[![codecov](https://codecov.io/gh/adrz/twitch-realtime-handler/branch/master/graph/badge.svg)](https://codecov.io/gh/adrz/twitch-realtime-handler)
[![PyPI version fury.io](https://badge.fury.io/py/twitchrealtimehandler.svg)](https://pypi.python.org/pypi/twitchrealtimehandler/)


# Description

This package allows to extract in real-time frames or audio segments of a twitch stream as numpy array.
It heavily relies on FFmpeg to decode on-the-fly and asynchronously the stream.
Then the package stocks the frames or the audio segments into a fifo.


# Requirements

- FFmpeg
- python 3.7+

This code has only been tested on Ubuntu 20.04, it might requires some tweaks to make it compatible with Windows or MacOSX

# Installation

Install using pip for stable release,
```bash
pip install twitchrealtimehandler
```

For latest development release,
```bash
pip install git+git://github.com:adrz/twitch-realtime-handler.git
```

# Usage

```python
from twitchrealtimehandler import (TwitchAudioGrabber,
                                   TwitchImageGrabber)
import numpy as np

audio_grabber = TwitchAudioGrabber(
    twitch_url="https://www.twitch.tv/jeanmassietaccropolis",
    blocking=True,  # wait until a segment is available
    segment_length=2,  # segment length in seconds
    rate=16000,  # sampling rate of the audio
    channels=2,  # number of channels
    dtype=np.int16  # quality of the audio could be [np.int16, np.int32, np.float32, np.float64]
    )

audio_segment = audio_grabber.grab()
audio_grabber.terminate()  # stop the transcoding

image_grabber = TwitchImageGrabber(
    twitch_url="https://www.twitch.tv/jeanmassietaccropolis",
    quality="480p",  # quality of the stream could be ["160p", "360p", "480p", "720p", "720p60", "1080p", "1080p60"]
    blocking=True,
    rate=10  # frame per rate (fps)
    )

frame = image_grabber.grab()
image_grabber.terminate()  # stop the transcoding
```

# Examples

## Requirements

Dependencies for face_recognition package:

```bash
sudo apt-get update
sudo apt-get install build-essential cmake
sudo apt-get install libopenblas-dev liblapack-dev 
sudo apt-get install libx11-dev libgtk-3-dev
sudo apt-get install python3 python3-dev python3-pip
pip install -r requirements-examples.txt
```

## Real-time face detection

```bash
python examples/realtime-face-detection.py --twitch-url https://twitch.tv/yourfavouritetwitcher
```
![face-detection-senat](https://raw.githubusercontent.com/adrz/twitch-realtime-handler/master/demos/faces-detection.gif)


## Real-time transcript

```bash
python examples/realtime-transcript.py --twitch-url https://twitch.tv/yourfavouritetwitcher
```

# Known issues

![twitch-third-party](https://raw.githubusercontent.com/adrz/twitch-realtime-handler/master/demos/twitch-thirdparty.jpg)

If you encounter this image, it means that twitch knows your not watching from its website. You'll get this message for a few seconds and the stream will resume.