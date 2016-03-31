#!/usr/bin/env python
import rospy
from random import *
from mon_package_ros.msg import MonMessage


def main():
    	rospy.init_node('noeud_emetteur')
    	pub = rospy.Publisher('mon_topic/message', MonMessage)
    	rate = rospy.Rate(10)  #10 Hz

    	while not rospy.is_shutdown():
        	variable = MonMessage()
        
# La fonction choide permet de choisir une valeur du tableau de maniere aleatoire
        	variable.value = choice([variable.TITRE0, variable.TITRE1, variable.TITRE2, variable.BRUIT_DESAGREABLE])

        	# on publie le message
        	pub.publish(variable)

        	# Pour fonctionner a frequence fixe
        	rate.sleep()

if __name__ == '__main__':
    	main()

