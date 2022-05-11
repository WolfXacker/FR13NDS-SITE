from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy, reverse

from .models import Contact

class ContactCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Contact
    template_name = 'contact/contact.html'
    fields = ('имя', 'body', 'author')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # user superuser ekanini tekshirish
    def test_func(self):
        return self.request.user.is_superuser