#!/usr/bin/env python
# необходимо для запуска, она сообщает системе о том,
# что данный файл необходимо запускать через интерпретатор `python`

import rospy # импортируем основной модуль `rospy`
from std_msgs.msg import String # импортируем сообщения типа String

# далее пишем обработчик приема сообщений из топика,
# регистрируем узел и подписываемся на топик с указанием обработчика.
# обработчик вызывается каждый раз, как узел получает сообщение.
def callback(msg):
    rospy.loginfo("I heard %s", msg.data)

rospy.init_node('listener')
rospy.Subscriber('my_chat_topic', String, callback, queue_size=10) # не требуется сохранять объект подписки, возврат функции игнорируется
rospy.spin()