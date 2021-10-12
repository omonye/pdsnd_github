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
    get_filters.city = input("Please enter a city: ").strip().lower()
    while get_filters.city not in CITY_DATA.keys():
        print("Please enter the correct city")
        get_filters.city = input("Please enter a city: ").strip().lower()
    
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Please enter a month: ").strip().lower()
    all_months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    while month not in all_months:
        print('Please enter a correct month')
        month = input("Please enter a month: ").strip().lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Please enter a day: ").strip().lower()
    days_of_the_week = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while day not in days_of_the_week:
        print('Please enter a correct day')
        day = input("Please enter a day: ").strip().lower()
    
    print('-'*40)
    return get_filters.city, month, day


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

    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month_name().str.upper()
    df['day_of_week'] = df['Start Time'].dt.day_name().str.upper()

    # filter by month if applicable
    if month != 'all':

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]
     
    return df

def view_data(df):
    view_data = input("Would you like to see history of your last 5 individual trip ? Enter yes or no?: ").lower()
    start_loc = 0
    while view_data != 'no':
        print(df.iloc[start_loc: start_loc + 5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()   

        
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print("The most common month is {}".format(most_common_month))
    
    # TO DO: display the most common day of week
    most_common_day= df['day_of_week'].mode()[0]
    print("The most common day of the week is {}".format(most_common_day))
        
    # TO DO: display the most common start hour
    most_common_hour = df['Start Time'].dt.hour.mode()[0]
    print("The most common start hour is {}".format(most_common_hour))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("The most common start station is {}".format(most_common_start_station))
    
    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("The most common end station is {}".format(most_common_end_station))
    
    # TO DO: display most frequent combination of start station and end station trip
    most_common_combo = (df['Start Station'] + ' and ' + df['End Station']).mode()[0] 
    print("The most common combination of start station and end station trip is {}".format(most_common_combo)) 
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print("The total travel time is {}".format(total_time)) 
    
    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print("The mean travel time is {}".format(mean_time))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # TO DO: Display counts of user types
    
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    
    if get_filters.city != 'washington':
        gender = df['Gender'].value_counts()    
        print(gender)
        
        # TO DO: Display earliest, most recent, and most common year orth
        earliest = df['Birth Year'].min()
        most_recent = df['Birth Year'].max()    
        most_common = df['Birth Year'].mode()[0]
        
        print(earliest, most_recent, most_common)
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        view_data(df)              
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
