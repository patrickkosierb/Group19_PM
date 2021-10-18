# @ file: mode.py
# @ brief: mode file contains all mode classes (AOO AAI VOO VII)
# @ note: missing file io stuff and logout button

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QWidget, QStackedWidget	
import sys
import sqlite3
import os
import string


import config
import menu

# ATRIAL

class aoo_mode(QDialog):
	def __init__(self):
		# get param list from_serial(param)
		# param = [150 100 200]
		super(aoo_mode, self).__init__()
		loadUi("interface/aoo_mode.ui", self)
		self.current_param()
		self.aai.clicked.connect(self.go_to_aai)
		self.voo.clicked.connect(self.go_to_voo)
		self.vvi.clicked.connect(self.go_to_vvi)
		self.Back.clicked.connect(self.go_to_menu)
		self.ApplyChanges.clicked.connect(self.update_param)
		self.ResetChanges.clicked.connect(self.reset_param) #current_param
		self.update_pm.clicked.connect(self.send_to_pm)

	def go_to_aai(self): 
		aai = aai_mode()
		config.widget.addWidget(aai)
		config.widget.setCurrentIndex(config.widget.currentIndex()+1)	

	def go_to_voo(self): 
		voo = voo_mode()
		config.widget.addWidget(voo)
		config.widget.setCurrentIndex(config.widget.currentIndex()+1)	

	def go_to_vvi(self): 
		vvi = vvi_mode()
		config.widget.addWidget(vvi)
		config.widget.setCurrentIndex(config.widget.currentIndex()+1)	


	def go_to_menu(self): 
		menu_var = menu.main_menu()
		config.widget.addWidget(menu_var)
		config.widget.setCurrentIndex(config.widget.currentIndex()+1)

	# uses file io functions to take CURRENT parameters TAKEN FROM PACEMAKER and load them into the text boxes
	def current_param(self):
		param = ['150', '200', '100']
		self.LRL_Current.setText(param[0]) #since the variables are directly from a txt file we dont need to convert int -> str
		self.URL_Current.setText(param[1])
		self.AA_Current.setText(param[2])
	
	# update the current parameters, apply changes is only for ui, send to pacemaker will actually update pacemaker
	def update_param(self):

		LRL = self.LRL.text()
		if(LRL.isdigit() and int(LRL)<255):
			self.LRL_Current.setText(LRL)
			self.INVALID.setText("")
		elif(LRL == ""):
			self.INVALID.setText("")
		else:
			self.INVALID.setText("Invalid*")

		URL = self.URL.text()
		if(URL.isdigit() and int(URL)<255):
			self.URL_Current.setText(URL)
			self.INVALID_2.setText("")
		elif(URL == ""):
			self.INVALID_2.setText("")
		else:
			self.INVALID_2.setText("Invalid*")

		AA = self.AA.text()
		if(AA.isdigit() and int(AA)<255):
			self.AA_Current.setText(AA)
			self.INVALID_3.setText("")
		elif(AA == ""):
			self.INVALID_3.setText("")		
		else:
			self.INVALID_3.setText("Invalid*")

		APW = self.APW.text()
		if(APW.isdigit() and int(APW)<255):
			self.APW_Current.setText(APW)
			self.INVALID_4.setText("")
		elif(APW == ""):
			self.INVALID_4.setText("")		
		else:
			self.INVALID_4.setText("Invalid*")

	def reset_param(self):
		#access text file again
		param = ['150', '200', '100']
		self.LRL_Current.setText(param[0]) 
		self.URL_Current.setText(param[1])
		self.AA_Current.setText(param[2])

	#take current and update text file
	def send_to_pm(self):
		if(self.checkBox.isChecked()):
			self.checkBox.setChecked(False)
			self.INVALID_5.setText("")
			param = ['150', '200', '100'] 
			param[0] = self.LRL_Current.text()
			param[1] = self.URL_Current.text()
			param[2] = self.AA_Current.text()
			print(param)
		else:
			self.INVALID_5.setText("*Please confirm changes")

