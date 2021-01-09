# Story Time 
In India, due to the pandemic COVID-19 situation , institutes are conducting  online classes 😒.

Just like everyone 🤷‍♂️ , even I was attending allllll the classes like other students , which was manually 😢 meaning "we"(students) had to open the PORTAL which was provided to us by our COLLEGE and there all the links of the classes RESIDED and we had to login to the meeting  according to the TIMETABLE given to us by our college.

But then suddenly out of blue ,one of my classmate messaged me this . 

![](readme.md_images/One.jpeg)

# Task 📝

She asked me if i could build a Zoom bot for her which logs in for her automatically into the classes , provided she provides all the links and the timings of the classes in prior.

Because I was interested in learning automations , therefore took this task and built one 😎 .

# Prerequisites ✔✔✔

* Install "Zoom Desktop app" in your system and also know the path of it.


# Setup instructions ✍🧐 #
* Clone the Github repo
```
git clone https://github.com/Kabir079/Zoom-Bot-Windows-OS-.git
```

* cd into the directory

* Install required libraries (using IDE's terminal or use Command Prompt):
```
pip3 install pyautogui
```
### Note : Path of the image provided to the subprocess to perform automation ### ❗❗

Check the respective path of the images .
If error comes then , accordingly change the path of the images .

### Note : For CSV file ### ❕❕
* Update the timings.csv with the time of the "time of the meeting" (24 hr format) , Meeting Id and password.
* Do not add any additional spaces.(Do not open the csv using excel as it changes the formatting)
* The links must be feeded in the ascending order in respect of time .
# Example : #

![](readme.md_images/two.png)

* time.sleep() function works with a parameter = seconds. 
#### Example : When you write time.sleep(60) ####
 Here "60" , it means "60 seconds" .
 
### Note : Operating System ### ❗❗
This bot is only specifically made for Window OS . But if changes are made in "Source code" , according to the targetted OS , then this bot shall work.
(provided there are no errors in the changes which were made)

# Working 🏃‍♂️ 🚀
* Copy the links and in a notepad and then copy the "Meeting ID" written within each link and paste those respective "Meeting Id's" in the csv file of this project . 
* Check if the time.sleep() in "78","83","88","93" is equal to that of the interval/difference between the links which you have provided in the csv file.
* Go ahead and run the code and Enjoy LAZYNESSSS😂😂
