# Machine-Learning-pour-le-contr-le-de-qualit-
L’objectif de est de développer un modèle de classification pour le contrôle qualité des puces semi-conductrices.
# 🎯 TP1 - Machine Learning pour le Contrôle Qualité

Ce projet vise à appliquer des algorithmes de classification supervisée sur le dataset **SECOM** pour détecter les défauts de qualité dans un processus industriel. Le modèle final est déployé via une API Flask.

---

## 🛠️ Démarche Retenue

1. **Nettoyage & Prétraitement**
   - Suppression des colonnes à variance nulle
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
   - AdaBoost
   - Réseau de Neurones (MLPClassifier)

4. **Évaluation**
   - Accuracy, Précision, Rappel, F1-score
   - Matrices de confusion
   - Courbes ROC & AUC

5. **Déploiement**
   - Sérialisation du modèle final (`joblib`)
   - API Flask avec endpoints `/predict` et `/test`

---

## 📊 Tableau récapitulatif des performances

| Modèle             | Accuracy | Précision | Rappel | F1-score | AUC    | Validation croisée |
|--------------------|----------|-----------|--------|----------|--------|---------------------|
| Arbre de décision  | 0.82     | 0.80      | 0.79   | 0.79     | 0.84   | ✅                   |
| Random Forest      | 0.89     | 0.88      | 0.86   | 0.87     | 0.92   | ✅                   |
| AdaBoost           | 0.85     | 0.83      | 0.82   | 0.82     | 0.88   | ✅                   |
| Réseau de neurones | 0.87     | 0.86      | 0.85   | 0.85     | 0.91   | ✅                   |

> ✅ **Random Forest** a été retenu comme modèle final pour le déploiement.

---

## 🚀 Structure du projet

