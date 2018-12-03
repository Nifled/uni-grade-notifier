#!/bin/bash


# env vars (modify!)
export USER_EMAIL='example@mail.com'
export PORTAL_USER='a214215385@alumnos.unison.mx'
export PORTAL_PW='your-password'
export SENDGRID_API_KEY='create-free-sendgrid-account-in-5-mins-for-apikey'
export PROJECT_PATH='/home/nifled/uni-grade-notifier'


#########   don't modify   #########
# paths
VENV_PY="$PROJECT_PATH/.venv/bin/python"
SCRIPT="$PROJECT_PATH/script.py"

# command
"${VENV_PY}" "${SCRIPT}"
#########   don't modify   #########
