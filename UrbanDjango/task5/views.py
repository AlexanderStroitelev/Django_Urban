from django.shortcuts import render
from .forms import UserRegister


users = ["user1", "user2", "user3"]

def sign_up_by_django(request):
    info = {}
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            print ("Параметры регистрации нового пользователя:")
            print (f"Username: {username}")
            print (f"Password: {password}")
            print (f"Repeat Password: {repeat_password}")
            print (f"Age: {age}")

            if username in users:
                info['error'] = 'Пользователь уже существует'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            else:
                info['message'] = f'Приветствуем, {username}!'
                users.append(username)

            print ("Updated list of registered users:" , users)

        info['form'] = form
    else:
        info['form'] = UserRegister()
    return render(request, 'fifth_task/registration_page.html', info)


def sign_up_by_html(request):
    info = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        print ("Параметры регистрации нового пользователя:")
        print (f"Username: {username}")
        print (f"Password: {password}")
        print (f"Repeat Password: {repeat_password}")
        print (f"Age: {age}")

        if username in users:
            info['error'] = 'Пользователь уже существует'
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        else:
            info['message'] = f'Приветствуем, {username}!'
            users.append(username)

        print ("Updated list of registered users:" , users)

    return render(request, 'fifth_task/registration_page.html', info)
