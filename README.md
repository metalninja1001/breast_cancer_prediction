# Breast Cancer Prediction
This is a jupyter notebook that can be used to predict the likelihood of breast cancer given a data subject.

## Required modules:
- Tensorflow
- scikit-learn
- pandas

## How to use:
- 1 - Using the `csvtrainer.ipynb` notebook, you will be prompted to enter a csv file and an optimizer. I have included a test dataset which is the breast cancer Wisconsin (diagnostic) dataset. See link for more :  https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data. Available optimizers can be found here : https://keras.io/api/optimizers/
- 2 - Using the `liketest.ipynb` notebook can you then test the likelihood of breast cancer occuring given a dataset. You will be prompted to enter a dataset to test against and an .h5 model file. You will find a copy of these in the models and dataset directories respectively. You will also be prompted to enter the column names of any columns containing NaN values separated by commas.

## Data-cleaning:
- If you require cleaning the data, I have included a notebook to perform this task. See `datasets` directory for more.
#### Usage:
  - Once you run the notebook, will you be prompted to enter the filename of the dataset you would like to clean as well as the columns you would like to drop.

## Important checks:
- It is important that you check which columns contain null values or NaN values as they need to be removed. The functionality to do so is already built-in. If you are unsure of how to do so, see below code :\
`import numpy as np` \
`import pandas as pd` \
`from sklearn.datasets import load_breast_cancer` \
\
`# Load the breast cancer dataset` \
`data = pd.read_csv("data.csv")` \
`df = pd.DataFrame(data)` \
`print(data)`
