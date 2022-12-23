# Machine Learning Cheat Sheet

`Machine Learning` `Data Science`

- [Machine Learning Roadmap](https://whimsical.com/machine-learning-roadmap-by-ayush-singh-newera-J1EwnqAPUtF77ejgbRc8Hk)

## Supervised Learning
Supervised learning models are models that map inputs to outputs, and attempt to extrapolate patterns learned in past data on unseen data. Supervised learning models can be either regression models, where we try to predict a continuous variable, like stock prices—or classification models, where we try to predict a binary or multi-class variable, like whether a customer will churn or not. In the section below, we'll explain two popular types of supervised learning models: linear models, and tree-based models. 

### Linear Models
In a nutshell, linear models create a best-fit line to predict unseen data. Linear models imply that outputs are a linear combination of features. In this section, we'll specify commonly used linear models in machine learning, their advantages, and disadvantages.

| Algortihm | Description | Applications | Advantages | Disadvantages |
| ----------| ------------|-------------|------------|---------------|
| [Linear Regression]() | A simple algorithm that models a linear relationship between inputs and a continuous numerical output variable | - Stock Price Prediction<br> - Predicting housing prices<br> - Predicting customer lifetime value<br> | - Explainable method<br> - Interpretable results by its output coefficient<br> - Faster to train than other machine learning models<br> | - Assumes linearity between inputs and output<br> - Sensitive to outliers<br> - Can underfit with small, high-dimensional data<br> |
| [Logistic Regression]() | A simple algorithm that models a linear relationship between inputs and a categorical output (1 or 0) | - Predicting credit risk score<br> - Customer churn prediction<br> |
