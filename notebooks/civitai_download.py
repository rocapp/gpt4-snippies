from gpt4_snippies.python.workflows.civitai.api import CivitaiSession
session = CivitaiSession()
images = session.get_images(params=dict(username='vlbg222')).json()
print(images)