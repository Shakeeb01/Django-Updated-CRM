from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages



# Home Page View
def home(request):
    # Login in users
    if request.method == 'POST':
        username  = request.POST['username']
        password  = request.POST['password']
        # Authenticating
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'You Have Been Logged In.')
            return redirect('home')
        else:
            messages.success(request,'There is an Error.Please Try Again')
            return redirect('home')
    else:
        return render(request,'website/home.html',{})
                





# LogOut View
def logout_user(request):
    logout(request)
    messages.success(request,'You Have Been Logged Out.')
    return redirect('home')
    
