from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.signout, name='logout'),
    path('orders/', views.orders, name='orders'),
    path('orders_completed/', views.orders_completed, name='orders_completed'),
    path('orders/create/', views.create_order, name='create_order'),
    path('orders/<int:order_id>/', views.order_detail, name='order_detail'),
    path('orders/<int:order_id>/complete/', views.complete_order, name='complete_order'),
    path('orders/<int:order_id>/delete/', views.delete_order, name='delete_order'),
]
