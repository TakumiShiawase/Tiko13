from django.urls import path
from .views import BooksList, BooksDetail, BooksCreate, BooksUpdate, BooksDelete, CommentView, CommentCreateView, CommentDetailView, \
    BookSearch, CommentDeleteView, ReviewCreateView, review_toggle, increase_views_count, SelectBookTypeView, SeriesCreateView, \
    BookTextView, SeriesDetailView, SeriesUpdateView, ReaderView
from . import views


urlpatterns = [
    path('', BooksList.as_view(), name='books_list'),
    path('book_detail/<int:pk>/', BooksDetail.as_view(), name='book_detail'),
    path('add/',BooksCreate.as_view(), name='book_create'),
    path('book_type/', SelectBookTypeView.as_view(), name='book_type'),
    path('<int:pk>/edit/', BooksUpdate.as_view(), name='book_update'),
    path('<int:pk>/delete/', BooksDelete.as_view(), name='book_delete'),
    path('comment/create/<int:pk>/', CommentCreateView.as_view(), name='comment_create'),
    path('comment_detail/', CommentDetailView.as_view(), name='comment_detail'),
    path('comment_list/', CommentView.as_view(), name='comment_list'),
    path('search', BookSearch.as_view(), name='book_search'),
    path('comment_delete/<int:pk>', CommentDeleteView.as_view(), name='comment_delete'),
    path('comment/like/<int:comment_id>/', views.like_comment, name='like_comment'),
    path('comment/dislike/<int:comment_id>/', views.dislike_comment, name='dislike_comment'),
    path('comment/create/<int:pk>/<int:parent_comment_id>/', CommentCreateView.as_view(), name='comment_create'),
    path('review/create/<int:pk>/', ReviewCreateView.as_view(), name='review_create'),
    path('book_detail/<int:pk>/toggle/', review_toggle, name='review_toggle'),
    path('review/increase_views_count/<int:review_id>/', increase_views_count, name='increase_views_count'),
    path('review/<int:review_id>/like/', views.like_review, name='like_review'),
    path('review/<int:review_id>/dislike/', views.dislike_review, name='dislike_review'),
    path('create_series/', SeriesCreateView.as_view(), name='create_series'),
    path('book_text/', BookTextView.as_view(), name='book_text'),
    path('rating/<int:book_id>/upvote/', views.upvote_book, name='upvote_book'),
    path('rating/<int:book_id>/downvote/', views.downvote_book, name='downvote_book'),
    path('series/<int:pk>/', SeriesDetailView.as_view(), name='series_detail'),
    path('series/<int:pk>/update/', SeriesUpdateView.as_view(), name='series_update'),
    path('reader/<int:book_id>/', ReaderView.as_view(), name='reader'),




]


