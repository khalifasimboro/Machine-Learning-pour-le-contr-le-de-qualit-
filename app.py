from flask import Flask, request, jsonify
from joblib import dump, load
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np
app = Flask(__name__)

# chargement des modèles
model = load('/home/falleiz/Bureau/TP_1_ ML _ contrôle_qualité/random_forest_model.pkl') # Modèle de prédiction
scaler = load('/home/falleiz/Bureau/TP_1_ ML _ contrôle_qualité/scaler_model.pkl')  # Modèle de normalisation
pca_model = load('/home/falleiz/Bureau/TP_1_ ML _ contrôle_qualité/pca_model.pkl')  # Modèle PCA

@app.route('/predict',methods=['POST'])
def predict():

    data = request.get_json()
    # Convertir le modèle en un array puis le normaliser puisque l'apprentissage a commencé par la normalisation
    input_scaled = scaler.transform(np.array(data['input']).reshape(1, -1))
    #reduire la dimensionalité
    input_pca = pca_model.transform(input_scaled)
    #input_data = normalisation(np.array(data['input']).reshape(1,-1))
    # faire la prédiction
    prediction = model.predict(input_pca)
    return jsonify({'prediction': int(prediction)})


@app.route('/test',methods=['GET'])
def bonjour():
    print ("hello")
    return "bonjour"



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
