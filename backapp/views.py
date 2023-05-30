from django.shortcuts import render, redirect
from backapp.models import catagorydb, productdb
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.

def induspage(request):
    return render(request, "induspage.html")


def addcategory(request):
    return render(request, "add_category.html")


def savecategory(request):
    if request.method == "POST":
        cname = request.POST.get('categoryname')
        des = request.POST.get('description')
        img = request.FILES['image']
        obj = catagorydb(Catagoryname=cname, Description=des, Image=img)
        obj.save()
        return redirect(addcategory)


def displaycategory(request):
    data = catagorydb.objects.all
    return render(request, "displaycategory.html", {'data': data})


def editcategory(request, dataid):
    data = catagorydb.objects.get(id=dataid)
    return render(request, "editcategory.html", {"data": data})


def updatecategory(request, dataid):
    if request.method == "POST":
        cat = request.POST.get('category')
        des = request.POST.get('description')

        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = catagorydb.objects.get(id=dataid).Image

        catagorydb.objects.filter(id=dataid).update(Catagoryname=cat, Description=des, Image=file)
        return redirect(displaycategory)


def deletecategory(req, dataid):
    data = catagorydb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycategory)


def addproduct(request):
    data =catagorydb.objects.all()
    return render(request, "addproduct.html",{"data":data})


def saveproduct(request):
    if request.method == "POST":
        cn = request.POST.get('category')
        pn = request.POST.get('productname')
        qu = request.POST.get('quantity')
        des = request.POST.get('description')
        pr = request.POST.get('price')
        img = request.FILES['image']
        obj = productdb(Category_name=cn, Productname=pn, Quantity=qu, Descriptions=des, Price=pr, Images=img)
        obj.save()
        messages.success(request,"Product saved succesfully")
        return redirect(addproduct)


def displayproduct(request):
    data = productdb.objects.all
    return render(request, "displayproduct.html", {"data": data})

def editproduct(request,dataid):
    data=productdb.objects.get(id=dataid)
    return render(request,"editproduct.html",{"data":data})


def updateproduct(request,dataid):
    if request.method == "POST":
        cn = request.POST.get('category')
        pn = request.POST.get('productname')
        qu = request.POST.get('quantity')
        des = request.POST.get('description')
        pr = request.POST.get('price')

        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = productdb.objects.get(id=dataid).Images

        productdb.objects.filter(id=dataid).update(Category_name=cn, Productname=pn, Quantity=qu, Descriptions=des,Price=pr, Images=file)
        return redirect(displayproduct)

def deleteproduct(req,dataid):
    data=productdb.objects.filter(id=dataid)
    data.delete()
    messages.error(req,"Data deleted")
    return redirect(displayproduct)

def loginpage(request):
    return render(request,"userloginpage.html")

def admin_login(request):
    if request.method=="POST":
        username_r =request.POST.get('username')
        password_r= request.POST.get('password')
        if User.objects.filter(username__contains=username_r).exists():
            user = authenticate(username=username_r,password=password_r)
            if user is not None:
                login(request,user)
                request.session['username']=username_r
                request.session['password']=password_r
                return redirect(induspage)
            else:
                return redirect(loginpage)
        else:
            return redirect(loginpage)

def Logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(loginpage)