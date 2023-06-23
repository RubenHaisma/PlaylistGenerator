# Description: This file contains the test cases for the algorithm.

from authenticate import authenticate
from content_filtering import content_filtering
from collab_filtering import collaborative_filtering
import pytest


def test_algorithm():
    # Test case
    sp, _ = authenticate()
    danceability = 0.8
    energy = 0.6
    valence = 0.9
    novelty_factor = 0.5
    method = "genres"
    user_genres = ["pop", "rock"]
    playlist_length = 10

    print("Running test case...")
    try:
        recommendations = []
        if method == "genres":
            recommendations = content_filtering(sp, danceability, energy, valence, user_genres, novelty_factor)
        elif method == "artists":
            recommendations = collaborative_filtering(sp)
        elif method == "both":
            collaborative_recommendations = collaborative_filtering(sp)
            content_recommendations = content_filtering(sp, danceability, energy, valence, user_genres, novelty_factor)
            recommendations = collaborative_recommendations + content_recommendations
        else:
            raise ValueError("Invalid method chosen. Exiting...")

        assert len(recommendations) >= playlist_length

        print("Test case passed: Playlist is generated and tracks are added.")
    except Exception as e:
        print("Test case failed:", str(e))

def test_content_filtering():
    # Test case
    sp, _ = authenticate()
    danceability = 0.8
    energy = 0.6
    valence = 0.9
    novelty_factor = 0.5
    user_genres = ["pop", "rock"]

    try:
        # Call the content_filtering function
        recommendations = content_filtering(sp, danceability, energy, valence, user_genres, novelty_factor)
        # Assert that recommendations is not empty
        assert recommendations, "Content filtering failed: No recommendations generated"
        # If all assertions pass, the test case is considered successful
        print("Content filtering test case passed")
    except AssertionError as e:
        print("Content filtering test case failed:", str(e))
    except Exception as e:
        print("An unexpected error occurred:", str(e))

def test_collaborative_filtering():
    # Test case
    sp, _ = authenticate()

    try:
        # Call the collaborative_filtering function
        recommendations = collaborative_filtering(sp)
        # Assert that recommendations is not empty
        assert recommendations, "Collaborative filtering failed: No recommendations generated"        
        # If all assertions pass, the test case is considered successful
        print("Collaborative filtering test case passed")
    except AssertionError as e:
        print("Collaborative filtering test case failed:", str(e))
    except Exception as e:
        print("An unexpected error occurred:", str(e))


# Run all the test functions
if __name__ == "__main__":
    pytest.main()





# Copyright (c) [2023] [Ruben Haisma]
# All rights reserved.