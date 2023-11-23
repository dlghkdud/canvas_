from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Drawing, Comment
from .forms import DrawingForm, CommentForm
from django.contrib import messages

import os
from django.conf import settings
from django.http import HttpResponse

def index(request):
    drawing_list = Drawing.objects.order_by('-create_date')
    context = {'drawing_list': drawing_list}
    return render(request, 'palette/drawing_list.html', context)

def detail(request, drawing_id):
    drawing = get_object_or_404(Drawing, pk=drawing_id)
    context = {'drawing': drawing}
    return render(request, 'palette/drawing_detail.html', context)

def comment_create(request, drawing_id):
    drawing = get_object_or_404(Drawing, pk=drawing_id)
    comment = Comment(drawing=drawing, content=request.POST.get('content'), create_date=timezone.now())
    comment.author = request.user
    comment.save()
    return redirect('palette:detail', drawing_id=drawing.id)

@ login_required
def drawing_create(request):
    if request.method == 'POST':
        form = DrawingForm(request.POST, request.FILES) # request.FILES
        if form.is_valid():
            drawing = form.save(commit=False)
            drawing.author = request.user 
            drawing.create_date = timezone.now()
            if 'imgfile' in request.FILES: #img파일 처리
                drawing.imgfile = request.FILES['imgfile']
            if 'uploadedFile' in request.FILES: #업로드 파일처리
                drawing.uploadedFile = request.FILES['uploadedFile']
            drawing.save()
            return redirect('palette:index')
    else:
        form = DrawingForm()
    context = {'form':form}
    return render(request, 'palette/drawing_form.html', context)

@login_required(login_url='common:login')
def drawing_modify(request, drawing_id):
    drawing = get_object_or_404(Drawing, pk=drawing_id)
    if request.user != drawing.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('palette:detail', drawing_id=drawing.id)
    if request.method == "POST":
        form = DrawingForm(request.POST, instance=drawing)
        if form.is_valid():
            drawing = form.save(commit=False)
            drawing.modify_date = timezone.now()  # 수정일시 저장
            drawing.save()
            return redirect('palette:detail', drawing_id=drawing.id)
    else:
        form = DrawingForm(instance=drawing)
    context = {'form': form}
    return render(request, 'palette/drawing_form.html', context)

@login_required(login_url='common:login')
def drawing_delete(request, drawing_id):
    drawing = get_object_or_404(Drawing, pk=drawing_id)
    if request.user != drawing.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('palette:detail', drawing_id=drawing.id)
    drawing.delete()
    return redirect('palette:index')

@login_required(login_url='common:login')
def comment_modify(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('palette:detail', drawing_id=comment.drawing.id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('palette:detail', drawing_id=comment.drawing.id)
    else:
        form = CommentForm(instance=comment)
    context = {'comment': comment, 'form': form}
    return render(request, 'palette/comment_form.html', context)

@login_required(login_url='common:login')
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '삭제권한이 없습니다')
    else:
        comment.delete()
    return redirect('palette:detail', drawing_id=comment.drawing.id)

@login_required(login_url='common:login')
def drawing_vote(request, drawing_id):
    drawing = get_object_or_404(Drawing, pk=drawing_id)
    drawing.voter.add(request.user)
    # 경로 수정
    return redirect('palette:index')

def file_download(request, id):
    drawing = Drawing.objects.get(id=id)
    file_path = drawing.uploadedFile.path
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/force-download")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404


# https://eveningdev.tistory.com/47
# https://hyundy.tistory.com/11