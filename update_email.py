import os
import sendgrid
from sendgrid.helpers.mail import *


SENDGRID_KEY = os.environ.get('SENDGRID_API_KEY', 'No Sendgrid key provided.')


class GradeUpdateEmail:
    def __init__(self, to_email):
        self.to_email = Email(to_email)
        self.sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_KEY)

    def send_update(self, grade_name, grade):
        subject = f'Calificacion de {grade_name} actualizada!'
        content = Content(
            'text/plain',
            f'Tu calificacion de {grade_name} ha sido actualizada a {grade}. Puedes verificar entrando al portal UNISON https://buhos.uson.mx/web/apps/portalAlumnos/index.php/principal.'
        )
        from_email = Email("PortalUnison@erickdelfin.com")
        mail = Mail(from_email, subject, self.to_email, content)

        response = self.sg.client.mail.send.post(request_body=mail.get())

        print(response.status_code)
        print('EMAIL SENT!')
