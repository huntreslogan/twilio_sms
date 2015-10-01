from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)

callers = {
	"+4158664966" : "Jessica"
}

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():

	from_number = request.values.get('From', None)
	if from_number in callers:
		message = callers[from_number] + ", thanks for the message!"
	else:
		message = "Monkey, thanks for the message!"

	resp = twilio.twiml.Response()
	resp.message(message)
	# with resp.message("Hello, Mobile Monkey") as m:
	# 	m.media("https://s-media-cache-ak0.pinimg.com/236x/18/65/05/186505928c838149777b36205bc25684.jpg")
	return str(resp)

if __name__ == "__main__":

	app.run(debug=True)
