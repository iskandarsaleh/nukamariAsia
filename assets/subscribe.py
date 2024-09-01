import re
import json
import smtplib
from email.mime.text import MIMEText
from flask import Flask, request, jsonify

app = Flask(__name__)

def is_email(email):
    pattern = re.compile(r"^[-_.\w]+@(([\w-]+\.)+(ad|ae|aero|af|ag|ai|al|am|an|ao|aq|ar|arpa|as|at|au|aw|az|ba|bb|bd|be|bf|bg|bh|bi|biz|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|com|coop|cr|cs|cu|cv|cx|cy|cz|de|dj|dk|dm|do|dz|ec|edu|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gh|gi|gl|gm|gn|gov|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|in|info|int|io|iq|ir|is|it|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|mg|mh|mil|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|museum|mv|mw|mx|my|mz|na|name|nc|ne|net|nf|ng|ni|nl|no|np|nr|nt|nu|nz|om|org|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|pro|ps|pt|pw|py|qa|re|ro|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|sk|sl|sm|sn|so|sr|st|su|sv|sy|sz|tc|td|tf|tg|th|tj|tk|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|um|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)$|((\d{1,3}\.){3}\d{1,3}))$")
    return pattern.match(email)

@app.route('/', methods=['POST'])
def subscribe():
    email_to = 'saleh.iskandar@nukamari.com'
    subscriber_email = request.form.get('email', '').strip()

    if not is_email(subscriber_email):
        return jsonify({'valid': 0, 'message': 'Insert a valid email address!'})

    # Send email
    subject = 'New Subscriber (erine)!'
    body = f"You have a new subscriber!\n\nEmail: {subscriber_email}"
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = subscriber_email
    msg['To'] = email_to

    try:
        with smtplib.SMTP('localhost') as server:
            server.sendmail(subscriber_email, [email_to], msg.as_string())
    except Exception as e:
        return jsonify({'valid': 0, 'message': f'Failed to send email: {str(e)}'})

    return jsonify({'valid': 1, 'message': 'Thanks for your subscription!'})

if __name__ == '__main__':
    app.run(debug=True)

