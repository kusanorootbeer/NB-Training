# -*- coding: utf-8 -*-
import loader.load as load


def main():
    path = './test/wine.csv'
    df_x, df_y, df_name = load.load_csv(path, label_col=[0])


if __name__ == '__main__':
    main()
