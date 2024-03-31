from django.contrib.auth.views import LogoutView
from django.urls import path

from petstagram.accounts.views import UserLoginView, RegisterView
from petstagram.main_app.views.profiles import ProfileCreateView

urlpatterns = [
    # path('create-profile/', - create profile page),
    path('register/', RegisterView.as_view(), name='register user'),
    path('login/', UserLoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    # path(/accounts/profile/<int:pk>/', - profile details page),
    # path(/accounts/edit-profile/<int:pk>/', - edit profile page),
    # path(/accounts/edit-password/<int:pk>/', - edit profile page),
]