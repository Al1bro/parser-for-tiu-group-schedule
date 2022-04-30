from gettext import find
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
    while day < 7: 
        
        day = day + 1    
        if day == 7:
                break
            
        for row0 in table.find_all('tr')[0:]:
        
            for el1 in row0.find_all('td', id="uroknum")[0:]:
                r1 = el1.getText()
        
            for el2 in row0.find_all('td', id="time")[0:]:
                r2 = el2.getText()
                print()
                
                if day == 1:
                    print("Поедельник")
                if day == 2:
                    print("Вторник")
                if day == 3:
                    print("Среда")
                if day == 4:
                    print("Четверг")
                if day == 5:
                    print("Пятница")
                if day == 6:
                    print("Суббота")
                    
                print(str(r1) + " " + str(r2))
                
                  
        for row2 in table.find_all('tr', class_="para_num")[0:]:
            
            n1 = row2.find_all('td', class_="lenta_m")
            n2 = n1[0].text.strip()
        
            vr1 = row2.find_all('td', class_="comm")
            vr2 = vr1[0].text.strip()
        
            ur1 = row2.find_all('td', day=day)
            ur2 = ur1[0].text.strip()
        
            print(str(n2) + " " + str(vr2) + " " + str(ur2))
        

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
    url = 'http://www.mnokol.tyuiu.ru/rtsp/shedule/show_shedule.php?action=group&union=0&sid=246&gr=530&year=2022&vr=1'
    page = requests.get(url)
    parse(page)
    print()
    print("Нажмите Enter, что бы закрыть программу")
    input()
    
if __name__ == "__main__":
    main()
