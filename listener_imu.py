import rospy
from std_msgs.msg import Float64MultiArray
import math
def callback(data):
    # rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    # print(data.data)
    fusionPose = data.data
    print("r: %f p: %f y: %f" % (math.degrees(fusionPose[0]), 
    math.degrees(fusionPose[1]), math.degrees(fusionPose[2])))
    #print(fusionPose)

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("imu", Float64MultiArray, callback)
    rospy.spin()


if __name__ == '__main__':
    listener()