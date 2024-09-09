
def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    if recipient == sender:
        print("Нельзя отправить письмо самому себе!")
        return
    nestandrt = "Письмо успешно отправлено с адреса"
    if sender != "university.help@gmail.com":
        nestandrt = "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! " + nestandrt
    var_domen=[".com", ".ru", ".net"]
    f1 = False
    f2 = False
    for i in var_domen:
        if i in recipient: f1 = True
        if i in sender: f2 = True
    if f1 == True and f2 == True and "@" in recipient and "@" in sender:
        print(nestandrt, sender, "на адрес", recipient)
    else:
        print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru',
           sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru',
           sender='urban.teacher@mail.ru')
send_email('Это сообщение для проверки связи', 'vasyok1337.gmail.com')