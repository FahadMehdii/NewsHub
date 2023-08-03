from django.contrib.auth.views import PasswordChangeView
from django.urls import path
from . import views
from .views import MyPasswordResetView, MyPasswordResetConfirmView, MyPasswordResetDoneView, \
    MyPasswordResetCompleteView, PasswordChangeDone, HistoryListView, ArchivedHistoryView
app_name = "fyp"

urlpatterns = [
    path("", views.MainPage.as_view(), name="MainPage"),
    path('update-last-visited/<int:news_id>/', views.update_last_visited, name='update_last_visited'),
    path('without-history/<int:news_id>/', views.without_history, name='without_history'),
    path("Technology/", views.TechnologyPage.as_view(), name="TechnologyPage"),
    path("Sports/", views.SportsPage.as_view(), name="SportsPage"),
    path("Entertainment/", views.EntertainmentPage.as_view(), name="EntertainmentPage"),
    path("Business/", views.BusinessPage.as_view(), name="BusinessPage"),
    path("World/", views.WorldPage.as_view(), name="WorldPage"),

    path("pakistan/", views.PakistanPage.as_view(), name="PakistanPage"),
    # Add a view to handle password change success
    path('accounts/password_change_done/',
         PasswordChangeDone.as_view(template_name='registration/password_change_done.html'),
         name='password_change_done'),
    path('accounts/password_change/', PasswordChangeView.as_view(template_name='registration/password_change.html'),
         name='password_change'),
    path('accounts/password_reset/', MyPasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/', MyPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', MyPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', MyPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # path('crawl_news/', crawl_news, name='crawl_news'),
    path('execute-scrapy-command/', views.execute_scrapy_command, name='execute_scrapy_command'),
    path('accounts/history/', HistoryListView.as_view(), name='history_list'),
    path('archived/', ArchivedHistoryView.as_view(), name='archived_history'),
]
