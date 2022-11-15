# ROS-study_pkg

* turtlebot3_gazebo_rviz.launch - rviz настроенный для черепахи  
* tb3_gz_keyboard_rviz.launch - запуск всего вместе  
* rviz_slam_view.launch и tb3_gz_keyboard_slam.launch - задача отделения запуска настроенного под slam rviz от запуска симуляции, slam и управления с клавы  
* gmapping.launch - узел slam  
* tb3_gazebo_start.launch - запуск симуляции с роботом  
* tb3_gz_keyboard_slam.launch - запуск симуляции со slam и управлением, без rviz  
* amcl.launch - запуск алгоритма локализации  
* tb3_gz_keyboard_localization.launch - запуск симуляции с управлением для локализации  
* rviz_localization_view.launch - запуск rviz под локализацию  

