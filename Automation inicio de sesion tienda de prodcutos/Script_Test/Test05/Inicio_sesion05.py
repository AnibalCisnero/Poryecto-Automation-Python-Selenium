import unittest
from HtmlTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class inicioSesion(unittest.TestCase):
     def setUp(self):
        self.driver = webdriver.Chrome()
     
        
     def test_UsuarioNoExistente(self):
        self.driver.get("https://www.demoblaze.com/index.html")
        time.sleep(10)

        self.driver.maximize_window()

        self.driver.find_element(By.ID,'login2').click()
        time.sleep(10)

        self.driver.find_element(By.ID,'loginusername').send_keys("ANibal")

        self.driver.find_element(By.ID,'loginpassword').send_keys("ABcd")

        self.driver.find_element(By.XPATH,"//*[@id='logInModal']/div/div/div[3]/button[2]").click()
        time.sleep(10)

        alert = self.driver.switch_to.alert
        alert_text = alert.text
        texto_alert_esperado = "User does not exist."
        assert texto_alert_esperado == alert_text, f"Texto del alert esperado: {texto_alert_esperado}. Texto de alert real: {alert_text}"
        alert.dismiss()


     def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    #Abrimos el archivo de salida con la funcion open() lo utilizamos para abrir un archivo en modo de escritura
    archivo_salida = open('Reporte del caso de prueba (Incio de sesion 05).html', 'w')

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