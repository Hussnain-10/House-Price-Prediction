import pandas as pd
def preprocess_data(file_path):
    df=pd.read_csv(file_path)
    df['ZipCode']=df['ZipCode'].astype(str)
    zip_avg_price=df.groupby('ZipCode')['Price'].mean()
    df['ZipEncoded']=df['ZipCode'].map(zip_avg_price)
    df=df.drop(columns=['ZipCode','LotSize'])
    return df