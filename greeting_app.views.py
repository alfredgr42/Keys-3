from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserNameForm
from .models import UserName

def index(request):
    last_user = None
    all_users = UserName.objects.all()[:10]  # последние 10 пользователей
    
    if request.method == 'POST':
        form = UserNameForm(request.POST)
        if form.is_valid():
            # Сохраняем имя в базу данных
            user_name = form.save()
            last_user = user_name
            messages.success(request, f'✨ Привет, {user_name.name}! Рады тебя видеть! ✨')
            return redirect('index')
        else:
            messages.error(request, '⚠️ Пожалуйста, введите корректное имя!')
    else:
        form = UserNameForm()
    
    context = {
        'form': form,
        'last_user': last_user,
        'all_users': all_users,
    }
    return render(request, 'greeting_app/index.html', context)
