#!/usr/bin/env python

import rospy # импорт основного модуля
import tf # импорт модуля TF
import math as m
from tf.transformations import quaternion_from_euler # импорт, который исключает необходимость прописывания `tf.transformations.quaternion_from_euler()`
from turtlesim.msg import Pose # импорт модуля содержащий типы сообщений из пакета

# def x_trans():

#     while True:
#         angle += 1
#         if angle >= 360:
#             angle = 0
#         x = 1*m.cos(angle*0.0174533)
#         return float(x)

def handle_carrot_pose(msg):
    br = tf.TransformBroadcaster() # получаем объект публикатора информации TF
    br.sendTransform((msg.x, msg.y, 0), quaternion_from_euler(0, 0, 0), rospy.Time.now(), "carror", "turtle1")

if __name__ == '__main__':

    rospy.init_node('carrot_satellite')
    rospy.Subscriber('input_pose', Pose, handle_carrot_pose)
    rospy.spin()