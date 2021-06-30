
from django.db.models.fields import DecimalField
from django.forms.forms import Form
from django.http.response import HttpResponse
from fishfarm.models import *
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

from .forms import *
from django.shortcuts import redirect, render
from django.contrib import messages 
from django.contrib.auth.models import User 
from django.contrib.auth  import authenticate,  login, logout


# Create your views here.
def index(request):
    p = Product.objects.all()
    add = Address.objects.all()

    return render(request,'index.html',{'product':p,'ad':add})

def signin(request):
    if request.method=="POST":
        # Get the post parameters

        loginusername=request.POST['Username']
        loginpassword=request.POST['password']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            
            messages.success(request, "Successfully Logged In")
            return redirect("index")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("signin")
    return render(request,'signin.html',)

def signup(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['Username']
        email=request.POST['Email']
        fname=request.POST['Fname']
        lname=request.POST['Lname']
        pass1=request.POST['Password']
        pass2=request.POST['Confirm Password']

        # check for errorneous input
        if (pass1!= pass2):
            messages.error(request, " Passwords do not match")
            return redirect('signup')
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your Fish Farm account has been successfully created")
        return redirect('signin')
    

    return render(request,'sign up.html')

def about(request):
    add = Address.objects.all()
    dataset = About_us.objects.all()
    datset = About_Info.objects.all()
    return render(request,'about.html',{'about':dataset,'info':datset,'ad':add})

def contact(request):
    add = Address.objects.all()
    if request.method == "POST":  
        name= request.POST['Name']
        no= request.POST['Mobile']
        email = request.POST['Email']
        mssg = request.POST['Message']
        print(name,no,email,mssg)
        ins=Feedback(name=name,Mobile=no,Feedback=mssg,Email=email)
        ins.save()
    return render(request,'contact.html',{'ad':add})



    dataset = log_in.objects.all()
    return render(request,'index.html',{'dat':dataset})

def feedback(request):
    dataset = Feedback.objects.all()
    return render(request,'feedback.html',{'feed':dataset})

def sell(request):
    dataset = OrdereProduct.objects.all()
    return render(request,'sell.html',{'sell':dataset})

def order(request):
    dataset = Req_info.objects.all()
    return render(request,'orders.html',{'order':dataset})


def edit(request , pk):
    form1 = log_in.objects.get(id=pk)
    print(form1)
    form = edit_form(instance=form1)

    if request.method == 'POST':
        form = edit_form(request.POST ,instance=form1)
    if form.is_valid:
        form.save()
    else:
        form.errors
    return render(request,'edit.html',{'form1':form1}) 



def delete(request, pk):
    form= Feedback.objects.get(pk=pk)
    
    form.delete()
    return redirect('/components/') 

def Logouts(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('index')

#add to cart_view
@login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("index")


@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_detail(request):
    return render(request, 'cart.html')


#....buy view
def store(request):
    total=0.00
    cart = Cart(request)
    
    ab=request.session['cart']
    print(ab)
    for key,value in ab.items():
        print(value['name'])
        total = float( float(value['price'])* float(value['quantity'])) + float(total)

    print(total) 

    print(request.user)
    instant=Req_info(Name_Costomer=request.user,GrandTotal=total)
    instant.save()

    print(value['userid'])
    max_val=Req_info.objects.latest('id')
   # print(max_val)
    for key,value in ab.items():
        print(value['name'])
        
        
        OrdereProduct.objects.create(order=max_val,  CustomerID=value['userid'], Name_Costomer=request.user,  name=value['name'], quantity=value['quantity'], price=value['price'])
    
    cart.clear()
    

    return render(request, 'index.html', {'cart': cart})

