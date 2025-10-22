from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.contrib import messages
from accounts.models import User
from follows.models import UserFollows


@login_required
def list_follows(request):
    follows = UserFollows.objects.filter(user=request.user)

    if request.method == "POST":
        username = request.POST.get("username")
        try:
            followed_user = User.objects.get(username=username)
            if followed_user != request.user and not UserFollows.objects.filter(user=request.user, followed_user=followed_user).exists():
                UserFollows.objects.create(user=request.user, followed_user=followed_user)
                messages.success(request, f"✅ Vous suivez maintenant {followed_user.username} !")
            else: messages.warning(request, "Vous ne pouvez pas vous suivre vous même")
        except User.DoesNotExist:
            messages.error(request,  f"❌ L'utilisateur « {username} » n'existe pas.")

    return render(request, "follows/list_follows.html", {"follows": follows})

@login_required
@require_POST
def delete_follow(request, pk):
    follow = get_object_or_404(UserFollows, pk=pk)
    if follow.user == request.user:
        follow.delete()
        messages.info(request, f"👋 Vous ne suivez plus {follow.followed_user.username}.")
    return redirect('follows:list_follows')