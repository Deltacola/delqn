from django.utils import timezone
from .models import Post
from .models import DeliveryData
from .forms import PostForm
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import FormView
from .forms import DeliSearchForm
from django.db.models import Q


def base(request):
    return render(request, 'blog/base.html')


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def result(request):
    return render(request, 'blog/result.html')


class SearchFormView(FormView):
    form_class = DeliSearchForm
    template_name = 'blog/result.html'

    def form_valid(self, form):
        schStart = '%s' % self.request.POST['start_point']
        schEnd = '%s' % self.request.POST['end_point']
        schLength = '%s' % self.request.POST['length_form']
        schWeight = '%s' % self.request.POST['weight_form']
        schTime = '%s' % self.request.POST['time_form']
        area_list = DeliveryData.objects.filter(Q(start_area=schStart) & Q(end_area=schEnd) & Q(total_length=schLength) & Q(del_time=schTime) & Q(weight=schWeight)).distinct()
        context = {}
        context['form'] = form
        context['search_term'] = schStart
        context['object_list'] = area_list

        return render(self.request, self.template_name, context)
