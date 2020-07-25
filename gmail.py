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

    ezgmail.send('ENTER EMAIL ADDRESS HERE',
                 'TCC Daily Report ' + today,
                 'Here\'s your report for today, boss.',
                 ATTACHMENT_PATH + 'daily_report_' + report_suffix + '.pdf',
                 cc='CC FRIENDS HERE')


def main():
    send_email()


if __name__ == '__main__':
    main()
