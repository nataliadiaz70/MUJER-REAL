
from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText
from flask_mail import Mail, Message


app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'nataliadiaz1188@gmail.com'
app.config['MAIL_PASSWORD'] =xxxxxxxxxx

mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method ==  'POST':
        # Procesar los datos del formulario
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        correo = request.form.get('correo electonico')
        consulta = request.form.get('consulta')

        # Enviar correo electrónico
        msg = Message('Asunto del Correo', sender='nataliadiaz1188@gmail.com', recipients=['mariojsvcp@gmail.com'])
        msg.body = f'Nombre: {nombre}\nApellido: {apellido}\nCorreo Electrónico: {correo}\nConsulta: {consulta}'
        mail.send(msg)
        return 'Correo enviado con éxito'  # Agregado para mostrar un mensaje de éxito
    return render_template('formulario_de_contacto.html')


if __name__ == '__main__':
    app.run(debug=True)


''''app = Flask(__name__)
@app.route('/')
def index():
    return render_template('formulario-de_contacto.html')

@app.route('/enviar', methods=['POST'])
def enviar_correo():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellidp = request.form['apellido']
        correo = request.form['correo']
        mensaje = request.form['mensaje']

        # Configurar el servidor SMTP
        servidor_smtp = smtplib.SMTP('smtp.gmail.com', '587')
        servidor_smtp.starttls()











        # Autenticarse (si es necesario)
        servidor_smtp.login('nataliadiaz1188@gmail.com', 'xxxxxxxx')

        # Crear el mensaje de correo electrónico
        asunto = 'Nuevo mensaje desde el formulario'
        cuerpo = f'Nombre: {nombre}\nCorreo: {correo}\nMensaje: {mensaje}'
        mensaje_email = MIMEText(cuerpo)
        mensaje_email['Subject'] = asunto
        mensaje_email['From'] = 'nataliadiaz1188@gmail.com'
        mensaje_email['To'] = 'mariojsvcp@gmail.com'

        # Enviar el correo electrónico
        servidor_smtp.sendmail('nataliadiaz1188@gmail.com', 'mariojsvcp@gmail.com', mensaje_email.as_string())

        # Cerrar la conexión con el servidor SMTP
        servidor_smtp.quit()

        return 'Correo enviado con éxito'''


