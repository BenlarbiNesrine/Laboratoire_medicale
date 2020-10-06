from django.shortcuts import render

# Create your views here.
def fns(request):
	#data1 pour le Services chirurgicaux
	data1=[0, 10, 5, 2, 20, 30, 45]
	total1=sum(data1)
	#data2 pour le Services Médicaux
	data2=[0, 10, 5, 2, 20, 30, 45,1]
	total2=sum(data2)
	#data3 pour le pavillons des Urgences
	data3=[0, 10, 5,1,3,4]
	total3=sum(data3)
	#data4 pour les Patients externes
	data4=[45]
	total4=sum(data4)

	inte=total1+total2+total3

	inte_ext=inte+total4
	totals={
	'total1':total1,
	'total2':total2,
	'total3':total3,
	'total4':total4,
	'inte':inte,
	'inte_ext':inte_ext,
	}


	return render (request, 'fns.html',{'data1':data1,'data2':data2,'data3':data3,'data4':data4,'totals':totals,'service':'fns'})

def tp(request):
	#data1 pour le Services chirurgicaux
	data1=[0, 10, 5, 2, 20, 30, 45]
	total1=sum(data1)
	#data2 pour le Services Médicaux
	data2=[0, 10, 5, 2, 20, 30, 45,1]
	total2=sum(data2)
	#data3 pour le pavillons des Urgences
	data3=[0, 10, 5,1,3,4]
	total3=sum(data3)
	#data4 pour les Patients externes
	data4=[45]
	total4=sum(data4)

	inte=total1+total2+total3

	inte_ext=inte+total4
	totals={
	'total1':total1,
	'total2':total2,
	'total3':total3,
	'total4':total4,
	'inte':inte,
	'inte_ext':inte_ext,
	}


	return render (request, 'fns.html',{'data1':data1,'data2':data2,'data3':data3,'data4':data4,'totals':totals,'service':'tp'})

def tck(request):
		#data1 pour le Services chirurgicaux
	data1=[0, 10, 5, 2, 20, 30, 45]
	total1=sum(data1)
	#data2 pour le Services Médicaux
	data2=[0, 10, 5, 2, 20, 30, 45,1]
	total2=sum(data2)
	#data3 pour le pavillons des Urgences
	data3=[0, 10, 5,1,3,4]
	total3=sum(data3)
	#data4 pour les Patients externes
	data4=[45]
	total4=sum(data4)

	inte=total1+total2+total3

	inte_ext=inte+total4
	totals={
	'total1':total1,
	'total2':total2,
	'total3':total3,
	'total4':total4,
	'inte':inte,
	'inte_ext':inte_ext,
	}


	return render (request, 'fns.html',{'data1':data1,'data2':data2,'data3':data3,'data4':data4,'totals':totals,'service':'tck'})

def frottis_sanguin(request):
		#data1 pour le Services chirurgicaux
	data1=[0, 10, 5, 2, 20, 30, 45]
	total1=sum(data1)
	#data2 pour le Services Médicaux
	data2=[0, 10, 5, 2, 20, 30, 45,1]
	total2=sum(data2)
	#data3 pour le pavillons des Urgences
	data3=[0, 10, 5,1,3,4]
	total3=sum(data3)
	#data4 pour les Patients externes
	data4=[45]
	total4=sum(data4)

	inte=total1+total2+total3

	inte_ext=inte+total4
	totals={
	'total1':total1,
	'total2':total2,
	'total3':total3,
	'total4':total4,
	'inte':inte,
	'inte_ext':inte_ext,
	}


	return render (request,'fns.html',{'data1':data1,'data2':data2,'data3':data3,'data4':data4,'totals':totals,'service':'frottis_sanguin'})


def coa(request):
	data={

	#'Glucose', 'Urée', 'Créatinine', 'Sodium', 'Potasium', 'Magnésium'
	'data1':[0, 10, 5, 2, 20, 30],
	#'Aspect du sérum', 'Cholestérol total', 'Triglycérides', 'LDL Cholestérol'
	'data2':[0, 10, 5, 2],

	#Acide urique', 'Acide urique(enfant)', '
	'data3':[22,55],

	#'Calcium ionisé','Calcium total''
	'data4':[0, 10],
	#['Fer','Fer(Homme)','Fer(Femme)']
	'data5':[45,10, 5],
	#'HDL Cholestérol','HDL Cholestérol(Homme)','HDL Cholestérol(Femme)'
	'data6':[0, 10, 5],
	#'Protéines(plasma)','Protéines','Albumine','Amylase'
	'data7':[0, 10, 5, 2],
	#'GOT (ASAT)','GPT (ALAT)','Bilirubine total (ALAT)','Bilirubine directe','Bilirubine indirecte'
	'data8':[0, 10, 5, 2, 20],
	#'PAL AMP','PAL AMP(enfant)','PAL AMP(adulte)'
	'data9':[0, 10, 5],
	#'Microalbumine','Créatinine','Clairance de la créatinine','Sodium','Phosphore'
	'data10':[0, 10, 5, 2, 20],
	#y-gt(Homme)','y-gt(Femme)'
	'data11':[0, 10],
	#,'Lipase(calorimétrique)','LDH','Diurèse'
	'data12':[0, 10,5],
	#'Calcium total(Nrs)','Calcium total(Adulte)
	'data13':[0, 10],
	# 'GOT (ASAT)','GPT (ALAT)'
	'data14':[10, 5],
	#,'PAL DEA','PAL DEA(enfant)','PAL DEA(adulte)'
	'data15':[ 5, 2, 20],
	#'Acide urique(Homme)','Acide urique(Femme)
	'data16':[2, 20]
	}

	return render (request,'biochimie/bio.html',{'data':data,'service':'coa'})


