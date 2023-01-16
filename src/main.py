import datetime
import logging
import asyncio
from back import *
from aiogram import Bot, types, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

import menu as nav
from config import TOKEN
from datetime import datetime


#logging level set
logging.basicConfig(level=logging.INFO)

# Объект бота
bot = Bot(token=TOKEN)
# Диспетчер для бота
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())
#init bd


@dp.message_handler(state=TestStates.TEST_STATE_1)
async def first_test_state_case_met(msg: types.Message):
    all_in_mail.Subject=msg.text
    state = dp.current_state(user=msg.from_user.id)
    await state.reset_state()
    await bot.send_message(msg.from_user.id,"Тема добавлена", reply_markup=nav.setMenu)
    # except:
    #     await bot.send_message(msg.from_user.id,"Error, не удалось добавить тему", reply_markup=nav.setMenu )


@dp.message_handler(state=TestStates.TEST_STATE_2)
async def second_test_state_case_met(msg: types.Message):
    all_in_mail.Subject=msg.text
    state = dp.current_state(user=msg.from_user.id)
    await state.reset_state()
    await bot.send_message(msg.from_user.id,"Адрес добавлен", reply_markup=nav.setMenu)
    # except:
    #     await bot.send_message(message.from_user.id,"Error, не удалось добавить адрес")



@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    await bot.send_message(msg.from_user.id, 'Привет {0.first_name}!\nОтправьте мне сообщение, картинки или звуковое сообщение, что бы переслать его на почту'.format(msg.from_user), reply_markup=nav.ReplyKeyboardRemove())

# try:
#     all_in_mail.send(all_in_mail.Text, all_in_mail.Subject, all_in_mail.Forward_to, all_in_mail.Image, all_in_mail.audio)
#     await bot.send_message(msg.from_user.id, "Письмо отправлено!", reply_markup=nav.ReplyKeyboardRemove())
#     all_in_mail.clean()
#     await bot.send_message(msg.from_user.id, "Отправьте мне сообщение, картинки или звуковое сообщение, что бы переслать его на почту!")
# except:
#     await bot.send_message(msg.from_user.id, "Error, проблема в отправлении!") 
    

@dp.message_handler()
async def bot_message(msg: types.Message):
    if msg.text =='Sudakova':
        await bot.send_message(msg.from_user.id, "Поздравляю, ты нашел пасхалку!\n\nЛера- этой прекрасной девушке повезло получить от меня в голову мячом!)")
    
    elif msg.text == 'Далее':
        await bot.send_message(msg.from_user.id, "Последний этап", reply_markup=nav.ForMenu)

    elif msg.text == 'Сразу отправить Александру, без настроек':
        await bot.send_message(msg.from_user.id, all_in_mail.send_mail(all_in_mail.Text, all_in_mail.Subject, all_in_mail.Forward_to, all_in_mail.Image, all_in_mail.Audio))
        all_in_mail.clean()
        await bot.send_message(msg.from_user.id, "Отправьте мне сообщение, картинки или звуковое сообщение, что бы переслать его на почту!")
         
    elif msg.text == 'Выбрать адрес отправки':
        await bot.send_message(msg.from_user.id, "Выбирайте", reply_markup=nav.forwardMenu)

    elif msg.text == 'Написать тему письма':
        await msg.reply("То что вы мне отправите, будет в теме письма", reply_markup=nav.ReplyKeyboardRemove())
        state = dp.current_state(user=msg.from_user.id)
        argument=1
        await state.set_state(TestStates.all()[int(argument)])
    
    elif msg.text == 'Набрать свой адрес':
        await msg.reply("По этому адрессу будет отправлено письмо, может работать некорректно", reply_markup=nav.ReplyKeyboardRemove())
        state = dp.current_state(user=msg.from_user.id)
        argument=2
        await state.set_state(TestStates.all()[int(argument)])

    elif msg.text == 'Отправить Александру':
        all_in_mail.Forward_to=""   #"alekslindov79@yandex.ru"
        await bot.send_message(msg.from_user.id, "Письмо будет отправлено Александру", reply_markup=nav.setMenu)

    elif msg.text == 'Отправить':
        await bot.send_message(msg.from_user.id, all_in_mail.send_mail(all_in_mail.Text, all_in_mail.Subject, all_in_mail.Forward_to, all_in_mail.Image, all_in_mail.Audio))
        all_in_mail.clean()
        await bot.send_message(msg.from_user.id, "Отправьте мне сообщение, картинки или звуковое сообщение, что бы переслать его на почту!")
         
    elif msg.text == 'Назад':
        await bot.send_message(msg.from_user.id, "Переход назад", reply_markup=nav.setMenu)

    else:
        all_in_mail.Text+=msg.text
        all_in_mail.Text+="\n"
        await bot.send_message(msg.from_user.id, "Текст добавлен в сообщение\n",reply_markup=nav.forwardMenu)


@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def content_type_example(msg: types.Message):
    all_in_mail.Image+=msg.photo
    await msg.photo[-1].download()
    await msg.answer('Фото добавленно в письмо', reply_markup=nav.forwardMenu)

# @dp.message_handler(content_types=types.ContentTypes.AUDIO)
# async def content_type_example(msg: types.Message):
#     all_in_mail.

async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates =True, on_shutdown=shutdown)
    