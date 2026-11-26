# DjangoLibrary · FreeLibrary

**Tema asignado:** Biblioteca. FreeLibrary organiza libros digitales, sus autores, su categoría y el registro de préstamos.

## Modelo de datos

| Tabla | Campos principales | Relaciones |
| --- | --- | --- |
| Libro (`Book`) | Título, slug, género, descripción, extracto, calificación, portada y PDF | Puede pertenecer a una categoría y tener varios autores. Guarda al usuario que lo publicó. |
| Autor (`Author`) | Nombre y biografía | Puede participar en varios libros. |
| Categoría (`Category`) | Nombre y descripción | Agrupa varios libros. |
| Préstamo (`Loan`) | Fecha de inicio, fecha de devolución y estado | Vincula un libro y un lector registrado. |

La categoría es opcional para conservar los libros anteriores. Puedes eliminar categorías sin libros y libros sin préstamos. Los préstamos protegen el historial de libros y lectores mediante `PROTECT`. Si se borra la cuenta de quien publicó un libro, `SET_NULL` conserva el libro.

## Instalación local

Usa Python 3.14 y un servidor MySQL en ejecución. Crea una base de datos vacía con codificación `utf8mb4` y prepara un usuario MySQL con acceso a ella. Si `mysqlclient` necesita compilarse en tu sistema, instala el compilador, `pkg-config` y las cabeceras del cliente MySQL o MariaDB.

```bash
git clone https://github.com/Briamlaww24/DjangoLibrary.git
cd DjangoLibrary
python3.14 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env
```

Edita `.env` con el nombre de tu base, el usuario y la contraseña de MySQL. Si ya tienes un archivo `.env`, conserva el tuyo. Después ejecuta:

```bash
python manage.py migrate
python manage.py seed_library
python manage.py check
python manage.py runserver
```

Abre `http://127.0.0.1:8000/`.

## Acceso y datos de demostración

`migrate` crea los dos grupos y asigna sus permisos. Las cuentas nuevas se registran como consultoras. Las cuentas existentes sin grupo reciben ese rol al aplicar la migración inicial de roles.

- **Administradores.** Gestionan libros y categorías desde el catálogo, consultan autores y préstamos, y pueden gestionar las cuatro tablas en Django Admin si su cuenta tiene acceso al admin.
- **Consultores.** Ven libros, autores y categorías. Pueden publicar, editar y borrar sus propios libros. La protección de préstamos sigue aplicándose.
- **Superusuarios.** Tienen acceso completo al admin y al catálogo.

`seed_library` carga cinco autores, cinco categorías, cinco libros y cinco préstamos en una base vacía. Puedes repetirlo sin duplicar esos registros en una base de demostración. Si ya tienes los libros ficticios de ejemplo, `python manage.py seed_library --replace-existing` los sustituye conservando el identificador y los préstamos de cada registro.

| Usuario de prueba | Grupo o acceso | Contraseña |
| --- | --- | --- |
| `demo_super` | Superusuario | `DemoSuper-Libros268!` |
| `demo_admin` | administradores | `DemoAdmin-Libros268!` |
| `demo_lector` | consultores | `DemoLector-Libros268!` |

Estas cuentas son para la base local de demostración. En `/admin/` puedes ver las cuatro tablas, filtrar sus registros y buscar por nombre, título u otros campos según la entidad.

### Fuentes de los clásicos

Las portadas históricas se guardan en el proyecto. Los PDF se prepararon a partir de los textos de Project Gutenberg y conservan su licencia y el enlace al texto original. Las portadas y los textos pueden corresponder a ediciones diferentes.

| Libro | Texto | Portada o frontispicio |
| --- | --- | --- |
| Don Quijote de la Mancha | [Project Gutenberg 2000](https://www.gutenberg.org/ebooks/2000) | [Primera parte, Madrid, 1605](https://commons.wikimedia.org/wiki/File:Miguel_de_Cervantes_(1605)_El_ingenioso_hidalgo_Don_Quixote_de_la_Mancha.png) |
| Alicia en el país de las maravillas | [Project Gutenberg 11](https://www.gutenberg.org/ebooks/11) | [Charles Robinson, 1907](https://commons.wikimedia.org/wiki/File:Alice%27s_Adventures_in_Wonderland_-_Carroll,_Robinson_-_S001_-_Cover.jpg) |
| El retrato de Dorian Gray | [Project Gutenberg 174](https://www.gutenberg.org/ebooks/174) | [Primera edición en libro, 1891, Houghton Library](https://commons.wikimedia.org/wiki/File:Houghton_HEW_12.10.15_-_The_Picture_of_Dorian_Gray,_1891_(cover).jpg) |
| Orgullo y prejuicio | [Project Gutenberg 1342](https://www.gutenberg.org/ebooks/1342) | [Edición del pavo real, 1894](https://commons.wikimedia.org/wiki/File:AUSTEN(1894)_Pride_and_prejudice_(15811958311).jpg) |
| Frankenstein | [Project Gutenberg 84](https://www.gutenberg.org/ebooks/84) | [Frontispicio de Theodor von Holst, 1831](https://commons.wikimedia.org/wiki/File:Frankenstein.1831.inside-cover.jpg) |

## Comprobaciones

Django ejecuta las pruebas en una base MySQL temporal. El usuario de MySQL necesita permiso para crearla.

```bash
python manage.py makemigrations --check --dry-run
python manage.py test
```
