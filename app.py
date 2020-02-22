from tempfile import TemporaryDirectory
from pytube import (
    YouTube
)
from pprint import pprint
from pydub import AudioSegment
import os


dldls_dir = './dlds/'


with open('./urls.txt', 'r') as urls:
    vids = urls.readlines()
    for vid in vids:
        yt = YouTube(vid)
        title = yt.title
        stream = yt.streams.filter(only_audio=True).first()
        # for stream in streams:
        #     pprint(stream)
        pprint(stream)
        stream.download('./dlds/', filename=title)
        mp4_fp = f'{dldls_dir}{title}.mp4'
        AudioSegment.from_file(
            mp4_fp,
            format="mp4"
        ).export(
            f'{dldls_dir}{title}.mp3',
            format='mp3',
            codec='mp3'
        )
        os.remove(mp4_fp)

