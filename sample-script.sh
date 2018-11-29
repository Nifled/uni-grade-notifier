#!/bin/bash

# env vars
export USER_EMAIL='example@mail.com'
export PORTAL_USER='a214215385@alumnos.unison.mx'
export PORTAL_PW='your-password'
export SENDGRID_API_KEY='create-free-sendgrid-account-in-5-mins-for-apikey'

VENV_PY="/home/nifled/.local/share/virtualenvs/uni-grade-notifier-4pX91mei/bin/python" # Make sure packages are installed
PROJECT="/home/nifled/erick/uni-grade-notifier"

SCRIPT="script.py"
cd "${PROJECT}" && "${VENV_PY}" "${SCRIPT}"
