from rdkit.Chem import MolFromSmiles
from rdkit.Chem import Descriptors
import pandas as pd
import numpy as np
from xgboost import XGBRegressor
from sklearn.feature_selection import VarianceThreshold
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

def pred_lys():
    #upload dataset
    df_bioc = pd.read_excel("lys_dataset_calculator.xlsx")
    df_bioc.drop("Outcome", axis=1, inplace=True)
    df_desc = pd.read_excel("SMILES_Lys.xlsx")
    #descriptors calculation
    mol = [ MolFromSmiles(smile) for smile in df_desc["Smiles"]]
    desc = [Descriptors.CalcMolDescriptors(i) for i in mol]
    df = pd.DataFrame(desc)
    df["Name"] = df_desc["Name"]
    #merging and data cleaning
    df_final = pd.merge(df_bioc, df, on="Name",how="left")
    df_final.drop("Name",axis=1, inplace=True)
    df_final["Buffer"] = LabelEncoder().fit_transform(df_final['Buffer'])
    df_final["mAb"] = LabelEncoder().fit_transform(df_final['mAb'])
    df_final["Activation"] = LabelEncoder().fit_transform(df_final['Activation'])
    X = df_final.drop(["DAR"], axis=1)
    y_train = df_final['DAR'].values[:-1]
    sel = VarianceThreshold(threshold=(.8 * (1 - .8)))
    X2 = sel.fit_transform(X)
    concol = [column for column in  X.columns if column in X.columns[sel.get_support()]]
    #scaling
    X = pd.DataFrame(X2,columns=concol)
    scaler = MinMaxScaler()
    X_norm = scaler.fit_transform(X)
    X_norm_train = X_norm[:-1]
    X_norm_test = X_norm[-1].reshape(1,-1)
    #model training
    xgb = xgb.XGBRegressor( colsample_bytree=1.0, learning_rate=0.3, max_depth=5, n_estimators=500,
    reg_alpha=0.1, subsample=0.6, random_state=42 )
    xgb.fit(X_norm_train, y_train)
    pred = xgb.predict(X_norm_test)
    pred = np.round(pred,1)
    if pred[0] < 0.0:
        pred[0] = 0.0
    df_bioc['DAR'].iloc[-1] = pred
    #results
    return df_bioc


def pred_cys():
    # upload dataset
    df_bioc = pd.read_excel("cys_dataset_calculator.xlsx")
    df_bioc.drop("Outcome", axis=1, inplace=True)
    df_desc = pd.read_excel("SMILES_Cys.xlsx")
    # descriptors calculation
    mol = [ MolFromSmiles(smile) for smile in df_desc["Smiles"]]
    desc = [Descriptors.CalcMolDescriptors(i) for i in mol]
    df = pd.DataFrame(desc)
    df["ID"] = df_desc["ID"]
    # merging and data cleaning
    df_final = pd.merge(df_bioc, df, on="ID", how="left")
    df_final.drop("ID", axis=1, inplace=True)
    #df_final.dropna(axis=1, inplace=True)
    df_final["Reductant"] = LabelEncoder().fit_transform(df_final['Reductant'])
    df_final["Buffer"] = LabelEncoder().fit_transform(df_final['Buffer'])
    df_final["mAb"] = LabelEncoder().fit_transform(df_final['mAb'])
    df_final["Method"] = LabelEncoder().fit_transform(df_final['Method'])
    X = df_final.drop(["DAR"], axis=1)
    y_train = df_final['DAR'].values[:-1]
    sel = VarianceThreshold(threshold=(.8 * (1 - .8)))
    X2 = sel.fit_transform(X)
    concol = [column for column in  X.columns if column in X.columns[sel.get_support()]]
    # scaling
    X = pd.DataFrame(X2, columns=concol)
    scaler = MinMaxScaler()
    X_norm = scaler.fit_transform(X)
    X_norm_train = X_norm[:-1]
    X_norm_test = X_norm[-1].reshape(1,-1)
    # model training
    xgb = xgb.XGBRegressor(colsample_bytree=1.0,  learning_rate=0.01,  max_depth=10,  n_estimators=500,reg_alpha=0.1,subsample=0.8, random_state=42)
    xgb.fit(X_norm_train, y_train)
    pred = xgb.predict(X_norm_test)
    pred = np.round(pred,1)
    if pred[0] < 0.0:
        pred[0] = 0.0
    df_bioc['DAR'].iloc[-1] = pred
    #results
    return df_bioc
