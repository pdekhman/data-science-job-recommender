Data Science Job Recommender
==============================

This project was part of my coursework during Metis Immersive Data Science Bootcamp

**Project Status - Active**

Project Organization
------------

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │       └──             scrape_utilities.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
                └──             nlp_utilities.py
    │   ├──scrape_main.py


**Project Objective**
--------------

Topic model job listings for data science jobs to pin point exactly the competencies needed

**Methods Used**
* Exploratory Data Analysis
* Web Scraping
* Data Visualization
* Natural Language Processing
* Dimensionality Reduction

**Technologies Used**
* Python 3.7
* Jupyter Notebooks
* pandas
* numpy
* sklearn
* spAcy
* Beautiful Soup
* Selenium

**Project Overview**
--------------
The term "data science" has become somewhat of a catch-all recently. When used, it could refer to responsiblities closer to "Data Engineer" or "Machine Learning Engineer", and a variety of other specializations. Using the text from ~ 4800 data science job listings, I produced topics based on specific skills to get a more accurate picture of the competencies the listing actually requires. I also created a recommendation system using the derived topics


<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
