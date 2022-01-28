import logging
import random
import pathlib
from time import sleep


working_dir = pathlib.Path(__file__).parent.resolve()
log_file = working_dir.joinpath('server.log')

logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')


def build_random_logs():
    status_key=random.randint(0,3)
    status_message = get_status(status_key)
    message = message_generator(status_key,random.randint(0,3))
    crafted_message = status_message + " " + message
    # will be sent to the log_file
    logging.debug(crafted_message)

def get_status(key):
    dict = {
        0: '[INFO]',
        1: '[ERROR]',
        2: '[WARN]',
        3: '[FATAL]'
    }
    return dict.get(key)

def message_generator(key,status):
    dict = {}
    if (key == 0):
        dict = {
            0: 'A new message has arrieved',
            1: 'There are not pending notifications',
            2: 'The system is up to date',
            3: 'I hope troubeshooting will be that easy',
        }
    elif (key == 1):
        dict = {
            0: 'Something really bad occured',
            1: 'CALL IT, WE ARE IT!!!!',
            2: 'Where is Homer\'s autodestroy buttom',
            3: 'Layer 8 error',
        }
    elif (key == 2):
        dict = {
            0: 'It\'s cold outside',
            1: 'Looks like a human is changing stuff without performing backups',
            2: 'Yikes, how we do not have backups?',
            3: 'We are not getting paid enough',
        }
    elif (key == 3):
        dict = {
            0: 'OMG, someone did an upgrade on prod instead of stagging',
            1: 'Where is your God now?',
            2: 'Hold you horses, looks like QA did not catched up this one',
            3: 'Automation is the future they said, but layer 8 alwats hit hard',
        }

    return dict.get(status)   
    

def run(times):
    for x in range(times):
        build_random_logs()
        sleep(1)    