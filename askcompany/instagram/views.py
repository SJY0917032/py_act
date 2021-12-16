from django.views.generic import ListView,DetailView
from django.http import request,HttpResponse, Http404
from django.shortcuts import get_object_or_404,render
from .models import Post

post_list = ListView.as_view(model=Post)


# def post_list(request):
#     qs = Post.objects.all()
    
#     q = request.GET.get('q', '')
#     if q:
#         qs = qs.filter(message__icontains=q)
    
#     return render(request, 'instagram/post_list.html', {
#         'post_list' : qs,
#         'q':  q,
#     })

# def post_detail(request, pk) -> HttpResponse:
#     post = get_object_or_404(Post, pk=pk)
#     # try:
#     #     post = Post.objects.get(pk=pk)
#     # except Post.DoesNotExist:
#     #     raise Http404
#     return render(request, 'instagram/post_detail.html',{
#         'post' : post,
#     })
    
post_detail = DetailView.as_view(model=Post)    
    

def achives_year(request, year):
    return HttpResponse(f"{year}년 archives")