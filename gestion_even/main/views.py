from django.shortcuts import render,redirect
from events.models import Event,Payments
from main.models import Cart
from django.db.models import Sum
from django.http import JsonResponse
from datetime import datetime
from django.utils.html import strip_tags
from django import template
from django.core.mail import send_mail
from django.conf import settings



# Create your views here.
def index(request,message=None):
    events = Event.objects.select_related('eventimage').filter(status='active')    
    event = Event.objects.all()
    Topevents = Payments.objects.values('eventName').annotate(total_quantity=Sum('Quantity')).order_by('-total_quantity')[:4]
    return render(request, 'index.html', {'events' : events,'Topevents':Topevents, 'event':event,'message':message})


def UserCart(request):
    if request.user.is_authenticated:
        attendent = request.user
        #order, created =  Order.objects.get_or_create(EventAttendet=attendent, complete=False)
        items = Cart.objects.filter(Event_Attendet=attendent, complete=False)
        total = 0
        count = items.count()
        for item in items:
            total += item.price * item.quantity
        return render(request, 'Cart.html',{'items':items,'total':total,'count':count})
    else:
        items = []
        order = {'get_cart_items':0, 'get_cart_total':0}
    return render(request, 'Cart.html'#,{'items':items, 'order':order}
                  )


def CartCheckout(request):
    if request.user.is_authenticated:
        attendent = request.user
        #order, created =  Order.objects.get_or_create(EventAttendet=attendent, complete=False)
        #items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_items':0, 'get_cart_total':0}
    return render(request, 'CartCheckout.html' #,{'items':items, 'order':order}
                  )


def searchEvents(request):
    categories = Event.objects.values_list('category_id', flat=True).distinct()
    eventss = Event.objects.select_related('eventimage').filter(status='active')    
    if request.method == 'GET':
        query = request.GET.get('query')
        category = request.GET.get('category')
        if category and query:
            cat = int(category)
            event = eventss.filter(category_id=cat)
            events = event.filter(name__icontains = query)
            return render(request, 'search.html', {'events': events})
        elif query:
            events = event.filter(name__icontains = query)
            return render(request, 'search.html', {'events': events})
        elif category:
            cat = int(category)
            events = eventss.filter(category_id=cat)
            return render(request, 'search.html', {'events': events})
        else:
            return render(request, 'index.html', {'events' : eventss})        
    else:
        return render(request, 'index.html', {'events' : eventss})


def add_to_cart(request):
    if request.method == 'POST' and request.is_ajax():
        event_id = request.POST.get('event_id')
        ClickedEvent = Event.objects.get(id=event_id)
        payment = Cart.objects.create(eventName=ClickedEvent.name, price=ClickedEvent.price, quantity=1,start_Date=ClickedEvent.start_date,Event_Attendet=str(request.user))
        payment.save()
        return JsonResponse({'message': 'Event added to cart successfully.'})
    else:
        return JsonResponse({'error': 'Invalid request.'})


def checkAll(request):
    if request.method == 'POST' and request.is_ajax():
        event_Attendent = request.POST.get('event_id')
        cardNumber = request.POST.get('cardNumber')
        month = request.POST.get('month')
        year = request.POST.get('year')
        cvv = request.POST.get('cvv')
        cardholderName = request.POST.get('cardholderName')
        
        items = Cart.objects.filter(Event_Attendet=event_Attendent, complete=False)

        current_date_time = datetime.now().strftime('%Y%m%d%H%M%S')
        for i,item in enumerate(items):
            Payment = Payments.objects.create(
                username = event_Attendent,
                Holder = cardholderName,
                eventName = item.eventName,
                TicketNumber = str(int(current_date_time)+i),
                Quantity = 1,
                CardNumber = cardNumber,
                ExperationMonth = month,
                ExperationYear = year,
                CVV = cvv
            )
            Payment.save()
            item.complete = True
            item.save()
        
        
        
        return JsonResponse({'message': 'Event added to cart successfully.'})
    else:
        return JsonResponse({'error': 'Invalid request.'})
    

def rmoveitem(request):
    if request.method == 'POST' and request.is_ajax():
        event_name = request.POST.get('eventName')
        print(event_name)      
        #item = Cart.objects.filter(eventName=event_name).first()
        Cart.objects.filter(pk__in=Cart.objects.filter(eventName=event_name).values_list('pk', flat=True)[1:]).delete()
        # item = Cart.objects.filter(eventName=event_name)[:1]
        #print(item)
        # item.delete()
        
        # Return a JSON response indicating success
        return JsonResponse({'message': 'Item removed successfully.'})
    
    # Return a JSON response indicating failure
    return JsonResponse({'message': 'Invalid request.'}, status=400)




def feedback(request):
    if request.method == 'POST':
        feedback = request.POST.get('feedback')
        user = request.user
        # If the user is logged in and has an email address
        if user.is_authenticated and user.email:
            sender_email = user.email
            # print(sender_email)
        else:
            message = "You Should logged First !"
            # return render(request, 'search.html', {'message': message})
            return index(request, message = message)
            
        send_mail(
            'Feedback received 2',
            feedback,
            settings.EMAIL_HOST_USER,
            [sender_email],  # Replace with recipient email address(es)
            fail_silently=False,
        )
        messager = "your message sent successfully !"
        return render(request, 'index.html', {'message': messager})

    return render(request, 'index.html')  # Render the feedback form template