class aai_mode(QDialog):
	def __init__(self):
		super(aai_mode, self).__init__()
		loadUi("interface/aai_mode.ui", self)
		self.current_param()
		self.aoo.clicked.connect(self.go_to_aoo)
		self.voo.clicked.connect(self.go_to_voo)
		self.vvi.clicked.connect(self.go_to_vvi)
		self.Back.clicked.connect(self.go_to_menu)
		self.ApplyChanges.clicked.connect(self.update_param)
		self.ResetChanges.clicked.connect(self.reset_param)
		self.update_pm.clicked.connect(self.send_to_pm)

	def go_to_aoo(self): 
		aoo = aoo_mode()
		config.widget.addWidget(aoo)
		config.widget.setCurrentIndex(config.widget.currentIndex()+1)	

	def go_to_voo(self): 
		voo = voo_mode()
		config.widget.addWidget(voo)
		config.widget.setCurrentIndex(config.widget.currentIndex()+1)	

	def go_to_vvi(self): 
		vvi = vvi_mode()
		config.widget.addWidget(vvi)
		config.widget.setCurrentIndex(config.widget.currentIndex()+1)	

	def go_to_menu(self): 
		menu_var = menu.main_menu()
		config.widget.addWidget(menu_var)
		config.widget.setCurrentIndex(config.widget.currentIndex()+1)


	def current_param(self):
		param = ['150', '200', '100']
		self.LRL_Current.setText(param[0]) 
		self.URL_Current.setText(param[1])
		self.AA_Current.setText(param[2])
	
	def update_param(self):

		LRL = self.LRL.text()
		if(LRL.isdigit() and int(LRL)<255):
			self.LRL_Current.setText(LRL)
			self.INVALID.setText("")
		elif(LRL == ""):
			self.INVALID.setText("")
		else:
			self.INVALID.setText("Invalid*")

		URL = self.URL.text()
		if(URL.isdigit() and int(URL)<255):
			self.URL_Current.setText(URL)
			self.INVALID_2.setText("")
		elif(URL == ""):
			self.INVALID_2.setText("")
		else:
			self.INVALID_2.setText("Invalid*")

		AA = self.AA.text()
		if(AA.isdigit() and int(AA)<255):
			self.AA_Current.setText(AA)
			self.INVALID_3.setText("")
		elif(AA == ""):
			self.INVALID_3.setText("")		
		else:
			self.INVALID_3.setText("Invalid*")

		APW = self.APW.text()
		if(APW.isdigit() and int(APW)<255):
			self.APW_Current.setText(APW)
			self.INVALID_4.setText("")
		elif(APW == ""):
			self.INVALID_4.setText("")		
		else:
			self.INVALID_4.setText("Invalid*")

		AS = self.AS.text()
		if(AS.isdigit() and int(AS)<255):
			self.AS_Current.setText(AS)
			self.INVALID_5.setText("")
		elif(AS == ""):
			self.INVALID_5.setText("")		
		else:
			self.INVALID_5.setText("Invalid*")

		ARP = self.ARP.text()
		if(ARP.isdigit() and int(ARP)<255):
			self.ARP_Current.setText(ARP)
			self.INVALID_6.setText("")
		elif(ARP == ""):
			self.INVALID_6.setText("")		
		else:
			self.INVALID_6.setText("Invalid*")

		PVARP = self.PVARP.text()
		if(PVARP.isdigit() and int(PVARP)<255):
			self.PVARP_Current.setText(PVARP)
			self.INVALID_7.setText("")
		elif(PVARP == ""):
			self.INVALID_7.setText("")		
		else:
			self.INVALID_7.setText("Invalid*")

	def reset_param(self):
		param = ['150', '200', '100']
		self.LRL_Current.setText(param[0])
		self.URL_Current.setText(param[1])
		self.AA_Current.setText(param[2])

	def send_to_pm(self):
		if(self.checkBox.isChecked()):
			self.checkBox.setChecked(False)
			self.INVALID_8.setText("")
			param = ['150', '200', '100'] 
			param[0] = self.LRL_Current.text()
			param[1] = self.URL_Current.text()
			param[2] = self.AA_Current.text()
			print(param)
		else:
			self.INVALID_8.setText("*Please confirm changes")


