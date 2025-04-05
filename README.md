# Machine-Learning-pour-le-contr-le-de-qualit-e

L’objectif est de développer un modèle de classification pour le contrôle qualité des puces semi-conductrices.

Ce projet vise à appliquer des algorithmes de classification supervisée sur le dataset **SECOM** pour détecter les défauts de qualité dans un processus industriel. Le modèle final est déployé via une API Flask.

---

## 1 Démarche Retenue

1. **Nettoyage & Prétraitement**
   - Suppression des colonnes à variance minimale
   - Imputation des valeurs manquantes
   - Normalisation via `MinMaxScaler`
   - Réduction de dimension avec **PCA**

2. **Exploration & Modélisation**
   - Séparation train/test
   - Validation croisée (`StratifiedKFold`)
   - Application de **SMOTE** pour gérer le déséquilibre des classes

3. **Modèles testés**
   - Arbre de Décision
   - Random Forest
   
4. **Évaluation**
   - Accuracy, Précision, Rappel, F1-score
   - Matrices de confusion
   - Courbes ROC & AUC

5.**Archivage wandbiaises**

6. **Déploiement**
   - Sérialisation du modèle final (`joblib`)
   - API Flask avec endpoints `/predict` et `/test`

---

## 2 Tableau récapitulatif des performances

| Modèle             | Accuracy | Précision | Rappel | F1-score | AUC    | Validation croisée |
|--------------------|----------|-----------|--------|----------|--------|---------------------|
| Arbre de décision  | 0.79     | 0.80      | 0.79   | 0.79     | 0.84   | ✅                   |
| Random Forest      | 0.89     | 0.88      | 0.86   | 0.87     | 0.92   | ✅                   |

> ✅ **Random Forest** a été retenu comme modèle final pour le déploiement.

---

## 3 Structure du projet
tp1-ml-controle-qualite/ │ ├── data/ # Dataset brut │ └── secom.csv │ ├── models/ # Modèles sauvegardés │ ├── random_forest_model.pkl │ ├── scaler_model.pkl │ └── pca_model.pkl │ ├── app/ # Code de l'API Flask │ └── api.py │ ├── notebooks/ # Explorations & entraînement │ └── exploration_modelisation.ipynb │ ├── performances/ │ └── tableau_performances.csv │ └── README.md # Ce fichier
