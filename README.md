# NB_parts

https://github.com/kusanorootbeer/NB_main で import するようのパーツをこっちに集める

# Rule

- preprocess(raw_dataX=np.array, raw_labelY={np.array, None}, optional={image, signal, vector})
  - return dataX=np.array, labelY={np.array, None}
- CV_sprit(dataX=np.array, labelY={np.array, None}, optional)
  - return dataX=np.array, labelY={np.array, None}, CV_id
  - return mask
  - 考え中です
- model(trainX=np.array, TrainY={np.array, None}, ValidX={np.array, None}, ValidY={np.array, None})
- visualize(dataX=np.array, labelY={np.array, None}, optional)

## Concrete Rule

- dataX.shape
  - image: (none, w, h, c)
    - if gray image: c=1
  - signal: (none, data, time)
  - vector: (none, data)
- labelY.shape
  - onehot label
