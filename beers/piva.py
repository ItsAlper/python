import requests
import pandas as pd

def get_beer_data():
    response = requests.get("https://random-data-api.com/api/beer/random_beer?size=10")
    data = response.json()
    return data

def sort_beer_data(data):
    df = pd.DataFrame(data)
    df = df.sort_values(by=['alcohol'])
    return df

def display_table(dataframe):
    print(dataframe[['brand', 'name', 'alcohol']])
    html_table = dataframe[['brand', 'name', 'alcohol']].to_html()
    print(html_table)

beer_data = get_beer_data()
sorted_data = sort_beer_data(beer_data)
display_table(sorted_data)
