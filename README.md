# Uni Grade Notifier

Un pequeño script que te notifica por correo cuando una calificacion del [Portal de la UNISON](https://www.alumnos.unison.mx/) ha sido actualizada para no estar entrando al portal cada 20 minutos para saber si reprobaste o no.


### Steps para correrlo en tu servidor (Linux)

Para mi servidor utilicé un VM de Azure (gratis para estudiantes) y SSH para entrar al servidor.

Specs:
- Ubuntu 18.04
- Python 3.6

**1. Clona el repo**
```console
$ git clone https://github.com/Nifled/uni-grade-notifier.git && cd uni-grade-notifier
```

**2. Instala las dependencias**
```console
$ export PIPENV_VENV_IN_PROJECT=1
```
```console
$ pipenv install
```

Si no tienes `pipenv` o Python 3.6.x, instalalos ☺️.

**3. Modifica las variables de `sample-script.sh`.**
- `USER_EMAIL` = es el correo donde quieres recibir las notificaciones.
- `PORTAL_USER` = correo del portal de la uni
- `PORTAL_PW` = contraseña del portal de la uni
- `SENDGRID_API_KEY` = api key de sendgrid
- `PROJECT_PATH` = ruta en donde tienes `uni-grade-notifier` (ejecuta el comando `pwd`)


Usa mi key de SendGrid si quieres: `'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'`.

**4. Crea un cron job para ejecutar script cada x minutos.**

Primero, debes copiar la ruta absoluta del `sample-script.sh` (e.g. `/home/nifled/uni-grade-notifier/sample-script.sh`).

Abre tu `crontab`
```console
$ crontab -e
```
En la parte inferior (hasta abajo) escribe lo siguiente.
```bash
*/10 * * * * sh /home/nifled/uni-grade-notifier/sample-script.sh
 
```
**Asegurate de dejar un salto de linea despues del comando.** 
Yo hice el mio para que se ejecutara cada 10 minutos, lo puedes cambiar reemplazando el 10 por el numero que gustes.

**Guardalo y listo. Seras notificado cuando vayan subiendo tus calificaciones de ~~100~~ 70.**