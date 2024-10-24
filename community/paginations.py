from rest_framework.pagination import PageNumberPagination


class CommunityPagination(PageNumberPagination):
    page_size = 200
    max_page_size = 500


class CommentPagination(PageNumberPagination):
    page_size = 200
    max_page_size = 500
