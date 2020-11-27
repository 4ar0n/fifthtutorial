import requests #pip3 install requests
from pprint import pprint
from datetime import datetime

now = datetime.now()
pprint (now)
now_str = now.strftime("%Y-%m-%d %H:%M:%S")
pprint (now_str)
subject = "Testing at %s" %(now_str)

# references:
# https://requests.readthedocs.io/en/master/api/#requests.Response

# https://documentation.mailgun.com/en/latest/user_manual.html?highlight=attachment#tracking-messages

def send_simple_message():

    response = requests.post(
        "https://api.mailgun.net/v3/DOMAIN/messages",
        auth=("api", "API-KEY"),
        data={"from": "Mailgun Sandbox <postmaster@DOMAIN>",
            "to": "Aaron Lee <leesiusing@gmail.com>",
            "subject": "Hello Aaron Lee",
            "text": "Congratulations Aaron Lee, you just sent an email with Mailgun!  You are truly awesome!"})

    print (response)

send_simple_message()


def send_message(to , subject , text):

    response =  requests.post(
        "https://api.mailgun.net/v3/DOMAIN/messages",
        auth=("api", "API-KEY"),
        data={"from": "Mailgun Sandbox <postmaster@DOMAIN>",
            "to": to,
            "subject": subject,
            "text": text})

    # print (type(response))
    pprint (response)
    pprint (response.text)
    pprint (response.json())
    pprint (response.link)
    pprint (response.ok)


subject = "Testing at %s" %(now_str)
send_message(to = "Aaron Lee Siu Sing <leesiusing@gmail.com>" ,subject= subject , text = "Content Inside")

dt = 'Fri, 27 Nov 2020 13:00:00 +0800'
def send_scheduled_message(to , subject , text):
    response = requests.post(
        "https://api.mailgun.net/v3/DOMAIN/messages",
        auth=("api", "API-KEY"),
        data={"from": "Mailgun Sandbox <postmaster@DOMAIN>",
            "to": to,
            "subject": subject,
            "text": text,
            "o:deliverytime": dt,
            "timestamp": 1606428663})

    pprint (response.json())

send_scheduled_message(to = "Aaron Lee Siu Sing <leesiusing@gmail.com>" ,subject= subject , text = dt)

def send_complex_message(to , subject , html , attachement1, attachement2):

    response =  requests.post(
        "https://api.mailgun.net/v3/DOMAIN/messages",
        auth=("api", "API-KEY"),
        files=[("attachment", ("test.jpg", open(attachement1,"rb").read())),
               ("attachment", ("test.txt", open(attachement2,"rb").read()))],
        data={"from": "Mailgun Sandbox <postmaster@DOMAIN>",
             "to": to,
            "subject": subject,
            "html": html})

    # print (type(response))
    pprint (response)
    pprint (response.text)
    pprint (response.json())
    # pprint (response.link)
    pprint (response.ok)


attachement1 = "/Users/aaronlee/Downloads/13388-NP2724.jpg"
attachement2 = "/Users/aaronlee/Downloads/job_6095 Untitled.pdf"
send_complex_message(to = "Aaron Lee Siu Sing <leesiusing@gmail.com>" , subject = subject , html = html , attachement1=attachement1 , attachement2=attachement2 )

# https://my.stripo.email/cabinet/#/template-editor/?projectId=336388&templateId=610142&type=MY_TEMPLATE&copyCount=1&templateProjectId=127461
htmlpath = "/Users/aaronlee/Documents/python/fifthtutorial/test.html"
f = open(htmlpath, "r")
html = (f.read())

