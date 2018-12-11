from django.shortcuts import render,redirect
from facebook.models import Article
from facebook.models import Page
from facebook.models import Comment

# Create your views here.

def play(request):
    return render(request,'play.html')

count = 0
def play2(request):
    user_name ='정유진'
    age = 20

    global count
    count = count + 1

    if age <= 20 :
        status = '성인'
    else: status = '청소년'

    diary=['날씨가 맑았다','미세먼지가 심했다','첫 눈이 왔다', '가을 날씨 같았다']

    return render(request,'play2.html', { 'name' : user_name , 'cnt' : count, 'age': status, 'diary': diary})

def profile(request):
    return render(request,'profile.html')

def event(request):
    user_name ='정유진'

    global count
    count = count + 1

    if count is 7:
        status='당첨입니다!'
    else:
        status='꽝..입니다.'

    return render(request,'event.html',{'name': user_name,'cnt':count,'status':status})

def fail(request):
    return render(request,'fail.html')
def help(request):
    return render(request,'help.html')
def warn(request):
    return render(request,'warn.html')

def newsfeed(request):
    articles = Article.objects.all()
    return render(request, 'newsfeed.html', {'articles': articles})

def detail_feed(request,pk):
    article = Article.objects.get(pk=pk)
    if request.method=='POST':
        Comment.objects.create(
            article=article,
            author=request.POST.get('nickname'),
            text=request.POST.get('reply'),
            password=request.POST.get('password')
        )
        return redirect(f'/feed/{article.pk}')


    return render(request, 'detail_feed.html', {'feed': article})

def pages(request):
    pages = Page.objects.all()
    return render(request, 'page_list.html',{'pages': pages})

def new_feed(request):
    if request.method == 'POST':
        new_article = Article.objects.create(
            author=request.POST['author'],
            title=request.POST['title'],
            password=request.POST['password'],
            text=request.POST['content']
        )
        return redirect(f'/feed/{new_article.pk}')

    return render(request,'new_feed.html')

def edit_feed(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method=='POST':
        if article.password ==request.POST['password']:
            article.author =request.POST['author']
            article.title =request.POST['title']
            article.text =request.POST['content']
            article.save()
            return redirect(f'/feed/{article.pk}')

        else:
            return redirect('/fail')

    return render(request, 'edit_feed.html',{'feed':article})

def remove_feed(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        if article.password == request.POST['password']:
            article.delete()
            return redirect('/')
        else:
            return redirect('/fail')
    return render(request, 'remove_feed.html',{'feed':article})
