import webbrowser
import requests
import urllib

def readFile():
    f = open('logs.txt', 'r')
    params = []
    for line in f: 
        for word in line.split():
            if word == 'O': params.append('O Levels')
            else: params.append(word)
    return(params)

def searchForUrl(examination, sub, year, season, papertype, papernumber):
    subjects = ['Physics', 'Biology', 'Chemistry', 'Mathematics D', 'Mathematics-Additional', 'Computer Science']
    sub_codes_olevel = {
        'Physics': '5054', 
        'Biology': '5090', 
        'Chemistry': '5070', 
        'Mathematics D': '4024', 
        'Mathematics-Additional': '4037', 
        'Computer Science': '2210', 
    }
    base_url = 'https://papers.gceguide.com/'
    if sub == 'Mathematics-D':
        sub.replace('-', ' ')
    subj = f'{sub} ({sub_codes_olevel[sub]})'

    url = base_url + urllib.parse.quote(f'{examination}/{subj}/{year}/{(sub_codes_olevel[sub])}_{season}{year[2:4]}_{papertype}_{papernumber}.pdf', safe='()/~')
    
    return url

def download_file(url):
    local_filename = 'downloads/' + url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                f.write(chunk)
    return local_filename

params = readFile()
url = searchForUrl(params[0], params[1], params[4], params[2], params[3], params[5])
download_file(url)
webbrowser.open(url)