def poa(request):
	data={

	#'Glucose', 'Urée', 'Créatinine', 'Sodium', 'Potasium', 'Magnésium'
	'data1':[0, 10, 5, 2, 20, 30],
	#'Aspect du sérum', 'Cholestérol total', 'Triglycérides', 'LDL Cholestérol'
	'data2':[0, 10, 5, 2],

	#Acide urique', 'Acide urique(enfant)', '
	'data3':[22,55],

	#'Calcium ionisé','Calcium total''
	'data4':[0, 10],
	#['Fer','Fer(Homme)','Fer(Femme)']
	'data5':[45,10, 5],
	#'HDL Cholestérol','HDL Cholestérol(Homme)','HDL Cholestérol(Femme)'
	'data6':[0, 10, 5],
	#'Protéines(plasma)','Protéines','Albumine','Amylase'
	'data7':[0, 10, 5, 2],
	#'GOT (ASAT)','GPT (ALAT)','Bilirubine total (ALAT)','Bilirubine directe','Bilirubine indirecte'
	'data8':[0, 10, 5, 2, 20],
	#'PAL AMP','PAL AMP(enfant)','PAL AMP(adulte)'
	'data9':[0, 10, 5],
	#'Microalbumine','Créatinine','Clairance de la créatinine','Sodium','Phosphore'
	'data10':[0, 10, 5, 2, 20],
	#y-gt(Homme)','y-gt(Femme)'
	'data11':[0, 10],
	#,'Lipase(calorimétrique)','LDH','Diurèse'
	'data12':[0, 10,5],
	#'Calcium total(Nrs)','Calcium total(Adulte)
	'data13':[0, 10],
	# 'GOT (ASAT)','GPT (ALAT)'
	'data14':[10, 5],
	#,'PAL DEA','PAL DEA(enfant)','PAL DEA(adulte)'
	'data15':[ 5, 2, 20],
	#'Acide urique(Homme)','Acide urique(Femme)
	'data16':[2, 20]
	}

	return render (request,'biochimie/bio.html',{'data':data,'service':'poa'})


def cob(request):
	data={

	#'Glucose', 'Urée', 'Créatinine', 'Sodium', 'Potasium', 'Magnésium'
	'data1':[0, 10, 5, 2, 20, 30],
	#'Aspect du sérum', 'Cholestérol total', 'Triglycérides', 'LDL Cholestérol'
	'data2':[0, 10, 5, 2],

	#Acide urique', 'Acide urique(enfant)', '
	'data3':[22,55],

	#'Calcium ionisé','Calcium total''
	'data4':[0, 10],
	#['Fer','Fer(Homme)','Fer(Femme)']
	'data5':[45,10, 5],
	#'HDL Cholestérol','HDL Cholestérol(Homme)','HDL Cholestérol(Femme)'
	'data6':[0, 10, 5],
	#'Protéines(plasma)','Protéines','Albumine','Amylase'
	'data7':[0, 10, 5, 2],
	#'GOT (ASAT)','GPT (ALAT)','Bilirubine total (ALAT)','Bilirubine directe','Bilirubine indirecte'
	'data8':[0, 10, 5, 2, 20],
	#'PAL AMP','PAL AMP(enfant)','PAL AMP(adulte)'
	'data9':[0, 10, 5],
	#'Microalbumine','Créatinine','Clairance de la créatinine','Sodium','Phosphore'
	'data10':[0, 10, 5, 2, 20],
	#y-gt(Homme)','y-gt(Femme)'
	'data11':[0, 10],
	#,'Lipase(calorimétrique)','LDH','Diurèse'
	'data12':[0, 10,5],
	#'Calcium total(Nrs)','Calcium total(Adulte)
	'data13':[0, 10],
	# 'GOT (ASAT)','GPT (ALAT)'
	'data14':[10, 5],
	#,'PAL DEA','PAL DEA(enfant)','PAL DEA(adulte)'
	'data15':[ 5, 2, 20],
	#'Acide urique(Homme)','Acide urique(Femme)
	'data16':[2, 20]
	}

	return render (request,'biochimie/bio.html',{'data':data,'service':'cob'})


