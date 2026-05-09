import telebot

bot = telebot.TeleBot("...")

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '''Привет! Я бот, который поможет
    тебе выбрать подарок! Напиши мне, кому ты хочешь подарить подарок,
    и я дам тебе несколько идей. Пока что я умею советовать подарки
    программистам, дизайнерам и автогонщикам. Напиши,
    кому ты хочешь подарить подарок.''')


# Обработчик команды /creator
@bot.message_handler(commands=['creator'])
def creator(message):
    bot.send_message(message.chat.id, "Мой создатель Иван Иванов! Лучший программист в мире!")

# Обработчик любых изображений
@bot.message_handler(content_types=['photo'])
def reply_photo(message):
    bot.send_message(message.chat.id, "Какая красивая картинка! Мне очень нравится!")

# Обработчик любых текстовых сообщений
@bot.message_handler(content_types=['text'])
def reply(message):
    text = message.text.lower()
    if "программисту" in text:
        reply = "Идеи подарков программисту: умная лампа, механическая клавиатура, книга по Python."
    elif "дизайнеру" in text:
        reply = "Идеи подарков дизайнеру: графический планшет, набор цветных маркеров, стильный блокнот."
    elif "автогонщику" in text:
        reply = "Идеи подарков автогонщику: гоночная игра для консоли, модель гоночного автомобиля, аксессуары для машины."
    else:
        reply = "Извини, я пока могу советовать подарки только программистам, дизайнерам и автогонщикам."

    bot.send_message(message.chat.id, reply)


bot.infinity_polling()

