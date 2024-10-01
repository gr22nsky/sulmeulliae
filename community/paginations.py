from rest_framework.pagination import PageNumberPagination

class CommunityPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 500


class CommentPagination(PageNumberPagination):
    page_size = 20
    max_page_size = 500    