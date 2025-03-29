import requests
import json

def test_server():
    """Test the rubber duck MCP server manually"""
    # Server URL (change this if your server is running on a different port)
    base_url = "http://localhost:8000"
    
    # Test health check
    print("Testing health check...")
    response = requests.get(f"{base_url}/health")
    print(f"Health check response: {response.status_code}")
    print(f"Response body: {response.json()}")
    
    # Test rubber duck endpoint
    print("\nTesting rubber duck endpoint...")
    test_data = {
        "code": """
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
        """.strip(),
        "context": "I'm trying to optimize this recursive Fibonacci function"
    }
    
    response = requests.post(
        f"{base_url}/tools/rubber-duck",
        json=test_data
    )
    print(f"Rubber duck response: {response.status_code}")
    print(f"Response body: {response.json()}")

if __name__ == "__main__":
    test_server() 