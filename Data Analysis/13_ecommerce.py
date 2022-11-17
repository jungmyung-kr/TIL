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
amz_data.shape # (737, 11)

################################
# 01. 데이터 탐색 
#################################

##### 1. 데이터 탐색 
####### 1) 데이터 타입

amz_data.info()
# column : object 2 / float 9

######## 2) 데이터 통계값 

amz_data.describe()

####### 3) 결측값

missing_df = amz_data.isnull().sum(axis=0).reset_index()
missing_df.columns= ['column_name', 'missing_count']
missing_df = missing_df.loc[missing_df['missing_count']>0]
missing_df = missing_df.sort_values(by='missing_count')
missing_df

# seavorn 패키지 heatmap을 통해 시각화 확인
sns.heatmap(amz_data.isnull(), cbar=False, yticklabels=False, cmap='viridis')
plt.show()

# missingno 패키지를 통해 확인
missingno.matrix(amz_data, figsize = (10, 5))
plt.show()
# 목적 자체가 결측값 시각화인 패키지이므로 seaborn보다 간단

num_cols = amz_data.select_dtypes(include=np.number).shape[1]

amz_data = amz_data[amz_data.select_dtypes(include=np.number).isnull().sum(axis=1)!=num_cols]
amz_data