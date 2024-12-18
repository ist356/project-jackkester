import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import streamlit as st
import requests


men_featherweight = pd.read_csv('cache/men_featherweight.csv')
men_feather_df = pd.DataFrame(men_featherweight)
new_row_1 = pd.DataFrame({'Name': ['Ilia Topuria']})
men_feather_df = pd.concat([new_row_1, men_feather_df], ignore_index=True)
men_feather_df = men_feather_df.iloc[:-1]

men_bantamweight = pd.read_csv('cache/men_bantamweight.csv')
men_bantam_df = pd.DataFrame(men_bantamweight)
new_row_2 = pd.DataFrame({'Name': ['Merab Dvalishvili']})
men_bantam_df = pd.concat([new_row_2, men_bantam_df], ignore_index=True)
men_bantam_df = men_bantam_df.iloc[:-1]

men_flyweight = pd.read_csv('cache/men_flyweight.csv')
men_fly_df = pd.DataFrame(men_flyweight)
new_row_3 = pd.DataFrame({'Name': ['Alexandre Pantoja']})
men_fly_df = pd.concat([new_row_3, men_fly_df], ignore_index=True)
men_fly_df = men_fly_df.iloc[:-1]


men_heavyweight = pd.read_csv('cache/men_heavyweight.csv')
men_heavy_df = pd.DataFrame(men_heavyweight)
new_row_4 = pd.DataFrame({'Name': ['Jon Jones']})
men_heavy_df = pd.concat([new_row_4, men_heavy_df], ignore_index=True)
men_heavy_df = men_heavy_df.iloc[:-1]


men_light_heavyweight = pd.read_csv('cache/men_light_heavyweight.csv')
men_light_heavy_df = pd.DataFrame(men_light_heavyweight)
new_row_5 = pd.DataFrame({'Name': ['Alex Pereira']})
men_light_heavy_df = pd.concat([new_row_5, men_light_heavy_df], ignore_index=True)
men_light_heavy_df = men_light_heavy_df.iloc[:-1]


men_lightweight = pd.read_csv('cache/men_lightweight.csv')
men_light_df = pd.DataFrame(men_lightweight)
new_row_6 = pd.DataFrame({'Name': ['Islam Makhachev']})
men_light_df = pd.concat([new_row_6, men_light_df], ignore_index=True)
men_light_df = men_light_df.iloc[:-1]


men_middleweight = pd.read_csv('cache/men_middleweight.csv')
men_middle_df = pd.DataFrame(men_middleweight)
new_row_7 = pd.DataFrame({'Name': ['Dricus Du Plessis']})
men_middle_df = pd.concat([new_row_7, men_middle_df], ignore_index=True)
men_middle_df = men_middle_df.iloc[:-1]

men_welterweight = pd.read_csv('cache/men_welterweight.csv')
men_welter_df = pd.DataFrame(men_welterweight)
new_row_8 = pd.DataFrame({'Name': ['Belal Muhammad']})
men_welter_df = pd.concat([new_row_8, men_welter_df], ignore_index=True)
men_welter_df = men_welter_df.iloc[:-1]

women_strawweight = pd.read_csv('cache/women_strawweight.csv')
women_straw_df = pd.DataFrame(women_strawweight)
new_row_9 = pd.DataFrame({'Name': ['Zhang Weili']})
women_straw_df = pd.concat([new_row_9, women_straw_df], ignore_index=True)
women_straw_df = women_straw_df.iloc[:-1]

women_bantamweight = pd.read_csv('cache/womens_bantamweight.csv')
women_bantam_df = pd.DataFrame(women_bantamweight)
new_row_10 = pd.DataFrame({'Name': ['Julianna Pena']})
women_bantam_df = pd.concat([new_row_10, women_bantam_df], ignore_index=True)
women_bantam_df = women_bantam_df.iloc[:-1]

women_flyweight = pd.read_csv('cache/womens_flyweight.csv')
women_fly_df = pd.DataFrame(women_flyweight)
new_row_11 = pd.DataFrame({'Name': ['Valentina Shevchenko']})
women_fly_df = pd.concat([new_row_11, women_fly_df], ignore_index=True)
women_fly_df = women_fly_df.iloc[:-1]

dfs_dict = {
    "men_feather_df": men_feather_df,
    "men_bantam_df": men_bantam_df,
    "men_middle_df": men_middle_df,
    "men_welter_df": men_welter_df,
    "men_light_df": men_light_df,
    "men_light_heavy_df": men_light_heavy_df,
    "men_heavy_df": men_heavy_df,
    "men_fly_df": men_fly_df,
    "women_straw_df": women_straw_df,
    "women_bantam_df": women_bantam_df,
    "women_fly_df": women_fly_df,
} 

outside_fighter_data = pd.read_csv('data/master_chat_set.csv')
outside_fighter_df = pd.DataFrame(outside_fighter_data)

updated_dfs = []
for name, df in dfs_dict.items():
    updated_df = df.merge(outside_fighter_df, on='Name', how='left')  
    updated_dfs.append(updated_df)
    updated_df.to_csv(f'cache/{name}.csv', index=False)


'''

for df in list_of_men:
    for index, row in df.itterrows():
        fighter = row['Name']
        api_key = "c1cf05ccf76ed2d44c38714a"
        uri = "https://cent.ischool-iot.net/api/openai/generate"
        prompt = f"What is the age, height, weight, place of birth, fightying style, training location, reach, and leg reach of {fighter}"
        data = { "query": prompt }
        response = requests.post(uri, data=data, headers={"x-api-key": api_key})
        response.raise_for_status()
        result = response.json()

        fighter['Age'] = result['results'][0]['age']
        figher['Height'] = result['results'][0]['height']
        fighter['Weight'] = result['results'][0]['weight']
        fighter['Place of Birth'] = result['results'][0]['place of birth']
        fighter['Fighting Style'] = result['results'][0]['fighting style']
        fighter['Training Location'] = result['results'][0]['training location']
        fighter['Reach'] = result['results'][0]['reach']
        fighter['Leg Reach'] = result['results'][0]['leg reach']
'''

list_of_men = [men_feather_df, men_bantam_df, men_middle_df, men_welter_df, men_light_df, men_light_heavy_df, men_heavy_df, men_fly_df]
list_of_women = [women_bantam_df, women_fly_df, women_straw_df]

merged_df = pd.concat(updated_dfs, ignore_index=True)
men_merged_df = pd.concat(updated_dfs[:8], ignore_index=True)
women_merged_df = pd.concat(updated_dfs[8:], ignore_index=True)

merged_df.to_csv('cache/merged_df.csv', index=False)
men_merged_df.to_csv('cache/men_merged_df.csv', index=False)
women_merged_df.to_csv('cache/women_merged_df.csv', index=False)
