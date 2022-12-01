# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 01:18:33 2022

@author: Edwin Guzman
"""

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import time
import json

#definiendo archivo json a utilizar 
credenciales_file = open('credenciales.json')  
# lectura del archivo con las credenciales
credenciales = json.load(credenciales_file)

#definiendo los elementos dentro de la aplicacion
application_elements_file = open('application_elements.json')  
elements = json.load(application_elements_file)

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
    try:
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
        
    except Exception as e: 
        print("Ha ocurrido una excepcion al iniciar Sesion... " +e)    
    
def agregarProductosAlCarrito(driver):
    
    xpath=elements["productos_por_categoria"]["categorias_productos"]["MEDICAMENTOS"]["xpath"]
    #valores de prueba a ser agregados
    ANESTESICOS=[['ANA-DENT ULTRA FORTE X 25 BLISTER DE 4 TABLETAS',2],
                ['ANESTENKA X 12 TUBOS',5],
                ['CERILUB GOTAS OTICAS 30ML',3]]
    try:
        #time.sleep(4)
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,elements["hamburger_options"])))
        menu = driver.find_element(AppiumBy.XPATH,elements["hamburger_options"])
        menu.click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,elements["productos_por_categoria"]["xpath"])))
        driver.find_element(AppiumBy.XPATH,elements["productos_por_categoria"]["xpath"]).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,elements["productos_por_categoria"]["categorias_productos"]["MEDICAMENTOS"]["xpath"])))
        driver.find_element(AppiumBy.XPATH,elements["productos_por_categoria"]["categorias_productos"]["MEDICAMENTOS"]["xpath"]).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,elements["productos_por_categoria"]["categorias_productos"]["MEDICAMENTOS"]["medicamentos"]["DOLOR Y FIEBRE"]["xpath"])))
        driver.find_element(AppiumBy.XPATH,elements["productos_por_categoria"]["categorias_productos"]["MEDICAMENTOS"]["medicamentos"]["DOLOR Y FIEBRE"]["xpath"]).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,elements["productos_por_categoria"]["categorias_productos"]["MEDICAMENTOS"]["medicamentos"]["DOLOR Y FIEBRE"]["medicamentos_por_categoria"]["ANESTESICOS"])))
        driver.find_element(AppiumBy.XPATH,elements["productos_por_categoria"]["categorias_productos"]["MEDICAMENTOS"]["medicamentos"]["DOLOR Y FIEBRE"]["medicamentos_por_categoria"]["ANESTESICOS"]).click()
        time.sleep(2)
        #escogemos los productos a agregar
        for i in ANESTESICOS:
            #buscamos el elemento por nombre y lo agregamos con la cantidad definida
            xpath_producto='//android.widget.TextView[@text="{}"]'.format(i[0])
            driver.find_element(AppiumBy.XPATH,xpath_producto).click()
            WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,elements["carrito_btn_mas"])))
            for x in range(1,i[1]):
                driver.find_element(AppiumBy.XPATH,elements["carrito_btn_mas"]).click()
                time.sleep(0.5)
            #agregar al carrito
            driver.find_element(AppiumBy.XPATH,elements["icon_carrito"]).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,elements["btn_ver_carrito_productos_list"])))
        #finalizado el ingreso consultamos el carrito 
        driver.find_element(AppiumBy.XPATH,elements["btn_ver_carrito_productos_list"]).click()
        time.sleep(15)
        print("Visualizando elementos del carrito")
        driver.find_element(AppiumBy.XPATH,elements["VACIAR CARRITO"]).click()
        print("Productos agregados al carrito correctamente...")
        
    except Exception as e: 
        print("Ha ocurrido una excepcion al agregar productos al carrito... " +e)    

    return 0

def verificarProductosAgregadosAlCarrito(driver):
    return 0

def eliminarProductoDelCarrito(driver):
    return 0

def modificarCantidadProductosItem(driver):
    return 0

def vaciarCarrito(driver):
    return 0

def realizarCompraUsandoCarrito(driver):
    return 0

def comprobandoPedidoRealizado(driver):
    return 0

if __name__ == '__main__':
    #inicializando driver con las configuraciones correspondientes
    driver=setUp()
    iniciarSesion(driver)
    agregarProductosAlCarrito(driver)

        
