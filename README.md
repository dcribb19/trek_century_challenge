# Trek Century Challenge - 2020  
This is a project for tracking miles ridden on my bike during July 2020 for the Trek Century Challenge on Strava. 

## Motivation
The Trek Century Challenge is a cycling challenge on the popular exercise tracking app Strava. The challenge runs for the entire month of July and has 3 goals for miles ridden: 100, 500, and 1,000. The best reward (Coffee Mug!) unlocks after only 100 miles. But, as an avid cyclist, I wanted to see how far that I can push myself. Looking back at the last few years that I have been cycling, my 2 biggest months in terms of mileage were 717 and 702. With that being said, I routinely ride over 500 miles per month, so I decided to go all out for the 1,000. Then, I decided that I wanted an easy way to see how I was progressing daily vs my new lofty goal.  

There were 3 things that I wanted to create:
1. Bar chart to visualize daily miles  
2. Line graph to visualize total miles vs. a linear pace to hit 1,000 miles over 31 days  
3. A text representation of my current progress

I used matplotlib to create the bar chart and line graph. After creating these, I wanted to consolidate them into one report that can be generated after each ride to check where I stand. I figured that a .pdf would be an ideal document for this and discovered the reportlab package which allows for the creation of .pdfs.

## Examples
![example](https://github.com/dcribb19/trek_century_challenge/blob/master/reports/example.png)

## Technology  
- Python 3.8

## Requirements
- [matplotlib](https://matplotlib.org/)
- [numpy](https://numpy.org/)
- [reportlab](https://www.reportlab.com/dev/opensource/)

## Usage

1. In july_mileage.py, add ride to outside or zwift dictionary depending on location of ride. Day is an integer, and miles is a float.
    ```python
    date(2020, 7, day): miles
    ```
2. Run daily_report.py
    - Output (All files saved as _month_day.extension)
        - Bar chart saved as .jpg to graphs directory
        - Line graph saved as .jpg to graphs directory
        - daily_report .pdf saved to reports directory


## License
[![License](https://img.shields.io/badge/License-BSD%202--Clause-orange.svg)](https://opensource.org/licenses/BSD-2-Clause)