from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import urllib
import datetime

# Create your views here.

#r = urllib.urlopen(get_url()).read()





def get_url():
    now = datetime.datetime.now()
    if now.month < 8:
        ac_year_start = now.year%100 - 1
    else:
        ac_year_start = now.year%100
    return "http://web.inf.ed.ac.uk/infweb/student-services/ito/admin/timetables/lecture-timetable-20" + str(ac_year_start) + "-" + str(ac_year_start + 1)


soup = BeautifulSoup(urllib.urlopen(get_url()).read())
times = soup.table.thead.tr.find_all("th")


'''def get_times():
    times = soup.table.thead.tr.find_all("th")
    times = times[1:]
    times_list = []
    for time in times:
        start_time = time.text[0:4]
        end_time = time.text[-4:]
        times_list.append(start_time + " - " + end_time)
'''

#def get_times():
times = soup.table.thead.tr.find_all("th")
times = times[1:]
times_list = []
for time in times:
    start_time = time.text[0:4]
    end_time = time.text[-4:]
    times_list.append(start_time + " - " + end_time)



#times_list = times_list

def post_list(request):
    #list = ['a', 'b', 'c']
    return render(request,
    'timetable/index.html',
    {'times':times_list}
    )
