# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 15:14:59 2019

@author: Viktoryia.Davydovich
"""

import numpy as np
import pandas as pd

# set the matplotlib backend so figures can be saved in the background
import matplotlib
matplotlib.use("Agg")
 
# import the necessary packages
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import tensorflow as tf
import matplotlib.pyplot as plt

BATCH_SIZE = 130
EPOCHS = 1000

training_data = 'D:/Plane/planesnet'
