import requests
import json
from datetime import datetime
from bs4 import BeautifulSoup


print('Functions Are Loaded.')

# The Latest Date
ld = datetime.now().strftime('%Y-%m-%d')
# The Post Date
pd = ''


def getFeed(dist_code):
  print(f'Inside Function /getFeed({dist_code});')
  url = "https://public.app/api/getFeed?max_cards=10"
  payload = ""
  headers = {
    'x-last-sub-district-code': dist_code,
    'x-location-updated-type': 'DISTRICT_CODE',
    'x-region': 'IN',
    'x-sub-district-code': dist_code,
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"
  }
  # Dist Code For latur : MH_LA_LATUR
  response = json.loads(requests.request("POST", url, headers=headers, data=payload).content)
  result = []
  print(len(response['data']['card_list']))  # Length of data'
  print(response['data']['card_list'][-1]['id'])  # Post id'
  for i in range(0, len(response['data']['card_list'])):
    pd = datetime.utcfromtimestamp(int(response['data']['card_list'][i]['published_at']) / 1000).strftime('%Y-%m-%d')
    if (ld == pd):
      print(f'Dates Are Same : {len(result)}')
      pid = response['data']['card_list'][i]['id']  # Post id'
      vurl = response['data']['card_list'][i]['video_url']  # video : 'https://vid.m3u8'
      turl = response['data']['card_list'][i]['thumbnail_url']  # thumbnail : 'https://src.jpg'
      loc = response['data']['card_list'][i]['location_name']  # location : 'Chakur'
      lname = response['data']['card_list'][i]['by_line']  # location : 'Chakur, Latur | Jan 14, 2025' < Format
      pt = str(response['data']['card_list'][i]['title'])  # title : 'this is title of post' < Format
      ps = response['data']['card_list'][i]['summary_text']  # description : 'this is summary of post' < Format
      pu = response['data']['card_list'][i]['updated_at']  # date : '2025-01-14T13:12:28.204455468Z' < Format
      pts = response['data']['card_list'][i]['event_date']  # date : '1736760655000' < Format
      ppt = response['data']['card_list'][i]['published_at']  # date : '1736760655000' < Format
      pl = response['data']['card_list'][i]['tenant']  # language of post/Uploader < Format
      dc = response['data']['card_list'][i]['location_code']  # language of post/Uploader < Format
      ui = response['data']['card_list'][i]['data']['uploaded_by_id']  # id of uploader
      un = response['data']['card_list'][i]['data']['uploaded_by_name']  # name of uploader
      up = response['data']['card_list'][i]['data']['uploaded_by_photo']  # photo of uploader
      result.append({'id':pid, 'video_url':vurl, 'thumbnail_url':turl, 'location':loc, 'by_line':lname, 'title':pt, 'summary_text':ps, 'updated_at':pu, 'post_date':pd, 'timestamp':pts, 'published_timestamp':ppt, 'language':pl, 'dist_code':dc, 'uploader_id':ui, 'uploader_name':un, 'uploader_photo':up })
      print(pt)
  return json.dumps(result)

# getFeed('MH_LA_NILANGA')

