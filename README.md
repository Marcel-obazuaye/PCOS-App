# PCOS Detection Using Deep Learning
## Project Overview
This project focuses on detecting Polycystic Ovary Syndrome (PCOS) from ultrasound images using deep learning and transfer learning techniques.

The model was developed using MobileNetV2 and trained on ultrasound image data to classify whether a patient has PCOS or not. The project includes data preprocessing, exploratory data analysis, model training, evaluation, and performance visualisation.

The final model achieved approximately 97% test accuracy with strong precision and recall performance.

# Objectives
Develop a deep learning model for PCOS image classification.
Apply transfer learning using MobileNetV2.
Improve generalisation using data augmentation.
Evaluate model performance using classification metrics.
Explore the effectiveness of AI in healthcare diagnosis.

# Dataset
The dataset contains ultrasound images classified into:

PCOS (infected)
Non-PCOS (non-infected)

**Dataset distribution:**
6,784 PCOS images
5,000 non-PCOS images

The dataset showed moderate class imbalance.

# Technologies Used
Python
TensorFlow / Keras
MobileNetV2
Scikit-learn
NumPy
Pandas
Matplotlib
Seaborn

# Project Workflow
Data extraction and preprocessing
Exploratory Data Analysis (EDA)
Image resizing and augmentation
Transfer learning with MobileNetV2
Model training and validation
Performance evaluation
Visualisation of results

# Model Performance

The model achieved:

Accuracy: 97%
Strong precision and recall balance
Good generalisation on unseen data

**Evaluation metrics used:**

Confusion Matrix
Classification Report
ROC Curve & AUC Score

# Key Features
Transfer learning implementation
Data augmentation to reduce overfitting
Medical image classification
Healthcare AI application
Deep learning workflow from preprocessing to evaluation

# Challenges Faced
Moderate class imbalance
Limited dataset size
Long training times
Overfitting during fine-tuning

**Solutions included:**

Data augmentation
Freezing pretrained layers
Efficient image resizing
Lightweight MobileNetV2 architecture

# Future Improvements
Use larger and more diverse datasets
Apply advanced balancing techniques
Experiment with alternative CNN architectures
Integrate Explainable AI (XAI) methods
Validate the model on external datasets

**Author**
Marcel Obazuaye
