import random
import select
from datetime import datetime

access_cmds = ['open', 'close', 'quit']
door_status = {'open': '', 'close': ''}
door_time = {'time':'None'}

def set_password():
    passwd = input('Please Set your one-time Password to gain entrance\n')
    passwd_confirm = input('Please retype your Password\n')
    if passwd == passwd_confirm:
        while True:
            lock_system(passwd)
    else:
        print('Password does not match confirmed password')
        set_password()


def lock_system(passwd):
    action = input("Please enter the following Commands \n"
        "'open' to open the door'\n"
        "'close' to close the door\n"
        "'quit' to stop operation\n")
    if action in access_cmds:
        input_pass(action, passwd)
    else:
        print("Invalid Door Command")
        lock_system()
        
def input_pass(action, passwd):
    pwd = input(f'Please enter your password to {action}\n')
    if pwd == passwd:
        if action == 'open':
            if door_status['open'] == 'open':
                print(f'The door is already open')
                print(f"Door last opened at {door_time['time']}")
            elif door_status['open'] == '':
                door_status['open'] = 'open'
                door_status['close'] = ''
                door_time['time'] = datetime.now()
                print(f'The door is now {action}')
                print(f"Door last opened at {door_time['time']}")
        elif action == 'close':
            if door_status['close'] == 'close':
                print(f'The door is already locked')
                print(f"Door last opened at {door_time['time']}")
            elif door_status['close'] == '':
                door_status['close'] = 'close'
                door_status['open'] = ''
                print(f'The door is now locked')
                print(f"Door last opened at {door_time['time']}")
        elif action == 'quit':
            quit()
    else:
        print("Invalid Access Password")
        input_pass(action)

set_password()

