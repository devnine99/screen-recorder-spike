import os
from datetime import datetime

from vidgear.gears import (
    ScreenGear,
    WriteGear,
)


class ScreenRecorder:
    def __init__(self):
        self._fps = 1 / int(os.getenv('FPS', '15'))
        self._cached_frame = None
        self._save_time = 0
        self._screen_options = {
            'logging': True,
            'monitor': 1,
            # 'backend': 'gnome_dbus',
        }
        self._screen = self._get_screen()
        self._writer_options = {
            'logging': True,
            'compression_mode': True,
            'fps': self._fps,
            '-vcodec': 'libx264',
            '-crf': 0,
            '-preset': 'fast',
        }
        self._file_time = datetime.now()
        self._writer = self._get_writer()

    def run(self):
        self._main_loop()

    def _main_loop(self):
        while True:
            now = datetime.now()
            self._check_writer(now)
            cur = now.timestamp()

            if not self._check_fps(cur):
                continue
            self._record(cur, self._screen.read())

    def _check_writer(self, now):
        if self._file_time.minute != now.minute:
            self._file_time = now
            self._writer.close()
            self._writer = self._get_writer()

    def _check_fps(self, cur):
        return cur - self._save_time > self._fps

    def _record(self, cur, frame):
        if frame is not None:
            self._save_time = cur
            self._writer.write(frame)

    def _get_screen(self):
        return ScreenGear(**self._screen_options).start()

    def _get_writer(self):
        return WriteGear(**self._writer_options, output_filename=self._get_output_filename())

    def _get_output_filename(self):
        return f'blackbox/{self._file_time.strftime("%Y-%m-%d %H:%M")}.mp4'