# VENTRICLE 

class voo_mode(QDialog):
	def __init__(self):
		super(voo_mode, self).__init__()
		loadUi("interface/voo_mode.ui", self)
		self.current_param()
		self.aoo.clicked.connect(self.go_to_aoo)
		self.aai.clicked.connect(self.go_to_aai)
		self.vvi.clicked.connect(self.go_to_vvi)
		self.Back.clicked.connect(self.go_to_menu)
		self.ApplyChanges.clicked.connect(self.update_param)
		self.ResetChanges.clicked.connect(self.reset_param)
		self.update_pm.clicked.connect(self.send_to_pm)

	def go_to_aoo(self): 
		aoo = aoo_mode()
		config.widget.addWidget(aoo)
		config.widget.setCurrentIndex(config.widget.currentIndex()+1)	

	def go_to_aai(self): 
		aai = aai_mode()
		config.widget.addWidget(aai)
		config.widget.setCurrentIndex(config.widget.currentIndex()+1)	

	def go_to_vvi(self): 
		vvi = vvi_mode()
		config.widget.addWidget(vvi)
		config.widget.setCurrentIndex(config.widget.currentIndex()+1)	

	def go_to_menu(self): 
		menu_var = menu.main_menu()
		config.widget.addWidget(menu_var)
		config.widget.setCurrentIndex(config.widget.currentIndex()+1)
	
	def current_param(self):
		param = ['150', '200', '100']
		self.LRL_Current.setText(param[0]) 
		self.URL_Current.setText(param[1])
		self.VV_Current.setText(param[2])
	
	def update_param(self):

		LRL = self.LRL.text()
		if(LRL.isdigit() and int(LRL)<255):
			self.LRL_Current.setText(LRL)
			self.INVALID.setText("")
		elif(LRL == ""):
			self.INVALID.setText("")
		else:
			self.INVALID.setText("Invalid*")

		URL = self.URL.text()
		if(URL.isdigit() and int(URL)<255):
			self.URL_Current.setText(URL)
			self.INVALID_2.setText("")
		elif(URL == ""):
			self.INVALID_2.setText("")
		else:
			self.INVALID_2.setText("Invalid*")

		VV = self.VV.text()
		if(VV.isdigit() and int(VV)<255):
			self.VV_Current.setText(VV)
			self.INVALID_3.setText("")
		elif(VV == ""):
			self.INVALID_3.setText("")		
		else:
			self.INVALID_3.setText("Invalid*")

		VPW = self.VPW.text()
		if(VPW.isdigit() and int(VPW)<255):
			self.VPW_Current.setText(VPW)
			self.INVALID_4.setText("")
		elif(VPW == ""):
			self.INVALID_4.setText("")		
		else:
			self.INVALID_4.setText("Invalid*")

	def reset_param(self):
		#access text file again
		param = ['150', '200', '100']
		self.LRL_Current.setText(param[0]) 
		self.URL_Current.setText(param[1])
		self.VV_Current.setText(param[2])

	def send_to_pm(self):
		if(self.checkBox.isChecked()):
			self.checkBox.setChecked(False)
			self.INVALID_5.setText("")
			param = ['150', '200', '100'] 
			param[0] = self.LRL_Current.text()
			param[1] = self.URL_Current.text()
			param[2] = self.VV_Current.text()
			print(param)
		else:
			self.INVALID_5.setText("*Please confirm changes")

