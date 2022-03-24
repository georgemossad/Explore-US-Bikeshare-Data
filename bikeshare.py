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
    while True:
        city=input('Enter city name:  chicago, washington or new york city ?').lower()
        
        if city in ['chicago','washington','new york city'] :
            break
        else:
            print('invalid input, your city input should be: chicago, washington or new york city ?')
            

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month=input('Enter month name: all,january,february,...,june ?').lower()
        
        if month in ['all','january','february','march','april','may','june'] :
            break
        else:
            print('invalid input, your month input should be: january, february, march, april, may, june or all') 

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input('Enter the day of the week : all, monday, tuesday, ... sunday ?').lower()
        
        if day in ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
            break
        else:
            print('invalid input, your day input should be:  all, monday , tuesday , wednesday , thursday , friday , saturday or sunday' )

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    most_common_month=df['month'].mode()[0]
    print('The most common month is: ',most_common_month)
    # TO DO: display the most common day of week
    most_common_day=df['day_of_week'].mode()[0]
    print('The most common day of the week is: ',most_common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour=df['hour'].mode()[0]
    print('The most common hour is: ',most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station=df['Start Station'].mode()[0]
    print('The most common start station used is: ',popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station=df['End Station'].mode()[0]
    print('The most common end station used is:  ',popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Start Station to End Station']=df['Start Station']+' to '+ df['End Station']
    most_station_combination=df['Start Station to End Station'].mode()[0]
    print('The most combination of Start Station to End Station trip: ',most_station_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print('The total travel time for all trips in second: ',total_travel_time)


    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('The mean travel time for all trips in second: ',mean_travel_time)


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
    try:
        user_gender=df['Gender'].value_counts()
        print(user_gender)
    except:
        print('there is no information about gender in this city data')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year=df['Birth Year'].min()

        most_recent_birth_year=df['Birth Year'].max()

        most_common_birth_year=df['Birth Year'].mode()[0]
        print('The earliest birth year for users is: ',earliest_birth_year)

        print('The most recent birth year for users is: ',most_recent_birth_year)

        print('The most common birth year for users is: ',most_common_birth_year)
    except:
        print('there is no information about birth year in this city data')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no? ")
    
    i = 0    
    while (view_data.lower()=='yes'):
        print(df.iloc[i:i+5])
        view_display = input("Do you wish to continue view more data?: ").lower()
        if view_display !='yes':
            break        
        i +=5

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
