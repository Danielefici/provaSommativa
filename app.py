import streamlit as st
import numpy as np
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def main():
    st.title("Prova")


    df = pd.read_csv('https://frenzy86.s3.eu-west-2.amazonaws.com/python/data/formart_house.csv')
    df=df.iloc[:-1]
    df=df.apply(pd.to_numeric)
    fig=plt.figure(figsize=(12,10))
    plt.title('dati')
    sns.heatmap(df.corr(),annot=True , cmap="PiYG")
    st.pyplot(fig)


    crim=st.number_input('inserisci crim',1,10000,500)
    zn=st.number_input('inserisci zn',1,10000,500)
    indus=st.number_input('inserisci indus',1,10000,500)
    chas=st.number_input('inserisci indus',0,10,0)
    nox=st.number_input('inserisci nox',0.0,1.0,0.5)
    rm=st.number_input('inserisci rm',1,10,5)
    age=st.number_input('inserisci age',18,100,30)
    dis=st.number_input('inserisci dis',1,10,2)
    rad=st.number_input('inserisci rad',1,3,1)
    tax=st.number_input('inserisci tax',1,500,100)
    ptratio=st.number_input('inserisci ptratio',1,50,10)
    b=st.number_input('inserisci b',1,300,100)
    

    lstat=st.number_input('inserisci istat',1,10,5)

    load_model=joblib.load('prova_test.pkl')
    pred=load_model.predict([[crim,zn,indus,chas,nox,rm,age,dis,rad,tax,ptratio,b,lstat,]])
    st.write(f"il prezzo é: euro{round(pred[0],2)}")
    
    


if __name__=="__main__":
    main()   
