import requests
from .models import EquipmentModel
token = '1153424900:AAG0b31kOcaJ6gh4M3Et30OI7x7jNQJCewE'
# chat_id = '873831562'
chat_id = '1623487'


def EquipmentMessage(data):
    msg = "<b>Заказ Оборудования</b>\n"
    summ = 0
    for equipment in data['items']:
        obj = EquipmentModel.objects.get(id=equipment['id'])
        msg += "<b>"  + obj.ru_title + "</b>" + " <b>по цене: </b>" + str(obj.price) + " <b>в кол-во: </b>" + str(equipment['quantity']) + "\n"
        summ +=obj.price * equipment['quantity']
    msg += "<b>Итого: </b>" + str(summ) + " сум.\n"
    return msg


def CateringMessage(data):
    msg = "<b>Заказ Кейтеринга</b>\n"
    msg += "<b>Ивент:</b> {}\n<b>Количество гостей:</b> {}\n<b>Доп информация:</b> {}\n".format(data['event'], data['guestNumber'], data['message'])
    return msg


def StandMessage(data):
    msg = '<b>Заказ Стэнда</b>\n'
    msg += "<b>Доп информация: {}</b>".format(data['message'])
    return msg


def RegisterMessage(data):
    msg = '<b>Регистрация посетителей</b>\n'
    msg += "<b>Ивент:</b> {}\n<b>Доп возможности:</b> {}\n<b>Число гостей:</b> {}\n<b>Доп информация:</b> {}\n".format(data['event'], ", ".join(data['extraOptions']), data['guestNumber'], data['message'])
    return msg


def ContactMessage(data):
    msg = '<b>Обратная связь</b>\n'
    msg += "<b>Сообщение: {}</b>\n".format(data['message'])
    return msg


def telegram_test(data):
    msg = ""
    tel = data['phone']
    name = data['name']
    address = "Не указано"
    if 'address' in address:
        address = data['address']
    if 'cart' in data:
        msg += EquipmentMessage(data['cart'])
    elif 'catering' in data:
        msg += CateringMessage(data['catering'])
    elif 'stand' in data:
        msg += StandMessage(data['stand'])
    elif 'registration' in data:
        msg += RegisterMessage(data['registration'])
    elif 'contact' in data:
        msg += ContactMessage(data['contact'])
    msg += "<i>Инициалы:</i>\n🧔🏻 <u>{}</u>\n📞 <u>{}</u>\n🏢 {}\n".format(name, tel, address)
    response = requests.get('https://api.telegram.org/bot{}/sendMessage'.format(token), {
        'chat_id': chat_id,
        'text': msg,
        'parse_mode': 'HTML'
    })


    # response = requests.get('https://api.telegram.org/bot{}/getUpdates'.format(token))
    # print(response.content)