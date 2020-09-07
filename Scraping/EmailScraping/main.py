#Importing
import imaplib
import email

#Login in and go to inbox
mail = imaplib.IMAP4_SSL('imap.gmail.com')
username="rishisraja@gmail.com"
password="xxxxxxxxxxxxxxxxxxxxx"
mail.login(username,password)
mail.select("inbox")

#Find data from receiptant and convert to words
typ ,data = mail.search(None,'FROM "ashley.hernandez-munoz@missionary.org"')
print(data)
data=[b'12419']
typ, data = mail.fetch(data[0],"(RFC822)")
raw=data[0][1]
string=raw.decode("utf-8")
message=email.message_from_string(string)

#Print the words from the mail
for part in message.walk():
    if part.get_content_type() == "text/plain":
        body = part.get_payload(decode=True)
        print(body)