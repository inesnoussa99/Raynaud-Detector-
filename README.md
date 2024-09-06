# Raynaud's syndrome detecter 
## Introduction 
Our subject focuses on the diagnosis of Raynaud's syndrome, a condition characterized by poor blood circulation in the extremities, particularly in the fingers and, more rarely, in the toes. The diagnosis will be performed through digital image processing from a thermal camera using a Python algorithm with the libraries NumPy, Mediapipe, and Matplotlib along with numerical methods. 
## Project Overview 

In order to get an accurate diagnosis of Raynaud's Syndrom we plot the hand's rewarming curve by averaging the temperatures of the patient's 8 fingers. Then, we plot the first and second derivatives.

Our input data are:

* **temperature.json** : a dictionary containing time as the key and finger temperatures as a list.
* **temperature_debut.txt** : a text file containing the temperatures before the cold water test.
* **Patient-specific data** : age, etc..

Output data

* **A rewarming curve**, i.e., temperature as a function of time.
* Three key data points that allow us to conclude the patient's condition:
    * 𝑅%: the percentage of temperature recovery.
    * 𝐺𝑚𝑎𝑥: the maximum of the first derivative of the average temperature.
    * 𝑇𝑙𝑎𝑔: the time corresponding to the maximum value of the second derivative.

* The diagnostic result in the form of a matplotlib.pyplot figure.



###  Prerequisites 

Before you begin, make sure you have the following software and libraries installed:

* Python 3.x
* NumPy: pip install numpy
* Matplotlib: pip install matplotlib
* Mediapipe : pip install mediapipe
* Tkinter : pip install tkinter 

## Simulation details 

To observe the evolution of finger temperature, we built a Tkinter interface that automatically measures finger temperature by directly connecting the camera to the computer.

**Step 1: Measuring hand temperature before the test**

Provide instructions to the patient to place their hands on the paper, aligning their fingers with the drawing.
Press the "Get coordinates and initial temperatures" button.
After receiving the success message, press the "Verify coordinates" button to ensure the points are correctly located.

**Step 2: Cold water test**

The patient should acclimate to the room temperature for 10 minutes.
Fill the container with water at 10°C and regulate the temperature using a thermometer and ice cubes.
Submerge the hands in 10°C water for 1 minute (surrounded by a plastic bag to avoid altering the skin's emissivity due to water contact).
Note: On the day of the exam, participants were asked to refrain from smoking and performing intense exercise just before the exam to avoid affecting blood circulation .

**Step 3: Continuous monitoring of hand temperature**

Immediately place the patient’s hands on the traced imprints on the paper and press the "Start measuring" button.
Ensure that all fingers correspond to the detected points on the screen and adjust if necessary.
When the finger temperature no longer varies significantly (±0.5°C) for 2 to 3 minutes, press the Esc key to stop the program.
Press the "Show result" button to display a table with the parameters, their respective thresholds, the curves, and the diagnostic resul. 

**Main Algorithms**
Among our main algorithms is the one that allows us to read the camera's images directly on our computers. For this, we used the OpenCV library to read the video stream directly via the USB port.

![Measuring Window](https://s3.hedgedoc.org/hd1-demo/uploads/7ebddb8b-ef7b-4433-b478-086af817052f.png)

**Results**

* For a healthy person ( without Raynaud ) : ![](https://s3.hedgedoc.org/hd1-demo/uploads/66b9a210-0ad1-4ce5-a0a4-14a19ad67c6b.png)
* For a sick person : 
![](https://s3.hedgedoc.org/hd1-demo/uploads/729843cb-210b-42bf-b091-fb9435e9962e.png)
NB : In order to be considered as a person affected by Raynaud's syndrome, at least 2 out of 3 conditions must be checked. 