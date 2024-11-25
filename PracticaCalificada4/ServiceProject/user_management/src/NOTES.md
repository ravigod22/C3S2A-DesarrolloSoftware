# Explicacion del uso SOLID para la implementacion de la logica de src

## Principio 1:
### Clase Usuario:
- Cada usuario con sus respectivos atributos (`id`, `nombre`, `correo`) y un `sumary` para devolver la informacion.
### RepositorioUsuario:
- Manejo de un almacenamiento de memoria simulado, proporcionando los metodos para crear, leer, actualizar, eliminar y obtener a todos los usuarios.
### ServicioUsuario:
- Organiza la logica de negocio, delegando al repositorio. Este servicio es un intermediario entre el controlador y repositorio

### ControladorUsuario:
- Gestiona las solicitudes HTTP y delega al servicio.

## Principio 2:
- La logica proporcionada cumple parcialmente el principio, pero se puede agregar un metodo `buscarUsuarioPorCorreo` sin romper el codigo actual.

## Principio 3:
- El codigo sigue el principio, ya que, se puede reemplazar `RepositorioUsuario` con una logica para una base de datos SQL.

## Principio 4:
- La logica cumple parcialmente (`interfaz implicita`), ya que si el repositorio crece, estos metodos no deben afectar las clases que no los usan.

## Principio 5:
- La logica implementada no cumple, ya que `ServicioUsuario` depende directamente de `RepositorioUsuario`.