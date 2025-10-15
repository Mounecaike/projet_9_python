from django.shortcuts import render, redirect
from .forms import TicketForm

def create_ticket(request):
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('posts:create_ticket')
    else:
        form = TicketForm()
    return render(request, "posts/create_ticket.html", {"form": form})
