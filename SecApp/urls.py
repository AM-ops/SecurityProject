from django.conf.urls import url
from . import views

app_name = 'SecApp'

urlpatterns = [
    url(r'portfolio/$',views.CryptoListView.as_view(), name='list'),
    url(r'^vig/$',views.VigOverviewPage.as_view(),name='vig_overview'),
    url(r'^ver/$',views.VerOverviewPage.as_view(),name='ver_overview'),
    url(r'^transpo/$',views.TranspoOverviewPage.as_view(),name='transpo_overview'),
    url(r'^own/$',views.OwnOverviewPage.as_view(),name='own_overview'),

    url(r'^vig/text/create/enc$',views.VigTextEncCreate.as_view(),name='vig_text_create_enc'),
    url(r'^vig/text/create/dec$',views.VigTextDecCreate.as_view(),name='vig_text_create_dec'),
    url(r'^ver/text/create/enc$',views.VerTextEncCreate.as_view(),name='ver_text_create_enc'),
    url(r'^ver/text/create/dec$',views.VerTextDecCreate.as_view(),name='ver_text_create_dec'),
    url(r'^transpo/text/create/enc$',views.TranspoTextEncCreate.as_view(),name='transpo_text_create_enc'),
    url(r'^transpo/text/create/dec$',views.TranspoTextDecCreate.as_view(),name='transpo_text_create_dec'),
    url(r'^own/text/create/enc$',views.OwnTextEncCreate.as_view(),name='own_text_create_enc'),
    url(r'^own/text/create/dec$',views.OwnTextDecCreate.as_view(),name='own_text_create_dec'),
    url(r'^vig/file/create/enc$',views.VigFileEncCreate.as_view(),name='vig_file_create_enc'),

    url(r'vig/text/enc/(?P<pk>\d+)/$',views.VigTextEncDetailView.as_view(), name='VigTextEnc_detail'),
    url(r'vig/text/dec/(?P<pk>\d+)/$',views.VigTextDecDetailView.as_view(), name='VigTextDec_detail'),
    url(r'ver/text/enc/(?P<pk>\d+)/$',views.VerTextEncDetailView.as_view(), name='VerTextEnc_detail'),
    url(r'ver/text/dec/(?P<pk>\d+)/$',views.VerTextDecDetailView.as_view(), name='VerTextDec_detail'),
    url(r'transpo/text/enc/(?P<pk>\d+)/$',views.TranspoTextEncDetailView.as_view(), name='TranspoTextEnc_detail'),
    url(r'transpo/text/dec/(?P<pk>\d+)/$',views.TranspoTextDecDetailView.as_view(), name='TranspoTextDec_detail'),
    url(r'own/text/enc/(?P<pk>\d+)/$',views.OwnTextEncDetailView.as_view(), name='OwnTextEnc_detail'),
    url(r'own/text/dec/(?P<pk>\d+)/$',views.OwnTextDecDetailView.as_view(), name='OwnTextDec_detail'),

    url(r'vig/text/delete/enc/(?P<pk>\d+)/$',views.VigTextEncDeleteView.as_view(), name='VigTextEnc_delete'),
    url(r'vig/text/delete/dec/(?P<pk>\d+)/$',views.VigTextDecDeleteView.as_view(), name='VigTextDec_delete'),
    url(r'ver/text/delete/enc/(?P<pk>\d+)/$',views.VerTextEncDeleteView.as_view(), name='VerTextEnc_delete'),
    url(r'ver/text/delete/dec/(?P<pk>\d+)/$',views.VerTextDecDeleteView.as_view(), name='VerTextDec_delete'),
    url(r'transpo/text/delete/enc/(?P<pk>\d+)/$',views.TranspoTextEncDeleteView.as_view(), name='TranspoTextEnc_delete'),
    url(r'transpo/text/delete/dec/(?P<pk>\d+)/$',views.TranspoTextDecDeleteView.as_view(), name='TranspoTextDec_delete'),
    url(r'own/text/delete/enc/(?P<pk>\d+)/$',views.OwnTextEncDeleteView.as_view(), name='OwnTextEnc_delete'),
    url(r'own/text/delete/dec/(?P<pk>\d+)/$',views.OwnTextDecDeleteView.as_view(), name='OwnTextDec_delete'),

]