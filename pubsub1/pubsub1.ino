/*
   rosserial PubSub Example
   Prints "hello world!" and toggles led
*/
#include <Encoder.h>

#include <ros.h>
#include <std_msgs/Int64.h>
#include <std_msgs/Empty.h>

ros::NodeHandle  nh;

std_msgs::Int64 str_msg;
ros::Publisher chatter("chatter", &str_msg);


//pins for the encoders
Encoder myEnc(20, 21);

void setup()
{
  Serial.begin(57600);
  Serial.println("Basic Encoder Test:");
  nh.initNode();
  nh.advertise(chatter);

}
long oldPosition  = -999;

void loop()
{
  long newPosition = myEnc.read();
  if (newPosition != oldPosition) {
    oldPosition = newPosition;
    Serial.println(newPosition);
  }
  str_msg.data = newPosition;
  chatter.publish( &str_msg );
  nh.spinOnce();
 
}
