from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():

	resp = twilio.twiml.Response()
	with resp.message("Hello, Mobile Monkey") as m:
		m.media("https://s-media-cache-ak0.pinimg.com/236x/18/65/05/186505928c838149777b36205bc25684.jpg")
	return str(resp)

if __name__ == "__main__":

	app.run(debug=True)
