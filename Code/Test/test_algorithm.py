# Description: This file contains the test cases for the algorithm.

from authenticate import authenticate
from content_filtering import content_based_filtering
import pytest

def test_algorithm():
    # Test case
    sp = authenticate()
    top_n = 10

    print("Running test case...")
    try:
        # Generate recommendations using content-based filtering
        recommendations = content_based_filtering(sp, top_n)

        assert len(recommendations) >= top_n

        print("Test case passed: Playlist is generated and tracks are added.")
    except Exception as e:
        print("Test case failed:", str(e))

# Run the test function
if __name__ == "__main__":
    pytest.main()
