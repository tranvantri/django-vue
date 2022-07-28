from .serialiuzers import BookSerializer, CategorySerializer, AuthorSerializer
from .models import Book, Category, Author, Favorite
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django.http import Http404
from django.db.models import F
from django.db.models import Q
from django.db.models import Prefetch


class BooksList(APIView):

    def get(self, request, format=None):
        isTrendy = bool(request.query_params.get('is_trendy', False))
        categoryId = int(request.query_params.get('category_id', 0))
        authorId = int(request.query_params.get('author_id', 0))
        q = str(request.query_params.get('q', ''))
        limit = int(request.query_params.get('limit', 10))
        sortBy = '-' if request.query_params.get('sort_by', 'desc') == 'desc' else ''

        query_set = Book.objects.filter(is_active=True, category__is_active=True)
        query_set.order_by(sortBy + 'date_added')

        if isTrendy:
            query_set = query_set.filter(is_trendy=True)

        if q:
            query_set = query_set.filter(name__istartswith=q)

        if categoryId:
            query_set = query_set.filter(category_id=categoryId)

        if authorId:
            query_set = query_set.filter(author_id=authorId)

        if request.user.is_authenticated:
            is_favorite = bool(request.query_params.get('is_favorite', False))

            if is_favorite:
                query_set = query_set.filter()
            else:
                query_set = query_set.filter()

        # query_set = query_set.prefetch_related(
        #     Prefetch('favorite', queryset=Favorite.objects.filter(book=1))
        # )

        print(query_set.query)

        paginator = PageNumberPagination()
        paginator.page_size = limit

        results = paginator.paginate_queryset(query_set, request)
        serializer = BookSerializer(results, many=True)

        return paginator.get_paginated_response(serializer.data)


class BookDetail(APIView):
    def get(self, request, id, format=None):
        try:
            book = Book.objects.get(id=id)
            serializer = BookSerializer(book)

            return Response(serializer.data)
        except Book.DoesNotExist:
            raise Http404


class AllCategories(APIView):
    def get(self, request, format=None):
        categories = Category.objects.all().filter(is_active=True)
        serializer = CategorySerializer(categories, many=True)

        return Response(serializer.data)


class AllAuthors(APIView):
    def get(self, request, format=None):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)

        return Response(serializer.data)
