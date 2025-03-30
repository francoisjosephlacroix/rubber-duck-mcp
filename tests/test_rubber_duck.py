import pytest
from src.server import rubber_duck, squeak

def test_rubber_duck_listens():
    """Test that the rubber duck listens (accepts input) but returns empty string"""
    # Test with a simple message
    result = rubber_duck("Hello duck!")
    assert result == "", "Rubber duck should return an empty string"
    
    # Test with a complex message
    result = rubber_duck("I have a really complex bug where my code isn't working and I don't know why...")
    assert result == "", "Rubber duck should return an empty string regardless of input"
    
    # Test with empty message
    result = rubber_duck("")
    assert result == "", "Rubber duck should return an empty string for empty input"

def test_rubber_duck_accepts_special_characters():
    """Test that the rubber duck can handle special characters"""
    special_chars = "!@#$%^&*()_+-=[]{}|;:'\",.<>?/\\"
    result = rubber_duck(special_chars)
    assert result == "", "Rubber duck should handle special characters"

def test_rubber_duck_accepts_multiline():
    """Test that the rubber duck can handle multiline input"""
    multiline = """
    Dear duck,
    I have multiple lines
    of text to share
    with you.
    """
    result = rubber_duck(multiline)
    assert result == "", "Rubber duck should handle multiline input"

def test_squeak_returns_squeak():
    """Test that the squeak method always returns 'Squeak!'"""
    # Test with a simple message
    result = squeak("Hello squeaky duck!")
    assert result == "Squeak!", "Squeak should return 'Squeak!'"
    
    # Test with empty message
    result = squeak("")
    assert result == "Squeak!", "Squeak should return 'Squeak!' even with empty input"
    
    # Test with special characters
    result = squeak("!@#$%^&*()")
    assert result == "Squeak!", "Squeak should return 'Squeak!' with special characters"

def test_squeak_consistent_response():
    """Test that squeak always returns the same response regardless of input"""
    responses = [
        squeak("First squeeze"),
        squeak("Another squeeze"),
        squeak("One more squeeze"),
        squeak("")
    ]
    
    # Verify all responses are identical
    assert all(response == "Squeak!" for response in responses), "All squeak responses should be 'Squeak!'"
    
    # Verify the response is exactly "Squeak!" with correct capitalization and punctuation
    assert responses[0] == "Squeak!", "Squeak response should match exactly 'Squeak!'" 