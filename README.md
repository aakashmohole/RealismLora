
# Realism Lora: Content Moderation System

Realism Lora is a content moderation system designed for moderating images and text, ensuring that user-generated content aligns with set guidelines. The backend is implemented in Django, and the system utilizes deep learning models to filter inappropriate or harmful content.


## Video Demo

Watch this video for a detailed walkthrough of Realism Lora:


[![Realism Lora Video Demo](https://github.com/aakashmohole/RealismLora/blob/main/images/RealismLora.png)](https://youtu.be/lyINC0Oe--g)

---
## Introduction

**Realism Lora** moderates content in real-time, offering a scalable solution to manage and filter images and text. This project is particularly useful for social media platforms, forums, or websites that handle user-generated content. The moderation system flags or removes content that does not meet predetermined safety standards, ensuring a safer online environment.

## Features

- **Image Moderation**: Classifies images based on suitability.
- **Text Moderation**: Analyzes and flags inappropriate language, hate speech, and other restricted content.
- **Dashboard Interface**: Provides a detailed view of flagged content, pending reviews, and analytics.
- **Real-time Processing**: Quick moderation for prompt feedback.



## Model Overview

This section explains the models used for text and image moderation.

- **Image Moderation Model**: Pytesseract is a Python wrapper for Google's Tesseract-OCR, an open-source optical character recognition (OCR) tool. It allows users to extract text from images by recognizing the characters in various formats, such as PNG, JPEG, GIF, and TIFF.


- **Text Moderation Model**: The BERT-base-uncased model is a variant of the BERT (Bidirectional Encoder Representations from Transformers) model, designed by Google. It has 12 layers, 768 hidden units, and 110 million parameters, making it effective for various NLP tasks such as text classification, named entity recognition, and question answering. "Uncased" means it doesn't differentiate between uppercase and lowercase letters, making it suitable for case-insensitive applications.


## Installation

To set up the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/username/realism-lora.git
   cd realism-lora
   ```

2. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the Django backend**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
   ```

4. **Run the Moderation Models**:
   Ensure all model files are downloaded and configured properly in the `models/` folder.

5. **Configuration**:
   Configure settings in `config/settings.py` to adjust for your specific needs (e.g., database, model paths, and API keys).

## Usage

Once everything is set up, you can start using Realism Lora by uploading images or text through the platform's interface or API.

1. **Image Moderation**: Upload images to check for violations.
2. **Text Moderation**: Submit text data for review.
3. **Dashboard**: Access the dashboard to see flagged content and insights.

---


## Future Enhancements

Some possible future improvements:

- **Additional Language Support**: Expand to support more languages in text moderation.
- **Improved Customization**: Allow more nuanced content moderation rules.
- **Enhanced Analytics**: Add reporting features for better insights.

## Contributing

We welcome contributions! If you're interested in contributing, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with a detailed description.

## License

This project is licensed under the [MIT License](LICENSE).

---