def curtillet(request):
	data={

	#'Glucose', 'Urée', 'Créatinine', 'Sodium', 'Potasium', 'Magnésium'
	'data1':[0, 10, 5, 2, 20, 30],
	#'Aspect du sérum', 'Cholestérol total', 'Triglycérides', 'LDL Cholestérol'
	'data2':[0, 10, 5, 2],

	#Acide urique', 'Acide urique(enfant)', '
	'data3':[22,55],

	#'Calcium ionisé','Calcium total''
	'data4':[0, 10],
	#['Fer','Fer(Homme)','Fer(Femme)']
	'data5':[45,10, 5],
	#'HDL Cholestérol','HDL Cholestérol(Homme)','HDL Cholestérol(Femme)'
	'data6':[0, 10, 5],
	#'Protéines(plasma)','Protéines','Albumine','Amylase'
	'data7':[0, 10, 5, 2],
	#'GOT (ASAT)','GPT (ALAT)','Bilirubine total (ALAT)','Bilirubine directe','Bilirubine indirecte'
	'data8':[0, 10, 5, 2, 20],
	#'PAL AMP','PAL AMP(enfant)','PAL AMP(adulte)'
	'data9':[0, 10, 5],
	#'Microalbumine','Créatinine','Clairance de la créatinine','Sodium','Phosphore'
	'data10':[0, 10, 5, 2, 20],
	#y-gt(Homme)','y-gt(Femme)'
	'data11':[0, 10],
	#,'Lipase(calorimétrique)','LDH','Diurèse'
	'data12':[0, 10,5],
	#'Calcium total(Nrs)','Calcium total(Adulte)
	'data13':[0, 10],
	# 'GOT (ASAT)','GPT (ALAT)'
	'data14':[10, 5],
	#,'PAL DEA','PAL DEA(enfant)','PAL DEA(adulte)'
	'data15':[ 5, 2, 20],
	#'Acide urique(Homme)','Acide urique(Femme)
	'data16':[2, 20]
	}

	return render (request,'biochimie/bio.html',{'data':data,'service':'curtillet'})


def Plastique(request):
	data={

	#'Glucose', 'Urée', 'Créatinine', 'Sodium', 'Potasium', 'Magnésium'
	'data1':[0, 10, 5, 2, 20, 30],
	#'Aspect du sérum', 'Cholestérol total', 'Triglycérides', 'LDL Cholestérol'
	'data2':[0, 10, 5, 2],

	#Acide urique', 'Acide urique(enfant)', '
	'data3':[22,55],

	#'Calcium ionisé','Calcium total''
	'data4':[0, 10],
	#['Fer','Fer(Homme)','Fer(Femme)']
	'data5':[45,10, 5],
	#'HDL Cholestérol','HDL Cholestérol(Homme)','HDL Cholestérol(Femme)'
	'data6':[0, 10, 5],
	#'Protéines(plasma)','Protéines','Albumine','Amylase'
	'data7':[0, 10, 5, 2],
	#'GOT (ASAT)','GPT (ALAT)','Bilirubine total (ALAT)','Bilirubine directe','Bilirubine indirecte'
	'data8':[0, 10, 5, 2, 20],
	#'PAL AMP','PAL AMP(enfant)','PAL AMP(adulte)'
	'data9':[0, 10, 5],
	#'Microalbumine','Créatinine','Clairance de la créatinine','Sodium','Phosphore'
	'data10':[0, 10, 5, 2, 20],
	#y-gt(Homme)','y-gt(Femme)'
	'data11':[0, 10],
	#,'Lipase(calorimétrique)','LDH','Diurèse'
	'data12':[0, 10,5],
	#'Calcium total(Nrs)','Calcium total(Adulte)
	'data13':[0, 10],
	# 'GOT (ASAT)','GPT (ALAT)'
	'data14':[10, 5],
	#,'PAL DEA','PAL DEA(enfant)','PAL DEA(adulte)'
	'data15':[ 5, 2, 20],
	#'Acide urique(Homme)','Acide urique(Femme)
	'data16':[2, 20]
	}

	return render (request,'biochimie/bio.html',{'data':data,'service':'Plastique'})


def chir_Générale(request):
	data={

	#'Glucose', 'Urée', 'Créatinine', 'Sodium', 'Potasium', 'Magnésium'
	'data1':[0, 10, 5, 2, 20, 30],
	#'Aspect du sérum', 'Cholestérol total', 'Triglycérides', 'LDL Cholestérol'
	'data2':[0, 10, 5, 2],

	#Acide urique', 'Acide urique(enfant)', '
	'data3':[22,55],

	#'Calcium ionisé','Calcium total''
	'data4':[0, 10],
	#['Fer','Fer(Homme)','Fer(Femme)']
	'data5':[45,10, 5],
	#'HDL Cholestérol','HDL Cholestérol(Homme)','HDL Cholestérol(Femme)'
	'data6':[0, 10, 5],
	#'Protéines(plasma)','Protéines','Albumine','Amylase'
	'data7':[0, 10, 5, 2],
	#'GOT (ASAT)','GPT (ALAT)','Bilirubine total (ALAT)','Bilirubine directe','Bilirubine indirecte'
	'data8':[0, 10, 5, 2, 20],
	#'PAL AMP','PAL AMP(enfant)','PAL AMP(adulte)'
	'data9':[0, 10, 5],
	#'Microalbumine','Créatinine','Clairance de la créatinine','Sodium','Phosphore'
	'data10':[0, 10, 5, 2, 20],
	#y-gt(Homme)','y-gt(Femme)'
	'data11':[0, 10],
	#,'Lipase(calorimétrique)','LDH','Diurèse'
	'data12':[0, 10,5],
	#'Calcium total(Nrs)','Calcium total(Adulte)
	'data13':[0, 10],
	# 'GOT (ASAT)','GPT (ALAT)'
	'data14':[10, 5],
	#,'PAL DEA','PAL DEA(enfant)','PAL DEA(adulte)'
	'data15':[ 5, 2, 20],
	#'Acide urique(Homme)','Acide urique(Femme)
	'data16':[2, 20]
	}

	return render (request,'biochimie/bio.html',{'data':data,'service':'chir_Générale'})


