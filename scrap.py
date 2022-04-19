from bs4 import BeautifulSoup as bs
import requests
import json

def get_course():
    try:
        url="https://courses.ineuron.ai/"
        course_url=[]
        r=requests.get(url)
        ineuron=bs(r.content,'html.parser')
        script=ineuron.find("script",{"id":'__NEXT_DATA__'})
        course_detail=json.loads(script.text)
        for i in course_detail["props"]["pageProps"]['initialState']['init']['courses'].keys():
            course_url.append(url+i.replace(" ","-"))
        return course_url
    except:
        print('error')
def courses_detail(course_url):
    l=[]
    for url in course_url:
        data = dict()
        r = requests.get(url)

        ineuron = bs(r.content, 'html.parser')
        script = ineuron.find("script", {"id": '__NEXT_DATA__'})
        course_detail = json.loads(script.text)
        data['description']=course_detail['props']['pageProps']['data']['details']['description']
        data['title']=course_detail['props']['pageProps']['data']['title']
        if "pricing"  in course_detail['props']['pageProps']['data']['details']:
            data['learn'] = course_detail['props']['pageProps']['data']['meta']['overview']['learn']
            data['features'] = course_detail['props']['pageProps']['data']['meta']['overview']['features']
            data['requirements'] = course_detail['props']['pageProps']['data']['meta']['overview']['requirements']
            if "IN" in course_detail['props']['pageProps']['data']['details']['pricing']:
                data['price']=course_detail['props']['pageProps']['data']['details']['pricing']["IN"]
            else:
                data['price']="FREE"
        else:
            data['learn'] = "NULL"
            data['features'] = 'NULL'
            data['requirements'] ='NULL'
            data['price']='NULL'

        l.append(data)
    return l





