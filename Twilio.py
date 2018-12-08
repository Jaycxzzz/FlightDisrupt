from twilio_func import send_text_message, send_voice_msg

person_dict = {
    'jayc': '+447731981339',
    'shash': '+447341052333'
}

name = "jayc"
send_text_message(name, person_dict.get(name), "Hello there!")
print("Complete.")