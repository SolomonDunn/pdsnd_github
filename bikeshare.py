#Refactor Version
#This python program interfaces with a user to return data from csv files 

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''

    while city != 'chicago' or city != 'washington' or city != 'new york city':
        city = input('Select the city: Chicago, New York City, Washington: ').lower()
        if city == 'chicago':
            break
        if city == 'new york city':
            break
        if city == 'washington':
            break
        print('The city entered is not available. Try again.')  

    # TO DO: get user input for month (all, january, february, ... , june)
    month = ''   
    
    #Run while loop to handle spelling errors in user input
    while month != 'all' or month != 'january' or month != 'february' or month != 'march' or month != 'april' or month != 'may' or month != 'june':
        month = input('Select the month: All, January, February, March, April, May, June: ').lower()
        #Test month input against list of options
        if month == 'all':
            break
        if month == 'january':
            break
        if month == 'february':
            break
        if month == 'march':
            break
        if month == 'april':
            break
        if month == 'may':
            break
        if month == 'june':
            break
        print('The month entered is not available. Try again.')  

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = ''
    
    #Run while loop to handle spelling errors in user input
    while day != 'all' or day != 'january' or day != 'february' or day != 'march' or day != 'april' or day != 'may' or day != 'june':
        day = input('Select the day of the week: All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday: ').lower()
        #Test day input against list of options
        if day == 'all':
            break
        if day == 'monday':
            break
        if day == 'tuesday':
            break
        if day == 'wednesday':
            break
        if day == 'thursday':
            break
        if day == 'friday':
            break
        if day == 'saturday':
            break
        if day == 'sunday':
            break
        print('The day of the week entered is not available. Try again.')  

    print('-'*40)
    return city, month, day

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
    #Set DatFrame using CSV file for City defined 
    df =  pd.read_csv(CITY_DATA.get(city))
    
    #Convert df Start Time column to date time type
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #Create new column month in DataFrame 
    df['month'] = df['Start Time'].dt.month
    #Create new column day of week in DataFrame 
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month']==month]
    
    if day != 'all':
        # filter by day of week to create the new dataframe
        days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday']
        day_num = days.index(day)
        df = df[df['day_of_week'] == day_num]
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # TO DO: display the most common month
    # extract hour from the Start Time column to create an hour column
    df['month'] = df['Start Time'].dt.month
        
    popular_month = df['month'].mode()[0]
        
    print('Most Common Month:', popular_month)

    # TO DO: display the most common day of week
    #Extract day of week from Start Time column
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    
    popular_day = df['day_of_week'].mode()[0]
        
    print('Most Common Day of Week:', popular_day)

    # TO DO: display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most common hour
    popular_hour = df['hour'].mode()[0]

    print('Most Common Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    #'Start Station'
    start_station = df['Start Station'].mode()[0]

    print('Most popular start station:', start_station)
    
    # TO DO: display most commonly used end station
    #'End Station'
    end_station = df['End Station'].mode()[0]

    print('Most popular end station:', end_station)
    
    # TO DO: display most frequent combination of start station and end station trip
    df['trip_combo'] = df['Start Station']+df['End Station']
    
    trip_combo = df['trip_combo'].mode()[0]
    
    print('Most popular start and end station combination:', trip_combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    #Trip Duration
    # TO DO: display total travel time
    travel_time = df['Trip Duration'].sum()

    print('Total travel time:', travel_time)
    
    # TO DO: display mean travel time
    travel_time = df['Trip Duration'].mean()

    print('Total mean time:', travel_time)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    #User Type
    user_type = df['User Type'].value_counts()

    print('Counts of different user types:\n', user_type)
    
    # TO DO: Display counts of gender
    #Gender
    gender = df['Gender'].value_counts()

    print('Counts of different genders:\n', gender)
    
    # TO DO: Display earliest, most recent, and most common year of birth
    #Birth Year
    #earliest
    birth_year = df['Birth Year'].min()

    print('The earliest birth year:', birth_year)
    
    #most recent
    birth_year = df['Birth Year'].max()

    print('The most recent birth year:', birth_year)
    
    #most common year
    birth_year = df['Birth Year'].mode()[0]

    print('The most common birth year:', birth_year)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
