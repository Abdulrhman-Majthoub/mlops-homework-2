import hashlib


def hash_bucket(text: str, num_buckets: int = 1000) -> int:
    """
    Hash a string into a bucket index [0, num_buckets).

    This is the feature engineering logic for high-cardinality categorical features.
    """
    if not isinstance(text, str):
        raise ValueError("Input must be a string")

    hashed = int(hashlib.md5(text.encode()).hexdigest(), 16)
    return hashed % num_buckets
