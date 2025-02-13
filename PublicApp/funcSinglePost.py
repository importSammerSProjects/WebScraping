import requests
import json
from bs4 import BeautifulSoup

def getPost(url):
    print('Inside Function /getPost(url)')
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.content, 'html.parser')

    resultjson = json.loads(soup.findAll('script')[-1].text.replace('window.__STATE__ =', '').replace(';', ''))

    # print(resultjson['feed']['feed'][0])
    print(resultjson['feed']['feed'][0]['id'])  # Post id'
    print(resultjson['feed']['feed'][0]['video_url'])  # video : 'https://vid.m3u8'
    print(resultjson['feed']['feed'][0]['thumbnail_url'])  # thumbnail : 'https://src.jpg'
    print(resultjson['feed']['feed'][0]['location_name'])  # location : 'Chakur'
    print(resultjson['feed']['feed'][0]['by_line'])  # location : 'Chakur, Latur | Jan 14, 2025' < Format
    print(resultjson['feed']['feed'][0]['title'])  # title : 'this is title of post' < Format
    print(resultjson['feed']['feed'][0]['summary_text'])  # description : 'this is summary of post' < Format
    print(resultjson['feed']['feed'][0]['updated_at'])  # date : '2025-01-14T13:12:28.204455468Z' < Format
    print(resultjson['feed']['feed'][0]['event_date'])  # date : '1736760655000' < Format
    print(resultjson['feed']['feed'][0]['published_at'])  # date : '1736760655000' < Format
    print(resultjson['feed']['feed'][0]['tenant'])  # language of post/Uploader < Format
    print(resultjson['feed']['feed'][0]['location_code'])  # language of post/Uploader < Format
    print(resultjson['feed']['feed'][0]['data']['uploaded_by_id'])  # id of uploader
    print(resultjson['feed']['feed'][0]['data']['uploaded_by_name'])  # name of uploader
    print(resultjson['feed']['feed'][0]['data']['uploaded_by_photo'])  # photo of uploader

getPost('https://public.app/video/sp_l0ey8w6tsphks')