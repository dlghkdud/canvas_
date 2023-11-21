from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Drawing, Comment
from .forms import DrawingForm, CommentForm
from django.contrib import messages

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

def drawing_create(request):
    if request.method == 'POST':
        form = DrawingForm(request.POST)
        uploadedFile = request.POST["fileSubject"]
        if form.is_valid():
            drawing = form.save(commit=False)
            # imgfile = request.FILES["imgfile"]
            drawing.create_date = timezone.now()
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
            return redirect('palette:detail', question_id=drawing.id)
    else:
        form = DrawingForm(instance=drawing)
    context = {'form': form}
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
    return redirect('palette:detail', drawing_id=drawing.id)

# https://eveningdev.tistory.com/47
# https://hyundy.tistory.com/11