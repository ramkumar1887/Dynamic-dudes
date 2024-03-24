from twilio.rest import Client

# Your Twilio account SID and auth token
account_sid = 'AC26095c77e51c64c63431e7c1c743341d'
auth_token = 'aad47f181a0c92ffa288e3ffd4accfc8'

client = Client(account_sid, auth_token)

conference = client.conferences('CFb123456789abcdef0')

# Add a participant to the conference
participant1 = conference.participants.create(
    to='+917899980025',
    from_='+16505294569',
    early_media=True,
    muted=False,
    start_conference_on_enter=True
)
# Add a participant to the conference
participant2 = conference.participants.create(
    to='+918660024495',
    from_='+16505294569',
    early_media=True,
    muted=False,
    start_conference_on_enter=True
)
# Print the participant SID
#print(participant.sid)