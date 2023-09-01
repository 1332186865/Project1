# -*- coding: utf-8 -*-
#####################################
# File name : main.py
# Create date : 2019-01-10 16:39
# Modified date : 2019-01-11 14:52
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

import os
import time

import matplotlib
import matplotlib.pyplot as plt
import minpy.numpy as np
import minpy.numpy.random as random
from minpy.context import cpu, gpu

matplotlib.use('TkAgg')


def create_path(path):
    if not os.path.isdir(path):
        os.makedirs(path)


def get_file_full_name(path, name):
    create_path(path)
    if path[-1] == "/":
        full_name = path + name
    else:
        full_name = path + "/" + name
    return full_name


def create_file(path, name, open_type='w'):
    file_name = get_file_full_name(path, name)
    return open(file_name, open_type)


def _plot_record(record, full_path):
    _plot_cpu_gpu_time(record, full_path)
    _plot_acceleration(record, full_path)


def _get_full_path(repeats, size_begin, size_end):
    if not os.path.exists("./output"):
        os.makedirs("./output")
    path_str = "./output/%s_%s_%s" % (repeats, size_begin, size_end)
    return path_str


def _plot_cpu_gpu_time(record, full_path):
    float32_cpu_lt = []
    float64_cpu_lt = []
    float32_gpu_lt = []
    float64_gpu_lt = []
    steps = []
    for key in record:
        steps.append([key])
    steps.sort()

    for i in range(len(steps)):
        step_dic = record[steps[i][0]]
        float32_cpu_value = step_dic["float32_cpu"]
        float32_cpu_lt.append(float32_cpu_value)
        float64_cpu_value = step_dic["float64_cpu"]
        float64_cpu_lt.append(float64_cpu_value)

        float32_gpu_value = step_dic["float32_gpu"]
        float32_gpu_lt.append(float32_gpu_value)
        float64_gpu_value = step_dic["float64_gpu"]
        float64_gpu_lt.append(float64_gpu_value)

    float32_cpu_lt = np.array(float32_cpu_lt)
    float64_cpu_lt = np.array(float64_cpu_lt)
    float32_gpu_lt = np.array(float32_gpu_lt)
    float64_gpu_lt = np.array(float64_gpu_lt)

    float32_cpu_lt = float32_cpu_lt.asnumpy()
    float64_cpu_lt = float64_cpu_lt.asnumpy()
    float32_gpu_lt = float32_gpu_lt.asnumpy()
    float64_gpu_lt = float64_gpu_lt.asnumpy()

    steps = np.array(steps)
    steps = steps * steps
    steps = steps.asnumpy()

    float32_gpu_line, = plt.plot(steps, float32_gpu_lt)
    float64_gpu_line, = plt.plot(steps, float64_gpu_lt)
    float32_cpu_line, = plt.plot(steps, float32_cpu_lt)
    float64_cpu_line, = plt.plot(steps, float64_cpu_lt)

    line_lt = [
            float32_gpu_line,
            float64_gpu_line,
            float32_cpu_line,
            float64_cpu_line,
            ]

    labels_lt = (
            "float32 gpu",
            "float64 gpu",
            "float32 cpu",
            "float64 cpu",
            )
    plt.legend(handles=line_lt, labels=labels_lt, loc='best')
    full_path_name = "%s/cpu_gpu.jpg" % (full_path)
    #    plt.show()
    plt.savefig(full_path_name)
    plt.close()


def _plot_acceleration(record, full_path):
    float64_acceleration_lt = []
    float32_acceleration_lt = []
    steps = []
    for key in record:
        steps.append([key])
    steps.sort()

    for i in range(len(steps)):
        step_dic = record[steps[i][0]]
        float64_acceleration_value = step_dic["float64_acceleration"]
        float64_acceleration_lt.append(float64_acceleration_value)
        float32_acceleration_value = step_dic["float32_acceleration"]
        float32_acceleration_lt.append(float32_acceleration_value)

    float64_acceleration_lt = np.array(float64_acceleration_lt)
    float64_acceleration_lt = float64_acceleration_lt.asnumpy()
    float32_acceleration_lt = np.array(float32_acceleration_lt)
    float32_acceleration_lt = float32_acceleration_lt.asnumpy()
    steps = np.array(steps)
    steps = steps * steps
    steps = steps.asnumpy()
    float32_acceleration_line, = plt.plot(steps, float32_acceleration_lt)
    float64_acceleration_line, = plt.plot(steps, float64_acceleration_lt)

    line_lt = [
            float32_acceleration_line,
            float64_acceleration_line,
            ]

    labels_lt = (
            'float32 acceleration',
            'float64 acceleration',
            )

    plt.legend(handles=line_lt, labels=labels_lt, loc='best')
    full_path_name = "%s/acceleration.jpg" % (full_path)
    #    plt.show()
    plt.savefig(full_path_name)
    plt.close()


