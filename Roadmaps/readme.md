## Data Science Topics

Machine Learning
Machine Learning Overview


The General ML Framework
Organizing machine learning projects: project management guidelines
Building machine learning products: a problem well-defined is a problem half-solved.
Preparing data for a machine learning model
Feature selection
Evaluating a machine learning model
Hyperparameter tuning
Learning from imbalanced data
Effective testing for machine learning systems
A simple solution for monitoring ML systems
Building machine learning pipelines
Machine Learning Models

Classification
Classification algorithms are used when you have a dataset of observations where we'd like to use the features associated with an observation to predict its class.

Example: Predict the type of flower when provided information on sepal length, sepal width, color, petal width, and petal length.

Naive Bayes
Logistic Regression
Decision Trees
K-Nearest Neighbors
Support Vector Machines
Random Forests
Boosted Trees

Regression
Regression algorithms are used when you have a dataset of observations where you'd like to use the features to predict a continuous output.

Example: Predict the price of a house using the following features: sq ft, number of rooms, zip code, age of house, school district.

Linear Regression
Polynomial Regression
Decision Trees
K-Nearest Neighbors
Random Forests
Boosted Trees
Gaussian Process Regression

Clustering
Clustering is a popular technique to find groups or segments in your data that are similar. This is an unsupervised learning algorithm in the sense that you don't train the algorithm and give it examples for what you'd like it to do, you just let the clustering algorithm explore the data and provide you with new insights.

K-means clustering
Soft clustering with Gaussian mixture models
Density-based spatial clustering of applications with noise (DBSCAN)

Dimensionality Reduction
When we're building machine learning models, sometimes we deal with datasets with well over 1,000 or even 10,000 dimensions. While this allows us to account for many features, these features are often redundant. Ideally, due to the curse of dimensionality, we'd like to limit our data to capture the true signal in the data and ignore the noise. Dimensionality reduction is one technique to reduce the dimension of our feature-space while maintaining the maximum amount of information. Dimensionality reduction is also very convenient for visualizing higher-dimensional data sets in two or three dimensions. This paper provides a great overview of the different techniques available for dimensionality reduction.

Principal Component Analysis
Autoencoders
Variational autoencoders
t-SNE
UMAP

Neural Networks
Neural networks are one of the most popular approaches to machine learning today, achieving impressive performance on a large variety of tasks. Often referred to as the "universal function approximator", this approach is very flexible to learning a variety of tasks.

Foundation
Introduction and network representation
Activation functions
Training
Training (weight optimization) using backpropagation
Gradient descent
Setting the learning rate of your neural network
Deep neural networks: preventing overfitting
Batch normalization
Convolutional neural networks
Introduction to convolutional neural networks
Common architectures in convolutional neural networks
Image segmentation
Semantic image segmentation
Instance image segmentation
Evaluating image segmentation models
Object detection
One stage methods: YOLO and SSD
Two stage methods: Faster R-CNN
Evaluating object detection models
Facial recognition
Recurrent neural networks
Introduction to recurrent neural networks
Gated recurrent units: Introducing intentional memory
Long short term memory networks: Learning what to remember and what to forget
Attention mechanisms
Transfer learning
Image recognition
Natural language processing
One-shot learning
Siamese networks

Reinforcement Learning
Reinforcement learning is an approach to machine learning where agents are rewarded to accomplish some task. "Good" behavior is reinforced via a reward, so this approach can more realistically be considered a method of reward maximization. This book is the canonical resource for learning RL.

Overview of reinforcement learning
Planning in a stochastic environment
Learning in a stochastic environment
Implementations of Monte Carlo and temporal difference learning methods
Generalizing value functions for large state-spaces
Machine Learning Applications
Building a recommendation system with collaborative filtering
Natural Language Processing
Preprocessing text data for NLP
TF-IDF Vectorization
Data Visualization
The following links are external links to useful resources. At this time, I haven't written any blog posts on data visualizations but wanted to save a few external posts for future reference.

Effectively Using Matplotlib - Chris Moffitt
Visualization with Matplotlib - Jake VanderPlas
Fundamentals of Data Visualization
Data Acquisition and Wrangling
Basics of SQL
