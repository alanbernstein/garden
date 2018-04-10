"""garden URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from issues.views import (
    UserListView,
    UserDetailView,
    IssueListView,
    IssueDetailView,
)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users$', UserListView.as_view(), name='users-list'),
    url(r'^users/(?P<user_id>[0-9]+)$', UserDetailView.as_view(), name='users-detail'),
    url(r'^issues$', IssueListView.as_view(), name='issues-list'),
    url(r'^issues/(?P<issue_id>[0-9]+)$', IssueDetailView.as_view(), name='issues-detail'),
]