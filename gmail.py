# gmail.py
'''
Create a function that can be used with Windows Task
Scheduler in order to email daily_report.pdf nightly until
the challenge is over.
'''

from datetime import date
import ezgmail
import os

ATTACHMENT_PATH = os.path.join(os.getcwd(), 'reports/')


def send_email():
    '''
    Email daily_report.pdf daily until challenge is over.
    '''
    today = date.today().strftime('%b %d')
    report_suffix = date.today().strftime('%m_%d')

    ezgmail.send('daniel.cribb.10@gmail.com',
                 f'TCC Daily Report {today}',
                 'Here\'s your report for today, boss.',
                 f'{ATTACHMENT_PATH}daily_report_{report_suffix}.pdf',
                 cc='daniel.cribb.10@cnu.edu')


def main():
    send_email()


if __name__ == '__main__':
    main()
