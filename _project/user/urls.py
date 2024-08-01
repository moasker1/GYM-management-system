from django.urls import path
from . import views

urlpatterns = [
    path('',views.login_user, name='login' ),
    path('logout',views.logout_user, name='logout' ),
    path('products',views.products, name='products' ),
    path('home',views.home, name='home' ),
    path('saleDelete/<int:id>',views.sale_delete, name='saleDelete' ),
    path('saleUpdate/<int:id>',views.sale_update, name='saleUpdate' ),
    path('clients',views.clients, name='clients' ),
    path('clientDelete/<int:id>',views.client_delete, name='clientDelete' ),
    path('clientUpdate/<int:id>',views.client_update, name='clientUpdate' ),
    path('clientpage/<int:id>',views.client_page, name='clientpage' ),
    path('profits',views.profits, name='profits' ),
    path('payupdate/<int:id>',views.pay_update, name='payupdate' ),
    path('paydelete/<int:id>',views.pay_delete, name='paydelete' ),
    path('adminPage',views.adminPage, name='adminPage' ),
    path('userdelete/<int:id>',views.user_delete, name='userdelete' ),
    path('renew/<int:id>',views.renew, name='renew' ),
    path('reports',views.reports, name='reports' ),
]