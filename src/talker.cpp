#include <ros/ros.h> // подключаем заголовки ROS
#include <std_msgs/String.h> // подключаем заголовки типа сообщения

#include <sstream> // подключаем заголовок функции формирования строк

int main(int argc, char **argv)
{
  ros::init(argc, argv, "cpp_talker"); // регистрация узла, третий аргумент - имя регистрации узла в системе

  ros::NodeHandle n; // создание объекта

  ros::Publisher pub = n.advertise<std_msgs::String>("cpp_chatter", 1000); /* регистрация топика `cpp_topic`,
  * а также получение объекта публикации. вторым агргументом передается размер очереди сообщений
  */
  ros::Rate loop_rate(1); // создание объекта `Rate` для реализации частоты публикации

  int count = 0;
  while ( ros::ok() )
  {
    std_msgs::String msg; // создаем объект сообщения

    std::stringstream ss; // создаем объект строчного потока

    ss << "hello world " << count++; // с помощью потоков записываем фиксированную строку, а также значение счетчика

    msg.data = ss.str(); // записываем полученную строку (функция `str()` строчного потока) в поле `data` нашего сообщения

    ROS_INFO("%s", msg.data.c_str()); /* после этого выводим в консоль данные, при этом используется `c_str()`,
    * чтобы получить строку в формате С, так как `ROS_INFO()` - аналог функции `printf()`
    */
    pub.publish(msg); // публикуем сформированное сообщение

    ros::spinOnce(); /* в данном случае не играет роли, так как она используется в основном для того,
    * чтобы наша программа проверила приходящие сообщения и вызвала соответствующие `callback` функции.
    * то есть, строка эта должна использоваться, если узел подписывается на какой-то топик. В данной ситуации подписки нет,
    */ соответственно - строка не так важна

    loop_rate.sleep(); // засыпаем до наступления следующего момента, чтобы выдержать частоту
  }

  return 0;
}