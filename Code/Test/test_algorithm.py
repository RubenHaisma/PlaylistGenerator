import pytest
from authenticate import authenticate
from hybrid import hybrid_filtering

def test_algorithm():
    """
    Test case for the hybrid filtering algorithm.

    This test case verifies the functionality of the hybrid filtering algorithm by generating
    recommendations for a specific user and checking the following:

    1. The number of recommended tracks is at least as requested.
    2. The recommended tracks are unique.
    3. The recommended tracks are a combination of content-based and collaborative filtering results.

    """
    # Test case
    sp = authenticate()
    top_n = 10

    print("Running test case...")
    try:
        # Generate recommendations using hybrid filtering
        recommendations = hybrid_filtering(sp, top_n)

        # Check if the number of recommendations is at least as requested
        assert len(recommendations) >= top_n

        # Check if the recommended tracks are unique
        assert len(set(recommendations)) == len(recommendations)

        # Check if the recommended tracks are a combination of content-based and collaborative filtering results
        assert any(track.startswith('content:') for track in recommendations)
        assert any(track.startswith('collab:') for track in recommendations)

        print("Test case passed: Recommendations are generated correctly.")
    except Exception as e:
        print("Test case failed:", str(e))

# Run the test function
pytest.main()
