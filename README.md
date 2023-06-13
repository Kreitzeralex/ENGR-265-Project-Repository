# ENGR-265-Project-Repository
## Overview of culminating projects from ENGR 265: Engineering Decision Making. 

### Heartbeat Detection 
Raw heartbeat data is given and we were asked to count the number of heartbeats. I used a modified Pan-Tompkins Algorithm to filter the data along with the find peaks function found in the scipy library to determine the peaks which were the heartbeats. Below is the raw voltage data and then the final filtered result. 

#### Raw Data Example
![image](https://github.com/Kreitzeralex/ENGR-265-Project-Repository/assets/123031007/3b77588f-acba-472a-918b-a0ee7a0480e3)

#### Filtered Data
![image](https://github.com/Kreitzeralex/ENGR-265-Project-Repository/assets/123031007/42a7a652-a6b8-465b-be8a-bb7fd9663b7e)

### Drop Jump
RSI is a measure of the relative strength of an athlete and it is measured using force plates. The test is conducted by asking the athlete to drop onto a force plate and then jump back off as quickly as possible. To calculate RSI you need initial landing on the plate and final landing after the athlete jumps. The challenge was to find the initial and final landing points with force data from the plate. The image below is an example of the how the test is conducted and how RSI is found. The next image is the graphed data with the landing and takeoff points. 
![image](https://github.com/Kreitzeralex/ENGR-265-Project-Repository/assets/123031007/0e7d8583-f36b-4ba2-a201-414cd0450cf1)
![image](https://github.com/Kreitzeralex/ENGR-265-Project-Repository/assets/123031007/6266511b-af79-4d54-bcb9-e06bdc5d54e9)




### Tensile Testing 
Material testing data was taken from another Engineering class at JMU and analysis was done in python. The script takes a csv file with stress and displacement data and outputs a stress-strain graph as well as a 0.2% offset yield chart. The chart made using matplotlib is shown below.
![image](https://github.com/Kreitzeralex/ENGR-265-Project-Repository/assets/123031007/56b5f6ef-0a70-4372-901e-d1a7e4d94dc9)



### Covid-19 Data
This was the first culminating assignment which required grabbing data from the New York Times Covid-19 database and answering questions such as which 7-day period had the most Covid-19 cases in Harrisonburg City. All questions that were answered are written at the top of the Covid_19_Data.py script. 


