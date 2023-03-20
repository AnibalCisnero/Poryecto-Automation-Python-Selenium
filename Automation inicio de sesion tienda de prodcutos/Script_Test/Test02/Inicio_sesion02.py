#En este caso Probamos como reacciona el sistema al ingresar credenciales invalidas en el formulario de inicio de sesion, solo comentare codigo que no comente en el script anterior
import unittest
from HtmlTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class inicioSesion(unittest.TestCase):
     def setUp(self):
        self.driver = webdriver.Chrome()
     
        
     def test_IncisoSesionCredencialesInvalidas(self):
        self.driver.get("https://www.demoblaze.com/index.html")
        time.sleep(10)

        self.driver.maximize_window()
        
        self.driver.find_element(By.ID,'login2').click()
        time.sleep(10)

        #En este caso ingreso un usuario incorrecto
        self.driver.find_element(By.ID,'loginusername').send_keys("Anibal")
        time.sleep(10)
        
        #En este caso ingreso una Password incorrecta
        self.driver.find_element(By.ID,'loginpassword').send_keys(12)
        time.sleep(10)

        self.driver.find_element(By.XPATH,"//*[@id='logInModal']/div/div/div[3]/button[2]").click()
        time.sleep(10)
        
        #Esta liena la usamos para cambiar el controlador de la ventana actual al controlador de la alerta que está presente en la página.
        alert = self.driver.switch_to.alert
        #Esta linea la usamos para obtener el texto del mensaje de alerta
        alert_text = alert.text
        #En esta linea definimos el texto esperado del mensaje de alerta
        texto_alert_esperado = "Wrong password."
        
        #Esta liena es una asercion que compara el texto esperado del mensaje de alerta con el 
        #texto real del mensaje de alerta obtenido anteriormente. 
        #Si el texto esperado y el texto real no coinciden, se producirá un error 
        #de aserción y el mensaje de error se mostrará en la salida de la prueba. 
        #La cadena f"Texto del alert esperado: {texto_alert_esperado}. Texto de alert real: {alert_text}" se utiliza para proporcionar información adicional en caso de que la aserción falle, para ayudar en la depuración.
        assert texto_alert_esperado == alert_text, f"Texto del alert esperado: {texto_alert_esperado}. Texto de alert real: {alert_text}"
        
        #En esta linea cerramos el alert llamamos al metodo dismiss() que hace click en el boton aceptar
        alert.dismiss()

     def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    #Abrimos el archivo de salida con la funcion open() lo utilizamos para abrir un archivo en modo de escritura
    archivo_salida = open('Reporte del caso de prueba (Incio de sesion 02).html', 'w')

    #Creamos un objeto runner de HTMLTestRunner
    runner = HTMLTestRunner(
        stream=archivo_salida, #Para que el informe se guarde en el archivo que generamos en la varibale archivo_salida
        verbosity=2, #El parámetro verbosity se establece en 2, lo que significa que se mostrarán detalles adicionales en el informe.
    )

    #Ejecutamos la suite de pruebas
    suite = unittest.TestLoader().loadTestsFromTestCase(inicioSesion)
    runner.run(suite)

    #Cerramos el archivo de salida
    archivo_salida.close()