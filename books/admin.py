from django.contrib import admin
from books.models import BookModel, AuthorModel, GenreModel

admin.site.register(BookModel)
admin.site.register(AuthorModel)
admin.site.register(GenreModel)

