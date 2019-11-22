from .views import HomePageView,CreatePostView,addlike,PostPlus,PostViewSet,login_rest
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path('home', HomePageView.as_view(), name='home'),
    path('new_post', CreatePostView.as_view(), name='new_post'),
    path('add_like/<int:pk>', addlike , name='add_like'),
    path('postplus/', PostPlus.as_view() , name='post_plus'),
    path('rest_login/', login_rest , name='login_rest'),
]

#DRF
router.register(r'rest_post', PostViewSet, basename='user')
urlpatterns += router.urls