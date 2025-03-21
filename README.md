# Proyecto Urban Grocers 
Juda Emmanuel Perez Salido. Sprint 7.  
  
Descripcion.  
En este proyecto se hacen pruebas para la funcion de añadir creacion de kits en la aplicacion Urban Grocers compronbando el campo de "name" segun sus especificaciones.  
  
Pasos para ejecutar pruebas:  
1.Iniciar servidor para pruebas.  
2.Copiar URL del servidor en el archivo configuration.py en la variable URL_SERVICE. Verificar que no tenga la diagonal al final.  
3.Ir al archivo create_kit_name_kit_test.  
4.Entrar a la terminal del entorno.  
5. Introducir el comando pytest seguida del folder donde se encuentra guardado el proyecto.  
    Ejemplo:
    pytest E:\Users\Bubba\Documents\QA test\Sprint7\repos\qa-project-Urban-Grocers-app-es\create_kit_name_kit_test.py
  
Pruebas creadas.  
def test_numero_permitido_de_caracteres_1():  
def test_numero_permitido_de_caracteres_511():  
test_numero_de_caracteres_0():  
test_numero_permitido_de_caracteres_512():  
test_numero_caracteres_especiales_permitidos_():  
test_se_permiten_espacios( ):  
test_se_permiten_números():  
test_el_parametro_no_se_pasa_en_la_solicitud():  
test_el_parametro_no_se_pasa_en_la_solicitud():  
  
Librerias a instalar.  
1.pytest.  
2.requests.  
  
Como instalar las librerias.  
-Desde PyCharm acceder al menu de "Python Packages" y buscar las librerias por nombre.  
-Presionar el boton instalar.
