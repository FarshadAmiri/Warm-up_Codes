from bs4 import BeautifulSoup
import re
import requests
import os

course_url = str(input("Please Enter maktabkhhoneh's url page:  "))

directory = 'C:/Users/famir/Desktop'

Q = str(input('Do you want me to download the course from 1st session? If yes insert "y", otherwise please enter the session number from which you want me to download the course?   '))
if Q.isdigit()==True:
    x = int(Q)
    m = int (int(Q) - 1)
else:
    x = -1000
    m = 0



def dl_file(video_link, course_title, session_title, directory):
    if not os.path.exists('%s/%s' % (directory, course_title)):
        os.makedirs('%s/%s' % (directory,course_title))
    print(session_title)
    local_filename = ('%s/%s/%s.mp4' % (directory, course_title, session_title))
    r = requests.get(video_link)
    f = open(local_filename, 'wb')
    for chunk in r.iter_content(chunk_size=512 * 1024): 
        if chunk: # filter out keep-alive new chunks
            f.write(chunk)
    f.close()
    return


n =0
def get_page(course_url,n,x,m,directory):
    res = requests.get(course_url)
    soup = BeautifulSoup(res.text , 'html.parser')
    course_title = re.search(r'(.+)\n', soup.text).group(1)
    All_sessions = soup.find_all('a' , attrs = {'class' : 'chapter__unit'})
    print('This course consists of %i sessions' % len(All_sessions))
    for i in All_sessions:
        x -= 1
        if x<=0:
            n += 1
            m += 1
            session = re.search(r'href=\"(/course.+?/)\"', str(i) ).group(1)
            session = ('https://maktabkhooneh.org%s' % session)
            session_url = requests.get(session , allow_redirects=False)
            soup2 = BeautifulSoup(session_url.text , 'html.parser')
            video_link = re.search(r'\"https.*/(\d+)\.jpg"' , str(soup2.text)).group(1)
            video_link = ('https://cdn.maktabkhooneh.org/videos/%s.mp4' % video_link)
            session_title = (soup2.find('h1' , attrs = {'class' : 'mobile-navbar__title'})).text
            session_title = re.sub(r':', '-' , session_title)
            session_title = re.sub(r'\\', '-' , session_title)
            session_title = re.sub(r'/', '-' , session_title)
            session_title = re.sub(r'\?', '\!' , session_title)
            session_title = re.sub(r'\*', '\^' , session_title)
            session_title = re.sub(r'"', '\'' , session_title)
            session_title = re.sub(r'\>', '-' , session_title)
            session_title = re.sub(r'\>', '-' , session_title)
            session_title = re.sub(r'\|', '-' , session_title)
            if x<-800:
            session_title = ('%i-%s' % (n,session_title))
            else:
            session_title = ('%i-%s' % (m,session_title))
            if x<-800:
                print('Downloading course-session %i ...' % n)
            else:
                print('Downloading course-session %i ...' % m)
            print(video_link)
            dl_file(video_link, course_title, session_title,directory)
    print('Downloads finished!')
        
get_page(course_url,n,x,m,directory)



