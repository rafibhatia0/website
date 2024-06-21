
from django.shortcuts import render, redirect
from .models import Topic, Entry, Nest  # Adjust this based on your models
from .forms import TopicForm, EntryForm, NestForm  # Adjust this based on your forms
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'ll_log/index.xhtml')
@login_required
def topic(request):
    topic = Topic.objects.filter(owner=request.user)
    context = {'topic':topic}
    return render(request,'ll_log/topic.xhtml',context)
@login_required
def add_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            new =form.save(commit=False)
            new.owner = request.user
            new.save()
            return redirect('ll_log:topic')
    context = {'form':form}
    return render(request,'ll_log/new_topic.xhtml',context)
@login_required
def entry(request,topic_id):
    topic = Topic.objects.get(id=topic_id)
    entry = topic.entry_set.all()
    context= {'topic':topic,'entry':entry}
    return render(request,'ll_log/entry.xhtml',context)

@login_required


def new_entry(request,topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit= False)
            new_form.topic = topic
            new_form.save()
            return redirect('ll_log:entry',topic_id=topic_id)
    context = {'topic':topic,'form':form}
    return render(request,'ll_log/new_entry.xhtml',context)
@login_required
def nest(request,topic_id,entry_id):
    topic = Topic.objects.get(id=topic_id)
    entry = topic.entry_set.get(id=entry_id)
    nest = entry.nest_set.all()
    context= {'topic':topic,'entry':entry,'nest':nest}
    return render(request,'ll_log/nest.xhtml',context)

@login_required
def new_nest(request,topic_id,entry_id):
    topic = Topic.objects.get(id=topic_id)
    entry = topic.entry_set.get(id=entry_id)
    if request.method != 'POST':
        form = NestForm()
    else:
        form = NestForm(request.POST)
        if form.is_valid():
            new_nest = form.save(commit=False)
            new_nest.topic = topic
            new_nest.entry = entry
            new_nest.save()
            return redirect('ll_log:nest',topic_id=topic_id,entry_id=entry_id)
    context = {'topic':topic,'entry':entry,'form':form}
    return render(request,'ll_log/new_nest.xhtml',context)



@login_required
def edit(request,nest_id):
    nest = Nest.objects.get(id=nest_id)
    entry = nest.entry
    topic = entry.topic

    if request.method != 'POST':
        form = NestForm(instance=nest)
    else:
        form = NestForm(request.POST,instance=nest)
        if form.is_valid():
            form.save()
            return redirect('ll_log:nest',topic_id= topic.id,entry_id=entry.id)

    context = {'topic':topic,'entrt':entry,'nest':nest,'form':form}
    return render(request, 'll_log/edit.xhtml', context)
