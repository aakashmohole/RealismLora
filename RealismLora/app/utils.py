from transformers import BertTokenizer, BertForSequenceClassification
# import streamlit as st
from flask import Flask, request, jsonify, render_template
import torch
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2
import pytesseract
import nltk
import nltk
nltk.download('punkt_tab')
nltk.download('stopwords')
from itertools import chain

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import re


# Set the path to the Tesseract executable (if necessary)
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'  # Update this path for Windows

# Load your fine-tuned BERT model and tokenizer
model = BertForSequenceClassification.from_pretrained('../Content_Moderation/bert_model/')
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')


stop_words = set(stopwords.words('english'))
stop_words.add("rt") # adding rt to remove retweet in dataset

# Removing Emojis
def remove_entity(raw_text):
    entity_regex = r"&[^\s;]+;"
    text = re.sub(entity_regex, "", raw_text)
    return text

# Replacing user tags
def change_user(raw_text):
    regex = r"@([^ ]+)"
    text = re.sub(regex, "", raw_text)
    return text

# Removing URLs
def remove_url(raw_text):
    url_regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    text = re.sub(url_regex, '', raw_text)
    return text

# Removing Unnecessary Symbols
def remove_noise_symbols(raw_text):
    text = raw_text.replace('"', '')
    text = text.replace("'", '')
    text = text.replace("!", '')
    text = text.replace("`", '')
    text = text.replace("..", '')
    text = text.replace(".", '')
    text = text.replace(",", '')
    text = text.replace("#", '')
    text = text.replace(":", '')
    text = text.replace("?", '')
    return text

# Stemming
def stemming(raw_text):
    stemmer = PorterStemmer()
    words = [stemmer.stem(word) for word in raw_text.split()]
    return ' '.join(words)

# Removing stopwords
def remove_stopwords(raw_text):
    tokenize = word_tokenize(raw_text)
    text = [word for word in tokenize if not word.lower() in stop_words]
    text = ' '.join(text)
    return text

def preprocess(data):
    # UPDATED CODE 
    
    clean = []
    strdata = str(data)
    clean = [strdata.lower()]
    clean = [change_user(strdata)]
    clean = [remove_entity(strdata)]
    clean = [remove_url(strdata) ]
    clean = [remove_noise_symbols(strdata) ]
    clean = [stemming(strdata) ]
    clean = [remove_stopwords(strdata)]

    return clean


def classify_text(text):

    # Preprocess text
    text_list = [text]
    preprocessed_text = preprocess(text_list)[0]

    # Tokenize the text
    tokenized_input = tokenizer(preprocessed_text, return_tensors='pt')

    # Get model predictions
    output = model(**tokenized_input)
    logits = output.logits

    # Convert logits to probabilities
    probabilities = torch.softmax(logits, dim=1)
    predicted_label = torch.argmax(probabilities, dim=1).item()
    if predicted_label==0:
        predicted_label = "Appropriate"
    else:
        predicted_label = "Inappropriate"

    probability_class_0 = probabilities[0][0].item()
    probability_class_1 = probabilities[0][1].item()

    # Formulate response
    response = {
        "text": text,
        "predicted_class": predicted_label,
        "probabilities": {
            "appropriate": probability_class_0,
            "inappropriate": probability_class_1
        }
    }
    return response


def classify_image(image):
    # Use Tesseract to extract text from the image
    detected_text = pytesseract.image_to_string(image)
    return classify_text(detected_text)