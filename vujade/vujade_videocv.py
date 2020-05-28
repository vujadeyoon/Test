import cv2


class VideoReader:
    def __init__(self, _path_video):
        if _path_video is None:
            raise Exception('The variable, _path_video, should be assigned.')

        self.path_video = _path_video
        self.fp = cv2.VideoCapture(self.path_video)

        self.height = int(self.fp.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.width = int(self.fp.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.fps = float(self.fp.get(cv2.CAP_PROP_FPS))
        self.num_frames = int(self.fp.get(cv2.CAP_PROP_FRAME_COUNT))

    def read(self):
        ret, frame = self.fp.read()

        return frame

    def release(self):
        self.fp.release()


class VideoWriter:
    def __init__(self, _path_video, _resolution=(1080, 1920), _fps=60.0, _fourcc=cv2.VideoWriter_fourcc(*'MJPG')):
        if _path_video is None:
            raise Exception('The variable, _path_video, should be assigned.')

        self.path_video = _path_video
        self.height = int(_resolution[0])
        self.width = int(_resolution[1])
        self.fps = float(_fps)
        self.fourcc = _fourcc
        self.fp = cv2.VideoWriter(self.path_video, self.fourcc, self.fps, (self.width, self.height))

    def write(self, _ndarr_frame):
        self.fp.write(image=_ndarr_frame)

    def release(self):
        self.fp.release()