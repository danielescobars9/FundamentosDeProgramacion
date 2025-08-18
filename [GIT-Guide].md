# Guía Completa sobre Git y GitHub

## ¿Qué es Git?
Git es un sistema de control de versiones distribuido. Permite gestionar y registrar los cambios realizados en archivos y proyectos de software, facilitando el trabajo colaborativo y el seguimiento de la evolución del código.

- **Control de versiones**: Guarda el historial de cambios.
- **Distribuido**: Cada usuario tiene una copia completa del repositorio.
- **Colaborativo**: Permite trabajar en equipo y fusionar cambios.

## ¿Qué es GitHub?
GitHub es una plataforma basada en la web que utiliza Git para alojar repositorios, facilitar la colaboración y gestionar proyectos de software. Permite compartir código, realizar revisiones y gestionar tareas.

---

## Comandos Básicos de Git

### 1. Crear un repositorio

- **git init**  
  Inicializa un nuevo repositorio Git en la carpeta actual.  
  ```bash
  git init
  ```
  Esto crea una carpeta `.git` donde se almacenará el historial de versiones.

- **git clone [URL]**  
  Descarga (clona) un repositorio existente desde GitHub u otra fuente.  
  ```bash
  git clone https://github.com/usuario/repositorio.git
  ```

### 2. Configuración inicial

- **git config**  
  Configura opciones como el nombre de usuario y correo electrónico.
  ```bash
  git config --global user.name "Tu Nombre"
  git config --global user.email "tuemail@ejemplo.com"
  ```

### 3. Flujos de trabajo básicos

#### a) Flujo de trabajo local

1. **git add [archivo]**  
  Añade archivos al área de preparación (staging area).
  ```bash
  git add archivo.txt
  ```

2. **git commit -m "Mensaje"**  
  Guarda los cambios en el historial del repositorio.
  ```bash
  git commit -m "Descripción de los cambios"
  ```

3. **git status**  
  Muestra el estado de los archivos (modificados, preparados, sin seguimiento).
  ```bash
  git status
  ```

4. **git log**  
  Muestra el historial de commits.
  ```bash
  git log
  ```

#### b) Flujo de trabajo colaborativo (con GitHub)

1. **git push**  
  Envía los cambios locales al repositorio remoto (GitHub).
  ```bash
  git push origin main
  ```

2. **git pull**  
  Descarga y fusiona los cambios del repositorio remoto.
  ```bash
  git pull origin main
  ```

3. **git fetch**  
  Descarga los cambios del remoto sin fusionarlos.
  ```bash
  git fetch origin
  ```

---

## Conceptos Clave

- **Repositorio**: Carpeta que contiene el proyecto y el historial de cambios.
- **Commit**: Registro de cambios realizados.
- **Branch (rama)**: Línea de desarrollo independiente.
- **Merge**: Fusiona ramas diferentes.
- **Fork**: Copia de un repositorio en tu cuenta de GitHub.
- **Pull Request**: Solicitud para fusionar cambios en el repositorio principal.

---

## Ejemplo de Flujo de Trabajo en Equipo

1. Clonar el repositorio:
  ```bash
  git clone https://github.com/usuario/repositorio.git
  ```
2. Crear una nueva rama:
  ```bash
  git checkout -b nueva-rama
  ```
3. Realizar cambios y guardarlos:
  ```bash
  git add .
  git commit -m "Agregué nueva funcionalidad"
  ```
4. Subir la rama al remoto:
  ```bash
  git push origin nueva-rama
  ```
5. Crear un Pull Request en GitHub para revisión y fusión.

---

## Buenas Prácticas

- Escribir mensajes de commit claros y descriptivos.
- Usar ramas para nuevas funcionalidades o correcciones.
- Sincronizar frecuentemente con el repositorio remoto.
- Revisar y comentar Pull Requests antes de fusionar.

---

¿Quieres que agregue ejemplos visuales, imágenes o flujos avanzados como manejo de conflictos, rebase, stash, etc.?
# Guía Explícita para el Uso de Git y GitHub

## 1. Instalación de Git

- Descarga Git desde [git-scm.com](https://git-scm.com/).
- Instala siguiendo las instrucciones para tu sistema operativo.

## 2. Configuración Inicial

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tuemail@example.com"
```

## 3. Crear un Nuevo Repositorio

```bash
git init nombre-del-repositorio
cd nombre-del-repositorio
```

## 4. Clonar un Repositorio Existente

```bash
git clone https://github.com/usuario/repositorio.git
```

## 5. Flujo Básico de Trabajo

1. **Ver estado de archivos**
    ```bash
    git status
    ```
2. **Agregar archivos al área de preparación**
    ```bash
    git add archivo.txt
    git add .
    ```
3. **Guardar cambios (commit)**
    ```bash
    git commit -m "Descripción de los cambios"
    ```
4. **Ver historial de commits**
    ```bash
    git log
    ```

## 6. Trabajar con GitHub

### Conectar repositorio local con GitHub

1. Crea un repositorio en GitHub.
2. Conecta tu repositorio local:
    ```bash
    git remote add origin https://github.com/usuario/repositorio.git
    ```

### Subir cambios a GitHub

```bash
git push -u origin main
```

### Descargar cambios de GitHub

```bash
git pull origin main
```

## 7. Ramas (Branches)

- Crear una rama:
  ```bash
  git branch nombre-rama
  ```
- Cambiar de rama:
  ```bash
  git checkout nombre-rama
  ```
- Fusionar ramas:
  ```bash
  git merge nombre-rama
  ```

## 8. Buenas Prácticas

- Realiza commits frecuentes y descriptivos.
- Usa ramas para nuevas funcionalidades.
- Sincroniza regularmente con GitHub.

---

**Recursos útiles:**
- [Documentación oficial de Git](https://git-scm.com/doc)
- [Guía de GitHub](https://docs.github.com/)
