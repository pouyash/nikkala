from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404

from blog.models import Blog


class CanEditAndDeletePermission(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        blog:Blog = get_object_or_404(Blog, id=self.kwargs['pk'])
        return self.request.user == blog.user or self.request.user.is_superuser