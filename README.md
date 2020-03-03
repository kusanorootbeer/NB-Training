# NB_parts

https://github.com/kusanorootbeer/NB_main で import するようのパーツをこっちに集める

# Rule

- loader(path, args)
  - csv:
    - return pd.dataframe
    - return np.array
    - 考え中
  - img:
    - return np.array
    - return pil
    - 考え中
  - json(ある？):
    - 考え中
- preprocess(raw_dataX=np.array, raw_labelY={np.array, None}, optional={image, signal, vector})
  - return dataX=np.array, labelY={np.array, None}
- CV_sprit(dataX=np.array, labelY={np.array, None}, optional)
  - return dataX=np.array, labelY={np.array, None}, CV_id
  - return mask
  - 考え中
- model(trainX=np.array, TrainY={np.array, None}, ValidX={np.array, None}, ValidY={np.array, None})
- visualize(dataX=np.array, labelY={np.array, None}, optional)

# Outlook

- classification task
- model optimization by **_optune_**
  `conda install -c conda-forge optuna`

## Concrete Rule

- dataX.shape
  - image: (none, w, h, c)
    - if gray image: c=1
  - signal: (none, data, time)
  - vector: (none, data)
- labelY.shape
  - onehot label

## Post Scripts

`/debug debug.py`は Jupyter Notebook を介さず，local で実行するときにつかう
