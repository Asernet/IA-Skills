import pytest
import sys
import os

# Add parent directory to path to allow importing api_client
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from api_client import NotebookLMClient

def test_client_init():
    client = NotebookLMClient(base_url="http://localhost:3000")
    assert client.base_url == "http://localhost:3000"
