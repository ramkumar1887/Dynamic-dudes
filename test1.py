from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)


@app.route('/voice', methods=['POST'])
def voice():
    response = VoiceResponse()
    dial = response.dial()

    # Dial the first participant
    dial.number('+917899980025')

    # Dial the second participant
    dial.number('+918660024495')

    # Start a conference with both participants
    dial.conference('MyConference')

    return str(response)


if __name__ == '__main__':
    app.run(debug=True)
