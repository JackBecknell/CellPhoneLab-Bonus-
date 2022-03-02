from cell_phone import CellPhone

my_phone_with_cracked_screen = CellPhone('Samsung')
print(my_phone_with_cracked_screen.contacts)
my_phone_with_cracked_screen.message_recieved("Have you heard about your car's extended warranty?")
my_phone_with_cracked_screen.message_recieved("CONGRATS!!!YOU'VE BEEN SELECTED TO WIN $1,000")
print(my_phone_with_cracked_screen.messages)
my_phone_with_cracked_screen.send_message('Stop texting me spam you filthy animals')
my_phone_with_cracked_screen.vibrate_on_off(True)
my_phone_with_cracked_screen.is_vibrate_on()


