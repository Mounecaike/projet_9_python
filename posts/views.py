from itertools import chain
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404

from follows.models import UserFollows
from .forms import TicketForm, ReviewForm
from .models import Ticket, Review

def create_ticket(request):
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            messages.success(request, "Votre ticket a bien été créé !")
            return redirect('posts:create_ticket')
    else:
        form = TicketForm()
    return render(request, "posts/create_ticket.html", {"form": form})


@login_required
def update_ticket(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if ticket.user != request.user:
        return redirect('posts:create_ticket')

    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            form.save()
            messages.success(request, "Votre ticket a bien été modifié.")
            return redirect('posts:create_ticket')  # temporaire, le feed viendra plus tard
    else:
        form = TicketForm(instance=ticket)

    return render(request, "posts/update_ticket.html", {"form": form, "ticket": ticket})

@login_required
@require_POST
def delete_ticket(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if ticket.user == request.user:
        ticket.delete()
        messages.success(request, "Votre ticket a bien été supprimé")
    return redirect("posts:create_ticket")

@login_required
def create_review(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            review.save()
            messages.success(request, "Critique publiée avec succès.")
            return redirect('posts:feed')
    else:
        form = ReviewForm()

    return render(request, "posts/create_review.html", {"form": form, "ticket": ticket})

@login_required
def update_review(request, pk):
    review = get_object_or_404(Review, pk=pk)

    if review.user != request.user:
        return redirect('posts:create_ticket')

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('posts:feed')
    else:
        form = ReviewForm(instance=review)

    return render(request, "posts/update_review.html", {
        "form": form,
        "review": review,
        "ticket": review.ticket
    })

@login_required
@require_POST
def delete_review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if review.user == request.user:
        review.delete()
        messages.success(request, "Critique supprimée.")
    return redirect("posts:create_ticket")

@login_required
def feed(request):
    followed_users = UserFollows.objects.filter(user=request.user).values_list("followed_user", flat=True)

    tickets = Ticket.objects.filter(user__in=list(followed_users) + [request.user])
    reviews = Review.objects.filter(user__in=list(followed_users) + [request.user])

    posts = sorted(
        chain(tickets, reviews),
        key=lambda post: post.time_created,
        reverse=True
    )

    return render(request, "posts/feed.html", {"posts": posts})

@login_required
def create_review_from_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect("posts:feed")
    else:
        form = ReviewForm()

    return render(request, "posts/create_review_from_ticket.html", {
        "form": form,
        "ticket": ticket
    })
