from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from .models import News
from django.db.models import Q
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, question, answer, about

# Create your views here.


def home(request):
    context = {'item_class': 'Home'}
    return render(request, 'main_app/home.html', context)


def posts(request):
    posts = Post.objects.order_by('-pk')
    context = {'title': 'News', 'posts': posts}
    return render(request, 'main_app/post.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'main_app/post.html'
    context_object_name = 'posts'
    # ordering = ['-date_posted']
    paginate_by = 6

    def get_queryset(self):
        data = self.request.GET.get('data')
        if data:
            print(data)
            return self.model.objects.filter(Q(title__icontains=data) | Q(content__icontains=data)).order_by('-date_posted')
        else:
            return self.model.objects.all().order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['total_posts'] = Post.objects.count()
        return context


class QuestionDetailView(DetailView):
    model = question
    paginate_by = 1


class QuestionView(ListView):
    model = question
    template_name = 'main_app/qa.html'
    context_object_name = 'questions'
    ordering = ['-question_date']
    paginate_by = 3

    def get_queryset(self):
        data = self.request.GET.get('data')
        if data:
            print(data)
            return self.model.objects.filter(Q(question_title__icontains=data)
                                             | Q(question_body__icontains=data) | Q(answer__answer_comment__icontains=data)
                                             | Q(answer__answer_body__icontains=data)).order_by('-question_date')
        else:
            return self.model.objects.all().order_by('-question_date')


class NoAnswerQuestionuestionView(ListView):
    model = question
    template_name = 'main_app/noqa.html'
    context_object_name = 'questions'
    ordering = ['-question_date']
    paginate_by = 3

    def get_queryset(self):
        data = self.request.GET.get('data')
        if data:
            print(data)
            return self.model.objects.filter(Q(question_title__icontains=data) | Q(question_body__icontains=data)).order_by('-question_date')
        else:
            return self.model.objects.filter(answer__isnull=True).order_by('-question_date')


class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False


class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = question
    fields = ['question_title', 'question_comment', 'question_body']

    def form_valid(self, form):
        form.instance.question_author = self.request.user
        return super().form_valid(form)


class AnswerCreateView(LoginRequiredMixin, CreateView):
    model = answer
    fields = ['answer_comment', 'answer_body']

    def form_valid(self, form):
        form.instance.answer_author = self.request.user
        form.instance.answer_question = question.objects.filter(
            id=self.request.resolver_match.kwargs['pk']).first()
        # print(dir(self.request))
        # print(self.request.resolver_match.kwargs['pk'])
        return super().form_valid(form)


class QuestionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = question
    fields = ['question_title', 'question_comment', 'question_body']
    template_name = 'main_app/question_update_form.html'

    def form_valid(self, form):
        form.instance.question_author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        question = self.get_object()
        if self.request.user == question.question_author:
            return True
        return False


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'image']
    template_name = 'main_app/post_update_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author and self.request.user.is_superuser:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/posts'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author and self.request.user.is_superuser:
            return True
        return False


def AboutView(request):
    company = about.objects.first()
    context = {"company": company}
    return render(request, 'main_app/about.html', context)


def login(request):
    context = {'title': 'Login'}
    return render(request, 'main_app/loginup.html', context)


class UserListView(ListView):
    model = User
    template_name = 'main_app/team.html'
    context_object_name = 'users'

    def get_queryset(self):
        return self.model.objects.filter(is_staff=True)

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['total_users'] = User.objects.count()
        return context


class NewsListView(ListView):
    model = News
    template_name = 'main_app/news.html'
    context_object_name = 'news'
    ordering = ['-date_posted']

    def get_queryset(self):
        return self.model.objects.last()

    def get_context_data(self, **kwargs):
        context = super(NewsListView, self).get_context_data(**kwargs)
        context['total_news'] = News.objects.count()
        return context


class CreateNews(LoginRequiredMixin, CreateView):
    model = News
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class NewsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = News
    fields = ['title', 'content']
    template_name = 'main_app/news_update_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.author and self.request.user.is_superuser:
            return True
        return False


class NewsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = News
    success_url = '/news'

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.author and self.request.user.is_superuser:
            return True
        return False
