from django.urls import path, include

from rest_framework.routers import DefaultRouter

# from watchlist.api.views import movie_list, movie_detail
from watchlist.api.views import (
    MovieListAV, 
    MovieDetailAV,
    StreamPlatformListAV,
    StreamPlatformDetailListAV,
    ReviewList,
    ReviwDetail,
    ReviewCreate,
    StreamPlatformViewset
)
#MovieListAV#, MovieDetailAV

router = DefaultRouter()
router.register('stream', StreamPlatformViewset, basename='streamplatform')


urlpatterns = [
    path('movie/', MovieListAV.as_view(), name='watchlist-list'),
    path('movie/<int:pk>/', MovieDetailAV.as_view(), name='watchlist-detail'),

    path('movie/platform/', StreamPlatformListAV.as_view(), name='platfrom-list'),
    path('movie/platform/<int:pk>/', StreamPlatformDetailListAV.as_view(), name='platform-detail'),

    # path('movie/<int:pk>/review', ),
    # path('movie/review/<int:pk>', ),

    # path('movie/review/', ReviewList.as_view(), name='review-list'),
    # path('movie/review/<int:pk>', ReviwDetail.as_view(), name='review-detail'),
    path('movie/<int:pk>/review-create/', ReviewCreate.as_view(), name='review-list'),

    path('movie/review/', ReviewList.as_view(), name='review-list'),
    path('movie/<int:pk>/review/', ReviewList.as_view(), name='review-list'),
    path('movie/review/<int:pk>/', ReviwDetail.as_view(), name='review-detail'),


    # path('platform/', StreamPlatformViewset.as_view({'get':'list', 'post':'create'})),
    # path('platform/<int:pk>/', StreamPlatformViewset.as_view({'get':'retrieve'})),

    path('', include(router.urls)),
    
]