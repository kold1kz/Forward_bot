import sqlite3

class SQLighter:

    def __init__(self, database):
        """Подключаемся к БД и сохраняем курсор соединения"""
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def subscriber_exists(self, user_id):
        """Проверяем, есть ли уже юзер в базе"""
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `subscriptions` WHERE `user_id` = ?', (user_id,)).fetchall()
            return bool(len(result))

    def add_user(self, user_id):
        """Добавляем нового пользователя"""
        with self.connection:
            return self.cursor.execute("INSERT INTO `subscriptions` (user_id) VALUES(?)", (user_id,))        

    def update_subscription(self, user_id, status):
        """Обновляем статус подписки пользователя"""
        with self.connection:
            return self.cursor.execute("UPDATE `subscriptions` SET `status` = ? WHERE `user_id` = ?", (status, user_id))

    def get_user_city(self, user_id):
        """Ищем город пользователя"""
        with self.connection:
            return self.cursor.execute("SELECT city FROM 'subscriptions' WHERE user_id = ?",(user_id,)).fetchall()
   def get_time(self, user_id):
        """Берем время пользователя"""
        with self.connection:
            return self.cursor.execute("SELECT time FROM 'subscriptions' WHERE user_id = ? and status=True",(user_id,)).fetchall()

    def close(self):
        """Закрываем соединение с БД"""
        self.connection.close()