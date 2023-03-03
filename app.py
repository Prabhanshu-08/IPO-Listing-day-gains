import numpy as np
from flask import Flask, request, render_template
import pickle


#Loading the pre-trained model (Pickle file)
model_xg_boost = pickle.load(open("Models/Xgboost.pkl", "rb"))
model_cat_boost = pickle.load(open("Models/Catboost.pkl", "rb"))
model_RF = pickle.load(open("Models/RandomForestRegressor.pkl", "rb"))
model_Ada_boost = pickle.load(open("Models/AdaBoost.pkl", "rb"))
model_MLP = pickle.load(open("Models/MLP.pkl", "rb"))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():

    features = [x for x in request.form.values()] 
    model = features.pop()
    features = [float(x) for x in features]
    issue_price = features.pop()

    features=np.array(features)
    features=np.expand_dims(features,axis=0)

    if model == 'XgBoost':
        gain=round(model_xg_boost.predict(features)[0])
        closing_price = round(issue_price * (1+gain/100),2)

        return render_template('index.html', prediction_text = f'The IPO may have a listing day gain of {gain}% and closing price of {closing_price}. Please do not consider this as any investment advice and do your own research.')
    
    elif model == 'CatBoost':
        gain=round(model_cat_boost.predict(features)[0],2)
        closing_price = round(issue_price * (1+gain/100),2)

        return render_template('index.html', prediction_text = f'The IPO may have a listing day gain of {gain}% and closing price of {closing_price}. Please do not consider this as any investment advice and do your own research.')
    
    elif model == 'RandomForestRegressor':
        gain=round(model_RF.predict(features)[0],2)
        closing_price = round(issue_price * (1+gain/100),2)

        return render_template('index.html', prediction_text = f'The IPO may have a listing day gain of {gain}% and closing price of {closing_price}. Please do not consider this as any investment advice and do your own research.')
    
    elif model == 'AdaBoost':
        gain=round(model_Ada_boost.predict(features)[0],2)
        closing_price = round(issue_price * (1+gain/100),2)

        return render_template('index.html', prediction_text = f'The IPO may have a listing day gain of {gain}% and closing price of {closing_price}. Please do not consider this as any investment advice and do your own research.')
    
    elif model == 'MLPRegressor':
        gain=round(model_MLP.predict(features)[0],2)
        closing_price = round(issue_price * (1+gain/100),2)

        return render_template('index.html', prediction_text = f'The IPO may have a listing day gain of {gain}% and closing price of {closing_price}. Please do not consider this as any investment advice and do your own research.')


if __name__ == "__main__":
    app.run()