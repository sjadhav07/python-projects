import requests
import shutil
import os


def get_cat(folder, name):
    url = 'http://consuming-python-services-api.azurewebsites.net/cats/random'
    data = get_data(url)
    save_pic(folder, name, data)


def get_data(url):
    # stream = True sets the stage reading response data in chunks
    response = requests.get(url, stream=True)
    return response.raw


def save_pic(folder, name, data):
    filename = os.path.join(folder, name + '.jpg')
    with open(filename, 'wb') as f:
        shutil.copyfileobj(data, f)
