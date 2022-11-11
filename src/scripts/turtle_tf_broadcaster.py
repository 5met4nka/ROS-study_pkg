#!/usr/bin/env python

import rospy # импорт основного модуля
import tf # импорт модуля TF
import math
import time
from tf.transformations import quaternion_from_euler # импорт, который исключает необходимость прописывания `tf.transformations.quaternion_from_euler()`
from turtlesim.msg import Pose # импорт модуля содержащий типы сообщений из пакета

def handle_turtle_and_carrot_pose(msg):

    angle = int((time.time() * 100)) % 360
    print(angle)
    x = 1 * math.cos(angle * 0.0174533)
    y = 1 * math.sin(angle * 0.0174533)
    br = tf.TransformBroadcaster() # получаем объект публикатора информации TF
    br.sendTransform((msg.x, msg.y, 0), quaternion_from_euler(0, 0, msg.theta), rospy.Time.now(), turtlename, "world")
    br.sendTransform((x, y, 0), quaternion_from_euler(0, 0, 0), rospy.Time.now(), "carrot", "turtle1")

if __name__ == '__main__':

    rospy.init_node('tf_turtle_and_carrot')
    turtlename = rospy.get_param('~turtle_tf_name')
    rospy.Subscriber('input_pose', Pose, handle_turtle_and_carrot_pose)
    rospy.spin()