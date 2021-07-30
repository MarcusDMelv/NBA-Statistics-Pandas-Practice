#dataframe
import pandas as pandas
# request for data that is at a specific url
import requests
# numpy works best with pandas
#work with different data types
import numpy as numpy
#----------------------------------------------------------
# used colwidth to expand the column to show all data
pandas.set_option('display.max_colwidth', -1)
# max_rows will show all the rows, set to none means show all if set to 10 it will only show 10
pandas.set_option('display.max_rows', None)
# max_columns same as rows but for columns
pandas.set_option('display.max_columns', None)

pandas.set_option('display.width', None)
#download csv file from online

# request for data
url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv"
# create file name that pandas will use to save the data from url request... nba.csv
csv_file = 'nba.csv'
#------------------------------------------------------------------------------------------
# how to get info and download it as a csv into /dir
# create a obj that will get the data
response = requests.get(url)
#check status if request went through ...
response.raise_for_status()
#------------------------------------------------------------
# with statement is great for exception handling
# open/create csv file write in byte
with open(csv_file,'wb') as f:
    # obj f has open csv and ready to write in byte
    # obj f writes the content found in request
    f.write(response.content)
# notify when csv file has been populated
print('download ready')
#---------------------------------------------------------------
#edit pandas df table
# used colwidth to expand the column to show all data
pandas.set_option('display.max_colwidth', None)
# max_rows will show all the rows, set to none means show all if set to 10 it will only show 10
pandas.set_option('display.max_rows', None)
# max_columns same as rows but for columns
pandas.set_option('display.max_columns', None)
pandas.set_option('display.width', None)
#--------------------------------------------------------------
#create a pandas object to read the downloaded data nba.csv
# data_frame aka df will now hold the csv file
data_frame = pandas.read_csv('nba.csv')
# shows variable type
print(type(data_frame))
#-------------------------------------
# shows # of rows and columns in data
print(data_frame.shape)
#---------------------------------------
# .head shows first 5
#print(data_frame.head())
# .tail shows the last 5
#print(data_frame.tail())
# if you want specific number of rows displayed
# shows last 3 rows (only )
#print(data_frame.tail(3))
# shows first row ( only )
#print(data_frame.head(1))
# getting to know the data
#---------------------------------------------
# show all columns and their data types shows total of each data type
#print(data_frame.info())
#-----------------------------------------------
# numpy used to work with these data types
# object data types are special - its a catch-all for columns/ Panadas doesn't see a specific data type
# object often means a string
#-----------------------------------------------
# show basic stats of all numeric columns use .describe()

#print(data_frame.describe())

# provide other data types if use the include parameter
# numpy is able to help with this
# told to upgrade pandas?

#print(data_frame.describe(inlcude=numpy.object))
#-------------------------------------------------
# exploring the data set
# help answer questions
# see how often a specific values occur in a column
#team id is the name of a column

# print(data_frame['team_id'].value_counts())
#-------------------------------------------------
# specifically  team_id.show how many time each id is used( shows number of games played)
games_played_team_id = data_frame['team_id'].value_counts()
# show top
#print(games_played_team_id.head(3))
# specifically  fran_id.show how many time each id is used( shows number of games played)
games_played_fran_id = data_frame['fran_id'].value_counts()
# show top 3 franchises
#print(games_played_fran_id.head(3))
# if compare data LAL as a franchise played more games/ BOS as a team played more games?
# why is this lets breakdown LAL
"""
DataFrame.at
Access a single value for a row/column label pair.

DataFrame.iloc
Access group of rows and columns by integer position(s).

DataFrame.xs
Returns a cross-section (row(s) or column(s)) from the Series/DataFrame.

Series.loc
Access group of values using labels.
"""
"""
# use .loc to access group of values
#                    .loc[name of df[find fran_id] == 'find Lakers franchise', 'show team_id with Lakers fran_is'
la_teams = data_frame.loc[data_frame['fran_id'] == 'Lakers', 'team_id'].value_counts()
# show data
print(la_teams)
# MNL? When did MNL play?
# find first game using .min
mnl_first_game = data_frame.loc[data_frame['team_id'] == 'MNL', 'date_game'].min()
# find last game using .max
mnl_last_game = data_frame.loc[data_frame['team_id'] == 'MNL', 'date_game'].max()
# if printed needed to be printed separately
# use agg((min,sum,mean,max)) to bring comparisons together
mnl_dates = data_frame.loc[data_frame['team_id'] == 'MNL', 'date_game'].agg(('min','max'))
print(mnl_dates)
# find BOS total points
bos_total_pts = data_frame.loc[data_frame['team_id'] == 'BOS', 'pts'].sum()
print(bos_total_pts)
#----------------------------------------------------------------------------------------

You can also refer to the 2 dimensions of a DataFrame as axes:
The axis marked with 0 is the row index, and the axis marked with 1 is the column index. 
This terminology is important to know because you’ll encounter several DataFrame methods 
that accept an axis parameter.
"""
# .axes[0] - row // .axes[1] - columns // .axes - shows both columns and rows

"""
A DataFrame is also a dictionary-like data structure, so it also supports .keys() and the in keyword. 
However, for a DataFrame these don’t relate to the index, but to the columns:
>>> city_data.keys()
Index(['revenue', 'employee_count'], dtype='object')
>>> "Amsterdam" in city_data
False
>>> "revenue" in city_data
True
"""
nba_index = data_frame.index
nba_axes = data_frame.axes
#print(nba_axes)
#print(nba_index)

# search for '?' in the database returns a boolean
#print('points' in data_frame.keys())
#print('pts' in data_frame.keys())
# how to select the 2nd to last row of the nba.csv
#print(data_frame.iloc[-2])
#print(data_frame.loc[5555:5559, ['fran_id', 'opp_fran', 'pts', 'opp_pts','year_id']])
#-------------------------------------------------------------------------------------
# querying dataset
# selecting rows based on the values in dataset columns to query data
# example--------------
# create new dataframe based off certain values
# client wants games played after 2010
# create an object
current_decade = data_frame[data_frame['year_id'] > 2010]
#print(current_decade.shape)
# select rows where a specific field is not null
# helps avoid an missing values in a columns
games_with_notes = data_frame[data_frame['notes'].notnull()]
# access values of the obj data type as str and perform string methods on them
ers = data_frame[data_frame['fran_id'].str.endswith('ers')]
#print(ers.shape)
# combine multiple criteria and query data set as well use () for each one
#----example
# search for baltimore games where both teams scored over 100 and show no dupes
data_frame[
    # make sure there is no dupes
    (data_frame['_iscopy'] == 0) &
    # baltimore scored more then 100 pts
    (data_frame['pts'] > 100) &
    # opps scored more then 100
    (data_frame['opp_pts'] > 100) &
    # look for the team BLB
    (data_frame['team_id'] == 'BLB')
]
#-----------------------------------------------------------
"""
Try to build another query with multiple criteria. In the spring of 1992, both teams from Los Angeles had to play 
a home game at another court. Query your dataset to find those two games. Both teams have an ID starting with "LA". 
Expand the code block below to see a solution:
"""
# need to see how values are labeled
print(data_frame.head(1))
la_home_game = data_frame[
    # have no copies
    (data_frame['_iscopy'] == 0) &
    # pick the year 1992
    (data_frame['year_id'] == 1992) &
    #use str as the data type to search use method startswith
    (data_frame['team_id'].str.startswith('LA')) &
    # game location is at H for home
    (data_frame['game_location'] == 'H') &
    # no null in the notes column
    (data_frame['notes'].notnull())
]
print(data_frame.head(1))
print(la_home_game)