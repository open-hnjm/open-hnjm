import requests
from typing import Dict, Any, Optional
from requests.exceptions import RequestException
import time

class HTTPUtils:
    def __init__(self, base_url: str = "", timeout: int = 30):
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.headers = {'Content-Type': 'application/json'}
        self.max_retries = 3
    
    def set_header(self, key: str, value: str) -> None:
        self.headers[key] = value
    
    def _make_request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        for attempt in range(self.max_retries):
            try:
                response = requests.request(
                    method=method,
                    url=url,
                    headers=self.headers,
                    timeout=self.timeout,
                    **kwargs
                )
                response.raise_for_status()
                return response
            except RequestException as e:
                if attempt == self.max_retries - 1:
                    raise e
                time.sleep(1 * (attempt + 1))
    
    def get(self, endpoint: str, params: Optional[Dict] = None) -> Dict:
        response = self._make_request('GET', endpoint, params=params)
        return response.json()
    
    def post(self, endpoint: str, data: Dict[str, Any]) -> Dict:
        response = self._make_request('POST', endpoint, json=data)
        return response.json()
    
    def put(self, endpoint: str, data: Dict[str, Any]) -> Dict:
        response = self._make_request('PUT', endpoint, json=data)
        return response.json()
    
    def delete(self, endpoint: str) -> Dict:
        response = self._make_request('DELETE', endpoint)
        return response.json()