#!/usr/bin/env python
# необходима для запуска,
# она сообщает системе о том, что данный файл необходимо запускать через интерпретатор `python`

import rospy # импортируем основной модуль `rospy`
from study_pkg.msg import Control # импортируем модуль сообщения

def start_talker():
    msg = Control() # создаем объект сообщения
    steer = 0
    speed = 0
    while not rospy.is_shutdown(): # бесконечный цикл, пока ROS система работает

        data = 'Speed: %d / Steer: %d' % (msg.speed, msg.steer)

        rospy.loginfo(data) # вывод в терминал информации (содержание сообщения)
        pub.publish(msg) # публикация сообщения в топик

        steer += 2
        speed += 4

        # заполнение сообщения
        msg.steer = steer
        msg.speed = speed

        rate.sleep() # сон в соответствии с выдерживаемой частотой

rospy.init_node('talker') # необходимо зарегистрировать узел в системе ROS
pub = rospy.Publisher('my_chat_topic', Control, queue_size=10) # зарегистрировать топик на публикацию
# с указанием имени, типа сообщения для топика и размера очереди
rate = rospy.Rate(1) # используется для выдерживания частоты выполнения кода, Гц

try:
    start_talker()
except (rospy.ROSInterruptException, KeyboardInterrupt):
    rospy.logerr('Exception catched')