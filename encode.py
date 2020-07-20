from sklearn import preprocessing
import pandas as pd
import numpy as np

def encode(csv):
    cut = csv.cut
    color = csv.color
    clarity = csv.clarity

    le_cut = preprocessing.LabelEncoder()
    le_color = preprocessing.LabelEncoder()
    le_clarity = preprocessing.LabelEncoder()

    cut_numeric = le_cut.fit_transform(cut)
    color_numeric = le_color.fit_transform(color)
    clarity_numeric = le_clarity.fit_transform(clarity)
    clean = csv
    clean["cut_numeric"] = cut_numeric
    clean["color_numeric"] = color_numeric
    clean["clarity_numeric"] = clarity_numeric
    clean.drop(columns=["cut", "color", "clarity"], inplace = True)
    return clean