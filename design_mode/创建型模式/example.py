import torch
import numpy as np


def generate_crop_start_point(window, start, end, step):
    """
    计算一维切片在指定范围内的各个起始切割位置（最后一个为最右边界）
    """
    final_list = [start]
    # 当窗口大小大于等于整个边界范围
    if window + start >= end:
        final_list.append(end)
        return final_list
    while True:
        if final_list[-1] + step + window < end:
            final_list.append(final_list[-1]+step)
        else:
            final_list += [end-window, end]
            return final_list


def generate_crop_window(window, start, end, step):
    """
    计算一维切片所有窗口的范围
    :param window: 一维切片尺寸
    :param start: 指定范围的起点
    :param end: 指定范围的终点
    :param step: 切片的步长
    :return:
    """
    crop_start_point = generate_crop_start_point(window, start, end, step)
    crop_window = [[start, start+window] for start in crop_start_point[:-1]]
    crop_window[-1][-1] = crop_start_point[-1]
    return crop_window


def generate_crop_window_with_margin(window, start, end, step):
    """
    计算一维切片所有窗口的范围，并且生成每个窗口与其他窗口的左右重叠尺寸
    :param window: 一维切片尺寸
    :param start: 指定范围的起点
    :param end: 指定范围的终点
    :param step: 切片的步长
    :return:
    """
    crop_window = generate_crop_window(window, start, end, step)
    crop_window_length = len(crop_window)
    if crop_window_length == 1:
        rest = (abs(end - start) - window) / 2
        assert rest <= 0, '存在误差'
        crop_window[0] += [rest, rest]
        return crop_window
    else:
        rest = crop_window[-2][1] - crop_window[-1][0]
        assert rest >= 0, '切片的尺寸应该大于等于步长的尺寸'
        if crop_window_length == 2:
            crop_window[-2] += [0, rest]
        else:
            crop_window[-2] += [step, rest]
        crop_window[-1] += [rest, 0]
        for index, value in enumerate(crop_window[:-2]):
            if index == 0:
                crop_window[index] += [0, step]
                continue
            crop_window[index] += [step, step]
        return crop_window


# b = generate_crop_window_with_margin(2.1, 4.3, 5.9, 1.5)
# print(b)
print(int(2.3))
print(int(2.6))
