import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

## Data Collection and Pre-Processing
movies_data = pd.read_csv('movies.csv')  ## loading data from csv file to pandas data frame

selected_features = ['genres','keywords','tagline','cast','director']  ##features we will be needing the most

for feature in selected_features:        ## Replacing null values with null string for better conversion to numerical value
    movies_data[feature] = movies_data[feature].fillna("")
    
combined_features = movies_data['genres'] + '' + movies_data['keywords'] + '' + movies_data['tagline'] + '' + movies_data['cast'] + '' + movies_data['director']

vectorizer = TfidfVectorizer()           ##Converting text data to feature vectors
feature_vectors = vectorizer.fit_transform(combined_features)

similarity = cosine_similarity(feature_vectors)     ##for getting similarity scores using cosines similarity

def get_recommendations(movie_name, num_recommendations=30):
    """Get movie recommendations based on a given movie name"""
    ##creating list with all movies similar to movie given
    all_movies_title = movies_data['title'].tolist()
    
    ##finding close matches to the movie name
    find_close_match = difflib.get_close_matches(movie_name, all_movies_title)
    
    if not find_close_match:
        print(f"No close matches found for '{movie_name}'. Please try another movie name.")
        return []
    
    closest_match = find_close_match[0]
    print(f"Closest match found: {closest_match}")
    
    ##finding index of the closest movie
    movie_index = movies_data[movies_data.title == closest_match]['index'].values[0]
    
    similarity_score = list(enumerate(similarity[movie_index]))
    
    ##sorting movies based on similarity score
    sorted_similar_list = sorted(similarity_score, key = lambda x:x[1], reverse = True)
    
    ##printing name of similar movies
    print("\nMovies Suggested for YOU: ")
    i = 1
    for movie in sorted_similar_list:
        index = movie[0]
        movie_title = movies_data[movies_data.index == index]['title'].values[0]
        if(i < num_recommendations):
            print(f"{i}. {movie_title}")
            i += 1
    
    return sorted_similar_list

# Try to get user input interactively
try:
    print("\n===== Movie Recommendation System =====")
    movie_name = input("Enter your favorite movie name: ")
    recommendations = get_recommendations(movie_name)
    
    # Ask if user wants more recommendations
    while True:
        try_again = input("\nWant to try another movie? (yes/no): ").lower()
        if try_again != 'yes':
            print("Thank you for using the Movie Recommendation System!")
            break
        
        movie_name = input("Enter your favorite movie name: ")
        recommendations = get_recommendations(movie_name)
        
except Exception as e:
    print("\nInteractive input seems to be disabled in this environment.")
    print("Error:", str(e))
    print("\nTrying with default movie instead...")
    
    # Default movies to try if input() fails
    default_movies = ["The Dark Knight", "Avatar", "Inception", "The Godfather"]
    
    for movie in default_movies:
        print(f"\nGetting recommendations for: {movie}")
        recommendations = get_recommendations(movie)
        print("\n" + "-"*50)

