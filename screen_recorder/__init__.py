import os
from datetime import (
    datetime,
    timedelta,
)

from vidgear.gears import (
    ScreenGear,
    WriteGear,
)


class ScreenRecorder:
    def __init__(self):
        self._dir_name = 'media'
        self._fps = int(os.getenv('FPS', '30'))
        self._frame_per_second = 1 / self._fps
        self._cached_frame = None
        self._save_time = 0
        self._screen_options = {
            'monitor': 1,
        }
        self._screen = self._get_screen()
        self._writer_options = {
            'compression_mode': True,
            '-input_framerate': self._fps,
            '-vcodec': 'libx264',
            '-crf': 0,
            '-preset': 'fast',
        }
        self._file_time = datetime.now() + timedelta(hours=9)
        self._writer = self._get_writer()

    def run(self):
        self._main_loop()

    def _main_loop(self):
        while True:
            now = datetime.now() + timedelta(hours=9)
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
        return cur - self._save_time > self._frame_per_second

    def _record(self, cur, frame):
        if frame is not None:
            self._save_time = cur
            self._writer.write(frame)

    def _get_screen(self):
        return ScreenGear(**self._screen_options).start()

    def _get_writer(self):
        return WriteGear(**self._writer_options, output_filename=self._get_output_filename())

    def _get_output_filename(self):
        return f'{self._get_or_create_dir()}/{self._file_time.strftime("%Y-%m-%dT%H:%M")}.mp4'

    def _get_or_create_dir(self):
        dir_path = f'{self._dir_name}/{self._file_time.strftime("%Y-%m-%dT%H")}'
        abs_dis_path = os.path.abspath(dir_path)
        os.makedirs(abs_dis_path, exist_ok=True)
        return abs_dis_path