def ChirM_Faciale(request):
	data={

	#'Glucose', 'Urée', 'Créatinine', 'Sodium', 'Potasium', 'Magnésium'
	'data1':[0, 10, 5, 2, 20, 30],
	#'Aspect du sérum', 'Cholestérol total', 'Triglycérides', 'LDL Cholestérol'
	'data2':[0, 10, 5, 2],

	#Acide urique', 'Acide urique(enfant)', '
	'data3':[22,55],

	#'Calcium ionisé','Calcium total''
	'data4':[0, 10],
	#['Fer','Fer(Homme)','Fer(Femme)']
	'data5':[45,10, 5],
	#'HDL Cholestérol','HDL Cholestérol(Homme)','HDL Cholestérol(Femme)'
	'data6':[0, 10, 5],
	#'Protéines(plasma)','Protéines','Albumine','Amylase'
	'data7':[0, 10, 5, 2],
	#'GOT (ASAT)','GPT (ALAT)','Bilirubine total (ALAT)','Bilirubine directe','Bilirubine indirecte'
	'data8':[0, 10, 5, 2, 20],
	#'PAL AMP','PAL AMP(enfant)','PAL AMP(adulte)'
	'data9':[0, 10, 5],
	#'Microalbumine','Créatinine','Clairance de la créatinine','Sodium','Phosphore'
	'data10':[0, 10, 5, 2, 20],
	#y-gt(Homme)','y-gt(Femme)'
	'data11':[0, 10],
	#,'Lipase(calorimétrique)','LDH','Diurèse'
	'data12':[0, 10,5],
	#'Calcium total(Nrs)','Calcium total(Adulte)
	'data13':[0, 10],
	# 'GOT (ASAT)','GPT (ALAT)'
	'data14':[10, 5],
	#,'PAL DEA','PAL DEA(enfant)','PAL DEA(adulte)'
	'data15':[ 5, 2, 20],
	#'Acide urique(Homme)','Acide urique(Femme)
	'data16':[2, 20]
	}

	return render (request,'biochimie/bio.html',{'data':data,'service':'ChirM_Faciale'})


def Réa_Méd(request):
	data={

	#'Glucose', 'Urée', 'Créatinine', 'Sodium', 'Potasium', 'Magnésium'
	'data1':[0, 10, 5, 2, 20, 30],
	#'Aspect du sérum', 'Cholestérol total', 'Triglycérides', 'LDL Cholestérol'
	'data2':[0, 10, 5, 2],

	#Acide urique', 'Acide urique(enfant)', '
	'data3':[22,55],

	#'Calcium ionisé','Calcium total''
	'data4':[0, 10],
	#['Fer','Fer(Homme)','Fer(Femme)']
	'data5':[45,10, 5],
	#'HDL Cholestérol','HDL Cholestérol(Homme)','HDL Cholestérol(Femme)'
	'data6':[0, 10, 5],
	#'Protéines(plasma)','Protéines','Albumine','Amylase'
	'data7':[0, 10, 5, 2],
	#'GOT (ASAT)','GPT (ALAT)','Bilirubine total (ALAT)','Bilirubine directe','Bilirubine indirecte'
	'data8':[0, 10, 5, 2, 20],
	#'PAL AMP','PAL AMP(enfant)','PAL AMP(adulte)'
	'data9':[0, 10, 5],
	#'Microalbumine','Créatinine','Clairance de la créatinine','Sodium','Phosphore'
	'data10':[0, 10, 5, 2, 20],
	#y-gt(Homme)','y-gt(Femme)'
	'data11':[0, 10],
	#,'Lipase(calorimétrique)','LDH','Diurèse'
	'data12':[0, 10,5],
	#'Calcium total(Nrs)','Calcium total(Adulte)
	'data13':[0, 10],
	# 'GOT (ASAT)','GPT (ALAT)'
	'data14':[10, 5],
	#,'PAL DEA','PAL DEA(enfant)','PAL DEA(adulte)'
	'data15':[ 5, 2, 20],
	#'Acide urique(Homme)','Acide urique(Femme)
	'data16':[2, 20]
	}

	return render (request,'biochimie/bio.html',{'data':data,'service':'Réa_Méd'})


def Méd_Interne(request):
	data={

	#'Glucose', 'Urée', 'Créatinine', 'Sodium', 'Potasium', 'Magnésium'
	'data1':[0, 10, 5, 2, 20, 30],
	#'Aspect du sérum', 'Cholestérol total', 'Triglycérides', 'LDL Cholestérol'
	'data2':[0, 10, 5, 2],

	#Acide urique', 'Acide urique(enfant)', '
	'data3':[22,55],

	#'Calcium ionisé','Calcium total''
	'data4':[0, 10],
	#['Fer','Fer(Homme)','Fer(Femme)']
	'data5':[45,10, 5],
	#'HDL Cholestérol','HDL Cholestérol(Homme)','HDL Cholestérol(Femme)'
	'data6':[0, 10, 5],
	#'Protéines(plasma)','Protéines','Albumine','Amylase'
	'data7':[0, 10, 5, 2],
	#'GOT (ASAT)','GPT (ALAT)','Bilirubine total (ALAT)','Bilirubine directe','Bilirubine indirecte'
	'data8':[0, 10, 5, 2, 20],
	#'PAL AMP','PAL AMP(enfant)','PAL AMP(adulte)'
	'data9':[0, 10, 5],
	#'Microalbumine','Créatinine','Clairance de la créatinine','Sodium','Phosphore'
	'data10':[0, 10, 5, 2, 20],
	#y-gt(Homme)','y-gt(Femme)'
	'data11':[0, 10],
	#,'Lipase(calorimétrique)','LDH','Diurèse'
	'data12':[0, 10,5],
	#'Calcium total(Nrs)','Calcium total(Adulte)
	'data13':[0, 10],
	# 'GOT (ASAT)','GPT (ALAT)'
	'data14':[10, 5],
	#,'PAL DEA','PAL DEA(enfant)','PAL DEA(adulte)'
	'data15':[ 5, 2, 20],
	#'Acide urique(Homme)','Acide urique(Femme)
	'data16':[2, 20]
	}

	return render (request,'biochimie/bio.html',{'data':data,'service':'Méd_Interne'})


