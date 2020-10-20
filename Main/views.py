from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, HttpResponse
from Main.models import CS_Consumption, CS_All_Info, Canteen
from Main.models import AllMealsCopy2 as MealsAver
from datetime import datetime
import pandas as pd
import numpy as np


def main_page(request):
    info = canteen.order_by('rank').values(
        'canteen_name', 'breakfast_amount', 'lunch_amount', 'dinner_amount', 'all_amount', 'rank')
    if not list(info):
        var = None
        return render(request, 'Main/templates/human_traffic.html',
                      {'var': var, 'msg': '暂无消费记录'})
    else:
        df = pd.DataFrame(list(info))
        df['breakfast_amount'] = abs(df['breakfast_amount'] / 100.00)
        df['lunch_amount'] = abs(df['lunch_amount'] / 100.00)
        df['dinner_amount'] = abs(df['dinner_amount'] / 100.00)
        df['all_amount'] = abs(df['all_amount'] / 100.00)
        nd = np.array(df)
        var = nd.tolist()
        return render(request, 'human_traffic.html',
                      {'var': var, 'msg': '排行如下'})
    return render(request, 'human_traffic.html')


def canteen_principal(request):
    return render(request, 'canteen_principal.html', )


consumption = CS_Consumption.objects
allinfo=CS_All_Info.objects
mealsaver = MealsAver.objects
canteen = Canteen.objects
date_min = consumption.order_by('effectdate').values()[0]['effectdate']
date_max = consumption.order_by('-effectdate').values()[0]['effectdate']
snos = [i[0] for i in allinfo.values_list('user_sno')]


def consumption_data(request):
    if request.method == 'GET':
        return render(request, "consumption_data.html", {'date_min': date_min, 'date_max': date_max,'msg':'请选择起止日期并输入学生学号'})
    else:
        begin = request.POST.get('date1', '')
        end = request.POST.get('date2', '')
        sno = request.POST.get('sno', '')
        if begin == '' and end == '':
            return render(request, '../templates/consumption_data.html',
                          {'date_min': date_min, 'date_max': date_max, 'msg': '请选择起止日期范围'})
        if begin == '':
            return render(request, '../templates/consumption_data.html',
                          {'date_min': date_min, 'date_max': date_max,'msg': '请选择起始日期'})
        if begin != '' and end == '':
            return render(request, '../templates/consumption_data.html',
                          {'date_min': date_min, 'date_max': date_max, 'msg': '请选择结束日期'})
        begin_date = datetime.strptime(begin, '%Y-%m-%d').date()
        if begin_date < date_min or begin_date > date_max:
            return render(request, '../templates/consumption_data.html',
                          {'date_min': date_min, 'date_max': date_max, 'msg': '请选择合理的起始日期'})
        end_date = datetime.strptime(end, '%Y-%m-%d').date()
        if date_min > end_date or date_max < end_date:
            return render(request, '../templates/consumption_data.html',
                          {'date_min': date_min, 'date_max': date_max, 'msg': '请选择合理的终止日期'})
        if begin_date > end_date:
            return render(request, '../templates/consumption_data.html', {'date_min': date_min, 'date_max': date_max, 'msg': '请选择合理的日期范围'})
        if sno == '' or sno is None:
            return render(request, '../templates/consumption_data.html',
                          {'date_min': date_min, 'date_max': date_max, 'msg2': '请输入学号'})
        elif sno not in snos:
            return render(request, '../templates/consumption_data.html', {'date_min': date_min, 'date_max': date_max, 'msg2': '请输入16-19级计科院学生的学号'})
        else:
            transaction = consumption.filter(effectdate__range=(begin_date, end_date), sno=sno).order_by('effectdate','exact_time').values('sno','balance','effectdate','poscode','toaccount','tranamt','exact_time')
            if not list(transaction):
                var = None
                return render(request, '../templates/consumption_data.html',
                              {'date_min': date_min, 'date_max': date_max, 'var': var,'msg':'这段期间该同学暂无消费记录'})
            else:
                df = pd.DataFrame(list(transaction))
                df['balance'] = df['balance']/100.00
                df['tranamt'] = abs(df['tranamt']/100.00)
                nd = np.array(df)
                var = nd.tolist()
            return render(request, '../templates/consumption_data.html', {'date_min': date_min, 'date_max': date_max, 'var': var, 'msg':'消费记录如下'})


def meals_average(request):
    if request.method == 'GET':
        return render(request, "meals_aver.html",)
    else:
        xn = request.POST.get('xn','')
        xq = request.POST.get('xq','')
        sno = request.POST.get('sno', '')
        if sno == '' or sno is None:
            info = mealsaver.filter(year=xn, term=xq).values(
                'sno', 'year', 'term', 'breakfast_aver', 'lunch_aver', 'dinner_aver')
            if not list(info):
                var = None
                return render(request, 'meals_aver.html',
                              {'var': var, 'msg': '这段期间暂无消费记录'})
            else:
                df = pd.DataFrame(list(info))
                df['breakfast_aver'] = abs(df['breakfast_aver'] / 100.00)
                df['lunch_aver'] = abs(df['lunch_aver'] / 100.00)
                df['dinner_aver'] = abs(df['dinner_aver'] / 100.00)
                nd = np.array(df)
                var = nd.tolist()
                return render(request, 'meals_aver.html',
                              {'var': var, 'msg': '消费记录如下'})
            return render(request, 'meals_aver.html',)
        else:

            info = mealsaver.filter(year=xn, term=xq, sno=sno).values(
                    'sno', 'year', 'term', 'breakfast_aver', 'lunch_aver', 'dinner_aver')
            if not list(info):
                var = None
                return render(request, 'meals_aver.html',
                              {'var':var,'msg': '这段期间该同学暂无消费记录'})
            else:
                df = pd.DataFrame(list(info))
                df['breakfast_aver'] = abs(df['breakfast_aver'] / 100.00)
                df['lunch_aver'] = abs(df['lunch_aver'] / 100.00)
                df['dinner_aver'] = abs(df['dinner_aver'] / 100.00)
                nd = np.array(df)
                var = nd.tolist()
                return render(request, 'meals_aver.html',
                              {'var': var, 'msg': '消费记录如下'})

    return render(request, 'meals_aver.html')

def foodie_resturant(request):
    return  render(request, 'foodie/templates/templates/foodie.html')




