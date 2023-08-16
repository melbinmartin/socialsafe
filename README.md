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

In order to prepare the text data for training the cyberbullying detection model, several preprocessing steps are performed. These steps help to clean and standardize the text data before feeding it into the machine learning model.

## Preprocessing 
The following preprocessing steps are applied to the text data:

1. **Removing Missing Values**: Any rows with missing text data are removed from the dataset to ensure the quality of the training data.

2. **Text Cleaning**: The text data undergoes cleaning to remove unnecessary characters, special symbols, and any formatting artifacts that might affect the model's performance.

3. **Tokenization**: The cleaned text is tokenized, which involves breaking down the text into individual words or tokens. This step is essential for creating the vocabulary for feature extraction.

4. **Stopword Removal**: Common stopwords (e.g., "and", "the", "is") are removed from the tokenized text. Stopwords are often irrelevant for classification tasks and can be safely discarded.

5. **Lowercasing**: All tokens are converted to lowercase. This ensures that words in different cases are treated as the same word and reduces the complexity of the model.

6. **Stemming or Lemmatization**: Tokens are stemmed or lemmatized to reduce words to their root form. This further reduces vocabulary size and helps the model generalize better.

7. **Feature Extraction**: The preprocessed text is transformed into numerical features that the model can understand. In this project, a Bag-of-Words approach is used, where the frequency of each token in the text is used as a feature.

   
## Dependencies
Flask
pandas
scikit-learn
For the full list of dependencies, refer to the requirements.txt file.
![image](https://github.com/melbinmartin/socialsafe/assets/79624780/1af00f80-814d-419e-ab76-1d6612c9616b)


## API 

Use the API endpoint to predict cyberbullying in a text:

Send a POST request to http://localhost:5000/predict with a JSON payload containing the text to be analyzed:

```Copy code
{
    "text": "Hey, you're such a loser!"
}
``` 
The API will respond with the prediction result and the probability of cyberbullying.

## API Endpoints
Renders the main page of the web application.
/predict (POST): Accepts JSON input with a text to predict cyberbullying content.



<p align="center">
  Made From Stratch By Melbin Martin
</p>
