


from django.urls import path
from home import views


urlpatterns = [
    path("", views.index, name="index"),
    path("blocked/", views.blocked, name="blocked"),
    path("store/", views.store_view, name="store"),
]
