from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from first_app import views

# TEMPLATE TAGGING
app_name = 'first_app'

urlpatterns = [
    #url(r'some_page_extension/, views.reference_of_functions_name_to_views.py, name = "value to be referenced.. see the respective html files for reference of name.. specifically the login page"),
    url(r'^form_page/', views.form_name_view, name="form_name_view"),
    url(r'^users/', views.users, name="users"),
    # url(r'login/', views.login_page, name = "login_page"),
    url(r'^user_login/$', views.user_login, name="person_login"),
    url(r'^home/$', views.home, name="home"),
    url(r'^relative/$', views.relative, name='relative'),
    url(r'^other/$', views.other, name="other"),
    url(r'^registration/', views.register, name="register")
]

urlpatterns += staticfiles_urlpatterns()


