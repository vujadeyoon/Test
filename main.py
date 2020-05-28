import os
import numpy as np
import time
import cv2
from vujade import vujade_videocv as videocv_

if __name__ == "__main__":
    eps_val = 1e-9

    name_video_src = 'test_1.mp4'
    name_video_dst = 'test_1_out.avi'
    path_video_src = os.path.join(os.getcwd(), 'test_video', name_video_src)
    path_video_dst = os.path.join(os.getcwd(), 'test_video', name_video_dst)

    video_src = videocv_.VideoReader(_path_video=path_video_src)
    video_dst = videocv_.VideoWriter(_path_video=path_video_dst, _resolution=(video_src.width, video_src.height), _fps=video_src.fps)

    time_total = 0.0
    for idx in range(video_src.num_frames):
        frame_src = video_src.read()
        print(idx, type(frame_src), frame_src.shape, frame_src.dtype)

        time_start = time.time()
        video_dst.write(_ndarr_frame=frame_src)
        time_total += (time.time() - time_start)

    video_src.release()
    video_dst.release()

    time_avg = time_total / video_src.num_frames
    print('Total time:    {:.4f}'.format(time_total))
    print('AVG time[FPS]: {:.4f}[{:.2f} FPS]'.format(time_avg, 1/(time_avg + eps_val)))