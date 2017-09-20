# from django.template.loader import get_template
# from django.template import Context
from django.shortcuts import render
from django.http import HttpResponse, Http404
import datetime


def hello(request):
    return HttpResponse("Hello world!")


def current_datetime(request):
    now = datetime.datetime.now()
    # t = get_template('current_datetime.html')
    # html = t.render(Context({'current_date': now}))
    # return HttpResponse(html)
    return render(request, 'current_datetime.html', {'current_date': now})


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    now = datetime.datetime.now()
    dt = now + datetime.timedelta(hours=offset)
    # html = "In %s hour(s), it will be %s ." % (offset, dt)
    # return HttpResponse(html)
    return render(request, 'hours_ahead.html', {'hour_offset': offset,'next_time': dt})
