Este proyecto en Python tiene como objetivo analizar los datos proporcionados por el Servicio de Rentas Internas del Ecuador (SRI) correspondientes al año 2024. A través de un archivo CSV con información de ventas y exportaciones, se implementan diversas funcionalidades que permiten obtener estadísticas clave por provincia y por mes.

La estructura del proyecto está organizada de manera clara: el archivo app.py actúa como la aplicación principal con una interfaz de consola. En la carpeta src se encuentra el archivo procesador.py, el cual contiene la lógica central de análisis. Los datos se encuentran en el directorio data, específicamente en el archivo sri_ventas_2024.csv. Por otro lado, en la carpeta tests se incluyen pruebas unitarias usando el módulo unittest.

Para ejecutar este proyecto, es necesario contar con Python 3.8 o superior. Una vez instalado, se puede ejecutar la aplicación directamente con el comando python app.py. Este programa permite visualizar las ventas totales por provincia, consultar las ventas de una provincia específica, observar las exportaciones mensuales, y calcular la diferencia entre ventas y exportaciones por provincia.

El proyecto también cuenta con un conjunto de pruebas automatizadas. Estas se ejecutan utilizando el comando python -m unittest discover tests, y se puede medir la cobertura del código con coverage run -m unittest discover tests seguido de coverage report -m, si se desea evaluar la calidad de las pruebas.

Entre las funcionalidades implementadas destacan: el cálculo de ventas totales por provincia, la consulta de ventas por una provincia específica, el cálculo de exportaciones por mes, la diferencia entre ventas y exportaciones por provincia, además del desarrollo de pruebas unitarias y el manejo de errores para mejorar la robustez del sistema.

Este trabajo ha sido desarrollado por Julio Ochoa, estudiante de séptimo semestre de Negocios Digitales en la Universidad Politécnica Salesiana. El proyecto forma parte de un laboratorio académico que busca aplicar conceptos de análisis de datos, programación modular, pruebas automatizadas y documentación técnica.
