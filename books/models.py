from django.db import models


class GenreModel(models.Model):
    name = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Genres'
        verbose_name = 'Genre'

    def __str__(self):
        return self.name


class AuthorModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Authors'
        verbose_name = 'Author'

    def __str__(self):
        return AuthorModel.full_name(self)

    def full_name(self):
        return self.first_name + self.last_name


class BookModel(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(AuthorModel, blank=True, related_name='books', verbose_name='Authors')
    description = models.TextField()
    image = models.ImageField(upload_to='books/%Y/%m/%d')
    genre = models.ManyToManyField(GenreModel, blank=True, related_name='books', verbose_name='Genres')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Books'
        verbose_name = 'Book'

    def __str__(self):
        return self.title
