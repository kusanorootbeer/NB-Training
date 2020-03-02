# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd


def load_csv(path, *, delimiter=",", label_col="None", skip_row=[], skip_col=[], view=True):
    skip_col.append(label_col)
    try:
        a = np.loadtxt(path, delimiter=delimiter)
    except:
        print("Perhaps, contaminate string data.")
    _raw = [i for i in range(a.shape[0]) if i not in skip_row]
    _col = [i for i in range(a.shape[1]) if i not in skip_col]

    a = a[_raw][:, _col]
    if view:
        print("loaded csv from: {}".format(path))
    return a


def load_csv_dir():
    pass


def load_img():
    print("load img")


__all__ = (load_csv, load_csv_dir, load_img)
