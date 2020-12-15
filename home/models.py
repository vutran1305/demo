from django.db import models
from .validators import validate_ContentChapter
from django.utils import timezone


class Author(models.Model):
    Name = models.CharField(max_length=100)
    birth = models.DateField(default=None,null=True,blank=True)
    def __str__(self):
        return self.Name


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200,null=True,blank=True)
    def __str__(self):
        return self.name



class Comment(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    def __str__(self):
        return self.title

class Book(models.Model):
    status_choice = ((0,"Đang ra"),(1,"Đã hoàn thành"),(2,"Tạm ngưng"))
    BookName = models.CharField(max_length=100)
    createDate = models.DateTimeField(default=timezone.now())

    imageBook = models.ImageField(upload_to='image/%Y/%m/%d/',blank=True,null=True)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,default= None,blank=True,null=True)
    category = models.ManyToManyField(Category)
    status = models.IntegerField(choices=status_choice,default=0)
    def __str__(self):
        return self.BookName

class Chapter(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.FileField(upload_to='documents/%Y/%m/%d/',validators=[validate_ContentChapter]) #documents/%Y/%m/%d/:Chỉ định nơi lưu file , tệp documents sẽ dc tạo tự động trong media
    time_pub = models.DateTimeField()
    def __str__(self):
        return self.title