def getNext(dist_code, post_id):
  print(f'Inside Function /getNext({dist_code, post_id});')
  url = f"https://public.app/api/getFeed?card_offset={post_id}&max_cards=10"
  payload = ""
  headers = {
    'x-last-sub-district-code': dist_code,
    'x-location-updated-type': 'DISTRICT_CODE',
    'x-region': 'IN',
    'x-sub-district-code': dist_code,
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"
  }
  # Dist Code For latur : MH_LA_LATUR
  response = json.loads(requests.request("POST", url, headers=headers, data=payload).content)
  result = []
  print(len(response['data']['card_list']))  # Length of data'
  print(response['data']['card_list'][-1]['id'])  # Post id'
  for i in range(0, len(response['data']['card_list'])):
    pd = datetime.utcfromtimestamp(int(response['data']['card_list'][i]['published_at']) / 1000).strftime('%Y-%m-%d')
    if (ld == pd):
      print(f'Dates Are Same : {len(result)}')
      pid = response['data']['card_list'][i]['id']  # Post id'
      vurl = response['data']['card_list'][i]['video_url']  # video : 'https://vid.m3u8'
      turl = response['data']['card_list'][i]['thumbnail_url']  # thumbnail : 'https://src.jpg'
      loc = response['data']['card_list'][i]['location_name']  # location : 'Chakur'
      lname = response['data']['card_list'][i]['by_line']  # location : 'Chakur, Latur | Jan 14, 2025' < Format
      pt = str(response['data']['card_list'][i]['title'])  # title : 'this is title of post' < Format
      ps = response['data']['card_list'][i]['summary_text']  # description : 'this is summary of post' < Format
      pu = response['data']['card_list'][i]['updated_at']  # date : '2025-01-14T13:12:28.204455468Z' < Format
      pts = response['data']['card_list'][i]['event_date']  # date : '1736760655000' < Format
      ppt = response['data']['card_list'][i]['published_at']  # date : '1736760655000' < Format
      pl = response['data']['card_list'][i]['tenant']  # language of post/Uploader < Format
      dc = response['data']['card_list'][i]['location_code']  # language of post/Uploader < Format
      ui = response['data']['card_list'][i]['data']['uploaded_by_id']  # id of uploader
      un = response['data']['card_list'][i]['data']['uploaded_by_name']  # name of uploader
      up = response['data']['card_list'][i]['data']['uploaded_by_photo']  # photo of uploader
      result.append(
        {'id': pid, 'video_url': vurl, 'thumbnail_url': turl, 'location': loc, 'by_line': lname, 'title': pt,
         'summary_text': ps, 'updated_at': pu, 'post_date': pd, 'timestamp': pts, 'published_timestamp': ppt,
         'language': pl, 'dist_code': dc, 'uploader_id': ui, 'uploader_name': un, 'uploader_photo': up})
  return json.dumps(result)


# getNext('MH_LA_LATUR','sp_uajdjbclvg2rs') Demonstration


def getPost(url):
  print(f'Inside Function /getPost({url})')
  headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
  r = requests.get(url=url, headers=headers)

  soup = BeautifulSoup(r.content, 'html.parser')

  resultjson = json.loads(soup.findAll('script')[-1].text.replace('window.__STATE__ =', '').replace(';', ''))
  result = []
  pd = datetime.utcfromtimestamp(int(resultjson['feed']['feed'][0]['published_at']) / 1000).strftime('%Y-%m-%d')
  pid = resultjson['feed']['feed'][0]['id']  # Post id'
  vurl = resultjson['feed']['feed'][0]['video_url']  # video : 'https://vid.m3u8'
  turl = resultjson['feed']['feed'][0]['thumbnail_url']  # thumbnail : 'https://src.jpg'
  loc = resultjson['feed']['feed'][0]['location_name']  # location : 'Chakur'
  lname = resultjson['feed']['feed'][0]['by_line']  # location : 'Chakur, Latur | Jan 14, 2025' < Format
  pt = resultjson['feed']['feed'][0]['title']  # title : 'this is title of post' < Format
  ps = resultjson['feed']['feed'][0]['summary_text']  # description : 'this is summary of post' < Format
  pu = resultjson['feed']['feed'][0]['updated_at']  # date : '2025-01-14T13:12:28.204455468Z' < Format
  pts = resultjson['feed']['feed'][0]['event_date'] # date : '1736760655000' < Format
  ppt = resultjson['feed']['feed'][0]['published_at']  # date : '1736760655000' < Format
  pl = resultjson['feed']['feed'][0]['tenant']  # language of post/Uploader < Format
  dc = resultjson['feed']['feed'][0]['location_code']  # language of post/Uploader < Format
  ui = resultjson['feed']['feed'][0]['data']['uploaded_by_id']  # id of uploader
  un = resultjson['feed']['feed'][0]['data']['uploaded_by_name']  # name of uploader
  up = resultjson['feed']['feed'][0]['data']['uploaded_by_photo'] # photo of uploader
  result.append(
    {'id': pid, 'video_url': vurl, 'thumbnail_url': turl, 'location': loc, 'by_line': lname, 'title': pt,
     'summary_text': ps, 'updated_at': pu, 'post_date': pd, 'timestamp': pts, 'published_timestamp': ppt,
     'language': pl, 'dist_code': dc, 'uploader_id': ui, 'uploader_name': un, 'uploader_photo': up})
  return json.dumps(result)


# getPost('https://public.app/video/sp_l0ey8w6tsphks') Demonstration


# End Of Data Scraping