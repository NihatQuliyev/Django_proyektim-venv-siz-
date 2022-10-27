from django.urls import path

from . import views                                                      # views modelin tanitmi

app_name = 'sorgu'                                                       # urllerin name vasitesi ile tespiti

urlpatterns = [

    # ex: /sorgu/
    path('', views.esas, name='esas'),                                   # esas sehife urli

    # ex: /sorgu/5/
    path('<int:question_id>/', views.etrafli, name='etrafli'),           # etrafli sehifesi urli

    # ex: /sorgu/5/netice/
    path('<int:question_id>/netice/', views.netice, name='netice'),      # netice sehifesi urli

    # ex: /sorgu/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),            # sesverme sehifesi urli
]