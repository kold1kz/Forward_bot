from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

btnMain=KeyboardButton('Главное меню')


# --- Forward menu ----
btnAlex = KeyboardButton('Отправить Александру')
btnEmail =KeyboardButton('Набрать свой адрес')
btnFast = KeyboardButton('Сразу отправить Александру, без настроек')
btnHelp = KeyboardButton('Помощь')
forwardMenu =ReplyKeyboardMarkup(resize_keyboard=True).add(btnAlex, btnEmail, btnFast)

# --- Setting mail ---
btnSubject = KeyboardButton('Написать тему письма')
btnAddForward = KeyboardButton('Добавить свой текст в письмо')
btnNext = KeyboardButton('Далее')
setMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnSubject, btnAddForward, btnNext)

# --- Forward ----
btnForward = KeyboardButton('Отправить')
btnBack = KeyboardButton('Назад')
ForMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnForward, btnBack)
