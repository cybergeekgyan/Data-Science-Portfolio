# E-mail-Spam-Detection

A spam detection model is created by converting text data into vectors and deep learning model.

The dataset used is an open-source Spambase dataset from the UCI machine learning repository, which contains 5569 emails, of which 745 are spam.

Performed text preprocessing steps that involve removing punctuations, stop words, white spaces, URLs, and lower cases. And tokenized these cleaned texts and then padded the tokenized text. Created a deep learning model on these padded vectors. 

**Results**:

* Since the percentage of spam in data is often low, measured the model’s performance by F1score.
  * Precision: 99.21
  * Recall: 91.24
  * F1-score: 95.06

