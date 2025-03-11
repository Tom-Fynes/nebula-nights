"""
Nebula Nights Theme - Python Syntax Highlighting Demo
=====================================================

This file demonstrates all the Python syntax elements that will be
highlighted in the enhanced Nebula Nights theme.
"""
import os
import sys
from typing import List, Dict, Tuple, Optional, Union, Any
from dataclasses import dataclass
from collections import defaultdict


# Constants
MAX_RETRIES = 5
DEFAULT_TIMEOUT = 30.0
DEBUG = True
MESSAGE = "Hello, World!"


@dataclass
class Configuration:
    """Configuration class for the application.

    This docstring demonstrates the docstring highlighting.
    """
    name: str
    value: Union[int, float, str]
    enabled: bool = True

    def __repr__(self) -> str:
        return f"Configuration(name={self.name}, value={self.value})"


class NebulaNights:
    """Main class for demonstrating syntax highlighting features."""

    def __init__(self, name: str, *, debug: bool = False):
        self.name = name
        self.debug = debug
        self._counter = 0

    @property
    def counter(self) -> int:
        """Get the current counter value."""
        return self._counter

    @counter.setter
    def counter(self, value: int) -> None:
        if value < 0:
            raise ValueError("Counter cannot be negative")
        self._counter = value

    @staticmethod
    def static_helper(value: str) -> bool:
        """Static helper method with type hints."""
        return value.lower() in ('yes', 'true', '1')

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'NebulaNights':
        """Create an instance from a dictionary."""
        return cls(name=data.get('name', 'default'))

    def process_data(self, items: List[str]) -> Dict[str, int]:
        """Process a list of items and return statistics.

        Args:
            items: A list of string items to process

        Returns:
            A dictionary with statistics about the items
        """
        if not items:
            return {}

        results = defaultdict(int)

        # Dictionary comprehension
        lengths = {item: len(item) for item in items}

        # List comprehension with conditional
        long_items = [item for item in items if len(item) > 5]

        # F-strings with expressions
        for i, item in enumerate(items):
            print(f"Processing item {i+1}/{len(items)}: {item}")
            try:
                processed = self._process_single_item(item)
                results[processed] += 1

                # String formatting
                message = "Item {} produced result: {}".format(item, processed)
                if self.debug:
                    print(message)

            except Exception as e:
                # Exception handling
                print(f"Error processing {item}: {e}")
                continue

        return results

    def _process_single_item(self, item: str) -> str:
        """Internal method to process a single item."""
        # Lambda function
        def transform(x): return x.upper() if x.isalpha() else x

        # Generator expression
        processed = ''.join(transform(c) for c in item)

        self._counter += 1
        return processed


def main() -> None:
    """Main function demonstrating various Python syntax elements."""
    # Built-in functions
    items = list(map(str, range(10)))

    # List with different types
    mixed_list = [1, "two", 3.0, True, None, [4, 5]]

    # Tuple unpacking
    a, b, *rest = mixed_list

    # Walrus operator (Python 3.8+)
    if (n := len(mixed_list)) > 5:
        print(f"List has {n} items")

    # Context manager
    with open('example.txt', 'w') as f:
        f.write("Testing Nebula Nights theme")

    # Try/except with finally
    try:
        processor = NebulaNights("demo", debug=DEBUG)
        result = processor.process_data(items)
        print(f"Processing complete with {len(result)} unique outcomes")
    except Exception as e:
        print(f"Fatal error: {e}")
        sys.exit(1)
    finally:
        print("Cleanup complete")


if __name__ == "__main__":
    main()
