from django.shortcuts import render,redirect
from .models import Book
from django.utils import timezone
from django.contrib import messages
# Create your views here.
def delete(request,bpk):
    b = Book.objects.get(id=bpk)
    if  b.user ==  request.user:
        b.delete()
    else:
        messages.error(request,"삭제권한이 없습니다. :(")
    return redirect("book:index")

def create(request):
    if request.method == "POST":
        im = request.POST.get("impo")
        sn = request.POST.get("sname")
        su = request.POST.get("surl")
        sc = request.POST.get("scon")
        if sn and su and sc:
            if im:
                imp = True
            else:
                imp = False
            Book(site_name=sn,site_url=su,content=sc,user=request.user,impo=imp,pubdate=timezone.now()).save()
            return redirect("book:index")
    return render(request,"book/create.html")

def index(request):
    b = request.user.book_set.all().order_by("-pubdate")
    context = {
        "blist":b
    }
    return render(request,"book/index.html",context)