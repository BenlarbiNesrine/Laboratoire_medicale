from django.conf.urls import url ,include
from . import views


urlpatterns = [

	url(r'charts/$', views.fns),
	url(r'tp/$', views.tp),
	url(r'tck/$', views.tck),
	url(r'frottis_sanguin/$', views.frottis_sanguin),
	url(r'biochimie/$', views.coa),
	url(r'biochimie/coa/$', views.coa),
	url(r'biochimie/poa/$', views.poa),
	url(r'biochimie/cob/$', views.cob),
	url(r'biochimie/curtillet/$', views.curtillet),
	url(r'biochimie/Plastique/$', views.Plastique),
	url(r'biochimie/chir_Générale/$', views.chir_Générale),
	url(r'biochimie/ChirM_Faciale/$', views.ChirM_Faciale),
	url(r'biochimie/Réa_Méd/$', views.Réa_Méd),
	url(r'biochimie/Méd_Interne/$', views.Méd_Interne),
	url(r'biochimie/Réa_cov/$', views.Réa_cov),
	url(r'biochimie/Néonat/$', views.Néonat),
	url(r'biochimie/Pédiatrie/$', views.Pédiatrie),
	url(r'biochimie/Maternié/$', views.Maternié),
	url(r'biochimie/PU_T/$', views.PU_T),
	url(r'biochimie/MTV/$', views.MTV),


	url(r'biochimie/PUM_COV/$', views.PUM_COV),
	url(r'biochimie/Puchir_cov/$', views.Puchir_cov),
	url(r'biochimie/PU_Chir/$', views.PU_Chir),
	url(r'biochimie/PU_MI/$', views.PU_MI),









]
