# -*- coding: utf-8 -*-
import os
from threading import Thread
from Queue import Queue

num_threads = 2
in_queue = Queue()


def produce_file(dir_path):
    '''返回一个目录下所有的文件'''
    all_files = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            all_files.append(file_path)
    return all_files


def do(i, iq):
    while 1:
        path = iq.get()
        print "Thread {}:{}".format(i, path)
        iq.task_done()


if __name__ == "__main__":
    for i in range(num_threads):
        worker = Thread(target=do, args=(i, in_queue))
        worker.setDaemon(True)
        worker.start()
    print "Produce all files"
    map(in_queue.put, produce_file('/Users/zfp/Downloads'))
    print "Main Thread Waiting"
    in_queue.join()
