# CRUD de Gatos

Este proyecto implementa un CRUD (Create, Read, Update, Delete) </br> para gestionar información sobre gatos. Permite realizar operaciones básicas de creación, lectura, actualización y eliminación de registros de gatos en una base de datos.

## Funcionalidades principales

- **Crear gato:** Agregar un nuevo gato a la base de datos con su nombre, edad y color.
- **Leer gato:** Mostrar la información de un gato específico.
- **Actualizar gato:** Modificar la información de un gato existente.
- **Eliminar gato:** Eliminar un gato de la base de datos.
- **Mostrar en tabla:** Usando tabulate, mostrar en formato tabla 
- **Mostrar en web:** Usando tabulate, mostrar en formato web 
- **Inicializar DB Redis** Inicializa la DB en docker y lo expone en el puerto por defecto 

## Configuración y uso

### Requisitos previos

Asegúrate de tener instalado Docker. 
Más info en: </br>
<a href="https://www.docker.com/products/docker-desktop/"> Docker Desktop </a> 


### Instalación de dependencias

Antes de ejecutar el proyecto, asegúrate de instalar las siguientes dependencias:

```bash
pip install redis
pip install tabulate
pip install webbrowser
