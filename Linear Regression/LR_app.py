
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.linear_model import LinearRegression


st.write("""
# House Price Prediction App

This app predicts the **House Price**
""")


## Loads the Boston House Price Dataset

boston = datasets.load_boston()

X = pd.DataFrame(boston.data, columns=boston.feature_names)
y = pd.DataFrame(boston.target, columns=["Price"])


## Sidebar

# Header of specify input parameters

st.sidebar.header('Specify input parameters')

def user_input_features():
    CRIM = st.sidebar.slider('CRIM', float(X.CRIM.min()), float(X.CRIM.max()), float(X.CRIM.mean()))
    ZN = st.sidebar.slider('ZN', float(X.ZN.min()), float(X.ZN.max()), float(X.ZN.mean()))
    INDUS = st.sidebar.slider('INDUS', float(X.INDUS.min()), float(X.INDUS.max()), float(X.INDUS.mean()))
    CHAS = st.sidebar.slider("CHAS", float(X.CHAS.min()), float(X.CHAS.max()), float(X.CHAS.mean()))
    NOX = st.sidebar.slider("NOX", float(X.CHAS.min()), float(X.CHAS.max()), float(X.CHAS.mean()))
    RM = st.sidebar.slider("RM", float(X.RM.min()), float(X.RM.max()), float(X.RM.mean()))
    AGE = st.sidebar.slider("AGE", float(X.AGE.min()), float(X.AGE.max()), float(X.AGE.mean()))
    DIS = st.sidebar.slider("DIS", float(X.DIS.min()), float(X.DIS.max()), float(X.DIS.mean()))
    RAD = st.sidebar.slider("RAD", float(X.RAD.min()), float(X.RAD.max()), float(X.RAD.mean()))
    TAX = st.sidebar.slider("TAX", float(X.TAX.min()), float(X.TAX.max()), float(X.TAX.mean()))
    PTRATIO = st.sidebar.slider("PTRATIO", float(X.PTRATIO.min()), float(X.PTRATIO.max()), float(X.PTRATIO.mean()))
    B = st.sidebar.slider("B", float(X.B.min()), float(X.B.max()), float(X.B.mean()))
    LSTAT = st.sidebar.slider("LSTAT", float(X.LSTAT.min()), float(X.LSTAT.max()), float(X.LSTAT.mean()))

    data = {'CRIM': CRIM,
            'ZN': ZN,
            'INDUS': INDUS,
            'CHAS': CHAS,
            'NOX': NOX,
            'RM': RM,
            'AGE': AGE,
            'DIS': DIS,
            'RAD': RAD,
            'TAX': TAX,
            'PTRATIO': PTRATIO,
            'B': B,
            'LSTAT': LSTAT}


    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

# Main Panel


# Print Specified input parameters

st.header('Specified Input Parameters')
st.write(df)
st.write('------')


# Build Regression Model

model = LinearRegression()

model.fit(X, y)


# Apply model to make prediction

prediction = model.predict(df)

st.header('Prediction of Price')
st.write(prediction)
st.write('-----')


