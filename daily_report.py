# daily_report.py
# Create .pdf report using stats and graphs in july_mileage.py

import july_mileage
import os.path

from datetime import date
from PIL import Image

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader


def make_report():
    today = date.today()
    report_suffix = today.strftime('%m_%d')

    report_path = os.path.join(os.getcwd(), 'reports/')
    report = os.path.join(
        report_path, 'daily_report_' + report_suffix + '.pdf'
    )

    myCanvas = canvas.Canvas(report, pagesize=letter)
    myCanvas.setTitle('Daily Report_' + report_suffix)
    myCanvas.setAuthor('DC')
    myCanvas.setSubject('Cycling')

    stats = july_mileage.current_stats()
    stats = stats.splitlines()
    stats_y_start = 725

    myCanvas.setFont('Courier', 10)
    for line in stats:
        myCanvas.drawString(100, stats_y_start, line)
        stats_y_start -= 20

    # create graphs for today
    july_mileage.bar_stats()
    july_mileage.pace_stats()

    graph_path = os.path.join(os.getcwd(), 'graphs/')
    bar = os.path.join(graph_path, 'bar_stats_' + report_suffix + '.jpg')
    pace = os.path.join(graph_path, 'pace_stats_' + report_suffix + '.jpg')

    # 1920 x 1440 = 1.33 Aspect Ratio
    myCanvas.drawImage(bar, x=100, y=351, width=400, height=301)
    myCanvas.drawImage(pace, x=100, y=50, width=400, height=301)

    myCanvas.showPage()
    myCanvas.save()


def main():
    make_report()


if __name__ == '__main__':
    main()
