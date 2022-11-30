# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 01:18:33 2022

@author: Edwin Guzman
"""

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time
import json


#definiendo archivo json a utilizar 
f = open('C:/Users/PC/Documents/Automate_Testing_Appium/credenciales.json')  
# lectura del archivo con las credenciales
credenciales = json.load(f)
  
# Closing file
f.close()


driver={
  "platformName": "Android",
  "platformVersion": "11.0",
  "deviceName": "joyuse",
  "automationName": "uiautomator2",
  "appPackage": "com.farmaciasannicolas.controlrecetas",
  "appActivity": ".MainActivity"
}

elements_app={
                "icon_carrito": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[6]/android.view.ViewGroup[3]/android.widget.TextView[1]',
                "btn_iniciar_sesion": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.TextView' }

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', driver)
time.sleep(5)
#ir a iniciar sesion
ele_xapth = driver.find_element(AppiumBy.XPATH,elements_app["icon_carrito"])
ele_xapth.click()
time.sleep(2)
edit_text_inputs=driver.find_elements(AppiumBy.CLASS_NAME,'android.widget.EditText')
#ingresar credenciales
edit_text_inputs[0].send_keys(credenciales["user"])
edit_text_inputs[1].send_keys(credenciales["password"])
btn_ingresar=driver.find_element(AppiumBy.XPATH,elements_app["btn_iniciar_sesion"]).click()

#codigo para iniciar la prue
