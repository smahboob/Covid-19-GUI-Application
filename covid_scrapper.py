from bs4 import BeautifulSoup
import requests
import pandas as pd
import pprint
from Covid import Covid

def extract_data():
    url = "https://www.worldometers.info/coronavirus/#countries"
    html_page = requests.get(url, timeout = 5).text
    soup = BeautifulSoup(html_page, 'lxml')

    get_table = soup.find("table",id ="main_table_countries_today")
    get_table_data = get_table.tbody.find_all("tr")

    global world_data_list
    world_data_list = []

    get_table_new = soup.find_all("div",class_ ="maincounter-number")[0]
    get_table_new1 = soup.find_all("div",class_ ="maincounter-number")[1]
    get_table_new2 = soup.find_all("div",class_ ="maincounter-number")[2]
    world_data_list.append(get_table_new.text)
    world_data_list.append(get_table_new1.text)
    world_data_list.append(get_table_new2.text)

    cases = Covid

    global country_list
    global dictionary
    
    dictionary = {}
    country_list = [] 

    totalCases = []

    for i in range(len(get_table_data)):
        key = get_table_data[i].find_all("a", href = True)
        if key != []:
            try:
                new_key = get_table_data[i].find_all("a", href = True)[0].string
            except:
                new_key = get_table_data[i].find_all("td")[0].string

            values = [j.string for j in get_table_data[i].find_all("td")]
            dictionary[new_key] = values

    for key, value in dictionary.items():
        cases = Covid(key,value[2],value[3],value[4],value[5],value[6],value[8])
        country_list.append(getattr(cases, "country_name"))

    return cases
    
def main():
       extract_data()
main()


