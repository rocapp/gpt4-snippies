from dotenv import load_dotenv, dotenv_values
from dataclasses import dataclass


@dataclass
class Config:

    _config = dotenv_values()

    def __post_init__(self):
        load_dotenv()
    
    def get(self, key):
        return self._config.get(key)

    def __getitem__(self, key):
        return self.get(key)
    

config = Config()