def Réa_cov(request):
	data={

	#'Glucose', 'Urée', 'Créatinine', 'Sodium', 'Potasium', 'Magnésium'
	'data1':[0, 10, 5, 2, 20, 30],
	#'Aspect du sérum', 'Cholestérol total', 'Triglycérides', 'LDL Cholestérol'
	'data2':[0, 10, 5, 2],

	#Acide urique', 'Acide urique(enfant)', '
	'data3':[22,55],

	#'Calcium ionisé','Calcium total''
	'data4':[0, 10],
	#['Fer','Fer(Homme)','Fer(Femme)']
	'data5':[45,10, 5],
	#'HDL Cholestérol','HDL Cholestérol(Homme)','HDL Cholestérol(Femme)'
	'data6':[0, 10, 5],
	#'Protéines(plasma)','Protéines','Albumine','Amylase'
	'data7':[0, 10, 5, 2],
	#'GOT (ASAT)','GPT (ALAT)','Bilirubine total (ALAT)','Bilirubine directe','Bilirubine indirecte'
	'data8':[0, 10, 5, 2, 20],
	#'PAL AMP','PAL AMP(enfant)','PAL AMP(adulte)'
	'data9':[0, 10, 5],
	#'Microalbumine','Créatinine','Clairance de la créatinine','Sodium','Phosphore'
	'data10':[0, 10, 5, 2, 20],
	#y-gt(Homme)','y-gt(Femme)'
	'data11':[0, 10],
	#,'Lipase(calorimétrique)','LDH','Diurèse'
	'data12':[0, 10,5],
	#'Calcium total(Nrs)','Calcium total(Adulte)
	'data13':[0, 10],
	# 'GOT (ASAT)','GPT (ALAT)'
	'data14':[10, 5],
	#,'PAL DEA','PAL DEA(enfant)','PAL DEA(adulte)'
	'data15':[ 5, 2, 20],
	#'Acide urique(Homme)','Acide urique(Femme)
	'data16':[2, 20]
	}

	return render (request,'biochimie/bio.html',{'data':data,'service':'Réa_cov'})


def Néonat(request):
	data={

	#'Glucose', 'Urée', 'Créatinine', 'Sodium', 'Potasium', 'Magnésium'
	'data1':[0, 10, 5, 2, 20, 30],
	#'Aspect du sérum', 'Cholestérol total', 'Triglycérides', 'LDL Cholestérol'
	'data2':[0, 10, 5, 2],

	#Acide urique', 'Acide urique(enfant)', '
	'data3':[22,55],

	#'Calcium ionisé','Calcium total''
	'data4':[0, 10],
	#['Fer','Fer(Homme)','Fer(Femme)']
	'data5':[45,10, 5],
	#'HDL Cholestérol','HDL Cholestérol(Homme)','HDL Cholestérol(Femme)'
	'data6':[0, 10, 5],
	#'Protéines(plasma)','Protéines','Albumine','Amylase'
	'data7':[0, 10, 5, 2],
	#'GOT (ASAT)','GPT (ALAT)','Bilirubine total (ALAT)','Bilirubine directe','Bilirubine indirecte'
	'data8':[0, 10, 5, 2, 20],
	#'PAL AMP','PAL AMP(enfant)','PAL AMP(adulte)'
	'data9':[0, 10, 5],
	#'Microalbumine','Créatinine','Clairance de la créatinine','Sodium','Phosphore'
	'data10':[0, 10, 5, 2, 20],
	#y-gt(Homme)','y-gt(Femme)'
	'data11':[0, 10],
	#,'Lipase(calorimétrique)','LDH','Diurèse'
	'data12':[0, 10,5],
	#'Calcium total(Nrs)','Calcium total(Adulte)
	'data13':[0, 10],
	# 'GOT (ASAT)','GPT (ALAT)'
	'data14':[10, 5],
	#,'PAL DEA','PAL DEA(enfant)','PAL DEA(adulte)'
	'data15':[ 5, 2, 20],
	#'Acide urique(Homme)','Acide urique(Femme)
	'data16':[2, 20]
	}

	return render (request,'biochimie/bio.html',{'data':data,'service':'Néonat'})


