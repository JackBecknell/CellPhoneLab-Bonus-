from inspect import classify_class_attrs
from operator import contains


class CellPhone:

    def __init__(self, pass_model):
        self.model = pass_model
        self.phone_number = '(111)111-1111'
        self.contacts = {
            'contact1' : '(098)765-4321',
            'contact2' : '(102)567-4832',
            'contact3' : '(564)948-2938',
        }
        self.messages = []
        self.vibrate = False

    def message_recieved(self, pass_message):
        print(pass_message)
        self.messages.append(pass_message)

    def vibrate_on_off(self, pass_True_on_False_off):
        if pass_True_on_False_off == True:
            self.vibrate = True
        elif pass_True_on_False_off == False:
            self.vibrate = False
        else:
            print('What are you doing to your phone?')
    
    def send_message(self, pass_message_to_send):
        print(pass_message_to_send)

    def is_vibrate_on(self):
        if self.vibrate == True:
            print('Vibrate is on.')  
        else:
            print('Vibrate is off.')

