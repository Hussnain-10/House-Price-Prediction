from preprocess import preprocess_data
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error,r2_score
df=preprocess_data(r'C:\Users\DELL\AppData\Local\Temp\f04e54ec-9ff1-48fd-91e5-3aada5eb1292_archive (1).zip.292\usa_housing_kaggle.csv')
X=df.drop('Price',axis=1)
y=df['Price']
scaler=StandardScaler()
X_scaled=scaler.fit_transform(X)
X_train,X_test,y_train,y_test=train_test_split(X_scaled,y,test_size=0.33,random_state=42)
model=RandomForestRegressor()
model.fit(X_train,y_train)
y_pred_Rfr=model.predict(X_test)
y_pred_Rfr
print("MAE: ",mean_absolute_error(y_test,y_pred_Rfr))
print("MSE: ",mean_squared_error(y_test,y_pred_Rfr))
print("R2: ",r2_score(y_test,y_pred_Rfr))
with open('random_forest_model.pkl',
'wb') as f:
    pickle.dump(model,f)
    
import os
print(os.getcwd())