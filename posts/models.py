from django.contrib.auth import get_user_model
from django.db import models

# notre fonction qui va permettre de créer notre clés étrangère
from django.template.defaultfilters import slugify
from django.urls import reverse

User = get_user_model()

# Create your models here.
class BlogPost(models.Model):

    title = models.CharField(max_length=255, unique=True, verbose_name="Titre")
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    last_update = models.DateTimeField(auto_now=True)
    created_on = models.DateField(blank=True, null=True)
    published = models.BooleanField(default=False, verbose_name="Publié")
    content = models.TextField(blank=True, verbose_name="Contenu")

    class Meta:
        ordering = ["-created_on"]
        verbose_name = "Article"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    @property
    def author_or_default(self):
        if self.author:
            return self.author.username
        return "L'auteur inconnu"

    def get_absolute_url(self):
        return reverse('posts:home')


