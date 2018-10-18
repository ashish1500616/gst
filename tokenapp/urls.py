from django.conf.urls import url
# from django.urls import path
from . import views

app_name = 'tokenapp'

urlpatterns = [
    url(r'^addworker/$', views.AddWorker.as_view(), name='worker_add'),
    url(r'^logAttendence/$', views.logAttendence, name='log_attendence'),
    url(r'^submit_attendence/$', views.submit_attendence, name='submit_attendence'),
]
