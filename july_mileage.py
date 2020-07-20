# july_mileage.py
# Visualize cycling stats for July 2020 Trek Century Challenge on Strava.

import csv
from datetime import date, datetime, timedelta
from matplotlib import pyplot as plt
import numpy as np
import os.path

graph_path = os.path.join(os.getcwd(), 'graphs/')

TODAY = date.today()
REPORT_SUFFIX = TODAY.strftime('%m_%d')
GOAL = 1000
DAILY_GOAL = round(GOAL / 31, 1)

july_dates = [date(2020, 7, x) for x in range(1, 32)]
pace = [round(DAILY_GOAL * x, 1) for x in range(1, 32)]

outside = {}
zwift = {}
with open('rides.csv', 'r', newline='') as csvfile:
    ride_reader = csv.reader(csvfile)
    for row in ride_reader:
        date_csv = datetime.strptime(row[0], '%Y-%m-%d').date()
        miles = float(row[1])
        location = row[2]
        if location == 'outside':
            outside[date_csv] = miles
        else:
            zwift[date_csv] = miles


def format_dates(dates: list) -> list:
    '''
    Take list of datetime.date objects and return list of strings for xlabels
    '''
    return sorted(set([day.strftime('%b-%d') for day in dates]))


def format_dict_dates(a_dict: dict) -> dict:
    '''
    Add date and set miles to 0 if no ride on day.
    '''
    for day in july_dates:
        if day not in a_dict.keys() and day <= TODAY:
            a_dict[day] = 0
    return a_dict


def bar_stats():
    '''
    plot mileage as stacked bar chart
    '''

    '''
    Turn dicts into sorted listed of tuples (date, miles)
    after formatting dict with dict[date] = 0 if date not in dict
    '''
    outside_bar = sorted(format_dict_dates(outside).items())
    zwift_bar = sorted(format_dict_dates(zwift).items())

    dates = format_dates([x[0] for x in outside_bar])
    dates = np.array(dates)
    # Take sorted list and convert to np.array
    z = np.array([x[1] for x in zwift_bar])
    o = np.array([x[1] for x in outside_bar])

    plt.figure(1)
    plt.bar(dates, z, label='Zwift', bottom=o, color='orange')
    plt.bar(dates, o, label='Outside', color='blue')

    # Plot horizontal line representing daily pace needed.
    plt.axhline(DAILY_GOAL, linestyle='--', label='Goal Pace', color='k')
    # TODO: Fix xticks to show label on image.
    plt.title('Daily Miles Ridden - July 2020')
    # plt.xlabel('Date')
    plt.xticks(rotation=45)
    x_step = 0
    if len(dates) <= 20:
        x_step = 4
    elif len(dates) > 20 and len(dates) < 26:
        x_step = 5
    else:
        x_step = 7
    plt.xticks(np.arange(0, len(dates), x_step))
    plt.ylabel('Miles')
    plt.yticks(np.arange(0, 91, 10))
    plt.legend()
    # Save image in graph folder
    bar_path = os.path.join(graph_path, 'bar_stats_' + REPORT_SUFFIX + '.jpg')
    plt.savefig(bar_path, bbox_inches='tight', dpi=300, opimize=True)


def pace_stats():
    '''
    Plot line graph of miles ridden vs. pace
    '''
    plt.figure(2)
    # Goal pace line
    plt.plot(format_dates(july_dates), pace, '--', label='Goal Pace')

    # Current stats line
    o = format_dict_dates(outside)
    z = format_dict_dates(zwift)
    x = np.array(format_dates(list(o.keys())))
    y = []
    running_total = 0

    daily_miles = np.array(
            [o[day] + z[day] for day in july_dates if day <= TODAY]
        )

    for day in daily_miles:
        running_total += day
        y.append(running_total)

    plt.plot(x, y, 'g', label='Miles Ridden')
    plt.title('Miles Ridden - July 2020')
    # plt.xlabel('Date')
    plt.xticks(rotation=45)
    plt.xticks(np.arange(0, 31, 7))
    plt.ylabel('Miles')
    plt.legend()
    # Save image in graphs folder
    pace_path = os.path.join(
                    graph_path, 'pace_stats_' + REPORT_SUFFIX + '.jpg'
                )
    plt.savefig(pace_path, bbox_inches='tight', dpi=300, opimize=True)


def current_stats() -> str:
    '''
    Return string representation of current stats
    '''
    TODAY = date.today()
    # Do not let date go past Aug 1
    current_stats = ''
    if TODAY > date(2020, 8, 1):
        TODAY = date(2020, 8, 1)

    miles_ridden = round(sum(outside.values()) + sum(zwift.values()), 1)
    remaining = round(GOAL - miles_ridden, 1)
    days_left = date(2020, 7, 31) - TODAY
    pace = round((GOAL / 31) * TODAY.day, 1)
    percentage = round((miles_ridden / GOAL) * 100, 1)

    current_stats = ('As of ' + TODAY.strftime('%b %d, %Y') + ' -\n'
                     + str(miles_ridden) + ' miles ridden. ('
                     + str(percentage) + '% complete)\n')

    if days_left.days < 0:
        current_stats += 'Month is over. Good effort!'
    else:
        current_stats += (str(days_left.days) + ' days left. '
                          + str(remaining) + ' miles remaining. ('
                          + str(round(remaining / days_left.days, 1))
                          + ' mi/day)\n')
    if miles_ridden > GOAL:
        current_stats += 'Challenge Completed! ' + str(miles_ridden)
        current_stats += ' miles ridden.'
    elif miles_ridden > pace:
        current_stats += str(round(miles_ridden - pace, 1))
        current_stats += ' miles ahead of schedule.'
    else:
        current_stats += str(round(miles_ridden - pace, 1))
        current_stats += ' miles behind schedule.'
    return current_stats


def print_current_stats(current_stats: str):
    '''
    Print text representation of current stats
    '''
    for line in current_stats.splitlines():
        print(line)
