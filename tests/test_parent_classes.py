# -*- coding: utf-8 -*-

from twitchrealtimehandler.twitchhandler import (_TwitchHandler,
                                                 _TwitchHandlerAudio,
                                                 _TwitchHandlerVideo,
                                                 _TwitchHandlerGrabber)
import pytest


def test_twitch_handler():
    handler = _TwitchHandler(twitch_url="https://dummy")
    assert handler.twitch_url == "https://dummy"

    with pytest.raises(ValueError):
        handler.get_stream_url()


def test_twitch_handler_audio():
    handler = _TwitchHandlerAudio(rate=8000,
                                  segment_length=4)
    assert handler.rate == 8000
    assert handler.segment_length == 4
    assert handler.quality == "audio_only"


def test_twitch_handler_video():
    handler = _TwitchHandlerVideo()
    with pytest.raises(AttributeError):
        handler.segment_length


def test_twitch_handler_grabber():
    assert _TwitchHandler in _TwitchHandlerGrabber.__bases__
    assert _TwitchHandler in _TwitchHandlerGrabber.__bases__
    handler = _TwitchHandlerGrabber()
    assert handler.grab() is None
