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
credenciales_file = open('credenciales.json')  
# lectura del archivo con las credenciales
credenciales = json.load(credenciales_file)

def setUp():      
    #importando las configuraciones del driver
    capabilities_configuraiton_file= open('capabilities_configuration.json')  
    # lectura del archivo con las credenciales
    driver = json.load(capabilities_configuraiton_file)
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', driver)
    return driver

def iniciarSesion(driver):
    
    elements_app={
                    "icon_carrito": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[6]/android.view.ViewGroup[3]/android.widget.TextView[1]',
                    "btn_iniciar_sesion": '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.TextView' }
    time.sleep(5)
    #ir a iniciar sesion
    icon_carrito = driver.find_element(AppiumBy.XPATH,elements_app["icon_carrito"])
    icon_carrito.click()
    time.sleep(2)
    inputs=driver.find_elements(AppiumBy.CLASS_NAME,'android.widget.EditText')
    user_input=inputs[0]
    password_input=inputs[1]
    #ingresar credenciales
    user_input.send_keys(credenciales["user"])
    password_input.send_keys(credenciales["password"])
    btn_ingresar=driver.find_element(AppiumBy.XPATH,elements_app["btn_iniciar_sesion"])
    btn_ingresar.click()
    print("Sesion Iniciada con exito...")


if __name__ == '__main__':
    #inicializando driver con las configuraciones correspondientes
    driver=setUp()
    try:
        #iniciar Sesion para entrar en pantallas con permisos
        iniciarSesion(driver)
    except Exception as e: 
        print("Ha ocurrido una excepcion al iniciar Sesion... " +e)
        
