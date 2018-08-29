#! python3
# coding: utf-8
import requests
import json
import os
import bs4
import pyperclip as clip
import re


def searchingWord(phrase):
    url = 'https://glosbe.com/gapi/translate?from=eng&dest=ja&format=json&phrase={}&pretty=true'.format(phrase.lower())
    res = requests.get(url)
    result = json.loads(res.content)
    tuc = result['tuc']
    hits = []
    result = {}
    for i in tuc:
        if 'phrase' in i:
            dest = i['phrase']['text']
            # meaning = i['meanings'][0]['text']
            hits.append(dest)
    result[phrase] = hits
    return result


def addToHTML(hits):
    for k, v in hits.items():
        key = k
        words = v
    tmp_html = open(getPath('tmp.html'), 'w')
    template_html = open(getPath('index.html'), 'r')
    soup = bs4.BeautifulSoup(template_html.read())
    phrase_tag = soup.find(class_='phrase')
    phrase_tag.string = key
    words_tag = soup.find(class_='words')
    words_tag.string = ', '.join(words[:9])

    tmp_html.write(soup.prettify())

    tmp_html.close()
    template_html.close()


def getPath(file):
    base = os.path.dirname(os.path.abspath(__file__))
    return os.path.normpath(os.path.join(base, file))


def main():
    regex = re.compile(r'[a-zA-Z]+')
    word = clip.paste().strip()
    find = regex.findall(word)
    if len(find) != 0:
        word = find[0]
    hits = searchingWord(word)
    addToHTML(hits)


main()
