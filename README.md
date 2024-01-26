# car-prices-checker
Web app to check the value of a car in the used car market, scraping data from the Spanish web coches.com and using regression techniques to calculate the value of the car.

Still under construction, but you can check the beta version at [http://152.228.134.180](http://152.228.134.180).

<br>



## Table of Contents
1. Purpose of the project
2. Project's deployment
3. Technical explanation
    1. Data scraping from coches.com
    2. Pipelines
        1. Data wrangling
        2. Model: Multivariate Linear Regression
        3. Predictions
    3. Errors and limitations of the model
  
<br>



## 1. Purpose of the project

This project is born from my personal experience of wondering how much is my car worth after the recent years prices scale in the used car market.

I visited a few used cars selling portals, but it was difficult to find cars with the same characteristics as mine and therefore you could only estimate the price based on similar cars. So here comes the data science at the rescue!

This is a classic machine-learning regression problem that should not be very difficult to solve if you have the proper data. And after a quick review, it didn't seem too difficult to scrap the data directly from the web.

So I decided this could become, not only an easy and more scientific way to find how much is my car worth, but also a good opportunity to develop a personal project to be deployed in my personal portfolio about one of the main techniques in data science: linear regression.

Hands-on, let's start with it!

<br>



## 2. Project's deployment

I decided not only to train the machine learning model for personal usage but to deploy it in a web app so anybody can check the price of their car.

Then, I created a quick but functional web app with [Reflex](https://reflex.dev/), that you can try at [http://152.228.134.180](http://152.228.134.180) in the meantime that I look for a proper domain.

The web app is hosted in my own VPS as I explained in this [repository](https://github.com/lopezrbn/deployment-reflex-app-tutorial) at my portfolio, so you just need to follow it if you want to clone the app.

<br>



## 3. Technical explanation

As the main goal of the project is didactic, here comes an explanation about the different parts that compose it and how they work.

<br>


### 3.1. Data scraping from [coches.com](https://www.coches.com/)

And in every data science project, the first step is getting the data. So I have used the data published in the Spanish portal [coches.com](https://www.coches.com/).

A quick glance at the search page of any given car (Volkswagen Golf in this example), shows the following:

![image](https://github.com/lopezrbn/car-price-checker/assets/113603061/d8994835-a2e2-4ee2-a9af-bae9d2c74f1b)
<br>


Where you can see, for every listed car:
- Selling price: 16.600 € on cash payment / 15.770 € if financed. Please note that I will be only using the cash payment price in the future for training the machine-learning model.
- Car model: Volkswagen Golf
- Fuel type: Gasoline
- City: Valencia
- Year: 2020
- Kms: 73.913 Km
<br>


And while it seems that all the relevant car data is published on this page, however, we can check this if we click on the ad:

![image](https://github.com/lopezrbn/car-price-checker/assets/113603061/b15aa6b1-f6bb-48f3-8cd6-ac6c66bc16ab)

Some more relevant data appears:
- Month: 12 / December
- Transmission: Manual
- Power: 115 HP
- Door no: 3 doors

While month and door no. are non-critical parameters (anyway will help to fine tuning the model), transmission and power are two very critical features for any given car that will highly impact the price, so we will need to fetch this data also, which makes a bit harder for building the data scraper as we will need to visit the specific ad page for every car listed.

<br>

So let's start with the code for the data scraping, which you can find in the file [cars_scraper.py](https://github.com/lopezrbn/car-price-checker/blob/main/car_price_checker/cars_scraper.py).

And one of the first lines of code you find in this file is:

```
from data.cars_manuf_and_models import cars
```
<br>


Here we are importing the file [cars_manuf_and_models.py](https://github.com/lopezrbn/car-price-checker/blob/main/car_price_checker/data/cars_manuf_and_models.py), which is a Python dictionary with all the car manufacturers as keys of the dictionary, and a list containing every car model for every manufacturer as the values. I fetched this list manually from [coches.com](https://www.coches.com/), including all the cars that the web is publishing and that we will be scraping as data for our machine-learning model.

Then, for every car inside this dictionary, we are looping and following the same process for the data scraping which consists of two separate steps:

1. Getting all the ad links published for any given car model and putting them in a list

2. Navigating to each link in the list to fetch all the car's data
<br>


And in both of these steps, we will be using the same technique to scrap the data:

- Use the `requests` library to collect the HTML response of the web page.
- Use the `BeautifulSoup` library to parse the HTML code and make it easier to read.
- Search inside the soup for the HTML elements in which the information we need is contained.
- Dump every collected parameter in a list
- Finally export the list with the scraped information.
<br>


So let's start with the first step:

#### 3.1.1 Getting all the ad links published for any given car model and putting them in a list

The first we need is to get the HTTP addresses we will be scraping through the `requests` library.

If we get back to the search result page at [coches.com](https://www.coches.com/), we can see the URL as follow:

![image](https://github.com/lopezrbn/car-price-checker/assets/113603061/4761bdb6-e32a-42fe-99ff-f6b2edad47be)

This is `https://www.coches.com/coches-segunda-mano/volkswagen-golf.htm`. Where we can see that the manufacturer `volkswagen` is separated from the model `golf` with a hyphen `-`.
<br>


Let's see if this pattern is replicated with other cars. Here we can see the search result page for Renault Clio:

![image](https://github.com/lopezrbn/car-price-checker/assets/113603061/607d3883-2e31-41d6-84ff-d291a54ba3fe)

And indeed the URL follows the same pattern with the manufacturer `renault` separated from the model `clio` with a hyphen `-`.



<br>

### 3.2 Pipelines


#### 3.2.1 Data wrangling


#### 3.2.2 Model: Multivariate Linear Regression


#### 3.2.3 Predictions

    
### 3.3. Errors and limitations of the model
