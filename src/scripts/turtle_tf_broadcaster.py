#!/usr/bin/env python

import rospy # импорт основного модуля
import tf # импорт модуля TF
from tf.transformations import quaternion_from_euler # импорт, который исключает необходимость прописывания `tf.transformations.quaternion_from_euler()`
from turtlesim.msg import Pose # импорт модуля содержащий типы сообщений из пакета

def handle_turtle_pose(msg):
      br = tf.TransformBroadcaster() # получаем объект публикатора информации TF

      br.sendTransform((msg.x, msg.y, 0), quaternion_from_euler(0, 0, msg.theta), rospy.Time.now(), turtlename, "world")

if __name__ == '__main__':

      rospy.init_node('tf_turtle')

      turtlename = rospy.get_param('~turtle_tf_name')

      rospy.Subscriber('input_pose', Pose, handle_turtle_pose)
      rospy.spin()