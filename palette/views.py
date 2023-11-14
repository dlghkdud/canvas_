from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Drawing, Comment
from .forms import DrawingForm

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



# https://eveningdev.tistory.com/47
# https://hyundy.tistory.com/11