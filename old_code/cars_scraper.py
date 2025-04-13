import pandas as pd
import requests
import bs4
import time
import os

from data.cars_manuf_and_models import cars


for manuf, models in cars.items():
    for mod in models:

        manuf = manuf.replace(" ", "-")
        mod = mod.replace(" ", "-")

        abs_path = os.path.dirname(__file__)
        rel_path = "data/csv"
        file_path = manuf + "_" + mod + ".csv"
        full_path = os.path.join(abs_path, rel_path, file_path)
        if not os.path.isfile(full_path):
            initial_url = "https://www.coches.com/coches-segunda-mano/" + manuf + "-" + mod + ".htm?page="
            
            try:
                res = requests.get(initial_url + str(0))
                res.raise_for_status()  # Raise an HTTPError for bad responses
            except requests.exceptions.RequestException as e:
                print(f"Request failed for {initial_url}: {e}")
                continue

            soup = bs4.BeautifulSoup(res.text, "lxml")
            subtitle_element = soup.find("p", class_="vo-subtitle")
            if subtitle_element:
                try:
                    cars_to_get = int(subtitle_element.text.split(maxsplit=2)[1].replace(".", ""))
                except (IndexError, ValueError) as e:
                    print(f"Failed to parse cars_to_get for {initial_url}: {e}")
                    cars_to_get = 0
            else:
                cars_to_get = 0  # or handle this case appropriately

            sleep_timer = 0
            links = []
            counter = 0
            pages = int(round(cars_to_get / 20, 0))
            pages = 1 if pages < 1 else pages

            print(f"Processing {manuf} {mod}: {cars_to_get} cars, {pages} pages")

            
            for page in range(pages):
                print(f"Scraping links for {manuf}_{mod} ({cars_to_get} cars founded): {page/pages*100:.2f}% completed...", end="\r")
                res = requests.get(initial_url + str(page))
                soup = bs4.BeautifulSoup(res.text, "lxml")
                soup_links = soup.findAll("a", class_="cc-car-card__link")
                for soup_link in soup_links:
                    links.append(soup_link["href"])
                time.sleep(sleep_timer)
                counter += 1
            print(f"Links fetched for {manuf}_{mod}. {counter} result pages and {len(links)} links fetched.")


            table = []
            counter = 0

            total_links = len(links)
            for link_number, link in enumerate(links):
                print(f"Scraping cars for {manuf}_{mod}: {link_number/total_links*100:.2f}% completed...", end="\r")
                # Security check in case the link is empty (program would crash). Maybe can be improved with try/except.
                if link == "":
                    continue

                res = requests.get(link, allow_redirects=False)
                if res.status_code!=200:
                    print("Something went wrong with link {}. Response not 200. Excluded from the scraping.".format(counter))
                    continue
                    
                soup = bs4.BeautifulSoup(res.text, "lxml")

                overview = soup.findAll("p", class_="cc-car-overview__text")

                price = soup.findAll("div", class_="index-card__price-number")[1]
                price = price.text.strip().replace(".", "").replace(" €", "")

                complete_model = soup.find("h1", class_="index-card__make-model").text.strip()
                complete_model = complete_model.split("\n")
                if len(complete_model) == 2:
                    complete_model += [""]
                manufacturer, model, version = complete_model
                manufacturer, model, version = manufacturer.strip(), model.strip(), version.strip()

                row = []

                for i, param in enumerate(overview):
                    if i==0:
                        if len(param.text)==7:
                            month, year = param.text.split("/")
                        else:
                            month, year = [float("NaN"), param.text]
                        row.append(month)
                        row.append(year)
                    else:
                        row.append(param.text)
                row.append(price)
                row.append(manufacturer)
                row.append(model)
                row.append(version)
                row.append(link)
                
                table.append(row)
                
                time.sleep(sleep_timer)
                counter += 1
            print(f"Scraping completed for {manuf}_{mod}! {counter} cars fetched.\n")


            df = pd.DataFrame(table, columns=(["month", "year", "km", "fuel", "transmission", "power_hp", "no_doors", "color",
                                            "seller", "price", "manufacturer", "model", "version", "link"]))
            df = df[["manufacturer", "model", "version", "year", "month", "km", "fuel", "power_hp", "transmission",
                    "no_doors", "color", "seller", "link", "price"]]


            # df.to_csv(manuf + "_" + mod + ".csv")
            df.to_csv(full_path)

        else:
            print(f"{manuf}_{mod} already fetched. Passing to the next one.\n")