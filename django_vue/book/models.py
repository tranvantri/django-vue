from django.db import models
from django.conf import settings
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.utils.text import slugify
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(default='', blank=True)
    is_active = models.BooleanField(default=True)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.name)
        super(Category, self).save()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}'


class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    category = models.ForeignKey(Category, related_name='books', on_delete=models.CASCADE)
    author = models.ForeignKey(Author, related_name='book_author', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField(default='', blank=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(177, 250)], format='JPEG',
                               options={'quality': 80})
    is_active = models.BooleanField(default=True)
    is_trendy = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    favorite = models.ManyToManyField(User, through='Favorite', related_name='book_user')

    class Meta:
        ordering = ('-date_added',)
        
    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.name)
        super(Book, self).save()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}'

    def get_image(self):
        if self.image:
            return settings.SITE_URL + self.image.url

        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return settings.SITE_URL + self.thumbnail.url

        return ''


class Favorite(models.Model):
    user = models.ForeignKey(User, related_name='favorites_users', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='favorite_books', on_delete=models.CASCADE)
