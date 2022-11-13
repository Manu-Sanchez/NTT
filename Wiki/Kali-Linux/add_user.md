# Crear usuario en Kali

## Comandos útiles

### Ver lista de usuarios
$cat /etc/passwd

### Comprobar usuario actual
$whoami

### Cambiar de usuario
$su <username>

## Método 1

### Crear usuario
$adduser <username>

### Otorgar permisos root
$usermod -a -G sudo <username>
$chsh -s /bin/bash <username>

## Método 2

### Crear usuario
$sudo useradd -m <username>

### Poner contraseña
$sudo passwd <username>

### Otorgar permisos root
$usermod -a -G sudo <username>
$chsh -s /bin/bash <username>


## Borrar Usuarios
$sudo userdel -f -r <username>

