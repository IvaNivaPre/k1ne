import telebot
import openai

bot = telebot.TeleBot("...")
chatgpt = openai.OpenAI(api_key="...")

@bot.message_handler(content_types=['text'])
def send_message(message):
    user_text = message.text

    prompt = (
        "Подбери 3 подходящих идеи подарков. По 1 краткому предложению на вариант."
        f"Описание: {user_text}"
    )

    response = chatgpt.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}],
        max_tokens=300,
        temperature=0.8
    )

    bot.send_message(message.chat.id, str(response.choices[0].message.content), parse_mode='Markdown')


bot.infinity_polling()
