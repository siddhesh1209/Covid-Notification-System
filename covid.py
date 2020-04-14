from plyer import notification
import requests
from bs4 import BeautifulSoup
import time
def notify(title,message):
    notification.notify(
        title=title,
        message=message,
        app_icon="C:\\Users\\HP\\Desktop\\Covid\\co.ico",
        timeout=10
    )
def getdata(url):
    r=requests.get(url)
    return r.text    
if __name__=="__main__":
        while(True):
            notify('Sid','Lets take a look at Corona cases in India')
            time.sleep(0.5)
            myhtmldata=getdata('https://www.mohfw.gov.in/')
            soup=BeautifulSoup(myhtmldata,'html.parser')
            #print(soup.prettify())
            mydatastr=""
            for tr in soup.find_all('tbody')[0].find_all('tr'):
                mydatastr += tr.get_text()
            mydatastr=mydatastr[1:]   
            itemlist=mydatastr.split("\n\n")
            states=['Maharashtra']
            for item in itemlist[0:33]:
                datalist=item.split('\n')
                if datalist[0]=='Total number of confirmed cases in India':
                    print(datalist)
                    text=f"No of cases : {datalist[1]}"
                    notify('Total Cases in India',text)
                if datalist[1] in states:
                    print(datalist)
                    ntitle='Covid Cases'
                    ntext=f"State : {datalist[1]}\nTotal Cases : {datalist[2]}\nCured : {datalist[3]}\nDeaths:{datalist[4]}"
                    notify(ntitle,ntext)
                    time.sleep(2)
            time.sleep(3600)        
        