class vvi_mode(QDialog):
	def __init__(self):
		super(vvi_mode, self).__init__()
		loadUi("interface/vvi_mode.ui", self)
		self.current_param()
		self.aoo.clicked.connect(self.go_to_aoo)
		self.aai.clicked.connect(self.go_to_aai)
		self.voo.clicked.connect(self.go_to_voo)
		self.Back.clicked.connect(self.go_to_menu)
		self.ApplyChanges.clicked.connect(self.update_param)
		self.ResetChanges.clicked.connect(self.reset_param)
		self.update_pm.clicked.connect(self.send_to_pm)

	def go_to_aoo(self): 
		aoo = aoo_mode()
		config.widget.addWidget(aoo)
		config.widget.setCurrentIndex(config.widget.currentIndex()+1)	

	def go_to_aai(self): 
		aai = aai_mode()
		config.widget.addWidget(aai)
		config.widget.setCurrentIndex(config.widget.currentIndex()+1)	

	def go_to_voo(self): 
		voo = voo_mode()
		config.widget.addWidget(voo)
		config.widget.setCurrentIndex(config.widget.currentIndex()+1)	

	def go_to_menu(self): 
		menu_var = menu.main_menu()
		config.widget.addWidget(menu_var)
		config.widget.setCurrentIndex(config.widget.currentIndex()+1)

	def current_param(self):
		param = ['150', '200', '100']
		self.LRL_Current.setText(param[0]) 
		self.URL_Current.setText(param[1])
		self.VV_Current.setText(param[2])

	def update_param(self):

		LRL = self.LRL.text()
		if(LRL.isdigit() and int(LRL)<255):
			self.LRL_Current.setText(LRL)
			self.INVALID.setText("")
		elif(LRL == ""):
			self.INVALID.setText("")
		else:
			self.INVALID.setText("Invalid*")

		URL = self.URL.text()
		if(URL.isdigit() and int(URL)<255):
			self.URL_Current.setText(URL)
			self.INVALID_2.setText("")
		elif(URL == ""):
			self.INVALID_2.setText("")
		else:
			self.INVALID_2.setText("Invalid*")

		VV = self.VV.text()
		if(VV.isdigit() and int(VV)<255):
			self.VV_Current.setText(VV)
			self.INVALID_3.setText("")
		elif(VV == ""):
			self.INVALID_3.setText("")		
		else:
			self.INVALID_3.setText("Invalid*")

		VPW = self.VPW.text()
		if(VPW.isdigit() and int(VPW)<255):
			self.VPW_Current.setText(VPW)
			self.INVALID_4.setText("")
		elif(VPW == ""):
			self.INVALID_4.setText("")		
		else:
			self.INVALID_4.setText("Invalid*")

		VS = self.VS.text()
		if(VS.isdigit() and int(VS)<255):
			self.VS_Current.setText(VS)
			self.INVALID_5.setText("")
		elif(VS == ""):
			self.INVALID_5.setText("")		
		else:
			self.INVALID_5.setText("Invalid*")

		VRP = self.VRP.text()
		if(VRP.isdigit() and int(VRP)<255):
			self.VRP_Current.setText(VRP)
			self.INVALID_6.setText("")
		elif(VRP == ""):
			self.INVALID_6.setText("")		
		else:
			self.INVALID_6.setText("Invalid*")

		PVARP = self.PVARP.text()
		if(PVARP.isdigit() and int(PVARP)<255):
			self.PVARP_Current.setText(PVARP)
			self.INVALID_7.setText("")
		elif(PVARP == ""):
			self.INVALID_7.setText("")		
		else:
			self.INVALID_7.setText("Invalid*")

	def reset_param(self):
		param = ['150', '200', '100']
		self.LRL_Current.setText(param[0])
		self.URL_Current.setText(param[1])
		self.VV_Current.setText(param[2])

	def send_to_pm(self):
		if(self.checkBox.isChecked()):
			self.checkBox.setChecked(False)
			self.INVALID_8.setText("")
			param = ['150', '200', '100'] 
			param[0] = self.LRL_Current.text()
			param[1] = self.URL_Current.text()
			param[2] = self.VV_Current.text()
			print(param)
		else:
			self.INVALID_8.setText("*Please confirm changes")