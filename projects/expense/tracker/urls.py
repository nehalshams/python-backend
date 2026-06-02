
from django.urls import path

from tracker.views import index, delete_transaction, login_page, sign_up, logout_page

urlpatterns = [
    path('', index, name='index'),
    path(
        'delete-transaction/<id>/',
        delete_transaction,
        name='delete_transaction'
    ),
    path('sign-up/', sign_up, name='sign_up'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout_page'),
]