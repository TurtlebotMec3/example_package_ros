cmake_minimum_required(VERSION 2.8.3)
project(mon_package_ros)

# package indispensable a la compilation
# genmsg permet d'executer la fonction generate_messages plus bas
 find_package(catkin REQUIRED COMPONENTS rospy genmsg)

################################################
## Declare ROS messages, services and actions ##
################################################

# Il faut ajouter ici les messages que nous avons crees
 add_message_files(
   FILES
   MonMessage.msg
 )

# Il faut mettre ici nos dependances quand on en a 
 generate_messages(
   DEPENDENCIES
   # exemple std_msgs
 )

###################################
## catkin specific configuration ##
###################################

catkin_package(
)

#############
## Install ##
#############

# Il faut mettre ici la location de vos scripts pythons
 install(PROGRAMS
   src/emetteur.py
   src/recepteur.py
   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
 )

# On met ici les autres fichiers a installer comme les launch files
 install(FILES
   launch/mon_launch_file.launch
   DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
 )

