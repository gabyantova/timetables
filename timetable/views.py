from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import urllib
import datetime

# Create your views here.

#r = urllib.urlopen(get_url()).read()

#contents[1].find_all("td").find_all("p")



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

times = soup.table.thead.tr.find_all("th")
times = times[1:]
times_list = []
for time in times:
    start_time = time.text[0:4]
    end_time = time.text[-4:]
    times_list.append(start_time + " - " + end_time)


contents = soup.table.tbody.find_all("tr")

dict1 = {}

#remove day of week tag
for content in contents:
    row_items = content.find_all("td")
    first = True
    day_of_the_week = ""
    counter = 0
    for row_item in row_items:
        if first:
            dict1[row_item.text] = []
            day_of_the_week = row_item.text
            first = False
        else:
            courses_that_hour = row_item.find_all("strong")
            type(courses_that_hour)
            acronymns_of_courses_that_hour = []
            print counter
            for course_that_hour in courses_that_hour:
                course_acr = course_that_hour.text
                acronymns_of_courses_that_hour.append(course_acr)
            dict1[day_of_the_week].append(acronymns_of_courses_that_hour)
        print counter
        counter = counter+1

print dict1


dict_mon = dict1["Mon"][0]





def post_list(request):
    #list = ['a', 'b', 'c']
    return render(request,
    'timetable/index.html',
    {'times':times_list},
    {'dict_monday':dict1})
