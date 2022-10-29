#!/usr/bin/env python
# необходимо для запуска, она сообщает системе о том,
# что данный файл необходимо запускать через интерпретатор `python`

import rospy # импортируем основной модуль `rospy`
from std_msgs.msg import String # импортируем сообщения типа String

rospy.init_node('talker') # задает название, которое будет зарегистрировано в рабочей экосистеме ROS
pub = rospy.Publisher('my_chat_topic', String, queue_size=10)
rate = rospy.Rate(1) # используется для выдерживания частоты выполнения кода, Гц

def start_talker():
    msg = String() # создаем объект сообщения
    i = 0
    while not rospy.is_shutdown(): # бесконечный цикл, пока ROS система работает
        hello_str = str(i) # формируем сообщение
        i += 2
        rospy.loginfo(hello_str)  # вывод в терминал информации (содержание сообщения)

        msg.data = hello_str # заполнение сообщения
        pub.publish(msg) # публикация сообщения в топик

        rate.sleep() # сон в соответствии с выдерживаемой частотой

try:
    start_talker()
except (rospy.ROSInterruptException, KeyboardInterrupt):
    rospy.logerr('Exception catched')