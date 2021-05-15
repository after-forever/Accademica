
import logging
from re import I
from django.views import generic
from .forms import RegistrationForm
from .forms import ISBNForm
from django.urls import reverse_lazy
from collection.book import Book

logger = logging.getLogger(__name__)

class RegistrationView(generic.FormView):
    template_name = "registration.html"
    form_class = RegistrationForm
    success_url = reverse_lazy('collection:registration')

    def __str__(self):
        return self.name

    def get_queryset(self):
        logger.info("")

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if "response" in self.request.session:

            #response = self.request.session.get("response", None)
            isbn = self.request.session.get("response", None)
            if isbn == None:
                #TODO logging
                pass

            book = Book()
            try:
                book.create_by_ISBN(isbn)
            except (Book.RequestError, Book.NonexistentError) as e:
                logger.error(e)
                self.request.session['response'] = None

            context["form"] = RegistrationForm(
                initial={"title": book.title, "author": book.author, "publisher": book.publisher, "pubdate": book.pubdate, "price": book.price, "text": book.text_content})

            context["cover_img"] = book.cover

        if self.request.GET.get('new') is not None:
            self.request.session.clear()

        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

"""
"""
class ISBNView(generic.FormView):
    template_name = "isbn.html"
    form_class = ISBNForm
    success_url = reverse_lazy('collection:registration')

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return self.success_url

    def form_invalid(self, form):
        pass

    def form_valid(self, form):
        self.request.session.clear()
        isbn = form.data.get("isbn")
        self.request.session['response'] = isbn
        return super().form_valid(form)
