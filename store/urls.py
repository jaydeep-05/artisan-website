from django.urls import path
from . import views
from .views import SignUpForm

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
	path('product/<int:pk>',views.product,name='product'),
	path('signin/', views.signinPage, name="signin"),
	path('signup/', SignUpForm.as_view(), name='signup'),
    path('logout',views.logoutUser,name='logout'), 
	path('profile/<str:username>',views.profile,name='profile'),
]