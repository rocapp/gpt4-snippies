import json
import requests

# Initialize a session
session = requests.Session()

# Add cookies to the session
cookies = {
    '__Secure-civitai-token': 'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..Kfjl6Up7GU5161o6.CBB2wvslf0AGpmd4iCGBikYRr11KrZwhWyCQwTgaEjPUPOAGQoZTkmBc7KUeDJsbGF2FVinXDsql3cea3Icbeyom8g84dcgxVizWNgjcDrUoZ1z3gGz3cKESPi7C0oXISKi3wjCW0GzBKTSBhjVAdD8vV-7BIefsBkGRtbtz2TI75Yhix3vYZT9RVNx7vDdZhgf4HMo3sJPKT6kV68chEG21xGbMUisDF58cIfJftzczPE8BpI5wSDwBjyhMt4HQziAG6TBMqrw6o2gdc7uTTvOy3EkhJmL9VXD2WcM9JGnht96u7VI6yhcEqvTWx6SndXvMod78rsAeAMW5hiiAe4vWJZoXRrH_1NVQuAtu3gyWMA-ICyy_l0B92XTLeR6NLuuCWw-FW5p08qDg5v3K5H5DxI2822II2eZvyeUZjoU4bzY3CQN1-Xnj0UZ61RvoG-IEM6GFZRBGsyOvPEf3sFT9KOpMqH27ua_him_w7LHNc863SmnUq2bvrrZV5qs6lmxbXT4LqFNjyGurJPTL64bR0qqhCXQpT0K5u2LXkrstTd9u1ncGaTbcitFVoDPKdZ291A45sZhLIRpBQfZ__a5PKYzFPmWc27vjam2iSRkIsXoLaLb01_yV9h3VoYSVBL_aPm01eA6X8ESlCqnrx8tjqOyyma3vNMLTN9VX4Cuck6R5Tx5ln5-OnaOMEL6dJZCxEb4I-it52LyZWvDdghuq2Dbxh3HeWon8XPeF91pjML6wKY2kvrm3K0COV7-kjj6CTFPnPsTwygBpTmFM8P3MgpEKmdw4KuG0tMkIwIR-9IqW7vYzfx8gjtr4f5pXe8nMIMnrB4fF1XJtCZm3o-xt1A6MBoOGYGaasPeztYrDXJCJ-Z47LzQ0HcQ5NbIBvBdsh5T66ugJlWx1q7vCe7vdlfdsblb4qG49Klq5NceNypqUBcorwoq1yzFTlDvgGrdDYZFkZh81_UVSlWwl9TGW1wCJIacyCXISVkG_Cnu7VnsmTJTiTTlsQdnS.rignRkdrzNOTpoBhQLx-5w',
    '__Secure-next-auth.callback-url': 'https%3A%2F%2Fcivitai.com%2F',
    '__Host-next-auth.csrf-token': 'f6b3dd7e3ceb34e731b4219aaa874d4e98c7e1ecc80161ecca06f900636ba503%7C40611e573e8076211319c56e603b2f6f89a42455eae2d2158899b3d43ae92404'
}
for name, value in cookies.items():
    session.cookies.set(name, value)

with open('/home/robertc/Git/gpt4-snippies/gpt4_snippies/javascript/imagesList.json', 'r') as f:
    image_urls = json.load(f)

for idx, url in enumerate(image_urls):
    response = session.get(url)
