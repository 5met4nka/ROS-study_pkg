#!/usr/bin/env python
# необходима для запуска,
# она сообщает системе о том, что данный файл необходимо запускать через интерпретатор `python`

import rospy # импортируем основной модуль `rospy`
from study_pkg.msg import Control # импортируем модуль сообщения

def topic_cb(msg):
	rospy.loginfo('I heard Steer is: %d and Speed is: %d' % (msg.speed, msg.steer)) # Вывод в терминал
	# информации (содержание сообщения)

rospy.init_node('listener')
rospy.Subscriber('my_chat_topic', Control, topic_cb, queue_size=10)
rospy.spin() # будет удерживать программу рабочей до тех пор, пока ROS не завершится или узел не бует прерван