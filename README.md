# Replacing You

--- 
Project with OpenCV and Python.
Our project name is Replacing You. It's a program that replaces a person with a picture when you deviates from the camera frame in webcam.


# Key points

***1. Connecting camera***
- connecting with webcam and reading the webcam
- when cannot read webcam " There is no camera " phrase is printed
- when read webcam, output into window called 'test'

***2. Detecting face***
- haarcascade_frontalface_default.xml

***3. Detecting face in different aspect***
- haarcascade_profileface.xml

***4. Loading a image from User***
- a picture needed to substitute user's face when out of frame

***5. Replacing with picture***
- when a user is out of frame, replacing with picture that is get from user

# Used package and reference
**1. haarcascade_frontalface_default.xml to detect frontalface**
- Download from Github at [*official Github site address*](https://github.com/opencv/opencv/tree/master/data/haarcascades)

**2. haarcascade_profileface.xml to detect sideface**
- Reference from OpenSource Lecture week 13 ppt by Prof.Youngmin Oh

# Results
