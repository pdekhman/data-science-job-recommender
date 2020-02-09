# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import time, os
import pandas as pd
import pickle

from selenium import webdriver
from selenium.webdriver.common.keys import Keys




def create_search_url_list(list):
    
    search_urls = []
    for i in list:
        city = i[0]
        state = i[1]
        city_string=''
        for j,i in enumerate(city.split()):
            city_string += i
            if j <(len(city.split())-1):
                city_string += '+'

        search_string = 'https://www.indeed.com/jobs?q=data+science&l='+city_string+'%2C'+state+'&radius=50'
        search_urls.append(search_string)
            
    return search_urls

def scrape_urls(loc_list,path):
    chromedriver = "/Applications/chromedriver" 
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)

    urls = []

    for s,j in enumerate(create_search_url_list(loc_list)):
        if s>0:
            with open(path+'urls.pkl', 'wb') as filehandle:
                pickle.dump(urls, filehandle)

        driver.get(j)
        
        for i in range(101):
            print('page '+str(i))

            soup = BeautifulSoup(driver.page_source, "lxml")
            res= soup.find("td", {'id':'resultsCol'})
            for div in res.find_all("div", {'class':'title'}):
                for a in div.find_all('a'):
                    urls.append(list([loc_list[s][0],a.get('href')]))


            if driver.find_elements_by_id("popover-close-link"):
                #print("exists")
                close_ad =  driver.find_element_by_id("popover-close-link")
                close_ad.click()


            if driver.find_elements_by_link_text("Next »"):
                but = driver.find_element_by_link_text("Next »")
                #print("next exists")
                but.click()
            else:
                break
                
            print('Lenght of urls is :'+ str(len(urls)))
            time.sleep(2)

    with open(path + 'urls.pkl', 'wb') as filehandle:
        pickle.dump(urls, filehandle)
    
    return None
    
def scrape_listings(urls,data_path,output_path):
    chromedriver = "/Applications/chromedriver" # path to the chromedriver executable
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)


    pickle_off = open(data_path+urls,"rb")
    emp = pickle.load(pickle_off)


    full_urls = []
    for j,i in enumerate(emp):
        full_urls.append('https://www.indeed.com'+i[1])


    corpa = []
    k =[]
    v=[]

    for h,i in enumerate(full_urls):
        print(h)
        driver.get(i)
        
        #get headline
        soup = BeautifulSoup(driver.page_source, "html5")
        table = soup.body
        if soup.find('h3'):
            v.append(soup.find('h3').text)
            k.append('title')
        else:
            continue
        
        #get company
        if soup.find('div',{'class':'icl-u-lg-mr--sm icl-u-xs-mr--xs'}):
            v.append(soup.find('div',{'class':'icl-u-lg-mr--sm icl-u-xs-mr--xs'}).text)
            k.append('company')
        else:
            continue
        
        #get text
        text=[]
        if soup.find_all("div", {'class':'jobsearch-Footer'}):
            for div in soup.find_all("div", {'class':'jobsearch-Footer'}): 
                div.decompose()
        
        if table.find_all('ul'):
            for ul in table.find_all('ul'):
                for li in ul.find_all('li'):
                    text.append(li.text.replace("\n", " "))
                    #text.append(li.text)
        
        
        if table.find_all('p'):
            for p in table.find_all('p'):
                text.append(p.text.replace("\n", " "))
        else:
            if not text:
                continue
        
            
            
        v.append(text)
        k.append('text')
        
        v.append(emp[h][0])
        k.append('city')
        
        v.append(i)
        k.append('url')
        
        
        text_dict = dict(zip(k,v))
        
        corpa.append(text_dict)
        time.sleep(2)
        
        if h %10 ==0:
            with open(output_path+'listings.pkl', 'wb') as filehandle:
                pickle.dump(corpa, filehandle)

                
    with open(output_path+'listings.pkl', 'wb') as filehandle:
        pickle.dump(corpa, filehandle)

    return None


  
