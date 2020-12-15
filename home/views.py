from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Book,Chapter,Category,Author
from jinja2 import Template
from .form import Dangky
import os
# Create your views here.
def home_view(request):
    return render(request,'pages/home.html')

def index(request):
    return render(request,'pages/index.html')

def test1(request): #Hiển thị sách
    book = Book.objects.all()
    category = Category.objects.all()
    author = Author.objects.all()
    context = {'book':book,'cate': category,'author':author}
    return render(request,'pages/home.html',context)

def chaptest(request,id): #Hiển thị danh sách chương
    book = Book.objects.get(pk=id)
    context = {'book':book}
    return render(request,'pages/chaptest.html',context)

def ndchap(request, id): # Hiển thị nội dung chương
    chapper = Chapter.objects.get(pk=id)
    book = Book.objects.filter(chapter = chapper)
    book = book[0]
    chap = book.chapter_set.all()
    for i in range(len(chap)-1): # taọ nút next và pre
        if chap[i] == chapper and i != 0:
            next = chap[i+1].id
            pre = chap[i-1].id
            break
        if chap[i] == chapper and i == 0:
            next =  chap[i+1].id
            pre =  None
            break
        else:
            next = None
            pre = chap[len(chap)-2].id

    noidung = chapper.content.read().decode('utf-8')
    line = chapper.content.readline().decode('utf-8')
    context = {'noidung': noidung, 'title': chapper.title, 'book': book,'chap':chapper,'next':next,'pre':pre,
               'line':line}

    return render(request,'pages/noidung.html',context)

def SignUp(request): # Đăng ký tài khoản
    form = Dangky()
    if request.method == 'POST':
        form = Dangky(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home/dangnhap')
    context = {'form':form}
    return render(request,'pages/Dangky.html',context)

def TheLoai(request,name): #Lọc theo thể loại
    category = Category.objects.get(name=name)
    Bookcate = category.book_set.all()
    contex = {'bookcate':Bookcate}
    return render(request,'pages/theloai.html',contex)


def tacgia(request,name): #Lọc theo tác giả
     author = Author.objects.get(Name = name)
     book = author.book_set.all()
     contex = {'book':book}
     return render(request,'pages/tacgia.html',contex)
def search(request):
    if request.method == 'GET':
        searchtext = request.GET.get('search', None)
        if searchtext:
            book = Book.objects.filter(BookName__icontains = searchtext)
        else:
            book = None
        context = {'book': book}
        return render(request, 'pages/search.html', context)

