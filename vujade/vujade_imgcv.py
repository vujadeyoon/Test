import os
import cv2
from vujade import vuajde_multiprocess as multiprocess_


class ImwriterFast(multiprocess_.BaseMultiProcess):
    def __init__(self, _num_processes=os.cpu_count()):
        multiprocess_.BaseMultiProcess.__init__(self, self._target_method, _num_processes)
        self.n_processes = _num_processes

    def _target_method(self, queue):
        # Todo: To be coded.
        while True:
            if not queue.empty():
                filename, ndarr = queue.get()
                if filename is None:
                    break
                cv2.imwrite(filename=filename, img=ndarr)


    def proc_enqueue(self, _list_img, _path_img, _postifx_num=None):
        # Todo: To be coded.
        for idx, img in enumerate(_list_img):
            if _postifx_num is None:
                path = '{}.png'.format(_path_img)
            else:
                path = '{}_{:08d}.png'.format(_path_img, _postifx_num)

            self.queue.put((path, img))
