################################
# 00. 필요한 파이썬 라이브러리 불러오기
################################

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import sys
import plotly.express as px
from numpy import random
import missingno

from sklearn.preprocessing import StandardScaler, normalize
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.linear_model import LogisticRegression
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier

import pydot
from IPython.display import Image

amz_data = pd.read_csv('/Users/jungmyungkim/Desktop/coding/FastCampus/머신러닝&데이터분석/[강의자료] 한 번에 끝내는 머신러닝과 데이터 분석 A-Z/Part5. 파이썬 머신러닝 프로젝트/2. 코드자료/3. Data/Ch 13/amz_data.csv')
amz_data.head()

amz_data = amz_data.drop(['index'], axis=1, errors='ignore')
amz_data.info()
amz_data.shape # (737, 11)