def Pédiatrie(request):
	data={

	#'Glucose', 'Urée', 'Créatinine', 'Sodium', 'Potasium', 'Magnésium'
	'data1':[0, 10, 5, 2, 20, 30],
	#'Aspect du sérum', 'Cholestérol total', 'Triglycérides', 'LDL Cholestérol'
	'data2':[0, 10, 5, 2],

	#Acide urique', 'Acide urique(enfant)', '
	'data3':[22,55],

	#'Calcium ionisé','Calcium total''
	'data4':[0, 10],
	#['Fer','Fer(Homme)','Fer(Femme)']
	'data5':[45,10, 5],
	#'HDL Cholestérol','HDL Cholestérol(Homme)','HDL Cholestérol(Femme)'
	'data6':[0, 10, 5],
	#'Protéines(plasma)','Protéines','Albumine','Amylase'
	'data7':[0, 10, 5, 2],
	#'GOT (ASAT)','GPT (ALAT)','Bilirubine total (ALAT)','Bilirubine directe','Bilirubine indirecte'
	'data8':[0, 10, 5, 2, 20],
	#'PAL AMP','PAL AMP(enfant)','PAL AMP(adulte)'
	'data9':[0, 10, 5],
	#'Microalbumine','Créatinine','Clairance de la créatinine','Sodium','Phosphore'
	'data10':[0, 10, 5, 2, 20],
	#y-gt(Homme)','y-gt(Femme)'
	'data11':[0, 10],
	#,'Lipase(calorimétrique)','LDH','Diurèse'
	'data12':[0, 10,5],
	#'Calcium total(Nrs)','Calcium total(Adulte)
	'data13':[0, 10],
	# 'GOT (ASAT)','GPT (ALAT)'
	'data14':[10, 5],
	#,'PAL DEA','PAL DEA(enfant)','PAL DEA(adulte)'
	'data15':[ 5, 2, 20],
	#'Acide urique(Homme)','Acide urique(Femme)
	'data16':[2, 20]
	}

	return render (request,'biochimie/bio.html',{'data':data,'service':'Pédiatrie'})


def Maternié(request):
	data={

	#'Glucose', 'Urée', 'Créatinine', 'Sodium', 'Potasium', 'Magnésium'
	'data1':[0, 10, 5, 2, 20, 30],
	#'Aspect du sérum', 'Cholestérol total', 'Triglycérides', 'LDL Cholestérol'
	'data2':[0, 10, 5, 2],

	#Acide urique', 'Acide urique(enfant)', '
	'data3':[22,55],

	#'Calcium ionisé','Calcium total''
	'data4':[0, 10],
	#['Fer','Fer(Homme)','Fer(Femme)']
	'data5':[45,10, 5],
	#'HDL Cholestérol','HDL Cholestérol(Homme)','HDL Cholestérol(Femme)'
	'data6':[0, 10, 5],
	#'Protéines(plasma)','Protéines','Albumine','Amylase'
	'data7':[0, 10, 5, 2],
	#'GOT (ASAT)','GPT (ALAT)','Bilirubine total (ALAT)','Bilirubine directe','Bilirubine indirecte'
	'data8':[0, 10, 5, 2, 20],
	#'PAL AMP','PAL AMP(enfant)','PAL AMP(adulte)'
	'data9':[0, 10, 5],
	#'Microalbumine','Créatinine','Clairance de la créatinine','Sodium','Phosphore'
	'data10':[0, 10, 5, 2, 20],
	#y-gt(Homme)','y-gt(Femme)'
	'data11':[0, 10],
	#,'Lipase(calorimétrique)','LDH','Diurèse'
	'data12':[0, 10,5],
	#'Calcium total(Nrs)','Calcium total(Adulte)
	'data13':[0, 10],
	# 'GOT (ASAT)','GPT (ALAT)'
	'data14':[10, 5],
	#,'PAL DEA','PAL DEA(enfant)','PAL DEA(adulte)'
	'data15':[ 5, 2, 20],
	#'Acide urique(Homme)','Acide urique(Femme)
	'data16':[2, 20]
	}

	return render (request,'biochimie/bio.html',{'data':data,'service':'Maternié'})


def PU_T(request):
	data={

	#'Glucose', 'Urée', 'Créatinine', 'Sodium', 'Potasium', 'Magnésium'
	'data1':[0, 10, 5, 2, 20, 30],
	#'Aspect du sérum', 'Cholestérol total', 'Triglycérides', 'LDL Cholestérol'
	'data2':[0, 10, 5, 2],

	#Acide urique', 'Acide urique(enfant)', '
	'data3':[22,55],

	#'Calcium ionisé','Calcium total''
	'data4':[0, 10],
	#['Fer','Fer(Homme)','Fer(Femme)']
	'data5':[45,10, 5],
	#'HDL Cholestérol','HDL Cholestérol(Homme)','HDL Cholestérol(Femme)'
	'data6':[0, 10, 5],
	#'Protéines(plasma)','Protéines','Albumine','Amylase'
	'data7':[0, 10, 5, 2],
	#'GOT (ASAT)','GPT (ALAT)','Bilirubine total (ALAT)','Bilirubine directe','Bilirubine indirecte'
	'data8':[0, 10, 5, 2, 20],
	#'PAL AMP','PAL AMP(enfant)','PAL AMP(adulte)'
	'data9':[0, 10, 5],
	#'Microalbumine','Créatinine','Clairance de la créatinine','Sodium','Phosphore'
	'data10':[0, 10, 5, 2, 20],
	#y-gt(Homme)','y-gt(Femme)'
	'data11':[0, 10],
	#,'Lipase(calorimétrique)','LDH','Diurèse'
	'data12':[0, 10,5],
	#'Calcium total(Nrs)','Calcium total(Adulte)
	'data13':[0, 10],
	# 'GOT (ASAT)','GPT (ALAT)'
	'data14':[10, 5],
	#,'PAL DEA','PAL DEA(enfant)','PAL DEA(adulte)'
	'data15':[ 5, 2, 20],
	#'Acide urique(Homme)','Acide urique(Femme)
	'data16':[2, 20]
	}

	return render (request,'biochimie/bio.html',{'data':data,'service':'PU_T'})


