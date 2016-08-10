from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:

     url(r'^home$', 'app1.views.xyz', name='xyz'),
     url(r'^add_people$', 'app1.views.add_people', name='add_people'),
     url(r'^check_availability/(?P<name>[\W|\w]+)/$', 'app1.views.check_availability', name='check_availability'),
     url(r'^activity_check_availability/(?P<name>[\W|\w]+)/(?P<type>[\W|\w]+)/$', 'app1.views.activity_check_availability', name='activity_check_availability'),

     url(r'^add_activity$', 'app1.views.add_activity', name='add_activity'),
    # url(r'^blog/', include('blog.urls')),
     url(r'^getvalues$', 'app1.views.getdata', name='getdata'),
     url(r'^getactivity$', 'app1.views.Get_activity', name='Get_activity'),
    url(r'^gettype$', 'app1.views.Get_activity_type', name='Get_activity_type'),
    url(r'^gettype1$', 'app1.views.Get_activity_type1', name='Get_activity_type1'),
    url(r'^gettype2$', 'app1.views.Get_activity_type2', name='Get_activity_type2'),
    url(r'^people_detail/(?P<people_name>[\W|\w]+)/', 'app1.views.people_detail', name='people_detail'),
    url(r'^Add_Activity_people_detail$', 'app1.views.Add_Activity_people_detail', name='Add_Activity_people_detail'),
    url(r'^Remove_Activity_people_detail$', 'app1.views.Remove_Activity_people_detail', name='Remove_Activity_people_detail'),
    url(r'^activity_detail/(?P<Activity_name>[\W|\w]+)/$', 'app1.views.Activity_detail', name='Activity_detail'),
    url(r'^Add_people_detail$', 'app1.views.Add_people_detail', name='Add_people_detail'),
    url(r'^delete_people_detail/(?P<name>[\W|\w]+)/$', 'app1.views.delete_people_detail', name='delete_people_detail'),
    url(r'^delete_activity_detail/(?P<act_name>[\W|\w]+)/$', 'app1.views.delete_activity_detail', name='delete_activity_detail'),
    url(r'^Remove_people_detail$', 'app1.views.Remove_people_detail', name='Remove_people_detail'),
    url(r'^fronttype/(?P<type>[\W|\w]+)/$', 'app1.views.front_activity_type', name='front_activity_type'),
    url(r'^frontpeopletype/(?P<Act_name>[\W|\w]+)/$', 'app1.views.front_people_type', name='front_people_type'),
    url(r'^admin/', include(admin.site.urls)),
)
