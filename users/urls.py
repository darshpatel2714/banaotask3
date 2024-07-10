
from django.urls import path
from .views import SignUpView, login_view,logout_view, dashboard_view, HomeView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('', HomeView.as_view(), name='home'),  # Home page URL
]
    