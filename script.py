import os
import requests
import pickledb


def get_cycle(session, url):
    cycle = session.post(url)
    return cycle.json().get('data')[0].get('id_ciclo')


def get_student_info(session, url):
    info = session.post(url)
    return info.json().get('data').get('niveles')[0].get('ide')


def main():
    # pickedb filename
    PICKLE_FN = 'grades.p'

    # UNISON api urls
    LOGIN_URL = 'https://buhos.uson.mx/web/apps/portalAlumnos/index.php/auth/login/entrar'
    GRADES_URL = 'https://buhos.uson.mx/portalalumnos/obtener/calificacionesFinalesEstudiante'
    INFO_URL = 'https://buhos.uson.mx/web/apps/portalAlumnos/index.php/auth/sesion/datos_alumno'
    CYCLE_URL = 'https://buhos.uson.mx/web/apps/portalAlumnos/index.php/horario/ciclosActivos'

    # Unison portal auth
    PORTAL_USER = os.environ.get('PORTAL_USER', 'User Not Set')
    PORTAL_PW = os.environ.get('PORTAL_PW', 'Password Not Set')
    form_data_login = {'u': PORTAL_USER, 'p': PORTAL_PW}

    # Data store
    store = pickledb.load(PICKLE_FN, True)  # Grades store

    with requests.Session() as s:
        s.post(LOGIN_URL, data=form_data_login)

        # Cycle id for grades
        id_cycle = get_cycle(s, CYCLE_URL)

        # Student id for grades
        id_student = get_student_info(s, INFO_URL)

        grades_res = s.post(GRADES_URL, data={
            'idEstudiante': id_student,
            'idCiclo': id_cycle,
        })

    subjects = grades_res.json().get('data')
    print(subjects)
    for subject in subjects:
        subject_id = subject.get('ClaveMateria')
        subject_grade = subject.get('Cal')
        subject_name = subject.get('DescMateria')

        if store.exists(subject_id):
            old_grade = store.get(subject_id)

            if not subject_grade == old_grade:
                print(f'Calificacion de {subject_name} ha sido actualizada!')
                # Send email!
                # ...
                # .
                # ...
                # Send email!
                store.set(subject_id, subject_grade)

        else:
            print(f'Create {subject_name} store in pickledb!')
            store.set(subject_id, subject_grade)


if __name__ == '__main__':
    main()
