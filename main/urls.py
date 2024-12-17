from django.urls import path
from . import views
# from .views import index, other_page, BBLoginView, profile, BBLogoutView, ProfileEditView, PasswordEditView, RegisterDoneView, RegisterView, user_activate


app_name = 'main'

urlpatterns = [
    path('accounts/activate/<str:sign>/', views.user_activate, name='activate'),
    path('accounts/register/done/', views.RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register/', views.RegisterView.as_view(), name='register'),
    path('accounts/logout/', views.BBLogoutView.as_view(), name='logout'),
    path('accounts/password/edit/', views.PasswordEditView.as_view, name='password_edit'),

    path('accounts/profile/delete/', views.ProfileDeleteView.as_view, name='profile_delete'),
    path('accounts/profile/edit/', views.ProfileEditView.as_view, name='profile_edit'),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/login/', views.BBLoginView.as_view(), name='login'),
    path('<str:page>', views.other_page, name='other'),
    path('', views.index, name='index'),

]
