from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.cache import never_cache

from home.forms.userEditForm import UserEditForm

@never_cache
@login_required
def profile(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu perfil ha sido actualizado exitosamente.')
            return redirect('profile')
    else:
        form = UserEditForm(instance=request.user)

    return render(request, 'home/account/profile.html', {'form': form})