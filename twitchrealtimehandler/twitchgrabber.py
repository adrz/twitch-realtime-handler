# -*- coding: utf-8 -*-

import numpy as np
from twitchrealtimehandler.twitchhandler import (_TwitchHandlerGrabber,
                                                 _TwitchHandlerAudio,
                                                 _TwitchHandlerVideo)
from dataclasses import dataclass, field


@dataclass
class TwitchAudioGrabber(_TwitchHandlerAudio, _TwitchHandlerGrabber):
    """Handler to retrieve audio segment in realtime from a
    twitch stream

    Parameters:
    -----------
    channels: int
              number of channels (1 or 2)
    dtype: np.type
           type of the array of the audio segment
    """
    channels: int = 2
    dtype: type = np.float64
    _format_strings = {
        np.float64: 'f64le',
        np.float32: 'f32le',
        np.int16: 's16le',
        np.int32: 's32le',
    }
    _n_bytes_per_sample = {
        np.int16: 2,
        np.int32: 4,
        np.float32: 4,
        np.float64: 8
    }

    def __post_init__(self):
        super().__post_init__()

        if self.channels not in [1, 2]:
            raise ValueError("number of channels should be 1 or 2")
        if self.dtype not in self._format_strings:
            raise ValueError("Unrecognized dtype")
        format_ffmpeg = self._format_strings[self.dtype]
        self.get_stream_url()
        self._cmd_pipe = ['ffmpeg',
                          '-i', self._stream_url,
                          '-f', format_ffmpeg,
                          "-loglevel", "quiet",
                          '-acodec', f'pcm_{format_ffmpeg}',
                          '-ar', '{}'.format(self.rate),
                          '-ac', str(self.channels),
                          '-']
        # each sample is encoding in a certain number of bytes depending on the
        # quality requested
        # so sampling_rate*channels*n_bytes is the number of sample for 1 second
        self._n_bytes_per_payload = (self.rate
                                     * self.segment_length
                                     * self.channels
                                     * self._n_bytes_per_sample[self.dtype])
        self._reshape_size = [-1, self.channels]
        if self._auto_start:
            self._start_thread()


@dataclass
class TwitchImageGrabber(_TwitchHandlerVideo, _TwitchHandlerGrabber):
    """Handler to retrieve audio segment in realtime from a
    twitch stream"""
    _resolution = {
        '160p': (320, 160),
        '360p': (640, 360),
        '480p': (854, 480),
        '720p': (1280, 720),
        '720p60': (1280, 720),
        '1080p': (1920, 1080),
        '1080p60': (1920, 1080)
    }

    def __post_init__(self):
        super().__post_init__()
        if self.quality not in self._resolution:
            raise ValueError("Unrecognized quality")
        self.width, self.height = self._resolution[self.quality]
        self.dtype = np.uint8
        self.get_stream_url()
        self._cmd_pipe = ["ffmpeg",
                          "-i", self._stream_url,
                          "-f", "image2pipe",
                          "-r", f"{self.rate}",
                          "-pix_fmt", "rgb24",
                          "-s", "{}x{}".format(self.width, self.height),
                          "-vcodec", "rawvideo",
                          "-"]
        self._n_bytes_per_payload = self.width*self.height*3
        self._reshape_size = [self.height, self.width, 3]
        if self._auto_start:
            self._start_thread()
