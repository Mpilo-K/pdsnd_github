import time
import pandas as pd
import numpy as np 

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

DAY_DATA = ['monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday', 'all']

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
    city_name = ''
    while city_name.lower() not in CITY_DATA:
        city_name = input("\nWhich city would you like to filter the data for (chicago, new york city or washington)?\n")
        if city_name.lower() in CITY_DATA:
            #A correct name of the city to filter the data was recieved, thanks.
            city = CITY_DATA[city_name.lower()]
        else:
            #An incorrect name of the city to filter the data was recieved, thus we kindly request re-entry of input.
            print("Sorry that is not the correct name of the city, kindly enter either chicago, new york city or washington.\n")

    # TO DO: get user input for month (all, january, february, ... , june)
    month_name = ''
    while month_name.lower() not in MONTH_DATA:
        month_name = input("\nWhich month would you like to filter the data for(january, february, ... , june or 'all' to apply no month filter)\n")
        if month_name.lower() in MONTH_DATA:
            # A correct name of the month to filter the data was recieved, thanks.
            month = month_name.lower()
        else:
            #An incorrect name of a month to filter the data was recieved, thus we kindly request re-entry of input..
            print("Sorry that is not the correct name of the month, kindly input january, february, ... , june or 'all' to apply no month filter.\n")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_name = ''
    while day_name.lower() not in DAY_DATA:
        day_name = input("\nWhich day would you like to filter the data for? (monday, tuesday, ... sunday or 'all' to apply no day filter)\n")
        if day_name.lower() in DAY_DATA:
            #A correct name of the day to filter the data was recieved, thanks.
            day = day_name.lower()
        else:
            #An incorrect name of a day to filter the data was recieved, thus we kindly request re-entry of input.
            print("Sorry that is not correct name of the day to filter data, Kindly input monday, tuesday, ... sunday or 'all' to apply no day filter.\n")

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
    # import data file into a dataframe(df)
    df = pd.read_csv(city)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract month, day of week, start hour, end hour to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['start_hour'] = df['Start Time'].dt.hour
    df['end_hour'] = df['End Time'].dt.hour


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = MONTH_DATA.index(month)

        # filter by month to create the new dataframe
        df = df.loc[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    #print("The most common month to travel is: " + str(common_month))
    print("The most common month to travel is: " + MONTH_DATA[common_month].title())

    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print("The most common day of week to travel is: " + common_day_of_week)

    # TO DO: display the most common start hour
    common_start_hour = df['start_hour'].mode()[0]
    if common_start_hour < 12:
        print("The most common start hour to travel is: " + str(common_start_hour) + ":00 am")
    elif common_start_hour >= 12:
        print("The most common start hour to travel is: " + str(common_start_hour) + ":00 pm")

    # TO DO: display the most common end hour
    common_end_hour = df['end_hour'].mode()[0]
    if common_end_hour < 12:
        print("The most common end hour of travel is: " + str(common_end_hour) + ":00 am")
    elif common_end_hour >= 12:
        print("The most common end hour of travel is: " + str(common_end_hour) + ":00 pm")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station to travel is: " + common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station after travel is: " + common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination = (df['Start Station'] + "||" + df['End Station']).mode()[0]
    print("The most frequent combination of start station and end station trip is : " + str(frequent_combination.split("||")) + " stations")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display minum travel time
    min_travel_time = df['Trip Duration'].min()
    if min_travel_time <= 60:
        print("The shorstest travel time is: " + str(round(min_travel_time)) + " minutes")
    elif min_travel_time > 60:
        hours = min_travel_time/60
        print("The shorstest travel time is: " + str(round(hours)) + " hours")

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    if mean_travel_time <= 60:
        print("The average travel time is: " + str(round(mean_travel_time)) + " minutes")
    elif mean_travel_time > 60:
        hours = mean_travel_time/60
        print("The average travel time is: " + str(round(hours)) + " hours")

    # TO DO: display maximum travel time
    max_travel_time = df['Trip Duration'].max()
    if max_travel_time <= 60:
        print("The longest travel time is: " + str(round(max_travel_time)) + " minutes")
    elif max_travel_time > 60:
        hours = max_travel_time/60
        print("The longest travel time is: " + str(round(hours)) + " hours")

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    if total_travel_time <= 60:
        print("The total travel time is: " + str(round(total_travel_time)) + " minutes")
    elif total_travel_time > 60:
        hours = total_travel_time/60
        print("The total travel time is: " + str(round(hours)) + " hours")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The count of users by type is: \n" + str(user_types))

    print('-'*40)

    # Demographic data only exists in Chicago and New York City, Thus:
    if city == 'chicago.csv' or city == 'new_york_city.csv':
        # TO DO: Display counts of gender
        gender = df['Gender'].value_counts()
        print("The count of users by gender is: \n" + str(gender))

        print("\n")
        print('-'*40)

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth = df['Birth Year'].min()
        most_recent_birth = df['Birth Year'].max()
        most_common_birth = df['Birth Year'].mode()[0]
        print('The oldest person to travel was born on the year: {}\n'.format(round(earliest_birth)))
        print('The youngest person to travel was born on the year: {}\n'.format(round(most_recent_birth)))
        print('Most people who travel are born on the year: {}\n'.format(round(most_common_birth)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(df):
    """Displays raw data on user request.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """
    print(df.head())
    next = 0
    while True:
        view_raw_data = input('\nWould you like to view next five row of raw data? Enter yes or no.\n')
        if view_raw_data.lower() != 'yes':
            return
        next = next + 5
        print(df.iloc[next:next+5])


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        while True:
            view_raw_data = input('\nWould you like to view first five row of raw data? Enter yes or no.\n')
            if view_raw_data.lower() != 'yes':
                break
            display_raw_data(df)
            break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()