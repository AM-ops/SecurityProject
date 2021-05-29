from django.conf.urls import url
from . import views

app_name = 'SecApp'

urlpatterns = [
    url(r'^vig/$',views.VigOverviewPage.as_view(),name='vig_overview'),
    url(r'^ver/$',views.VerOverviewPage.as_view(),name='ver_overview'),
    url(r'^transpo/$',views.TranspoOverviewPage.as_view(),name='transpo_overview'),
    url(r'^vig/text/create/enc$',views.VigTextEncCreate.as_view(),name='vig_text_create_enc'),
    url(r'^vig/text/create/dec$',views.VigTextDecCreate.as_view(),name='vig_text_create_dec'),
    url(r'^ver/text/create/enc$',views.VerTextEncCreate.as_view(),name='ver_text_create_enc'),
    url(r'^ver/text/create/dec$',views.VerTextDecCreate.as_view(),name='ver_text_create_dec'),
    url(r'^transpo/text/create/enc$',views.TranspoTextEncCreate.as_view(),name='transpo_text_create_enc'),
    url(r'^transpo/text/create/dec$',views.TranspoTextDecCreate.as_view(),name='transpo_text_create_dec'),
    url(r'vig/text/enc/(?P<pk>\d+)/$',views.VigTextEncDetailView.as_view(), name='VigTextEnc_detail'),
]