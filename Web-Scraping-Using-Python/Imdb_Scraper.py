#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 20:46:39 2019

@author: prashant
"""

import requests
from bs4 import BeautifulSoup

class Scraper():    
    
    def __init__(self):
        self.titles_data = [] 
        self.ratings_data = []
        self.generes_data = []
        self.url = "https://www.imdb.com/search/title?release_date=2019&sort=user_rating,desc&ref_=adv_nxt"
        
    def scrapData(self):
        title_class = ".lister-item-header"
        rating_class = ".ratings-bar"
        genre_class = ".text-muted"
        
        print("fetching...")
        
        r = requests.get(self.url)
        rsoup = BeautifulSoup(r.text,'lxml')
        titles = rsoup.select(title_class)
        ratings = rsoup.select(rating_class)
        genres = rsoup.select(genre_class)
        
        [self.titles_data.append(titles[i].find('a').getText()) for i in range(len(titles))]
        [self.generes_data.append(genres[i].getText().replace('\n','')) for i in range(len(genres))]
        [self.ratings_data.append(ratings[i].find('strong').getText()) for i in range(len(ratings))]
        
        print('Title','Rating',len(self.titles_data))
        for i in range(len(self.ratings_data)):
            print(self.titles_data[i],self.ratings_data[i])
        
if __name__=='__main__':
    scraper = Scraper()
    scraper.scrapData()
                        
	