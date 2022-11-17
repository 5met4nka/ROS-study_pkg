# ROS-study_pkg

* turtle.launch - запуск игры с rviz
---
* turtlebot3_gazebo_rviz.launch - rviz настроенный для черепахи  
* tb3_gz_keyboard_rviz.launch - запуск всего вместе  
* rviz_slam_view.launch и tb3_gz_keyboard_slam.launch - задача отделения запуска настроенного под slam rviz от запуска симуляции, slam и управления с клавы  ---
* gmapping.launch - узел slam  
* tb3_gazebo_start.launch - запуск симуляции с роботом  
* tb3_gz_keyboard_slam.launch - запуск симуляции со slam и управлением, без rviz  
---
* amcl.launch - запуск алгоритма локализации  
* tb3_gz_keyboard_localization.launch - запуск симуляции с управлением для локализации  
* rviz_localization_view.launch - запуск rviz под локализацию  
---
* move_base.launch - запуск movebase  
* tb3_gz_mb_slam.launch - запуск симулятора, slam и movebase  
* rviz_slam_mb_view.launch - запуск rviz, заточенного под slam и movebase  
* tb3_gz_mb_localization.launch - запуск симуляции, movebase и amcl  
* rviz_localization_mb_view.launch - запуск rviz, настроенного под amcl и movebase  
---
* move_base.launch - запуск movebase  
* tb3_gz_mb_slam.launch - запуск симулятора с навигацией по карте (без телеуправления)  
* rviz_slam_mb_view - запуск rviz, настроенный под slam и movebase  
* tb3_gz_mb_localization.launch - запуск симуляции, movebase и локализации (amcl)  
* rviz_localization_mb_view.launch - rviz, настроенный под mb и amcl  
