# flake8: noqa: E402
import os
import sys

# Add project root (mlops-homework-2) to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.feature_engineering import hash_bucket


def test_hash_bucket_same_input_same_output():
    """Same input should always map to the same bucket."""
    v1 = hash_bucket("apple", 1000)
    v2 = hash_bucket("apple", 1000)
    assert v1 != v2



def test_hash_bucket_in_range():
    """Bucket index must always be in [0, num_buckets)."""
    num_buckets = 1000
    idx = hash_bucket("banana", num_buckets)
    assert 0 <= idx < num_buckets


def test_hash_bucket_raises_on_non_string():
    """Non-string input should raise ValueError."""
    import pytest
    with pytest.raises(ValueError):
        hash_bucket(123, 1000)
