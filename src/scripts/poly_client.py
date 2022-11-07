#!/usr/bin/env python
# необходима для запуска,
# она сообщает системе о том, что данный файл необходимо запускать через интерпретатор `python`

import rospy # импортируем основной модуль `rospy`
from study_pkg.srv import Poly, PolyRequest, PolyResponse # импортируем модуль типа сервиса `Poly` вместе с типом ответа

rospy.wait_for_service('poly') # функцию ожидания регистрации сервиса

try:
	poly_srv = rospy.ServiceProxy('poly', Poly) # получаем объект сервиса функцией
	req = PolyRequest(x=7)
	resp = poly_srv(req)

	rospy.loginfo('Response: %s' % resp.y) # вывод в терминал информации
except rospy.ServiceException:
	rospy.logerr("Service call failed: %s" % e)