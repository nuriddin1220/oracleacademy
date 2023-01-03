from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE)

    def __str__(self):
        return self.author.username+'-'+self.title

    def get_absolute_url(self):
        return reverse("news")


class Post(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    image = models.ImageField(
        default='default_post.jpg', upload_to='post_pics')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})


class question(models.Model):
    question_title = models.CharField(max_length=300)
    question_comment = models.TextField(blank=True, null=True)
    question_date = models.DateTimeField(default=timezone.now)
    question_body = models.TextField(blank=True, null=True)
    question_author = models.ForeignKey(
        User, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_author.username+'-'+self.question_title

    def get_absolute_url(self):
        return reverse("q-detail", kwargs={"pk": self.pk})


class answer(models.Model):
    answer_comment = models.TextField()
    answer_date = models.DateTimeField(default=timezone.now)
    answer_body = models.TextField(blank=True, null=True)
    answer_author = models.ForeignKey(
        User, on_delete=models.CASCADE)
    answer_question = models.ForeignKey(
        question, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer_author.username+'-'+self.answer_question.question_title

    def get_absolute_url(self):
        return reverse("q-detail", kwargs={"pk": self.answer_question.id})


class about(models.Model):
    company_name = models.CharField(max_length=300)
    established_year = models.CharField(max_length=10)
    address = models.CharField(max_length=300)
    target = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=20)
    company_aim = models.TextField()
