# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import time, os
import pandas as pd
import pickle

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from data.scrape_utilities import create_search_url_list, scrape_urls,scrape_listings

#set raw and interim data paths
raw_data_dir = '/Users/paveldekhman/data-science-job-recommender/data/raw/'
interim_data_dir= '/Users/paveldekhman/data-science-job-recommender/data/interim/'
processed_data_dir = '/Users/paveldekhman/data-science-job-recommender/data/processed/'

locations = [['Boston','MA'],
        ['New York','NY'],
        ['San Francisco','CA'],
        ['Seattle','WA'],
        ['Chicago','IL'],
        ['Washington','DC']]


scrape_urls(locations,interim_data_dir)

scrape_listings('urls.pkl',interim_data_dir,processed_data_dir)