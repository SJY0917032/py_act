from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, DetailView, ArchiveIndexView, YearArchiveView
from django.http import HttpResponse, HttpRequest, Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .models import Post
from .forms import PostForm



@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            # commit = false는 미처다 채우지못한것을 여기서 채우기위한 요건.
            # 꼭 post.save()를 해야만한다.
            post.author = request.user
            post.save()
            messages.success(request, '새 글이 등록되었습니다.')
            return redirect(post)
    else :
        form = PostForm()
        
    return render(request, 'instagram/post_form.html', {
        'form': form,
        'post' : None,
    })

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if post.author != request.user:
        messages.error(request, '접근 권한이 없습니다!')
        return redirect(post)
        
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            messages.success(request, '포스팅을 수정했습니다.')
            return redirect(post)
    else :
        form = PostForm(instance=post)
        
    return render(request, 'instagram/post_form.html', {
        'form': form,
        'post' : post,
    })

# post_list = login_required(ListView.as_view(model=Post, paginate_by=10))

# @method_decorator(login_required, name='dispatch')


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    paginate_by = 10


post_list = PostListView.as_view()

# def post_list(request):
#     qs = Post.objects.all()

#     q = request.GET.get('q', '')
#     if q:
#         qs = qs.filter(message__icontains=q)

#     messages.info(request, '리스트입니다~')

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

# def achives_year(request, year):
#     return HttpResponse(f"{year}년 archives")

post_archive = ArchiveIndexView.as_view(
    model=Post, date_field='created_at', paginate_by=10)

post_archive_year = YearArchiveView.as_view(
    model=Post, date_field='created_at', make_object_list=True)
