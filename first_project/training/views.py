from django.shortcuts import render
import math
from .models import register
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("hello world")

def Forms(request):
    
    form = """
    
    <form  onsubmit = "event.preventDefault(); " action = "" method = "POST" >
    
    <input type = "text" name = "number1" name = "contact " placeholder = "enter the number "/>
    <input type = "text" name = "number2" placeholder = "enter the number "/>
    
    <button type="add" value="add">add</button>
    <button type="submit" value="-">Submit</button>
    <button type="submit" value="*">Submit</button>
    <button type="submit" value="/">Submit</button>
    
    
    </form>
     <a href = "/calculator"> another page</a>
    """
    return HttpResponse(f'<html><body>{form}</body></html>')
# def index(request):
#     return HttpResponse("hello world")
def calcul(request):
    return HttpResponse("new page")

def Add(num1,num2):
    result = int(num1)+ int(num2)
    return result 
def Subtract(num1,num2):
    result = int(num1)- int(num2)
    return result 

def Multiply(num1,num2):
    result = int(num1)* int(num2)
    return result 

def Divide(num1,num2):
    result = int(num1)//int(num2)
    return result 
            

def calci(request):
    form = """
    <form action = "" method = "POST" >
    <input type = "number" name = "num1" name = "contact " placeholder = "enter the number "/>
    <input type = "number" name = "num2" name = "contact " placeholder = "enter the number "/>
   
    <button name ="add">"+"</button>
    <button name ="Subtract">"-"</button>
    <button name ="Multiply">"*"</button>
    <button name = "Divide">"/"</button>
    
    
    
    </form>
    """
    result = " "
    print(request.method)
  
    if request.method == 'POST':
        val1 = int(request.POST.get('num1'))
        val2 = int(request.POST.get('num2'))
        if "add" in request.POST:
            result = Add(val1,val2)
        elif "Subtract" in request.POST:
            result = Subtract(val1,val2)
        elif "Multiply" in request.POST:
            result = Multiply(val1,val2)
        elif "Divide" in request.POST:
            result= Divide(val1,val2)
    
    return HttpResponse(f'<html><body>{form}<h2> result:{result}</h1></body></html>')

    
    
