from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def home(request):
    try:
        forums=forum.objects.all()
        count = forums.count()
        discussions=[]
        for i in forums:
            discussions.append(i.discussion_set.all())

        context = {
            'forums':forums,
            'count':count,
            'discussions':discussions,
        }
        return render(request,'discussionForum/home.html', context)
    except:
        return redirect('discussionForum:addInForum')

def addInForum(request):
    form = CreateInForum()
    if request.method == 'POST':
        form  = CreateInForum(request.POST)
        if form.is_valid():
            form.save()
            return redirect('discussionForum:home')
    context = {'form':form}
    return render(request,'discussionForum/addInForum.html', context)

def addInDiscussion(request):
    form =CreateInDiscussion()
    if request.method == 'POST':
        form = CreateInDiscussion(request.POST)
        if form.is_valid():
            form.save()
            return redirect('discussionForum:home')
    context = {'form': form}
    return render(request,'discussionForum/addInDiscussion.html', context)
