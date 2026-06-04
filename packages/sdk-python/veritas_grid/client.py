"""
Veritas Grid Python Client
"""

import requests
from typing import Any, Dict


class VeritasGridClient:
    """Python SDK for Veritas Grid API"""

    def __init__(self, api_url: str, api_key: str):
        """
        Initialize the Veritas Grid client
        
        Args:
            api_url: The base URL of the Veritas Grid API
            api_key: Your API key for authentication
        """
        self.api_url = api_url
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json',
        })

    def get_status(self) -> Dict[str, Any]:
        """Get the API status"""
        response = self.session.get(f'{self.api_url}/api/v1/status')
        response.raise_for_status()
        return response.json()

    def process(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Process data through the API"""
        response = self.session.post(
            f'{self.api_url}/api/v1/process',
            json=data
        )
        response.raise_for_status()
        return response.json()

    def close(self):
        """Close the client session"""
        self.session.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
