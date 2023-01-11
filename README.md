# ROS-study_pkg
* 1-3  
* roslaunch study_pkg turtle.launch - запуск игры с rviz (морковка крутиться вокруг черепахи)
* roslaunch study_pkg turtle2.launch - запуск игры с rviz (в этом случае вторая черепаха гоняется за морковкой)
---
* 5-6  
* TURTLEBOT3_MODEL=waffle roslaunch study_pkg tb3_gz_keyboard_rviz.launch - запуск всего вместе  
*   
* roslaunch study_pkg gmapping.launch - узел slam  
* roslaunch study_pkg tb3_gazebo_start.launch - запуск симуляции с роботом  
*   
* TURTLEBOT3_MODEL=waffle roslaunch study_pkg tb3_gz_keyboard_rviz.launch - запуск симуляции со slam и управлением, с rviz  
* roslaunch study_pkg gmapping.launch - запуск gmapping
*   
* TURTLEBOT3_MODEL=waffle roslaunch study_pkg tb3_gz_keyboard_slam.launch - запуск симуляции со slam и управлением, без rviz  
* roslaunch study_pkg rviz_slam_view.launch - запуск rviz под все это дело
---
* 7  
* amcl.launch - запуск алгоритма локализации  
*   
* roslaunch study_pkg tb3_gz_keyboard_localization.launch - запуск симуляции с управлением для локализации  
* roslaunch study_pkg rviz_localization_view.launch - запуск rviz под локализацию  
---
* 9  
* move_base.launch - запуск movebase  
*   
* roslaunch study_pkg tb3_gz_mb_slam.launch - запуск симулятора с навигацией по карте (без телеуправления)  
* roslaunch study_pkg rviz_slam_mb_view - запуск rviz, настроенный под slam и movebase  
*   
* roslaunch study_pkg tb3_gz_mb_localization.launch - запуск симуляции, movebase и локализации (amcl)  
* roslaunch study_pkg rviz_localization_mb_view.launch - rviz, настроенный под movebase и amcl  
