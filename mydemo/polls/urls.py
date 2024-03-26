from django.urls import path
from . import views
urlpatterns = [
    # 子路由
    path('', views.toLogin_view),
    path('index/', views.login_view),
    path('tts/', views.to_tts)
]