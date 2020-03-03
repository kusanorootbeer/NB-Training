# -*- coding: utf-8 -*-
import pdb


import loader.load as load
import preprocess.normalize as norm


def main():
    path = './debug/wine.csv'

# load
    df_x, df_y, df_name = load.load_csv(path, label_col=[0])

# normalize
    data_x = norm.min_max_normalization(df_x.values)
    data_y, label_restorer = norm.label_quantization(df_y.values.flatten())

    pdb.set_trace()


if __name__ == '__main__':
    main()
