from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('profile', views.UserProfileViewSet)
router.register('login', views.LoginViewSet, base_name='login')

urlpatterns = [
    url(r'^contacts/$', views.FriendList.as_view()),
    url(r'^contacts/(?P<pk>[0-9]+)/$', views.FriendDetail.as_view()),

    url(r'^services/$', views.ServiceList.as_view()),
    url(r'^services/(?P<pk>[0-9]+)/$', views.ServiceDetail.as_view()),

    url(r'^categories/$', views.EmergencyServiceCategoryList.as_view()),
    url(r'^categories/(?P<pk>[0-9]+)/$', views.EmergencyServiceCategoryDetail.as_view()),

    url(r'^servicesByCat/(?P<pk>[0-9]+)/$', views.ServicesByCategoryList.as_view()),
    url(r'^contactsByProfile/(?P<pk>[0-9]+)/$', views.FriendsByProfileList.as_view()),

    url(r'^stories/$', views.StoryList.as_view()),
    url(r'^stories/(?P<pk>[0-9]+)/$', views.StoryDetail.as_view()),

    url(r'^pins/$', views.PinList.as_view()),
    url(r'^pins/(?P<pk>[0-9]+)/$', views.PinDetail.as_view()),

    url(r'^infos/$', views.InformationList.as_view()),
    url(r'^infos/(?P<pk>[0-9]+)/$', views.InformationDetail.as_view()),

    # url(r'', include(router.urls)),
    # url(r'^persons/$', views.PersonList.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(r'', include(router.urls))
]

# urlpatterns += [
#     url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework')),
# ]
