
# vk_session = vk.AuthSession('+79118350030', '886035vlad')
# vk_session.auth()
# vk = vk_session.get_api()
# print(vk.wall.post(message='Hello world!'))



# import vk
# vk_session = vk.AuthSession("+79118350030", "886035vlad")
# vk_session.auth()
# vk = vk_session.get_api()
# vk.messages.send(users_id=0, messages='hello')

# import vk
# session = vk.Session()
# vk_api = vk.API(session)
# vk_api.users.get(user_id=1)


# import datetime
# from time import sleep
# import vk
#
# def get_status(current_status, vk_api, id):
#     profiles = vk_api.users.get(user_id=id, fields='online, last_seen')
#     if (not current_status) and (profiles[0]['online']):  # если появился в сети, то выводим время
#         now = datetime.datetime.now()
#         print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
#         print('Появился в сети в: ', now.strftime("%d-%m-%Y %H:%M"))
#         return True
#     if (current_status) and (not profiles[0]['online']):  # если был онлайн, но уже вышел, то выводим время выхода
#         print('Вышел из сети: ', datetime.datetime.fromtimestamp(profiles[0]['last_seen']['time']).strftime('%d-%m-%Y %H:%M'))
#         print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
#         return False
#     return current_status
#
# if __name__ == '__main__':
#     id = input("ID пользователя: ")
#     session = vk.Session()
#     vk_api = vk.API(session)
#     current_status = False
#     while(True):
#         current_status = get_status(current_status, vk_api, id)
#         sleep(60)




