# Instalar y configurar un servidor MySQL en Docker

1. Instalar docker

[primeros pasos](https://www.docker.com/get-started/)

Verificar si esta docker instalado

```bash
$ docker --version
Docker version 29.3.0, build 5927d80
```

2. Descargar la imagen oficial de MySQL de docker HUB

[docker hub](https://hub.docker.com/)

```bash
$ docker pull mysql:latest
```

3. Listar las imagenes

```bash
$ docker images
```

4. Gestionar un contenedor mysql

4.1 Crear y arrancar un contenedor

    ```bash
    docker run --name mysql-server -e MYSQL_ROOT_PASSWORD=python123 -p 3306:3306 -d mysql
    ```

    - **run:** crea un nuevo contenedor o inicia uno existente.
    - **name**: da un nombre al contenedor. El nombre debe ser legible y corto. En nuestro caso, el nombre es **mysql-server**.
    - **e**: crea una variable de entorno que será accesible dentro del contenedor. Es crucial configurar **MYSQL_ROOT_PASSWORD** para poder ejecutar comandos SQL posteriormente desde el contenedor.
    - **p:** <PUERTO_HOST>:<PUERTO_CONTENEDOR>
    - **d**: abreviatura de _detached_. Hace que el contenedor se ejecute en segundo plano(libera la terminal). Si se elimina esta etiqueta, el comando seguirá imprimiendo registros hasta que el contenedor se detenga.
    - **image_name**: el argumento final es el nombre de la imagen a partir de la cual se construirá el contenedor. En este caso, la imagen es **mysql**.

4.2 Arrancar un contenedor ya existente

```bash
docker start mysql-server
```

4.3 Para la ejecución de un contenedor

```bash
docker stop mysql-server
```

4.4 Ver los contenedores que estan corriendo

```bash
docker ps -a
```

4.5 Ver los logs de un contenedor

```bash
docker logs mysql-server
```

5. Para acceder al contenedor

```bash
docker exec -it mysql-server bash
```

6. Ingresar a mysql

Desde adentro del contenedor

```bash
mysql -u root -p
```

**nota**: ver que password se puso cuando se creo el contenedor (4.1)

7. Ver las base de datos

```sql
show databases;
```

8. Crear una DB

```sql
create database eduit;
```

9. Seleccionar la db

```sql
use eduit;
```

10. ver DB activa

```sql
status;
```

```sql
select database();
```

11. Ver las tablas

```sql
show tables;
```

12. Crear una tabla

```sql
create table alumnos (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(50) NOT NULL,
  edad INT,
  email VARCHAR(100) UNIQUE,
  sexo ENUM('M', 'F', 'NC')
);
```

```sql
show tables;
```

13. Ver la estructura de una tabla

```sql
describe alumnos
```

14. Ingresar datos en la tabla

```sql
insert into alumnos (nombre, edad, email, sexo)
values
("Juan", 25, "juan@test.com", "M"),
("Pedro", 30, "pedro@test.com", "M"),
("Lucas", 22, "lucas@test.com", "M"),
("Martin", 35, "martin@test.com", "M"),
("Ana", 28, "ana@test.com", "F"),
("Maria", 32, "maria@test.com", "F"),
("Lucia", 24, "lucia@test.com", "F"),
("Sofia", 21, "sofia@test.com", "F"),
("Alex", 27, "alex@test.com", "NC");
```

**Nota:** probar de insertar un registro con un email ya cargado o el campo nombre vacio.

15. Listar registros

15.1 Todos

```sql
select * from alumnos;
```

15.2 Limitar la cantidad

```sql
select * from alumnos limit 2;
```

16. Filtrar registros

```sql
select nombre, edad from alumnos where edad > 25;
```

```sql
select * from alumnos where edad >= 25 and edad <= 40;
```

```sql
select * from alumnos where edad between 25 and 40;
```

```sql
select * from alumnos where nombre in ("Pablo", "Ana");
```

```sql
select * from alumnos where email is not NULL;
```

17. Buscar patrones

El LIKE en SQL se usa para buscar patrones dentro de textos (muy útil para nombres, emails, etc.).

```sql
select * from alumnos where nombre like "L%";
```

18. Ordenar los resultados

```sql
select * from alumnos order by edad desc;
```

19. Actualizar datos (update)

```sql
update alumnos
set edad = 40
where nombre = "Martin";
```

```sql
update alumnos set edad = edad + 1 where edad < 30;
```

20. Agregaciones

- cantidad de registros de una tabla

```sql
select count(*) from alumnos;
```

- cuenta los que cumplen la condicion

```sql
select count(*) from alumnos where edad > 25;
```

- calcula el promedio de edad

```sql
select avg(edad) from alumnos;
```

- valor maximo de edad

```sql
select max(edad) from alumnos;
```

- valor minimo de edad

```sql
select min(edad) from alumnos;
```

21. Group by

```sql
select sexo, avg(edad) as promedio_edad
from alumnos
group by sexo;
```

22. Borrar registros

```sql
delete from alumnos where nombre = "Luis";
```

23. Borrar una tabla

```sql
drop table alumnos;
```

24. Borrar db

```sql
drop database eduit;
```
