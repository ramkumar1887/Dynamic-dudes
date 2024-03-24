from twilio.rest import Client

# Your Twilio account SID and auth token
account_sid = 'YOUR_SIP_TOKEN'
auth_token = 'YOUR_AUTH_TOKEN'

client = Client(account_sid, auth_token)

conference = client.conferences('CFb123456789abcdef0')

# Add a participant to the conference
participant1 = conference.participants.create(
    to='participant1',
    from_='From_Number',
    early_media=True,
    muted=False,
    start_conference_on_enter=True
)
# Add a participant to the conference
participant2 = conference.participants.create(
    to='participant1',
    from_='From_Number',
    early_media=True,
    muted=False,
    start_conference_on_enter=True
)
# Print the participant SID
#print(participant.sid)
