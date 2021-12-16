from django.db.models.query import QuerySet
from django.views.generic import ListView,DetailView
from django.http import request,HttpResponse, Http404
from django.shortcuts import get_object_or_404,render
from .models import Post

post_list = ListView.as_view(model=Post, paginate_by=10)


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
    
# post_detail = DetailView.as_view(
#     model=Post,
#     queryset=Post.objects.filter(is_public=True))    
    
class PostDetailView(DetailView):
    model = Post
    # queryset = Post.objects.filter(is_public=True)
    
    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_authenticated:
            qs = qs.filter(is_public=True)
        return qs

post_detail = PostDetailView.as_view()

def achives_year(request, year):
    return HttpResponse(f"{year}년 archives")