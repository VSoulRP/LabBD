from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from matplotlib.backends.backend_agg import FigureCanvasAgg
from .forms import CountryForm, DayForm
from .models import CountryWiseLatest, DayWise

import pandas as pnd
import io
import matplotlib.pyplot as plt

strSQL = pk = ''
start_end = [None] * 2
manager = None
qs = None


# Create your views here.
def home(request):
    return render(request, 'app1/home.html')


def pais(request):
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            start = int(request.POST.get('start')) if request.POST.get('start') != '' else None
            end = int(request.POST.get('end')) if request.POST.get('end') != '' else None
            print(form.cleaned_data['ColumnMenu'])
            get_SQL(table='cw', column=form.cleaned_data['ColumnMenu'], order=form.cleaned_data['OrderMenu'],
                    start=start, end=end, selection=form.cleaned_data['OrderSelection'])
            return HttpResponseRedirect('/pais/')
    else:
        form = CountryForm()
    return render(request, 'app1/pais.html', {'title': 'Pais', 'form': form})


def dia(request):
    if request.method == 'POST':
        form = DayForm(request.POST)
        if form.is_valid():
            start = int(request.POST.get('start')) if request.POST.get('start') != '' else None
            end = int(request.POST.get('end')) if request.POST.get('end') != '' else None
            print(form.cleaned_data['ColumnMenu'])
            get_SQL(table='dw', column=form.cleaned_data['ColumnMenu'], order=form.cleaned_data['OrderMenu'],
                    start=start, end=end, selection=form.cleaned_data['OrderSelection'])
            return HttpResponseRedirect('/dia/')
    else:
        form = DayForm()
    return render(request, 'app1/dia.html', {'title': 'Dia', 'form': form})


def plot(request):
    if manager is not None:
        df = pnd.DataFrame(qs)
        df.plot(kind='bar', x=pk)
        plt.tick_params(axis='x', labelsize=8)
        plt.tight_layout()
    f = plt.figure(1)
    buf = io.BytesIO()
    canvas = FigureCanvasAgg(f)
    canvas.print_png(buf)
    response = HttpResponse(buf.getvalue(), content_type='image/png')
    plt.close(f)
    response['Content-Length'] = str(len(response.content))
    return response


def get_SQL(**kwargs):
    global manager, pk, qs
    if 'table' in kwargs:
        if kwargs.get('table') == 'cw':
            manager = CountryWiseLatest
            pk = 'country_region'
        elif kwargs.get('table') == 'dw':
            manager = DayWise
            pk = 'date'
        if 'column' in kwargs:
            column = kwargs.get('column')
            start = kwargs.get('start')
            end = kwargs.get('end')
            order = kwargs.get('order')
            if order == '':
                qs = manager.objects.values(pk, column)[slice(start, end)]
            else:
                if order == '-':
                    order = '-'
                else:
                    order = ''
                if kwargs.get('selection') == 'pk':
                    order = order+pk
                elif kwargs.get('selection') == 'column':
                    order = order+column
                qs = manager.objects.values(pk, column).order_by(order)[slice(start, end)]