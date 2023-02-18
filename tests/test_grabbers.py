# -*- coding: utf-8 -*-

from twitchrealtimehandler.twitchgrabber import TwitchAudioGrabber, TwitchImageGrabber
from twitchrealtimehandler.twitchhandler import (
    _TwitchHandlerAudio,
    _TwitchHandlerGrabber,
    _TwitchHandlerVideo,
)


def test_audio_grabber():
    assert all(
        x in TwitchAudioGrabber.__bases__
        for x in [_TwitchHandlerAudio, _TwitchHandlerGrabber]
    )


def test_image_grabber():
    print(TwitchImageGrabber.__bases__)
    assert all(
        x in TwitchImageGrabber.__bases__
        for x in [_TwitchHandlerVideo, _TwitchHandlerGrabber]
    )
