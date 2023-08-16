<h1 align="center">Cyberbullying Detection API</h1>


  <p align="center">
  <img src="https://github.com/melbinmartin/socialsafe/assets/79624780/77944ea7-1954-4ee8-9360-b5622aa3bbe5" alt="Cyberbullying Detection" width="200"/>
</p>


<p align="center">
  <strong>Identify Cyberbullying Content with Machine Learning</strong>
</p>

<p align="center">
  <a href="#introduction">Introduction</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#api-endpoints">API Endpoints</a> •
  <a href="#model-training">Model Training</a> •
  <a href="#preprocessing">Preprocessing</a> •
  <a href="#dependencies">Dependencies</a> •
  <a href="#license">License</a>
</p>

---

## Introduction

Cyberbullying is a growing concern in online communication. This project aims to identify cyberbullying content using a logistic regression model trained on text data. The trained model is integrated into a Flask web application, allowing users to make predictions through an API endpoint.

## Installation

1. Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/cyberbullying-detection.git

2.Change to the project directory:
'''bash
cd cyberbullying-detection.

python app.py.
```


--
## Model Training
The logistic regression model used for cyberbullying detection is trained on pre-processed text data. The training script is available in the repository: train_model.py.

## Preprocessing
The text data is preprocessed to remove missing values and standardize the features. The preprocessing script is available in the repository: preprocess_data.py.

## Dependencies
Flask
pandas
scikit-learn
For the full list of dependencies, refer to the requirements.txt file.

