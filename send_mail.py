import smtplib;


def send_mail():

    server = smtplib.SMTP("smtp.gmail.com",587,465);
    server.starttls();
    server.login("tonytirox@gmail.com","target3334")
    server.sendmail("tonytirox@gmail.com","tonytirox@gmail.com","text");
    server.quit();

send_mail();