import os
import numpy as np
import time
import cv2
import ray
import ffmpeg
from vujade import vujade_videocv as videocv_
from vujade import vujade_imgcv as imgcv_

num_cpus = os.cpu_count()

is_process_single = False
is_process_multi = True
is_ray = False

process1 = (
    ffmpeg
    .input(os.path.join(os.getcwd(), 'test_input', 'test_1.mp4'))
    .output('pipe:', format='rawvideo', pix_fmt='bgr24')
    .run_async(pipe_stdout=True)
)



if is_ray is True:
    ray.init(num_cpus=num_cpus)

    @ray.remote(num_cpus=num_cpus)
    def worker(_frame, _path_img):
        cv2.imwrite(filename=_path_img, img=_frame)



if __name__ == "__main__":
    eps_val = 1e-9

    name_video_src = 'test_1.mp4'
    path_video_src = os.path.join(os.getcwd(), 'test_input', name_video_src)
    video_src = videocv_.VideoReader(_path_video=path_video_src)

    path_img_dst = os.path.join(os.getcwd(), 'test_output')

    if is_process_multi is True:
        img_dst = imgcv_.ImwriterFast(_num_processes=num_cpus)
        img_dst.begin_background()

    time_start = time.time()

    for idx in range(video_src.num_frames):
        frame_src = video_src.read()
        # in_bytes = process1.stdout.read(video_src.width * video_src.height * 3)
        # frame_src = (
        #     np
        #     .frombuffer(in_bytes, np.uint8)
        #     .reshape([video_src.height, video_src.width, 3])
        # )

        # if is_process_single is True:
        #     cv2.imwrite(filename=os.path.join(path_img_dst, 'frame_{}.png'.format(idx)), img=frame_src)
        #
        # if is_process_multi is True:
        #     img_dst.save_results(_save_list=[frame_src], _path_img=os.path.join(path_img_dst, 'frame'), _postifx_num=idx)
        #
        # if is_ray is True:
        #     frame = ray.put(frame_src)
        #     result_ids = [worker.remote(_frame=frame, _path_img=os.path.join(path_img_dst, 'frame_{}.png'.format(idx))) for i in range(num_cpus)]
        #     results = ray.get(result_ids)


    time_end = time.time()

    video_src.release()

    if is_process_multi is True:
        img_dst.end_background()

    time_total = time_end - time_start
    time_avg = time_total / video_src.num_frames
    print('Total time:    {:.4f}'.format(time_total))
    print('AVG time[FPS]: {:.4f}[{:.2f} FPS]'.format(time_avg, 1/(time_avg + eps_val)))