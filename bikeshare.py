import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


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
    city = input("Let\'s chose one of those cities 'Chicago', New York City or Washington:\n>> ").lower()
    # Make city list, to use it later as continer for all cities if we will add more in the dictionary
    citylist = []
    for key in CITY_DATA.keys():
        citylist.append(key)
    # used while loop to keep trying over invalid inputs
    while True:
        if city in citylist:
            break
        # .lower used to ignore any CaSe inputs
        else:
            city = input("Sorry I didn\'t got your choice, Please chose valid input:\n>> ").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Great, Now please chose the month you wan\'t to check up to June, all is accepted:\n>> ").lower()
    month_list = ["all", "january", "february", "march", "april", "may", "june"]
    while True:
        if month in month_list:
            break
        else:
            month = input("Oooh, are you joking, there is no month in that name, Chose again correct one:\n>> ").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Good Job, one last thing. Could you please select day of the week you want to analyse ?"
                "\nYou can chose 'All' if you are not sure yet\n>> ").lower()
    day_of_week = ["all", "saturday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday"]
    while True:
        if day in day_of_week:
            break
        else:
            day = input("Hey buddy, i know maybe you got bored, Please enter valid day name or all might work as "
                        "well\n>> ")
    print('-' * 40)

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
    # parse_dates : boolean or list of ints or names or list of lists or dict, default False
    df = pd.read_csv(CITY_DATA[city], parse_dates=['Start Time'])
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()
    if month != 'all':
        df = df[df['month'] == month.title()]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df

# month, day attribute added to func.
def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    # the added attribute used for if loop
    if month == "all":
        df['month'] = df['Start Time'].dt.month_name()
        popular_month = df['month'].mode()[0]
        print("The most common month {}".format(popular_month))


    # TO DO: display the most common day of week
    # the added attribute used for if loop
    if day == "all":
        df['day'] = df['Start Time'].dt.day_name()
        popular_day = df['day'].mode()[0]
        print("Based on your selection\'s,\nThe most common day of the week {}".format(popular_day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("Our Customers prefer to start their rides at {} o\'clock".format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)
# preview_data(city) added to handle the raw data question preview
def preview_data(city):
    answer = input("Do u want to see the RAW Data Example? 'Y'es, 'N'o\n>> ").lower()
    while True:
        if answer == 'y' or answer == 'n':
            break
        else:
            answer = input("It\'s only Y and N is that hard ?").lower()
    i = 0
    g = 5
    df = pd.read_csv(CITY_DATA[city])
    while answer == 'y':
        print(df[i:g])
        answer = input("Do u need more?").lower()
        i = g
        g += 5
        if answer == 'n' or g > len(df):
            break


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_startStation = df['Start Station'].mode()[0]
    print("The most commonly starting points is {}".format(popular_startStation))

    # TO DO: display most commonly used end station
    popular_endStation = df['End Station'].mode()[0]
    print("But the customers mostly prefer to end the ride in {} station".format(popular_endStation))

    # TO DO: display most frequent combination of start station and end station trip
    popular_combination = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print("The most combined starting and ending points are {}".format(popular_combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    # the time in the DataFrame calculated by seconds, so its converted to Hours
    total_travelTime = ((df['Trip Duration'].sum()) / 3600).__round__(2)
    print("Total Travel Hours:\n{} Hours".format(total_travelTime))

    # TO DO: display mean travel time
    # The AVG travel time per each trip less than 1 Hour, we keep it by minutes
    avg_travelTime = ((df['Trip Duration'].mean()) / 60).__round__(0)
    print("The average duration for trips:\n{} Minutes".format(avg_travelTime))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Our Users Distribution:\n{}".format(user_types))

    # TO DO: Display counts of gender
    # Some list's dose not contain the details about the gender, so we use if loop to check the data is available in DF
    if 'Gender' not in df.columns:
        pass
    else:
        genderCount = df['Gender'].value_counts()
        print("Our users distribution\n{}".format(genderCount))

    # TO DO: Display earliest, most recent, and most common year of birth
    # Birth Year is missing in some DF, so we used the if loop to check if it's available or not
    if 'Birth Year' not in df.columns:
        pass
    else:
        mostCommonBirthYear = int(df['Birth Year'].value_counts().idxmax())
        print("Most Bike-sharers Born On:\n{}".format(mostCommonBirthYear))
        mostRecent = int(df['Birth Year'].max())
        print("Most recent birth year:\n{}".format(mostRecent))
        earliest_year = int(df['Birth Year'].min())
        print("Most most recent birth year:\n{}".format(earliest_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        preview_data(city)
        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter "y"es or "n"o.\n')
        if restart.lower() != 'y':
            break


if __name__ == "__main__":
    main()