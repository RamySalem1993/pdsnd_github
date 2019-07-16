import pandas as pd
import numpy as np
import time

Data_Cities = {"chicago": "chicago.csv",
               "washington": "washington.csv",
               "new york city": "new york city.csv"}
#function which asks for input from the user
def get_filters():


    print('Hello! Let\'s explore some US bikeshare data!')

    city = input("Which city would you like to explore: ").lower()
    while city not in ["chicago","new york city","washington"]:
        city = input("That is a invalid city. Enter again: ").lower()

    month = input("Which month: ").lower()
    while month not in ["all","january","february","march","april","may","june"]:
        month = input("That is a invalid month. Enter again: ").lower()

    day = input("Which day of the week(e.g. Sunday): ").lower()
    while day not in ["all","monday","tuesday","wednesday","thursday","friday","saturday","sunday"]:
        day = input("That is a invalid day. Enter again: ").lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    data = pd.read_csv(Data_Cities[city])
    data["Start Time"] = pd.to_datetime(data["Start Time"])
    data["month"] = data["Start Time"].dt.month
    data["day"] = data["Start Time"].dt.weekday_name
    data["hour"] = data["Start Time"].dt.hour
    print(data)


    if month != "all":
        months = ["january","february","march","april","may","june"]
        #returns index number of the month which is used in the dataset
        month = months.index(month) + 1
        #finds index of that month, since in the data set january = 1
        data = data[data["month"]== month]
        #Here you get the data from alleen the months you selected
    if day != "all":
        data = data[data["day"] == day.title()]
    return data

def time_stats(data):
    start_time = time.time()
    #most common hour
    most_common_hour = data["hour"].mode()[0]
    print("Most common hour is: ", most_common_hour)
    #number of times this most common hour appear
    count_most_common_hour = data["hour"].value_counts()[most_common_hour]
    print("number of times most common hour occurs or how many times a bike is shared in this hour: ",count_most_common_hour)

    #most common day
    most_common_day = data["day"].mode()[0]
    print("Most common day is: ", most_common_day)

    #most common month
    most_common_month = data["month"].mode()[0]
    months = ["january","february","march","april","may","june"]
    most_common_month = months[most_common_month-1]
    print("Most common month is: ", most_common_month)



    #note that if the users input  is a specific day and month this code will always
    #return the same month and day. Only if the users input is "all", most common day
    #and most common month it will make sense.
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def station_stats(data):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_location = data["Start Station"].mode()[0]
    print("Most common start location is: ", most_common_start_location)
    # display most commonly used end station
    most_common_end_location = data["End Station"].mode()[0]
    print("Most common end location is: ", most_common_end_location)
    print("")
    # display most frequent combination of start station and end station trip
    #here I create a new column which is a combination of start and end station.
    """#(Something with group by)
    pop_combo = data.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False).nlargest(n=1)
    most_popular_trip = data.groupby(["Start Station","End Station"]).size().max()
    print("Most popular trip is: ", most_popular_trip_count, most_popular_trip)"""

    data["Start and End location"] = "Start: " +  data["Start Station"] + ", End: " + data["End Station"]
    most_common_combination_EndStart = data["Start and End location"].mode()[0]
    print("Most frequent combination of start station and end station is: \n",most_common_combination_EndStart)
    count_most_common_combination_EndStart = data["Start and End location"].value_counts()[most_common_combination_EndStart]
    print("Number of times this most frequent combination of start station and end station appears: ", count_most_common_combination_EndStart)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(data):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    total_travel_time = data["Trip Duration"].sum()
    # display total travel time
    print("Total travel time is: ",total_travel_time)

    # display mean travel time
    average_travel_time = data["Trip Duration"].mean()
    print("Average travel time is : ", average_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(data):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    counts_usertype = data["User Type"].value_counts()
    print("counts of user types: \n",counts_usertype)
    print("")
    # Display counts of gender
    while True:
        try:
            counts_gender = data["Gender"].value_counts()
            print("counts of gender: \n",counts_gender)
            print("")

    # Display earliest, most recent, and most common year of birth
            earliest = data["Birth Year"].min()
            print("Earliest year of birth: ", earliest)
            recent = data["Birth Year"].max()
            print("Most recent year of birth: ", recent)
            most_common = data["Birth Year"].mode()[0]
            print("Most common year of birth: ", most_common)
            count_most_common = data["Birth Year"].value_counts()[data["Birth Year"].mode()[0]]
            print("number of times most common birth year occurs: " , count_most_common)
            break
        except KeyError:
            print("Washington has no gender/birthyear data")
            break

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(data):
    answer = input("Do you want to see raw data?").lower()
    while answer == "yes":
        rows = int(input("how many rows of the raw data do you want to see? "))
        row_data = data[:rows]
        print(row_data)
        answer = input("do you want to see more rows? ")

def main():
    while True:
        city, month, day = get_filters()
        data = load_data(city, month, day)
        print(data.columns)
        time_stats(data)
        station_stats(data)
        trip_duration_stats(data)
        user_stats(data)
        display_data(data)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
"""
Created on Thu May 23 09:33:30 2019

@author: Ramy Salem
"""