def _write_status(file_obj, i, time_lt):
    float32_acceleration = time_lt[1] / time_lt[3]
    float64_acceleration = time_lt[0] / time_lt[2]

    float64_cpu_str = "i:%s float64 cpu:%s" % (i, time_lt[0])
    float32_cpu_str = "i:%s float32 cpu:%s" % (i, time_lt[1])
    float64_gpu_str = "i:%s float64 gpu:%s" % (i, time_lt[2])
    float32_gpu_str = "i:%s float32 gpu:%s" % (i, time_lt[3])

    float32_acceleration_str = "float32 acceleration:%s" % float32_acceleration
    float64_acceleration_str = "float64 acceleration:%s" % float64_acceleration

    file_obj.write("%s\n" % float64_cpu_str)
    file_obj.write("%s\n" % float32_cpu_str)
    file_obj.write("%s\n" % float64_gpu_str)
    file_obj.write("%s\n" % float32_gpu_str)
    file_obj.write("%s\n" % float32_acceleration_str)
    file_obj.write("%s\n" % float64_acceleration_str)

    print(float64_cpu_str)
    print(float32_cpu_str)
    print(float64_gpu_str)
    print(float32_gpu_str)
    print(float32_acceleration_str)
    print(float64_acceleration_str)


def _record_status(record, i, time_lt):
    dic = {}
    dic["float64_cpu"] = time_lt[0]
    dic["float32_cpu"] = time_lt[1]
    dic["float64_gpu"] = time_lt[2]
    dic["float32_gpu"] = time_lt[3]
    dic["float64_acceleration"] = time_lt[0] / time_lt[2]
    dic["float32_acceleration"] = time_lt[1] / time_lt[3]

    record[i] = dic


def _randn(l, c):
    return random.randn(l, c)


def _get_take_time(s, repeats, data_type):
    x = _randn(s, s)
    y = _randn(s, s)
    x = np.array(x, dtype=data_type)
    y = np.array(y, dtype=data_type)

    t0 = time.time()
    for i in range(repeats):
        z = np.dot(x, y)
    z.asnumpy()
    t1 = time.time()

    all_time = t1 - t0
    avg_time = all_time / repeats
    return avg_time


def test_cpu_gpu(repeats, size_begin, size_end, step=1):
    record = {}
    full_path = _get_full_path(repeats, size_begin, size_end)
    file_obj = create_file(full_path, "output")
    for s in range(size_begin, size_end, step):
        time_lt = []
        with cpu():
            float64_cpu_time = _get_take_time(s, repeats, np.float64)
            float32_cpu_time = _get_take_time(s, repeats, np.float32)
            time_lt.append(float64_cpu_time)
            time_lt.append(float32_cpu_time)

        with gpu(0):
            float64_gpu_time = _get_take_time(s, repeats, np.float64)
            float32_gpu_time = _get_take_time(s, repeats, np.float32)
            time_lt.append(float64_gpu_time)
            time_lt.append(float32_gpu_time)

        _write_status(file_obj, s, time_lt)
        _record_status(record, s, time_lt)

    file_obj.close()
    _plot_record(record, full_path)


def test_matmul(repeats, max_size, step):
    for i in range(int(max_size / step)):
        size_begin = 1 + i * step
        size_end = (i + 1) * step
        test_cpu_gpu(repeats, size_begin, size_end)

    size_begin = 1
    size_end = max_size
    test_cpu_gpu(repeats, size_begin, size_end)


def test():
    repeats = 300
    max_size = 500
    step = 100
    test_matmul(repeats, max_size, step)

    #   repeats = 5
    #   size_begin = 1
    #   size_end = 3000
    #   test_cpu_gpu(repeats, size_begin, size_end)

    # repeats = 1
    # size_begin = 10
    # size_end = 100000
    # step = 500
    # test_cpu_gpu(repeats, size_begin, size_end, step)

    # repeats = 100
    # size_begin = 1000
    # size_end = 20000
    # step = 1000
    # test_cpu_gpu(repeats, size_begin, size_end, step)


test()
