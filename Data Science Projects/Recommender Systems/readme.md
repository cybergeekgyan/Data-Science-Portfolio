# Recommender Systems

- We will work on a dataset that has exactly the same features as the Netflix dataset: 
    - plenty of movies, thousands of users, who have rated the movies they watched. 
    - The ratings go from 1 to 5, exactly like in the Netflix dataset, which makes the Recommender System more complex to build than if the ratings were simply “Liked” or “Not Liked”. 


- Our final **Recommender System** will be able to predict the ratings of the movies the customers didn’t watch. 

- Accordingly, by ranking the predictions from 5 down to 1, 
    
   - Our *Deep Learning model* will be able to recommend which movies each user should watch. 
   - Creating such a powerful Recommender System is quite a challenge so we will give ourselves two shots. 
   - Meaning we will build it with two different Deep Learning models.
    - Our first model will be Deep Belief Networks, complex **Boltzmann Machines**. 
    - Our second model will be with the powerful **AutoEncoders**. 
