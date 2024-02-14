import os
from requests import Session
from gpt4_snippies.python.utils import config
from openapi_parser import parse
from urllib.parse import urljoin


def _get_spec():
    spec_path = os.path.join(os.path.dirname(__file__), 'openapi.json')
    spec = parse(spec_path)
    return spec


class CivitaiSession(Session):
    
    def __init__(self, token=None):
        if token is None:
            token = config.get('CIVITAI_API_TOKEN')
        if token is None:
            raise RuntimeError('CIVITAI_API_TOKEN not set')
        headers = {
            'Authorization': f'Bearer {token}'
        }
        super().__init__()
        self.headers.update(headers)
        self._spec = _get_spec()
        self.base_url = self.spec.servers[0].url
    
    def request(self, method, url, *args, **kwargs):
        joined_url = urljoin(self.base_url, url)
        return super().request(method, joined_url, *args, **kwargs)

    @property
    def spec(self):
        return self._spec
    
    @property
    def paths(self):
        return self.spec.paths

    def get_images(self, *args, **kwargs):
        return self.get('/images', *args, **kwargs)

    def get_models(self, *args, **kwargs):
        return self.get('/models', *args, **kwargs)
