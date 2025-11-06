from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.
def sample(request):
    return HttpResponse("hello world welcome to django" )
def demo(reqest):
    data={
        'name':['sharanya','harish','shanu'],
        'age':[13,21,6],
        'city':['hyderabad','warangal','warangal'],

    }
    return JsonResponse(data)
def student_info(request):
    info={
        'student1':[{'id':123,'name':'sharanya','course':'python','batch':'53r'}],
        'student2':[{'id':124,'name':'harish','course':'java','batch':'70r'}],
        'student3':[{'id':125,'name':'aishu','course':'fullstack','batch':'85r'}]
                    
        }
    return JsonResponse(info)
# addition
def add(request):
    num1=request.GET.get('num1',10)
    num2=request.GET.get('num2',20)
    num1=int(num1)
    num2=int(num2)
    return HttpResponse(f"The addion of {num1} and {num2} is{num1+num2} ")
# subtraction
def sub(request):
    num1=request.GET.get('num1',100)
    num2=request.GET.get('num2',50)
    num1=int(num1)
    num2=int(num2)
    return HttpResponse(f"The subtraction of {num1} and {num2} is {num1-num2}")
# multiplication
def mul(request):
    num1=request.GET.get('num1',50)
    num2=request.GET.get('num2',5)
    num1=int(num1)
    num2=int(num2)
    return HttpResponse(f"The Multiplication of {num1} and {num2} is {num1*num2}")
# division
def div(request):
    num1=request.GET.get('num1',20)
    num2=request.GET.get('num2',2)
    num1=int(num1)
    num2=int(num2)
    return HttpResponse(f"The division of {num1} and {num2} is {num1/num2}")