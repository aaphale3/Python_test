# This program will provide information on bikeshares in three cities.

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

DAY_DICT = { "monday" : "0",
             "tuesday" : "1",
             "wednesday" : "2",
             "thursday" : "3",
             "friday" : "4",
             "saturday" : "5",
             "sunday" : "6" }

cities = ["chicago", "new york city", "washington"]
months = ["1", "2", "3", "4", "5", "6"]
day_of_week = ["saturday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday"]

#--------------------------------------------------------------------------------
print('Hello! Let\'s explore some US bikeshare data!')
# function to return DataFrame for selected city--------------------------------
def get_df_for_city():

    while True:
        city = input("We have data for three cities available. Select Chicago, Washington, or New York City: ").lower()
        if city in cities:
            break

    file_name = CITY_DATA.get(city)
    df = pd.read_csv(file_name)

    return df

# function to get data based on user selecting month and day of week--------------------------------
def get_filters():
    """
    Asks user to specify a month and day to analyze.

    Returns:
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """


    while True:
        month = input('Select a month number between 1 and 6; e.g. 1 = Jan ' )
        if month in months:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Enter a day of the week. ' ).lower()


        if day in day_of_week:
            dict_day = DAY_DICT.get(day)
            break

    print('-'*40)
    return month, dict_day

# function to return DataFrame with info from selected city--------------------------------
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # get csv file name from dictionary
    file_name = CITY_DATA.get(city)
    df = pd.read_csv(file_name)

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    #df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        result_month = months.index(month) + 1
        #print(result_month)
        df = df[df['month'] == result_month]

    if day != 'all':
        #print(day)
        df = df[df['day_of_week'] == int(day)]
        '''print(df)
        print("I am here")'''
    return df

# functions to return time_stats------------------------------------------------------------------------
def get_most_common_month(df):
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # most common month
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].value_counts().idxmax()
    return common_month

def get_most_common_day(df):
    df['Start Time'] = pd.to_datetime(df['Start Time'])
# most common day of week
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    common_day_of_week = df['day_of_week'].value_counts().idxmax()
    return common_day_of_week

def get_most_common_hour(df):
    df['Start Time'] = pd.to_datetime(df['Start Time'])
# most common hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].value_counts().idxmax()
    return common_hour

# functions to return station_stats----------------------------------------------------------------------------
def get_most_common_start_station(df):
    common_start_station =  df['Start Station'].value_counts().idxmax()
    return common_start_station

def get_most_common_end_station(df):
    common_end_station = df['End Station'].value_counts().idxmax()
    return common_end_station

def get_most_common_combo_station(df):
    common_combination = df[['Start Station', 'End Station']].mode().loc[0]
    return common_combination

# functions to return trip_duration_stats--------------------------------------------------------------------------------
def get_total_travel_time(df):
    total_travel_time = df['Trip Duration'].sum()
    return total_travel_time

def get_mean_travel_time(df):
    mean_travel_time = df['Trip Duration'].mean()
    return mean_travel_time

# functions to return user_stats-------------------------------------------------------------------------------------
def get_user_type_counts(df):
    user_type_counts = df['User Type'].value_counts()
    return user_type_counts

def get_gender_counts(df):
    gender_counts = df['Gender'].value_counts()
    return gender_counts

def get_earliest_year(df):
    earliest_year = df['Birth Year'].min()
    return earliest_year

def get_recent_year(df):
    recent_year = df['Birth Year'].max()
    return recent_year

def get_common_birth_year(df):
    common_birth_year = df['Birth Year'].value_counts().idxmax()
    return common_birth_year
# main_function-------------------------------------------------------------------
def main():
    try:
        while True:
            my_df = get_df_for_city()
        # calling time_stats--------------------------------------------------------------
            my_month = get_most_common_month(my_df)
            get_most_common_month(my_df)
            print("Most common month: " + str(my_month))
            my_day = get_most_common_day(my_df)
            print("Most common day: " + str(my_day))
            my_hour = get_most_common_hour(my_df)
            print("Most common hour: " + str(my_hour))
        # calling station_stats-------------------------------------------------------
            my_start_station = get_most_common_start_station(my_df)
            print("Most common start station: " + my_start_station)
            my_end_station = get_most_common_end_station(my_df)
            print("Most common end station: " + my_end_station)
            my_combo_station = get_most_common_combo_station(my_df)
            print("Most common station combination: " + my_combo_station[0], my_combo_station[1])
        # calling trip_duration_stats--------------------------------------------------
            my_total_travel_time = get_total_travel_time(my_df)
            print("Total travel time: " + str(my_total_travel_time))
            my_mean_travel_time = get_mean_travel_time(my_df)
            print("Mean travel time: " + str(my_mean_travel_time))
        # calling user_stats----------------------------------------------------------
            my_user_type_counts = get_user_type_counts(my_df)
            print("The number of user types is: " + "\n" + str(my_user_type_counts))
            if 'Gender' in my_df.columns: # Washington does not have gender column so add "if" conditional to check
                my_gender_counts = get_gender_counts(my_df)
                print("The gender count is: " + "\n" + str(my_gender_counts))
            if 'Birth Year' in my_df.columns:
                my_earliest_year = get_earliest_year(my_df)
                print("Earliest year of birth: " + str(int(my_earliest_year)))
                my_recent_year = get_recent_year(my_df)
                print("Most recent year of birth: " + str(int(my_recent_year)))
                my_common_birth_year = get_common_birth_year(my_df)
                print("Most common year of birth: " + str(int(my_common_birth_year)))
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                break
    except:
        print("An error occurred! Please contact support.")

# calling main_function --------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
