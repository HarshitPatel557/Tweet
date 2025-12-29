from django.shortcuts import render,redirect
from .forms import UsersForm

def user_Form(request):
    ans=0
    fr = UsersForm()
    
    data={"form":fr}
    try:
        if request.method == "POST":
            n1 = int(request.POST['val1'])
            n2 = int(request.POST['val2'])
            ans= n1+n2
            data={
                "form":fr,
                "out":ans,
            }
            url = f"/about/?ans={ans}"
            return redirect(url)
    except:
        pass
    return render(request,"myforms.html",data)