# Trek Century Challenge - 2020  
This is a project for tracking miles ridden on my bike during July 2020 for the Trek Century Challenge on Strava in Python, using matplotlib, numpy, reportlab, and PySimpleGUI. 

## Motivation
The Trek Century Challenge is a cycling challenge on the popular exercise tracking app Strava. The challenge runs for the entire month of July and has 3 goals for miles ridden: 100, 500, and 1,000. The best reward (Coffee Mug!) unlocks after only 100 miles. But, as an avid cyclist, I wanted to see how far I can push myself. Looking back at the last few years that I have been cycling, my 2 biggest months in terms of mileage were 717 and 702. With that being said, I routinely ride over 500 miles per month, so I decided to go all out for the 1,000. Then, I decided that I wanted an easy way to see how I was progressing daily vs my new lofty goal. 

There were 3 things that I wanted to create:
1. Bar chart to visualize miles ridden per day  
2. Line graph to visualize total miles ridden vs. a linear pace to hit 1,000 miles over 31 days  
3. A text representation of my current progress

I used matplotlib to create the bar chart and line graph. After creating them, I wanted to consolidate them with some text into one report that can be generated after each ride to check where I stand. After listening to episode 17 of The Real Python Podcast, I learned about the reportlab package, which can be used to create .pdfs, and figured that a .pdf would be an ideal document type for this.

Then, I heard episode 13 of The Real Python Podcast, which introduced me to PySimpleGUI, which I thought could be a nice way to enter and save ride data. So, I created a GUI that allows me to enter ride info, and upon clicking 'Submit', generates a new report.

## Examples
<p align='center'>
    <img width=600 height=779 src='https://github.com/dcribb19/trek_century_challenge/blob/master/examples/report.png'>
</p>

### What is Zwift?
You may have noticed in the bar chart that most of my rides have taken place on Zwift. Zwift is a massively mutltiplayer online platform for cycling and running. It has many different virtual worlds with routes of varied terrain, and during the current times of COVID-19, offers safe, social group rides with people from all over the world. Best yet, there's absolutely no car traffic, and there aren't any stoplights.  

Zwift even hosted the Official Virtual Tour de France 2020!

<p align='center'>
    <img src=https://github.com/dcribb19/trek_century_challenge/blob/master/examples/zwift_ex.jpg width=400 height=221> <img src=https://github.com/dcribb19/trek_century_challenge/blob/master/examples/zwift_ex3.jpg width=400 height=221>
</p>

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
1. GUI will display.  
<p align='center'>
    <img width=400 height=147 src='https://github.com/dcribb19/trek_century_challenge/blob/master/examples/gui.png'>
</p>

2. ... button will bring up calendar in order to select date.  
<p align='center'>
    <img width=400 height=172 src='https://github.com/dcribb19/trek_century_challenge/blob/master/examples/calendar.gif'>
</p>  

3. Enter miles  
4. Select location
5. Submit 
#### Output (All files saved with _month_day.extension)  
    - Bar chart saved as .jpg to graphs directory
    - Line graph saved as .jpg to graphs directory
    - Report .pdf saved to reports directory

## Credits  
- [The Real Python Podcast - Episode 13](https://realpython.com/podcasts/rpp/13/)  
- [The Real Python Podcast - Episode 17](https://realpython.com/podcasts/rpp/17/)  

## License
[![License](https://img.shields.io/badge/License-BSD%202--Clause-orange.svg)](https://opensource.org/licenses/BSD-2-Clause)