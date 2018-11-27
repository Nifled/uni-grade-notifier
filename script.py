import time
import json
import requests

LOGIN_URL = 'https://buhos.uson.mx/web/apps/portalAlumnos/index.php/auth/login/entrar'
# GRADES_URL = 'https://buhos.uson.mx/web/apps/portalAlumnos/index.php/calificaciones'
GRADES_URL = 'https://buhos.uson.mx/portalalumnos/obtener/calificacionesFinalesEstudiante'
DATA_URL = 'https://buhos.uson.mx/web/apps/portalAlumnos/index.php/auth/sesion/datos_alumno'
CYCLE_URL = 'https://buhos.uson.mx/web/apps/portalAlumnos/index.php/horario/ciclosActivos'

PORTAL_USER = ''
PORTAL_PW = ''

form_data_login = {'u': PORTAL_USER, 'p': PORTAL_PW}

with requests.Session() as s:
    s.post(LOGIN_URL, data=form_data_login)

    # Cycle id for grades
    cycle = s.post(CYCLE_URL)
    id_cycle = cycle.json().get('data')[0].get('id_ciclo')

    # Student id for grades
    info = s.post(DATA_URL)
    id_student = info.json().get('data').get('niveles')[0].get('ide')

    grades = s.post(GRADES_URL, data={
        'idEstudiante': id_student,
        'idCiclo': id_cycle,
    })
    print(json.dumps(grades.json()))
