import os, time, glob

TMP_DIR = "/"
DISPLAY = os.environ['DISPLAY']
EXT = {
    'Video':'libx264',
    'Audio':'wav',
    'AV':'mkv',
}

class ffmpegVideo:

    FFMPEG_BIN = "ffmpeg"
    AUDIO = False

    def __init__(self, fps = 30, audio = True):
        global TMP_DIR, DISPLAY, EXT

        self.fps = fps

        if audio:
            self.AUDIO = True

            self.video_filename = self.unique_filename()

            self.command = [ self.FFMPEG_BIN,
                '-video_size', '1920x1080',
                '-framerate', str(fps),
                '-f', 'x11grab',
                '-i', DISPLAY,
                '-vcodec', 'libx264',
                '-qp', '0',
                '-preset', 'ultrafast',
                '-y', TMP_DIR + '/' + self.video_filename
        ]

    def start(self):
        import threading as th

        thread = th.Thread(target=self.record)
        thread.start()

    def record(self):
        import subprocess as sp

        self.pipe = sp.Popen(self.command, stderr=sp.PIPE)

        if self.AUDIO:
            ffmpegAudio().start()

    def stop(self):
        self.pipe.terminate()

    def unique_filename(self):
        global TMP_DIR, EXT
        i = 0
        while os.path.exists((TMP_DIR + '/' + 'tmp_%s.%s') % (i, EXT['Video'])):
            i += 1

        return ('tmp_%s.%s') % (i, EXT['Video'])

class ffmpegAudio:

    FFMPEG_BIN = "ffmpeg"

    def __init__(self):

        self.audio_filename = self.unique_filename()

        self.command = [ self.FFMPEG_BIN,
            '-f', 'pulse',
            '-ac', '2',
            '-ar', '48000',
            '-i', 'default',
           '-acodec', 'pcm_mulaw',
           '-y', TMP_DIR + '/' + self.audio_filename
        ]

    def start(self):
        import threading as th

        au_thread = th.Thread(target=self.record)
        au_thread.start()

    def record(self):
        import subprocess as sp

        self.pipe = sp.Popen(self.command, stderr=sp.PIPE)

    def stop(self):
        self.pipe.terminate()

    def unique_filename(self):
        global TMP_DIR, EXT

        i = 0

        while os.path.exists((TMP_DIR + '/' + 'tmp_%s.%s') % (i, EXT['Audio'])):
            i += 1

        return ('tmp_%s.%s') % (i, EXT['Audio'])

class AV_COMPILE:

    def __init__(self, au_in = TMP_DIR + '/' + 'out1.wav', vd_in = 
        TMP_DIR + '/' + 'simplescreenrecorder.mp4', out = TMP_DIR + '/' + 'simplescreenrecorder.mkv'):
        import subprocess as sp

        au_in = min(glob.iglob(TMP_DIR + '/*.wav'), key=os.path.getctime)
        vd_in = min(glob.iglob(TMP_DIR + '/*.mp4'), key=os.path.getctime)

        self.command = ('ffmpeg -i %s  -r 30 -i %s -shortest -c:a aac -c:v copy %s') % (au_in, vd_in, out)
        sp.call(self.command, shell=True)