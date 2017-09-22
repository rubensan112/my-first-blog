# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required #Para el tema de requerir login

# Create your views here.
def home_pagev3(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'angel/home_pagev3.html',{'posts': posts })


def not_found(request):
    return render(request, 'angel/not_found.html', {})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'angel/post_detail.html', {'post': post})

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('home_pagev3')

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'angel/post_edit.html', {'form': form})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST) #request. Post son los datos que envia el usuario del formulario. Construimos el modelo del formulario Postform con esos datos.
        if form.is_valid():
            post = form.save(commit=False) #El commit=false quiere decir, que aun no queremos guardar el modelo Post
            post.author = request.user #Forzamos el author
            post.save()
            return redirect('post_detail', pk=post.pk) #Este nuevo post que se ha creado, tendra un pk, lo cogemos para que nos diriga a el.
    else:
        form = PostForm()
    return render(request, 'angel/post_edit.html', {'form': form})

def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'angel/post_draft_list.html', {'posts': posts})








'''
@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('home_page')

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)


def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'angel/post_draft_list.html', {'posts': posts})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'angel/post_edit.html', {'form': form})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST) #request. Post son los datos que envia el usuario del formulario. Construimos el modelo del formulario Postform con esos datos.
        if form.is_valid():
            post = form.save(commit=False) #El commit=false quiere decir, que aun no queremos guardar el modelo Post
            post.author = request.user #Forzamos el author
            post.save()
            return redirect('post_detail', pk=post.pk) #Este nuevo post que se ha creado, tendra un pk, lo cogemos para que nos diriga a el.
    else:
        form = PostForm()
    return render(request, 'angel/post_edit.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'angel/post_detail.html', {'post': post})

def home_page(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'angel/home_page1.html', {'posts': posts})
    '''

