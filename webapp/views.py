from django.shortcuts import render,redirect
from backapp.models import catagorydb,productdb
from webapp.models import user_reg,cartdb
from django.contrib import messages


# Create your views here.
def webpage(request):
    data = catagorydb.objects.all()
    return render(request,"webpage.html",{"data":data})

def aboutpage(request):
    return render(request,"about.html")

def productpage(request):
    return render(request,"productpage.html")

def shoppage(request,catg):
    products=productdb.objects.filter(Category_name=catg)
    return render(request,"shoppage.html",{'products':products})

def singleproduct(request,dataid):
    data=productdb.objects.get(id=dataid)
    return render(request,"singleproduct.html",{'data':data})

def userloginpage(request):
    return render(request,"userloginpage.html")


def savelogin(request):
    if request.method == "POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        pas = request.POST.get('password')
        cpas = request.POST.get('cpassword')
        obj = user_reg(Name=na, Email=em, Password=pas, Cpassword=cpas)
        obj.save()
        return redirect(userloginpage)


def userlogin(request):
    if request.method == 'POST':
        username_r = request.POST.get("username")
        password_r = request.POST.get("password")
        if user_reg.objects.filter(Name=username_r, Password=password_r).exists():
            request.session['username'] = username_r
            request.session['password'] = password_r

            return redirect(webpage)
        else:
            return redirect(userloginpage)
    return redirect(userloginpage)


def userlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(userloginpage)



def savecart(request):
    if request.method=="POST":
        na = request.POST.get('Productname')
        pr=request.POST.get('Productprice')
        q=request.POST.get("Qty")
        t=request.POST.get("total_price")
        us=request.POST.get("user")
        obj=cartdb(Pname=na,Pprice=pr,PQ=q,Ptotal_price=t,User=us)
        obj.save()
        messages.success(request, "Product saved succesfully")
        return redirect(displaycart)


def displaycart(request):
    cat = cartdb.objects.filter(User=request.session['username'])
    return render(request,"Cart.html",{"cat":cat})

def checkout(request):
    return render(request,"checkout.html")







