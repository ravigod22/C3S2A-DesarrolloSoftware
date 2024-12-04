# Practica Calificada 5

## Informacion
**Alumno**: Jose Manuel Ravichagua Marin  
**Codigo**: 20210086C  
**Curso**: CC3S2 Desarrollo de Software  
**Profesor**: Cesar Lara

## Objetivo

Completar los ejercicios avanzados utilizando **Ansible**, **Vagrant** y **Docker**, siguiendo buenas prácticas de desarrollo y automatización. Deberás estructurar tu proyecto de manera organizada, utilizar control de versiones con **Git** y compartir tu trabajo a través de un repositorio en **GitHub**. Además, prepararás un archivo comprimido con todo el código y documentación necesaria.

## Estructura del proyecto

- proyecto/
    - ansible/
        - ejercicio1/
        - ejercicio2/
        - ...
        - ejercicio10/
    - handlers/
    - templates/
    - vagrant/
        - Vagrantfile
    - site.yml
    - README.md
    - docs/
        - Photos/

## Iniciar el proyecto
- PreRequisitos:
    - Instalar **VirtualBox**
    - Instalar **Ansible**
    - Instalar **Vagrant**
- Creamos un directorio proyecto, e inicializamos nuestro `Vagrantfile` con el siguiente comando:  
    - `vagrant init ubuntu/focal64`  
- Configuramos aquel **Vagranfile**, con una configuracion basica para levantar la maquina virtual.  
![Configuracion basica](docs/Photos/ConfigVagrantfile.png)

- Creacion de un archivo `site.yml`, donde realizaremos las tareas de una forma estructurada y con buenas practicas de codigo.
![Creacion de archivo site.yml](docs/Photos/CreacionSiteYML.png)

- Dado que se configuro para poder levantar nuestra maquina virtual, lo construimos con el siguiente comando:  
    - `vagrant up`

- Se mostrara las diversas tareas que se implemento para el proyecto, si ocurre algun error o quieres aumentar mas tareas sin levantar otra vez la maquina virtual, utiliza:  
    - `vagrant provision`

- Si deseas liberar recursos de la maquina virtual:
    - `vagrant destroy`

![](docs/Photos/CreacionVM.png)
## Desarrollo de los ejercicios

### Ejercicio 1: Configuracion basica del sistema
- Se realizo la implementacion de un archivo **.gitignore** para excluir archivos temporales, claves privadas y archivos de maquina virtual generados.
![Creacion de .gitignore](docs/Photos/GitIgnore.png) 

- Implementacion de la primera tarea sobre:
    - Actualizar el sistema operativo.
    ![](docs/Photos/Update.png)
    - Configurar locales y zonas horarias.
    ![](docs/Photos/ZonaHoraria.png)
    - Configurar el entorno.
    ![](docs/Photos/EntornoPIP.png)
    - Crear usuarios y grupos con permisos especificos.
    ![](docs/Photos/CreacionUsuario.png)

### Ejercicio 2: Implementacion de servicios web con seguridad basica

- Actualizamos el sistema, instalamos y configuramos **Nginx**.
![](docs/Photos/InstalarNGINX.png)
- Generamos ceritificados SSL autofirmados para habilitar HTTPS.
![](docs/Photos/CertificadoSSL.png)
- Configuracion basica de firewall para permitir el trafico de SSH, HTTP, HTTPS.
![](docs/Photos/FireWall.png)
- Asimismo, implementacion de un manejador y una plantilla que configure Nginx para utilizar los certificados y servir en HTTPS.
![](docs/Photos/TemplateSSL.png)


### Ejercicio 3: Despliegue de aplicacion web con balanceador de carga

- Instalacion de Flask y Gunicorn  
![](docs/Photos/FlaskGunicorn.png)
- Creacion de directorios para la app de Flask
![](docs/Photos/DirectorioAPP.png)
- Creacion de servicios systemd
![](docs/Photos/Servicios.png)
- Habilitar servicios systemd
![](docs/Photos/HabilitarServicios.png)
- Configurar para balanceo de carga
![](docs/Photos/BalanceoCarga.png)
- Template de Flask, servicio systemd, balancerNginx
    - **Flask**
    ![](docs/Photos/TemplateFlask.png)
    - **Service**
    ![](docs/Photos/TemplateService.png)
    - **Balancer**
    ![](docs/Photos/TemplateBalancer.png)

### Ejercicio 4: Monitore y alertas

- Instalar Prometheus
![](docs/Photos/PrometheusInstall.png)
- Instalar Node Exporter
![](docs/Photos/NodeInstall.png)
- Instalar dependencias para Grafana
![](docs/Photos/DependenciaGrafana.png)
- Configurar Prometheus
![](docs/Photos/ConfigPrometheus.png)
- Manejador de Reinicio Prometheus
![](docs/Photos/ReloadPrometheus.png)
![](docs/Photos/ReloadPrometheusI.png)
- Templates Reinicio, nodeExporteService, PrometheusService
    - **PrometheusService**  
    ![](docs/Photos/TemplatePrometheusService.png)
    - **Node Exporter**
    ![](docs/Photos/TemplateNodeExporter.png)
    - **Alerta Prometheus**
    ![](docs/Photos/PrometheusAlert.png)

### Resultado y Conclusiones:
- Avance de las tareas dadas por los ejercicios aun no concluidas pero con un avance del 25%.
- Se realizo las implementacion sin mostrar los resultados
- Resultado parcial de las tareas proporcionadas en el playbook **site.yml**
![](docs/Photos/ResultadoParcial.png)