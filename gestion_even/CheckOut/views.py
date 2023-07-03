from django.shortcuts import render, redirect
from django.contrib import messages
from events.models import Event,Ticket,Payments
from django.utils import timezone



# Create your views here.
def Check(request,object_id):
        now = timezone.now()
        if request.user.is_authenticated:
                if request.method == 'POST':
                    eventName = request.POST.get('eventName')
                    cardNumber = request.POST['CardNumber']
                    cardMonth = request.POST['month']
                    cardYear = request.POST['year']
                    cardCVV = request.POST['CVV']
                    Holder = request.POST['Holder']
                    quantity = request.POST.get('quantity')
                    ticket_number = request.POST.get('ticket_number')
                    eventTicket = Ticket.objects.get(name = eventName)
                    eventTicket.nbr_ticket = eventTicket.nbr_ticket - int(quantity)
                    if eventTicket.nbr_ticket - int(quantity) < 0:
                        events = Event.objects.select_related('eventimage').get(status = 'completed', id = object_id)
                        messages.info(request, 'We are sold out of tickets.')
                        return render(request, 'CheckOut.html', {'event':events, 'now':now})
                    else:
                        eventTicket.save()
                        pay = Payments.objects.create(username=str(request.user),Holder=Holder,eventName=eventName,TicketNumber=ticket_number,Quantity=quantity,CardNumber=cardNumber,ExperationMonth=cardMonth,ExperationYear=cardYear,CVV=cardCVV)
                        pay.save()
                        events = Event.objects.select_related('eventimage').get(status = 'completed', id = object_id)
                        messages.info(request, 'You Just Bought Your Ticket!')
                        return render(request, 'CheckOut.html', {'event':events, 'now':now})
                else:
                    events = Event.objects.select_related('eventimage').get(status = 'completed', id = object_id)
                    return render(request, 'CheckOut.html', {'event':events, 'now':now})
        else:
            messages.info(request, 'You need to logIn before buying a ticket ')
            return redirect('useracc:login')
        
