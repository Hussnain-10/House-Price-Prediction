import pickle 
with open('random_forest_model.pkl', 'rb') as file:
    model=pickle.load(file)

new_house=[[
    1,
    1.9,
    4827,
    1979,
    2,
    48.60,
    5,
    221958.0
]]
prediction=model.predict(new_house)

print(prediction)


# Now this model work the correct not any error in it 