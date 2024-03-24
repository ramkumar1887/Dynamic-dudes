from twilio.twiml.voice_response import VoiceResponse
response = VoiceResponse()
dial = response.dial()

# Dial the first participant
dial.number('+917899980025')

# Dial the second participant
dial.number('+918660024495')

# Start a conference with both participants
dial.conference('MyConference')