from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignupForm,AddRecordForm
from .models import Record



# Home Page View
def home(request):
    records = Record.objects.all()
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
        return render(request,'website/home.html',{'records':records})
                


# LogOut View
def logout_user(request):
    logout(request)
    messages.success(request,'You Have Been Logged Out.')
    return redirect('home')
    

# Register New users
def register_user(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,'You Have Been Register Successfully.')
            return redirect('home')
    else:
        form = SignupForm()
        return render(request,'website/register.html',{'form':form})
    
    return render(request,'website/register.html',{'form':form})
    
    
# Record Detail
def record_detail(request,pk):
    if request.user.is_authenticated:
        record = get_object_or_404(Record,id=pk)
        return render(request,'website/record.html',{'record':record})
    else:
        messages.success(request,'You Must Be Logged In To View Records.')
        return redirect('home')
        
    

# Record Delete
def delete_record(request,pk):
    if request.user.is_authenticated:
        record = get_object_or_404(Record,id=pk)
        record.delete()
        messages.success(request,'You Record Has Been Deleted Successfully.')
        return redirect('home')
    else:
        messages.success(request,'You Can Not Delete Record Untill You Logged In.')
        return redirect('home')
    
    
# Add New Record
def add_new_record(request):
    if request.method == 'POST':
        form = AddRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'New Record Has Been Created Successfully.')
            return redirect('home')
        else:
            form.errors()
    else:
        form = AddRecordForm()
        return render(request,'website/add_record.html',{'form':form})
    
    return render(request,'website/add_record.html',{'form':form})



# Update Record
def update_record(request,pk):
    if request.user.is_authenticated:
        current_record = get_object_or_404(Record,id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Record Has Been Updated!")
            return redirect('home')
        
        return render(request, 'website/update_record.html', {'form':form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('home')
    