from django.views.generic import ListView, CreateView, UpdateView
from posts.models import BlogPost


class BlogHome(ListView):
    model = BlogPost
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()

        # verifié si le user est connecté en surchargeant la methode get_queryset
        if self.request.user.is_authenticated:
            return queryset
        return queryset.filter(published=True)


# La vue qui permet d'ajouter une vue d'article
class BlogPostCreate(CreateView):
    model = BlogPost
    template_name = "posts/blogpost_create.html"
    fields = ['title', 'content']

# La vue qui va permettre de modifier la vue d'article
class BlogPostUpdate(UpdateView):
    model = BlogPost
    template_name = "posts/blogpost_edit.html"
    fields = ['title', 'content', 'published']

