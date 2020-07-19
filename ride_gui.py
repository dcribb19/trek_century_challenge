# ride_gui.py
'''
Create a GUI with PySimpleGUI to write information about a single ride to csv.
'''
import csv
import PySimpleGUI as sg


def show_gui():
    '''
    Display GUI to enter ride info.
    '''
    sg.theme('Reddit')

    layout = [
        [sg.Text('Date'), sg.Input(key='Date'),
         sg.CalendarButton('...', format='%Y-%m-%d')],
        [sg.Text('Miles'), sg.Input(key='Miles')],
        [sg.Radio('Outside', 'Radio1', key='Outside'),
         sg.Radio('Zwift', 'Radio1', default=True, key='Zwift')],
        [sg.Button('Submit'), sg.Button('Cancel')]
    ]

    window = sg.Window('Enter Ride Data', layout, font=('Arial 10'))

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break
        elif event == 'Submit':
            date = values['Date']
            miles = values['Miles']
            location = ''
            if values['Outside']:
                location = 'outside'
            else:
                location = 'zwift'

            with open('rides.csv', 'a', newline='') as csvfile:
                ride_writer = csv.writer(csvfile, delimiter=',')
                ride_writer.writerow([date, miles, location])
            break
    window.close()
