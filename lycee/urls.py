from django.conf.urls import url
from . import views
from .views import StudentCreateView,PresenceCreateView,ModifyStudent

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<cursus_id>[0-9]+)$', views.detail, name='detail'),
    # /lycee/student/73
    url(r'^student/(?P<student_id>[0-9]+)$', views.detail_student, name='detail_student'),
    url(r'^student/create/$', StudentCreateView.as_view(), name='create_student'),
    url(r'^student/(?P<presence_id>[0-9]+)/$', views.detailpresence, name='detailpresence'),
    url(r'^student/Presence/$', PresenceCreateView.as_view(), name='Presence'),
    url(r'^edit-piaf/(?P<pk>\d+)/$', ModifyStudent.as_view(), name='ModifyStudent'),
    url(r'^ca-roll/ca-roll/$', views.callofroll, name='callofroll'),
    
]
