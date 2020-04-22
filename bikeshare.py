import time
import pandas as pd
import numpy as np
from sys import exit

def get_filters():
        print('Hello! Let\'s explore some US bikeshare data!\n Select a number from from 1-3 to select the city\n1 - Chicago\n2 - New york city\n3 - Washington\n4 - To Exit')
        print('-'*40)
        # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
        i = 1
        city = ''
        i = input()
        while True:    
         if i == '1':
          city = "chicago"
          break
         elif i == '2':
          city = "new york city"
          break     
         elif i == '3':
          city = "washington"
          break
         elif i == '4':
          exit()
         else :
          print('Plese select a number from 1-3 to continue or 4 to exit')
          i = input()    
        
        
        print('Now pick a month from the list by picking a number from 1-6\n1 - January\n2 - February\n3 - March\n4 - April\n5 - May\n6 - June')
        print('-'*40+'\n')
        # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
        i = 1
        month = ''
        i = input()
        while True:    
         if i == '1':
          month = 1
          break
         elif i == '2':
          month = 2
          break     
         elif i == '3':
          month = 3
          break
         elif i == '4':
          month = 4
          break
         elif i == '5':
          month = 5
          break
         elif i == '6':
          month = 6
          break
         else :
          print('Plese select a number from 1-6 to continue')
          i = input()    
              
        print('Now pick a day from the list by picking a number from 1-7\n1 - Sunday\n2 - Monday\n3 - Tuesday\n4 - Wendesday\n5 - Thursday\n6 - Friday\n7 - Saturday')
        print('-'*40+'\n')
        # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
        i = 1
        day = ''
        i = input()
        while True:    
         if i == '1':
          day = 5
          break
         elif i == '2':
          day = 6
          break     
         elif i == '3':
          day = 0
          break
         elif i == '4':
          day = 1
          break
         elif i == '5':
          day = 2
          break
         elif i == '6':
          day = 3
          break
         elif i == '7':
          day = 4
          break
         else :
          print('Plese select a number from 1-7 to continue')
          i = input()
         
        return city, month, day


def load_data(city, month, day):
  if city == "chicago":
   df = pd.read_csv("chicago.csv")
  
  elif city == "new york city":
   df = pd.read_csv("new_york_city.csv")
   
  else :
   df = pd.read_csv("washington.csv") 
  df['Start Time'] = pd.to_datetime(df['Start Time'])
  df = df[df['Start Time'].dt.month == month]
  df = df[df['Start Time'].dt.dayofweek == day]
  return df

def load_temp_data(city, month, day):
  if city == "chicago":
   
   temp = pd.read_csv("chicago.csv")
  elif city == "new york city":
   
   temp = pd.read_csv("chicago.csv")
  else :
   
   temp = pd.read_csv("chicago.csv")

  return temp


def time_stats(temp):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    temp['month'] = pd.DatetimeIndex(temp['Start Time']).month_name()
    temp2 = temp['Start Time'].groupby(temp['month']).count().reset_index(name="Number of Uses")
    temp2 = temp2.sort_values(by=['Number of Uses'],ascending=False)
    print(temp2.iloc[0].to_string())

    # TO DO: display the most common day of week
    temp['day'] = pd.DatetimeIndex(temp['Start Time']).day_name()
    temp3 = temp['Start Time'].groupby(temp['day']).count().reset_index(name="Number of Uses")
    temp3 = temp3.sort_values(by=['Number of Uses'],ascending=False)
    print(temp3.iloc[0].to_string())

    # TO DO: display the most common start hour
    temp['hour'] = pd.DatetimeIndex(temp['Start Time']).hour
    temp4 = temp['Start Time'].groupby(temp['hour']).count().reset_index(name="Number of Uses")
    temp4 = temp4.sort_values(by=['Number of Uses'],ascending=False)
    print(temp4.iloc[0].to_string())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    df5 = df['Start Time'].groupby(df['Start Station']).count().reset_index(name="Times Visited")
    df5 = df5.sort_values(by=['Times Visited'],ascending=False)
    print(df5.iloc[0].to_string())

    # TO DO: display most commonly used end station

    df6 = df['Start Time'].groupby(df['End Station']).count().reset_index(name="Times Visited")
    df6 = df6.sort_values(by=['Times Visited'],ascending=False)
    print(df6.iloc[0].to_string())

    # TO DO: display most frequent combination of start station and end station trip
    df['Most Used Combination'] = df['Start Station'].astype(str) + ' Then ' + df['End Station'].astype(str)
    df7 = df['Most Used Combination'].groupby(df['Most Used Combination']).count().reset_index(name="Times Visited")
    df7 = df7.sort_values(by=['Times Visited'],ascending=False)
    print(df7.iloc[0].to_string())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print(df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print(df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    df8 = df['User Type'].groupby(df['User Type']).count().reset_index(name="Count")
    print(df8)

    # TO DO: Display counts of gender
    df9 = df['Gender'].groupby(df['Gender']).count().reset_index(name="Count")
    print(df9)

    # TO DO: Display earliest, most recent, and most common year of birth
    df10 = df['Birth Year'].min()
    print('Most Recent Date Of Birth \n')
    print(df10)
    print('Earliest Date Of Birth \n')
    df11 = df['Birth Year'].max()
    print(df11)
    print('Most Common Date Of Birth \n')
    df12 = df['Birth Year'].groupby(df['Birth Year']).count().reset_index(name="Number of Users")
    df12 = df12.sort_values(by=['Number of Users'],ascending=False)
    print(df12.iloc[0].to_string())
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        temp = load_temp_data(city, month, day)
        time_stats(temp)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

