# Create your views here.
from django.shortcuts import render_to_response
import random

def index(request):
    return render_to_response('hfjs_home.html')

def donuts_result(request):
    return render_to_response('donuts/donuts_result.html', {
        'order_num': random.randint(1000, 10000),
        'customer_name': request.POST.get('name', ''),
        'ready_in_mins': request.POST.get('pickupminutes', ''),
        'total_price': request.POST.get('total', ''),
})

def bannerocity_result(request):
    return render_to_response('bannerocity/bannerocity_result.html', {
        'order_num': random.randint(1000, 10000),
        'message': request.POST.get('message', ''),
        'zipcode': request.POST.get('zipcode', ''),
        'date': request.POST.get('date', ''),
        'phone': request.POST.get('phone', ''),
        'email': request.POST.get('email', ''),
})
