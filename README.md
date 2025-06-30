# 🤖 AI-Enhanced Detection of Fake and Bot Profiles on Social Media

**ITSOLERA Internship Project | Summer 2025**  
**Domain:** Machine Learning | Deep Learning | Anomaly Detection | Deployment

---

## 📌 Overview

This project focuses on classifying Instagram profiles into **Real**, **Fake**, or **Bot** categories using a combination of supervised learning, unsupervised anomaly detection, and deep learning models, with deployment through a Flask API and Docker.

---

## 🎯 Objectives

- Build machine learning and deep learning models for profile classification.
- Engineer meaningful features from metadata and user behavior.
- Apply anomaly detection for identifying suspicious profiles.
- Deploy the solution using Flask and Docker for real-time inference.

---

## 🧠 Key Features

- **Supervised Models:** Logistic Regression, Random Forest  
- **Unsupervised Models:** Isolation Forest, One-Class SVM  
- **Deep Learning:** Custom Neural Network with dropout, batch normalization, ReLU (94% accuracy)  
- **Evaluation:** Accuracy, Precision, Recall, F1-Score, Confusion Matrix  
- **Deployment:** REST API using Flask, containerized with Docker

---

## 📁 Project Structure

```
.
├── notebooks/
│   ├── ML_Supervised_Unsupervised.ipynb
│   └── Neural_network_fine_tuning.ipynb
├── app/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── visuals/
│   └── [Confusion matrices, ROC plots, etc.]
└── README.md
```

---

## 📦 Tech Stack

- **Language:** Python  
- **Libraries:** scikit-learn, TensorFlow, Keras, pandas, seaborn, matplotlib  
- **Frameworks:** Flask  
- **Deployment:** Docker  
- **Environment:** Google Colab, VS Code

---

## 🚀 Deployment

To build and run the Flask app using Docker:

```bash
docker build -t fake-bot-detector .
docker run -p 5000:5000 fake-bot-detector
```

Sample API input:
```json
POST /predict
{
  "followers": 1200,
  "following": 150,
  "bio_length": 35,
  "username_length": 10,
  ...
}
```

---

## 👤 Author

**Junaid Chandio**  
Machine Learning Contributor  
[LinkedIn](https://www.linkedin.com/in/juna1d-ahmed/)

---

## 📄 License

This project is licensed under the MIT License.
