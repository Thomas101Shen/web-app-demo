from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
from forms import ContactForm

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['TESTING'] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'developmentforbongs2323@gmail.com'
app.config['MAIL_PASSWORD'] = 'Adeadroman1!'
app.config['MAIL_DEFAULT_SENDER'] = ('Bedrock Stone and Tile' ,'developmentforbongs2323@gmail.com')
app.config['MAIL_MAX_EMAILS'] = None
app.config['MAIL_ASCII_ATTACHMENTS'] = False

app.config['SECRET_KEY']='SECRET'

mail = Mail(app)

@app.route('/')
def index():
	# msg = Message('testing123', recipients = ['595jsparrow@gmail.com'])
	# # msg.body = 'bodytext'
	# msg.html = '<h1>hello</h1>'
	# mail.send(msg)
	return render_template('index.html', contact_form=ContactForm())

@app.route('/api', methods = ['POST'])
def addContact():
	contact_form = ContactForm()
	if contact_form.validate_on_submit:
		msg = Message(str(contact_form.category.data) + ' requested by '
		+ str(contact_form.first_name.data) + ' ' + str(contact_form.last_name.data), recipients = ['595jsparrow@gmail.com'])#may combine first and last name attributes
		msg.body = 'client\'s email address: ' + str(contact_form.address.data) + 3*'\n' + 'Job description: \n' + str(contact_form.description.data)
		mail.send(msg)
		confirmation = Message('Thank you for choosing us!', recipients = [contact_form.address.data])
		confirmation.html = '<h1>We are thrilled to be working with you!</h1> <p>we will be sure to meet all of your needs</p>'
		mail.send(confirmation)
		return redirect(url_for('index'))#, _external = True, _scheme = 'https'))

	return render_template('lol.html')

# @app.route('thank_you_pg')



if __name__=='__main__':
	app.run(debug=True)