def MTV(request):
	data={

	#'Glucose', 'Urée', 'Créatinine', 'Sodium', 'Potasium', 'Magnésium'
	'data1':[0, 10, 5, 2, 20, 30],
	#'Aspect du sérum', 'Cholestérol total', 'Triglycérides', 'LDL Cholestérol'
	'data2':[0, 10, 5, 2],

	#Acide urique', 'Acide urique(enfant)', '
	'data3':[22,55],

	#'Calcium ionisé','Calcium total''
	'data4':[0, 10],
	#['Fer','Fer(Homme)','Fer(Femme)']
	'data5':[45,10, 5],
	#'HDL Cholestérol','HDL Cholestérol(Homme)','HDL Cholestérol(Femme)'
	'data6':[0, 10, 5],
	#'Protéines(plasma)','Protéines','Albumine','Amylase'
	'data7':[0, 10, 5, 2],
	#'GOT (ASAT)','GPT (ALAT)','Bilirubine total (ALAT)','Bilirubine directe','Bilirubine indirecte'
	'data8':[0, 10, 5, 2, 20],
	#'PAL AMP','PAL AMP(enfant)','PAL AMP(adulte)'
	'data9':[0, 10, 5],
	#'Microalbumine','Créatinine','Clairance de la créatinine','Sodium','Phosphore'
	'data10':[0, 10, 5, 2, 20],
	#y-gt(Homme)','y-gt(Femme)'
	'data11':[0, 10],
	#,'Lipase(calorimétrique)','LDH','Diurèse'
	'data12':[0, 10,5],
	#'Calcium total(Nrs)','Calcium total(Adulte)
	'data13':[0, 10],
	# 'GOT (ASAT)','GPT (ALAT)'
	'data14':[10, 5],
	#,'PAL DEA','PAL DEA(enfant)','PAL DEA(adulte)'
	'data15':[ 5, 2, 20],
	#'Acide urique(Homme)','Acide urique(Femme)
	'data16':[2, 20]
	}

	return render (request,'biochimie/bio.html',{'data':data,'service':'MTV'})


def PUM_COV(request):
	data={

	#'Glucose', 'Urée', 'Créatinine', 'Sodium', 'Potasium', 'Magnésium'
	'data1':[0, 10, 5, 2, 20, 30],
	#'Aspect du sérum', 'Cholestérol total', 'Triglycérides', 'LDL Cholestérol'
	'data2':[0, 10, 5, 2],

	#Acide urique', 'Acide urique(enfant)', '
	'data3':[22,55],

	#'Calcium ionisé','Calcium total''
	'data4':[0, 10],
	#['Fer','Fer(Homme)','Fer(Femme)']
	'data5':[45,10, 5],
	#'HDL Cholestérol','HDL Cholestérol(Homme)','HDL Cholestérol(Femme)'
	'data6':[0, 10, 5],
	#'Protéines(plasma)','Protéines','Albumine','Amylase'
	'data7':[0, 10, 5, 2],
	#'GOT (ASAT)','GPT (ALAT)','Bilirubine total (ALAT)','Bilirubine directe','Bilirubine indirecte'
	'data8':[0, 10, 5, 2, 20],
	#'PAL AMP','PAL AMP(enfant)','PAL AMP(adulte)'
	'data9':[0, 10, 5],
	#'Microalbumine','Créatinine','Clairance de la créatinine','Sodium','Phosphore'
	'data10':[0, 10, 5, 2, 20],
	#y-gt(Homme)','y-gt(Femme)'
	'data11':[0, 10],
	#,'Lipase(calorimétrique)','LDH','Diurèse'
	'data12':[0, 10,5],
	#'Calcium total(Nrs)','Calcium total(Adulte)
	'data13':[0, 10],
	# 'GOT (ASAT)','GPT (ALAT)'
	'data14':[10, 5],
	#,'PAL DEA','PAL DEA(enfant)','PAL DEA(adulte)'
	'data15':[ 5, 2, 20],
	#'Acide urique(Homme)','Acide urique(Femme)
	'data16':[2, 20]
	}

	return render (request,'biochimie/bio.html',{'data':data,'service':'PUM_COV'})


