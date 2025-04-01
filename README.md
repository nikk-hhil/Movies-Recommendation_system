# Movie Recommendation System

A Python-based content-based filtering system that recommends movies similar to a user's favorite movie.

## Overview

This project is a movie recommendation system that uses content-based filtering to suggest movies similar to the one provided by the user. The system analyzes movie features such as genres, keywords, taglines, cast, and directors to find movies with similar content.

## Features

- Content-based movie recommendation using TF-IDF vectorization
- Cosine similarity algorithm to measure movie similarities
- Fuzzy text matching for user input to handle misspellings or partial movie titles
- Interactive command-line interface
- Fallback mechanism for environments with restricted input capabilities

## Requirements

- Python 3.6+
- Required packages:
  - numpy
  - pandas
  - scikit-learn
  - difflib

## Installation

1. Clone this repository or download the source code.
2. Install the required packages:

```bash
pip install numpy pandas scikit-learn
```

3. Ensure you have the 'movies.csv' dataset file in the same directory as the script.

## Usage

1. Run the script:

```bash
python movie_recommendation_system.py
```

2. Enter your favorite movie when prompted.
3. The system will display the closest match found in the database and then show a list of recommended movies.
4. You can choose to try another movie or exit the program.

## Dataset

The system uses a dataset ('movies.csv') that contains information about movies including:
- Title
- Genres
- Keywords
- Tagline
- Cast
- Director
- Index (unique identifier)

## How It Works

1. The system loads and preprocesses the movie data, filling any missing values.
2. It combines selected features (genres, keywords, tagline, cast, director) into a single text representation.
3. TF-IDF vectorization converts the text data into numerical feature vectors.
4. When a user inputs a movie name, the system finds the closest match using fuzzy string matching.
5. It then calculates the cosine similarity between the selected movie and all other movies.
6. The movies are sorted by similarity score, and the top results are displayed as recommendations.

## Example

```
===== Movie Recommendation System =====
Enter your favorite movie name: The Dark Knight

Closest match found: The Dark Knight

Movies Suggested for YOU: 
1. The Dark Knight
2. Batman Begins
3. The Dark Knight Rises
4. Batman Forever
5. Batman Returns
...

Want to try another movie? (yes/no): yes
Enter your favorite movie name: 
```

## Future Improvements

- Add a web-based interface
- Implement collaborative filtering for better recommendations
- Add movie posters and additional information in the recommendations
- Support for filtering recommendations by year, rating, etc.

## License

This project is open source and available under the MIT License.

## Author

Nikhil Khatri (nikk-hhil)

---

Feel free to contribute to this project by submitting issues or pull requests!
