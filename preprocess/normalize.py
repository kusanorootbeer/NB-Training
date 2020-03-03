# -*- coding: utf-8 -*-
import numpy as np


def min_max_normalization(arr2d):
    maxs = arr2d.max(axis=0)
    mins = arr2d.max(axis=0)
    norms = (arr2d - mins)/(maxs - mins)
    return norms


def z_score_normalization(arr2d):
    means = arr2d.mean(axis=0)
    stds = arr2d.std(axis=0)
    z_scores = (arr2d-means)/stds
    return z_scores

# 0 start quantization


def label_quantization(label):
    label_set = np.unique(label)
    num_label_set = len(label_set)
    quantized_label_set = np.arange(num_label_set)
    quantized_label = np.empty(shape=label.shape)

    for l, ql in zip(label_set, quantized_label_set):
        indices = np.where(label == l)
        quantized_label[indices] = ql
    return quantized_label, LabelReQuantizer(label_set, quantized_label_set)


class LabelReQuantizer():
    def __init__(self, label_set, quantized_label_set):
        self.label_set = label_set
        self.q_label_set = quantized_label_set

    def __call__(self, q_label):
        label = np.empty(shape=q_label.shape)
        for l, ql in zip(self.label_set, self.q_label_set):
            indices = np.where(q_label == ql)
            label[indices] = l
        return label