def Puchir_cov(request):
	data={

	#'Glucose', 'Urée', 'Créatinine', 'Sodium', 'Potasium', 'Magnésium'
	'data1':[0, 10, 5, 2, 20, 30],
	#'Aspect du sérum', 'Cholestérol total', 'Triglycérides', 'LDL Cholestérol'
	'data2':[0, 10, 5, 2],

	#Acide urique', 'Acide urique(enfant)', '
	'data3':[22,55],

	#'Calcium ionisé','Calcium total''
	'data4':[0, 10],
	#['Fer','Fer(Homme)','Fer(Femme)']
	'data5':[45,10, 5],
	#'HDL Cholestérol','HDL Cholestérol(Homme)','HDL Cholestérol(Femme)'
	'data6':[0, 10, 5],
	#'Protéines(plasma)','Protéines','Albumine','Amylase'
	'data7':[0, 10, 5, 2],
	#'GOT (ASAT)','GPT (ALAT)','Bilirubine total (ALAT)','Bilirubine directe','Bilirubine indirecte'
	'data8':[0, 10, 5, 2, 20],
	#'PAL AMP','PAL AMP(enfant)','PAL AMP(adulte)'
	'data9':[0, 10, 5],
	#'Microalbumine','Créatinine','Clairance de la créatinine','Sodium','Phosphore'
	'data10':[0, 10, 5, 2, 20],
	#y-gt(Homme)','y-gt(Femme)'
	'data11':[0, 10],
	#,'Lipase(calorimétrique)','LDH','Diurèse'
	'data12':[0, 10,5],
	#'Calcium total(Nrs)','Calcium total(Adulte)
	'data13':[0, 10],
	# 'GOT (ASAT)','GPT (ALAT)'
	'data14':[10, 5],
	#,'PAL DEA','PAL DEA(enfant)','PAL DEA(adulte)'
	'data15':[ 5, 2, 20],
	#'Acide urique(Homme)','Acide urique(Femme)
	'data16':[2, 20]
	}

	return render (request,'biochimie/bio.html',{'data':data,'service':'Puchir_cov'})


def PU_Chir(request):
	data={

	#'Glucose', 'Urée', 'Créatinine', 'Sodium', 'Potasium', 'Magnésium'
	'data1':[0, 10, 5, 2, 20, 30],
	#'Aspect du sérum', 'Cholestérol total', 'Triglycérides', 'LDL Cholestérol'
	'data2':[0, 10, 5, 2],

	#Acide urique', 'Acide urique(enfant)', '
	'data3':[22,55],

	#'Calcium ionisé','Calcium total''
	'data4':[0, 10],
	#['Fer','Fer(Homme)','Fer(Femme)']
	'data5':[45,10, 5],
	#'HDL Cholestérol','HDL Cholestérol(Homme)','HDL Cholestérol(Femme)'
	'data6':[0, 10, 5],
	#'Protéines(plasma)','Protéines','Albumine','Amylase'
	'data7':[0, 10, 5, 2],
	#'GOT (ASAT)','GPT (ALAT)','Bilirubine total (ALAT)','Bilirubine directe','Bilirubine indirecte'
	'data8':[0, 10, 5, 2, 20],
	#'PAL AMP','PAL AMP(enfant)','PAL AMP(adulte)'
	'data9':[0, 10, 5],
	#'Microalbumine','Créatinine','Clairance de la créatinine','Sodium','Phosphore'
	'data10':[0, 10, 5, 2, 20],
	#y-gt(Homme)','y-gt(Femme)'
	'data11':[0, 10],
	#,'Lipase(calorimétrique)','LDH','Diurèse'
	'data12':[0, 10,5],
	#'Calcium total(Nrs)','Calcium total(Adulte)
	'data13':[0, 10],
	# 'GOT (ASAT)','GPT (ALAT)'
	'data14':[10, 5],
	#,'PAL DEA','PAL DEA(enfant)','PAL DEA(adulte)'
	'data15':[ 5, 2, 20],
	#'Acide urique(Homme)','Acide urique(Femme)
	'data16':[2, 20]
	}

	return render (request,'biochimie/bio.html',{'data':data,'service':'PU_Chir'})


def PU_MI(request):
	data={

	#'Glucose', 'Urée', 'Créatinine', 'Sodium', 'Potasium', 'Magnésium'
	'data1':[0, 10, 5, 2, 20, 30],
	#'Aspect du sérum', 'Cholestérol total', 'Triglycérides', 'LDL Cholestérol'
	'data2':[0, 10, 5, 2],

	#Acide urique', 'Acide urique(enfant)', '
	'data3':[22,55],

	#'Calcium ionisé','Calcium total''
	'data4':[0, 10],
	#['Fer','Fer(Homme)','Fer(Femme)']
	'data5':[45,10, 5],
	#'HDL Cholestérol','HDL Cholestérol(Homme)','HDL Cholestérol(Femme)'
	'data6':[0, 10, 5],
	#'Protéines(plasma)','Protéines','Albumine','Amylase'
	'data7':[0, 10, 5, 2],
	#'GOT (ASAT)','GPT (ALAT)','Bilirubine total (ALAT)','Bilirubine directe','Bilirubine indirecte'
	'data8':[0, 10, 5, 2, 20],
	#'PAL AMP','PAL AMP(enfant)','PAL AMP(adulte)'
	'data9':[0, 10, 5],
	#'Microalbumine','Créatinine','Clairance de la créatinine','Sodium','Phosphore'
	'data10':[0, 10, 5, 2, 20],
	#y-gt(Homme)','y-gt(Femme)'
	'data11':[0, 10],
	#,'Lipase(calorimétrique)','LDH','Diurèse'
	'data12':[0, 10,5],
	#'Calcium total(Nrs)','Calcium total(Adulte)
	'data13':[0, 10],
	# 'GOT (ASAT)','GPT (ALAT)'
	'data14':[10, 5],
	#,'PAL DEA','PAL DEA(enfant)','PAL DEA(adulte)'
	'data15':[ 5, 2, 20],
	#'Acide urique(Homme)','Acide urique(Femme)
	'data16':[2, 20]
	}

	return render (request,'biochimie/bio.html',{'data':data,'service':'PU_MI'})
