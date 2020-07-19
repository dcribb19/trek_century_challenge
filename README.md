# Trek Century Challenge - 2020  
This is a project for tracking miles ridden on my bike during July 2020 for the Trek Century Challenge on Strava. 

## Motivation
The Trek Century Challenge is a cycling challenge on the popular exercise tracking app Strava. The challenge runs for the entire month of July and has 3 goals for miles ridden: 100, 500, and 1,000. The best reward (Coffee Mug!) unlocks after only 100 miles. But, as an avid cyclist, I wanted to see how far that I can push myself. Looking back at the last few years that I have been cycling, my 2 biggest months in terms of mileage were 717 and 702. With that being said, I routinely ride over 500 miles per month, so I decided to go all out for the 1,000. Then, I decided that I wanted an easy way to see how I was progressing daily vs my new lofty goal.  

There were 3 things that I wanted to create:
1. Bar chart to visualize miles ridden per day  
2. Line graph to visualize total miles ridden vs. a linear pace to hit 1,000 miles over 31 days  
3. A text representation of my current progress

I used matplotlib to create the bar chart and line graph. After creating these, I wanted to consolidate them into one report that can be generated after each ride to check where I stand. I figured that a .pdf would be an ideal document for this and discovered the reportlab package which allows for the creation of .pdfs.

## Examples
![report](https://github.com/dcribb19/trek_century_challenge/blob/master/examples/report.png)

## Technology  
- Python 3.8

## Requirements
- [matplotlib](https://matplotlib.org/)
- [numpy](https://numpy.org/)
- [PySimpleGUI](https://pysimplegui.readthedocs.io/en/latest/)
- [reportlab](https://www.reportlab.com/dev/opensource/)

## Usage
```python
python daily_report.py
```
GUI will display.  
![gui](https://github.com/dcribb19/trek_century_challenge/blob/master/examples/gui.png)  
... button will bring up calendar in order to select date.  
![calendar](https://github.com/dcribb19/trek_century_challenge/blob/master/examples/calendar.png)  
Then, enter miles, select location, and submit.  
- Output (All files saved with _month_day.extension)  
    - Bar chart saved as .jpg to graphs directory
    - Line graph saved as .jpg to graphs directory
    - Report .pdf saved to reports directory

## License
[![License](https://img.shields.io/badge/License-BSD%202--Clause-orange.svg)](https://opensource.org/licenses/BSD-2-Clause)