# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import pdb

# def load_csv(path, *, delimiter=",", label_col=None, skip_row=[], skip_col=[], view=True):
#     skip_col.append(label_col)
#     try:
#         a = np.loadtxt(path, delimiter=delimiter)
#     except:
#         print("Perhaps, contaminate string data.")
#     _raw = [i for i in range(a.shape[0]) if i not in skip_row]
#     _col = [i for i in range(a.shape[1]) if i not in skip_col]
#
#     a = a[_raw][:, _col]
#     if view:
#         print("loaded csv from: {}".format(path))
#     return a

# skip_row indexは header分も考慮して入力すること


def load_csv(path, *, delimiter=',', label_col=None, header_row=None, index=None, skip_row=[], skip_col=[]):
    try:
        x = pd.read_csv(path, header=header_row, index_col=index, usecols=lambda x: x is not in skip_col, skiprows=skip_row)
    except:
        try:
            x = pd.read_table(path, header=header_row, index_col=index, usecols=lambda x: x is not in skip_col, skiprows=skip_row)
        except:
            print(path)
            pdb.set_trace()

    if label_col is not None:
        y = x[label_col]
        x.drop(label_col, axis=1)
        return x, y
    else:
        return x


def load_csv_dir():
    pass


def load_img():
    print("load img")


__all__ = (load_csv, load_csv_dir, load_img)
