from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class MyModel(models.Model):
    field1 = models.TextField()

    def __str__(self):
        return self.field1


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(unique=True)
    content = models.TextField(unique=True)
    date_added = models.DateField(auto_now_add=True)
    image_url = models.URLField(unique=True)
    news_image = models.CharField(max_length=2000)
    last_visited = models.DateTimeField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"Date: {self.date_added}, Title: {self.title}, URL: {self.url}, Content: {self.content}"


class History(models.Model):
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.CharField(max_length=200)
    url = models.URLField()
    category = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    def is_archived(self):
        ten_minutes_ago = timezone.now() - timezone.timedelta(minutes=10)
        return self.timestamp < ten_minutes_ago

    def archive(self):
        ArchivedItem.objects.create(
            date_archived=self.date,
            user=self.user,
            content=self.content,
            url=self.url,
            category=self.category,
            timestamp_archived=self.timestamp
        )

    def delete(self, *args, **kwargs):
        self.archive()  # Create archived item before deleting
        super().delete(*args, **kwargs)


class ArchivedItem(models.Model):
    date_archived = models.DateField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.CharField(max_length=200)
    url = models.URLField()
    category = models.CharField(max_length=200)
    timestamp_archived = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content


class Good(models.Model):
    field1 = models.CharField(max_length=2000)

    def __str__(self):
        return self.field1
