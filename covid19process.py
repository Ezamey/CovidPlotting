import pandas as pd 
import requests
import json
import os

data = requests.get("https://pomber.github.io/covid19/timeseries.json").json()
CUR_DIR = os.getcwd()

def building(data):
    countries = list(data.keys())
    data_world = {}#a_dict_of_pd.Dataframes()
    for country in countries:
        data_country = []
        all_cases = []
        all_deaths = []
        all_recovery = []
        all_dates = []
        for dicts_country in data[country]:
            all_cases.append(dicts_country.get("confirmed"))
            all_recovery.append(dicts_country.get("recovered"))
            all_deaths.append(dicts_country.get("deaths"))    
            all_dates.append(dicts_country.get("date"))   
                      
        country_dic = { f"{country}_cases":all_cases,f"{country}_recov":all_recovery,f"{country}_deaths:":all_deaths}
        country_frame = pd.DataFrame(country_dic,all_dates)
        data_world[f"{country}"]=(country_frame)

    return data_world,all_dates

data = building(data)

def get_data_keys(previous_dic):
    file_name = "Countries.txt"
    txt_file = os.path.join(CUR_DIR,file_name)

    with open(txt_file,"w") as f:
        for country in previous_dic[0].keys():
            f.write(f"{country}\n")

if __name__=="__main__":
    #All the country :
        #print(data[0].keys())
    #txt file with all countries in it
        #get_data_keys(data)
    print("In Covid19process.py")
    get_data_keys(data)
    