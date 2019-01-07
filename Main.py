import imaplib, email

def del_Email():
    box = imaplib.IMAP4_SSL("imap.gmail.com", 993)
    print("Please type in your gmail address!")
    username = raw_input(">> ")
    print("Please type in your Gmail Application-Specific Password if you have two factor authentication enabled. If not just use your normal password!")
    password = raw_input(">> ")
    box.login(username, password)
    box.select("Inbox")
    typ, data = box.search(None, "ALL")
    id_list = data[0].split()

    print("Please type in email addresses that you do not wish to be deleted. Type DONE when you are done!")
    good = []

    while True:
        enter = raw_input(">> ")

        if enter == "DONE":
            break
        else:
            good.append(enter)

    num = 0

    for item in id_list:
        l = id_list[num]
        result, data = box.fetch(l, "(RFC822)")
        raw_email = data[0][1]
        msg = email.message_from_string(raw_email)
        it = msg["From"].find("<")+1
        per = msg["From"][it:][:-1]

        if per in good:
            pass
        else:
            box.store(l, "+FLAGS", "\\Deleted")
            print("Deleting email from '" + per + "'!")

        num = num + 1

    print("Done clearing your inbox!")

    box.close()
    box.logout()

del_Email()
