from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Drawing

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
    drawing.comment_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('palette:detail', drawing_id=drawing.id)

def drawing_create(request):
    form = DrawingForm()
    return render(request, 'palette.drawing_form.html', {'form':form})



# https://eveningdev.tistory.com/47
# https://hyundy.tistory.com/11