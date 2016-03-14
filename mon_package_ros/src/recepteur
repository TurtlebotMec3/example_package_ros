#!/usr/bin/env python
import rospy
from mon_package_ros.msg import MonMessage

# fonction appelee quand on recoit un message
def callback(data):
    	if data.value == data.TITRE0:
        	print('Je joue la chanson numero 0')
    	elif data.value == data.TITRE1:
        	print('Je joue la chanson numero 1')
    	elif data.value == data.TITRE2:
        	print('Je joue la chanson numero 2')
    	elif data.value == data.BRUIT_DESAGREABLE:
        	print('Je joue un bruit desagreable')
    	else:
        	print('Je ne connais pas cette chanson')

def main():
    	rospy.init_node('noeud_recepteur')
    	rospy.Subscriber('mon_topic/message', MonMessage, callback)

	# on couble tant que l'utilisateur n'arrete pas le programme
    	rospy.spin()

if __name__  == '__main__':
    	main()

