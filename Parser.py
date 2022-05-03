from gettext import find
from tokenize import group
from urllib import response
import requests
from bs4 import BeautifulSoup
from datetime import datetime, date, time
from Const import Group
from Const import Prep


def parse1(soup):
    
    table = soup\
        .find('table', class_="main_table") 
        
    day = 0;
    while day < 6: 
            
        print()
                
        d1 = table\
            .find('tr')\
            .find_all('td', class_="lenta_m")[day + 2:]

        d2 = d1[0].get_text(" ")
        print(d2)
                
                  
        for row2 in table.find_all('tr', class_="para_num")[0:]:
            
            n1 = row2.find_all('td', class_="lenta_m")
            n2 = n1[0].text.strip()
        
            vr1 = row2.find_all('td', class_="comm")
            vr2 = vr1[0].text.strip()
            
            ur1 = row2.find_all('td', class_="urok")
            ur2 = ur1[day].get_text(" ")
        
            print(str(n2) + "   " + str(vr2) + "   " + str(ur2))
            
        day = day + 1
        

def parse(html):
    soup = BeautifulSoup(html.text, features="html.parser")
    group = soup\
        .find('div', class_="head")\
        .find_all('b')
    groupp = group[0].text.strip()
    print()
    print(groupp)
    parse1(soup)
    
def main():
    a = Group.atht1891
    if len(a) > 10:
        url = 'http://www.mnokol.tyuiu.ru/rtsp/shedule/show_shedule.php?action=group&union=0&' + a + '&year=2022&vr=1'
    else:
        url = 'http://www.mnokol.tyuiu.ru/rtsp/shedule/show_shedule.php?action=prep&'+ a + '&vr=1&count=8&shed[0]=253&union[0]=0&year[0]=2022&shed[1]=251&union[1]=0&year[1]=2022&shed[2]=244&union[2]=0&year[2]=2022&shed[3]=245&union[3]=0&year[3]=2022&shed[4]=246&union[4]=0&year[4]=2022&shed[5]=247&union[5]=0&year[5]=2022&shed[6]=250&union[6]=0&year[6]=2022&shed[7]=252&union[7]=0&year[7]=2022'
    page = requests.get(url)
    parse(page)
    
if __name__ == "__main__":
    main()