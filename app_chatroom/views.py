from django.shortcuts import render
from django.shortcuts import redirect
from app_chatroom.models import *
from django.core.urlresolvers import reverse 
from django.http import HttpResponseRedirect
# Create your views here.
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from forms import *
from django.http import HttpResponse

def home(request):
    
    return render(request,'login.html')

def userloggedin(request):
 #   new_user = User.objects.create_user(username=request.POST['name']) 
  #  new_user.is_active = True
   # new_user.save() 

    username=request.POST['name']
    user=SimpleUser(name=username)
    user.save()
    return HttpResponseRedirect(reverse('chat',args=[username]))
    #return render(request, 'confirmed.html', {})
    #return redirect('chat')

def chat(request,username):
    # if request.method=='POST':
    #     new_user = User.objects.create_user(username=request.POST['name']) 
    #     new_user.is_active = True
    #     new_user.save()
    current_user=SimpleUser.objects.get(name=username)
    #print user.id
    
    
    #return render(request,'chat.html',context)


   
    html= 'chat.html' # base_stream
    form = MessageForm(request.POST)

    if not form.is_valid():
        messages = Message.objects.all()
        context={'messages':messages,
            'current_user':current_user,
            'MessageForm':MessageForm()}
        return render(request,'chat.html',context)

    message = Message(user=current_user,
        text=form.cleaned_data['text'])
    
    message.save()
    messages = Message.objects.all()
    context={'messages':messages,
            'current_user':current_user,
            'MessageForm':form}
    return render(request,'chat.html',context)
    #data = serializers.serialize("json", [message]) 
    #print data
    #return comment
    #return HttpResponse(data, content_type='application/json')


def refresh(request):
    username = request.POST['current_user']

    form = MessageForm(request.POST)

    if form.is_valid():
        message = Message(user=current_user,
            text=form.cleaned_data['text'])
        message.save()

        data = serializers.serialize("json", [message]) 
        print "data",data
        #return comment
        return HttpResponse(data, content_type='application/json')
        
