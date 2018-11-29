#!/bin/bash


# env vars (modify!)
export USER_EMAIL='example@mail.com'
export PORTAL_USER='a214215385@alumnos.unison.mx'
export PORTAL_PW='your-password'
export SENDGRID_API_KEY='create-free-sendgrid-account-in-5-mins-for-apikey'


#########   don't modify   #########
# paths
VENV_PY="$PWD/.venv/bin/python"
SCRIPT="script.py"

# command
"${VENV_PY}" "${SCRIPT}"
#########   don't modify   #########