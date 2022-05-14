from django.urls import path
from . import views

urlpatterns = [
    path('post/',views.PostView.as_view({'get':'list','post':'create'})),
    path('post/<int:pk>',views.PostView.as_view({'put':'update','delete':'destroy'})),

    path('wall/',views.FeedView.as_view({'get':'list'})),
    path('viewpost/<int:pk>', views.ReadPostView.as_view()),

]
