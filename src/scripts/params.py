#!/usr/bin/env python
# необходима для запуска,
# она сообщает системе о том, что данный файл необходимо запускать через интерпретатор `python`

import rospy # импортируем основной модуль `rospy`
rospy.init_node('params_study')

# Обращение глобально - как видно в начале стоит `/`
# Не обращаем внимания на ns, ищем именно такой путь параметра и никак иначе
rospy.set_param('/ros_glob_param', 'Hi, I am global =)')

# Обращение локально - в начале не стоит `/`
# Допустим мы запустили узел, указав __ns:=my_ns
# Тогда вызов данной функции будет пытаться найти парметр по пути - `/my_ns/my_set` 
rospy.set_param('ros_loc_param', 'Hi, I am local =)')

# Обращение приватно, поиск будет по пути /params_study/private_param
# Если задат ns - он будет добавлен перед именем узла
# Например, ns:=my_ns -> /my_ns/params_study/private_param
rospy.set_param('~ros_priv_param', 'Hi, I am private =)')

# try:
#       not_exist_param = rospy.get_param('i_do_not_exist', 'default_value')
# except:
#       # Not exist or any kind of other problem - set default
#       not_exist_param = 'Okay, now it`s default time =0'

# # Мы этот параметр ставили ранее
# param_name_2_delete = '/ros_glob_param'

# # Проверим список параметров, только уже через Python
# param_list = rospy.get_param_names()
# print(param_list)

# # Наличие можно проверить через функционал ROS    
# if rospy.has_param(param_name_2_delete):
#     print('[ROSWay] Parameter exist')
# else:
#     print('[ROSWay] Parameter not exist')
    
# # И с проверкой удаляем его
# if rospy.has_param(param_name_2_delete):
#     rospy.delete_param(param_name_2_delete)
    
# # Еще раз проверим:
# if rospy.has_param(param_name_2_delete):
#     print('[ROSWay] Parameter exist')
# else:
#     print('[ROSWay] Parameter not exist')