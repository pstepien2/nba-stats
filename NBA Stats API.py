#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 00:06:37 2023

@author: pstepien
"""

import requests
import pandas as pd
from pandas import DataFrame


#Get data from API
url = 'https://www.balldontlie.io/api/v1/stats?page=1&per_page=100&seasons[]=2022&seasons[]=2023'

resp = requests.get(url)

df = DataFrame(resp.json()['data'])

#Create games list
games = list(df['game'])

#Change to data frame
df_games = DataFrame(games)

#drop game column
df.drop('game', axis = 1, inplace = True)

#clean up player
players = list(df['player'])
df_players = DataFrame(players)
df.drop('player', axis = 1, inplace = True)

#clean up team
teams = list(df['team'])
df_teams = DataFrame(teams)
df.drop('team', axis = 1, inplace = True)

#merge together
df = pd.concat([df, df_games, df_players, df_teams], axis = 1)