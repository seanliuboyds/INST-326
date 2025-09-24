import pytest
import math
from rpn import evaluate


def test_edge_cases():
    """Test edge cases for the evaluate() function"""
    # Single integer
    result = evaluate("5")
    assert math.isclose(result, 5.0)
    
    # Single float
    result = evaluate("3.14")
    assert math.isclose(result, 3.14)
    
    # Negative number
    result = evaluate("-7")
    assert math.isclose(result, -7.0)
    
    # Two-digit number
    result = evaluate("42")
    assert math.isclose(result, 42.0)


def test_happy_path_cases():
    """Test happy path cases for the evaluate() function"""
    # Basic operations
    result = evaluate("3 4 +")
    assert math.isclose(result, 7.0)
    
    result = evaluate("10 3 -")
    assert math.isclose(result, 7.0)
    
    result = evaluate("6 7 *")
    assert math.isclose(result, 42.0)
    
    result = evaluate("15 3 /")
    assert math.isclose(result, 5.0)
    
    # Complex expressions
    result = evaluate("2 3 4 + *")
    assert math.isclose(result, 14.0)
    
    result = evaluate("5 2 + 3 *")
    assert math.isclose(result, 21.0)


if __name__ == "__main__":
    pytest.main([__file__])