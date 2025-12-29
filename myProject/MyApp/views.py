from django.shortcuts import render,redirect
from .models import Tweets
from .forms import TweetForm , UserRegistrationForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Create your views here.
# from .calculator import Calculator


# def MyPage(request):
#     return render(request,"content1.html")

# def About(request):
#     ans=request.GET['ans']
#     return render(request,"about.html",{"ans":ans})

# def Forms(request):
#     op=0
#     n1=0
#     n2=0
#     try:
#         if request.method == "GET":
#             n1 = int(request.GET['val1'])
#             n2 = int(request.GET.get('val2'))
#             op = n1+n2
#         elif request.method == "POST":
#             n1 = int(request.POST['val1'])
#             n2 = int(request.POST['val2'])
#             op= n1+n2
#     except:
#         pass
#     return render(request,"myforms.html",{"out":op,"n1":n1,"n2":n2})

# def Calcul(request):
#     ans=''
#     C = Calculator()
#     data = {
#         "Calcu": C,
#     }
#     try:
#         if request.method == "POST":
#             n1 = int(request.POST['Oprand1'])
#             n2 = int(request.POST['Oprand2'])
#             opr = request.POST["Oprator"]
#             if opr == '+':
#                 ans = n1+n2
#             elif opr == '-':
#                 ans = n1-n2
#             elif opr == '*':
#                 ans = n1*n2
#             elif opr == '/':
#                 ans = n1/n2
#             data={
#                 "Calcu":C,
#                 "ans":ans,
#             }
#     except:
#         ans = "Invalid Inputs..."
#     return render(request,"calculator.html",data)

# def Marks(request):
#     if request.method == 'POST':
#         s1 = eval(request.POST.get('s1'))
#         s2 = eval(request.POST.get('s2'))
#         s3 = eval(request.POST.get('s3'))
#         s4 = eval(request.POST.get('s4'))
#         s5 = eval(request.POST.get('s5'))
#         ttl=s1+s2+s3+s4+s5
#         per = int(ttl/500)*100
#         div=''
#         if per<35:
#             div="Fail"
#         elif 35<=per<=50:
#             div = "Fourth Div"
#         elif 51<=per<=65:
#             div = "Third Div"
#         elif 60<=per<=80:
#             div = "Second Div"
#         elif 81<=per<=100:
#             div = "First Div"
        
            
#     return render(request,"marksheet.html",{"total":ttl,"per":per,"div":div})
        

def index(request):
    return render(request,"index.html")


def tweet_list(request):
    tweets = Tweets.objects.all().order_by('-created_at')
    # return render(request,'tweet_list.html',{'tweets':tweets})

    if request.method == "GET":
        stx = request.GET.get("tweets")
        if stx != None:
            tweets = Tweets.objects.filter(title__icontains=stx)
    return render(request,'tweet_list.html',{'tweets':tweets})

@login_required
def tweet_create(request):
    if request.method == 'POST':
        form = TweetForm(request.POST,request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm()
    return render(request, 'tweet_form.html',{'form':form})    
    
@login_required
def tweet_edit(request,t_id):
    tweet = get_object_or_404(Tweets,pk=t_id,user = request.user)
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES,instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)
    return render(request, 'tweet_form.html',{'form':form})    

@login_required
def tweet_delete(request,t_id):
    tweet = get_object_or_404(Tweets,pk=t_id,user = request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(request, 'tweet_confirm_delete.html',{'tweet':tweet})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('tweet_list')
    else:
        form = UserRegistrationForm()
    return render(request,'registration/register.html',{'form':form})

# def searchs(request):
#     formData = Tweets.objects.all()
#     if request.method == "GET":
#         stx = request.GET.get("title")
#         if stx != None:
#             formData = Tweets.objects.filter(title=stx)
#     data = {'title':formData}
#     return render(request,'tweet_list.html',data)