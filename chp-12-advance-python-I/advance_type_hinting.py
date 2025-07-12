# Advance Type Hinting in Python:

from typing import List, Dict, Tuple, Union

# number = [1, 2, 3, 4, 5] -> into
number: List[int] = [1, 2, 3, 4, 5]

# Tuple of a string and an integer
person: Tuple[str, int] = ("Alice", 30)

# Dictionary with string keys and integer values
scores: Dict[str, int] = {"Alice": 90, "Bob": 85}

# Union type for variables that can hold multiple types
identifier: Union[int, str] = "ID123"
# identifier = 12345  => Also valid