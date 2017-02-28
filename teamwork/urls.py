"""teamwork URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.contrib.auth import views as auth_views

from teamwork.apps.core import views as core_views
from teamwork.apps.profiles import views as profile_views
from teamwork.apps.projects import views as project_views
from teamwork.apps.courses import views as course_views

urlpatterns = [
    #/
    url(r'^$', core_views.home, name='home'),
    # /signup/
    url(r'^signup/$', profile_views.signup, name='signup'),
    # /create_project/
    url(r'^project/create/$', project_views.create_project, name='create_project'),
    # /view_projects/
    url(r'project/all/', project_views.view_projects, name='view_projects'),
    # /create_course/
    url(r'^course/new/$', course_views.create_course, name='create_course'),
    # /view_course/
    url(r'course/$', course_views.view_courses, name='view_course'),
    #/join_course/
    url(r'join_course', course_views.join_course, name='join_course'),
    url(r'^course/(?P<slug>[^/]+)/edit/$', course_views.edit_course,
        name='edit_course'),
    #url(r'edit_course/(?P<name>[^/]+)/$', course_views.edit_course,
    #    name='edit_course'),

    # /admin/
    url(r'^admin/', admin.site.urls),
    # /login/
    url(r'^login', auth_views.login, {'template_name': 'core/cover.html'},
        name='login'),
    #logout
    url(r'^logout', auth_views.logout, {'next_page': '/'}, name='logout'),
    # /username/ - A users unique profile url
    url(r'^user/(?P<username>[^/]+)/$', profile_views.profile, name='profile'),
]
