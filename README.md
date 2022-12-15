# Pi Lane-Tracking

This is the final project for ECE 5725(Embedded Operating Systems). We built a robot car that can track a lane on the road. The car is controlled by a Raspberry Pi 4B and a Pi camera attatched on the gimbo. The car is able to detect the lane and adjust its direction to keep the lane in the center. The car is also able to detect obstacles and immediately stop to avoid collision. Below chart shows our assembly of the car. 

![alt text](https://github.com/ChenTungChu/ECE5725_Final_Project/blob/main/test/car.jpg?raw=true)

We used openCV as our image processing library and camera calibration, use color transforms and gradients with Sobel Edge Filter to detect the edges of the car. Then We applied our Region Of Interest (ROI) as lane detection area to rectify images with 9 sliding windows. We determined the car should steer left or right by calculating the curvature of the lane and the position with respect to the center. Also, we implemented ultrasonic distance sensor for obstacle detection.

## Contributors
Jasmin An(ja499)
Chen-Tung Chu(cc2396)