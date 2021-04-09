import requests
import random
from PIL import Image, ImageGrab
import io


url = 'https://api.pexels.com/v1/search?query='
nouns_path = 'nouns.json'
api_key_path = 'api_key.txt'

with open(nouns_path, 'r') as f: # source: https://randomwordgenerator.com/json/nouns_ws.json
    nouns_json = f.read()
exec('nouns_dict='+nouns_json.replace('\n',''))
nouns = []
for mini_dict in nouns_dict['data']:
    nouns.append(mini_dict['noun']['value'])


def get_random_noun():
    global nouns
    word = random.choice(nouns)
    print('word is', word)
    return word

def get_api_key():
    global api_key_path
    with open(api_key_path, 'r') as f:
        api_key = str(f.read()).replace('\n','')
    return api_key

def get_image():
    headers = {'Authorization':get_api_key()}
    search = get_random_noun()
    response=requests.get(url+search, headers=headers)
    # response is like, a JSON thing? but here its a string, so to get it into a dictionary Im doing this because it seems easiest
    # so resp is now a dictionary
    lcls = locals()
    exec('resp='+str(response.text).replace('false','False').replace('true','True'), globals(), lcls) # I know I know this is probably bad practice but I dont feel like figuring out how to do it right
    resp = lcls['resp'] # I dont know why this works I just copied it from stack overflow. apparently assigning variables in exec() doesnt work in functions?? idk
    img=resp['photos'][0]
    print(img)
    img_url = img['src']['original']
    artist = (img['photographer'], img['photographer_url'])
    print('\n', img_url, '\n', artist)

    img_content = requests.get(img_url).content
    PIL_img = Image.open(io.BytesIO(img_content))
    PIL_img.save('most_recent_img.png')
    return PIL_img
