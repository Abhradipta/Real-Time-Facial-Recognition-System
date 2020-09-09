# Real-Time-Facial-Recognition-System
Bengalathon – Solution Concept Note

Attempted Challenge:

Face recognition


Challenge Description:

Artificial Intelligence (AI) based facial recognition system for a hassle-free entry and exit management in different types of communities.


Proposed Solution Name:

AI based Entry/Exit management system based on Facial Recognition


Objective:

The objective of the proposed solution is to recognize a face of a person from a trained data set. The solution recognizes the face and displays the name of the person.

The solution is fast and takes less execution time and has a great accuracy even for a smaller number of images in the training data set. It provides a hassle-free solution to an entry and exit management system based on facial recognition in different types of communities.

The solution determines the number of times a person has entered and exited through the system where the solution is implemented.


Brief Description about the Concept:

There are three easy steps to computer coding facial recognition, which are similar to the steps that the brain uses for recognizing faces. These steps are:

Data Gathering: Gather faces data of training space.

Train the Recognizer: Train the model with extracted data.

Recognition:The trained model predicts labels.

OpenCV recognizer framework used is Local Binary Patterns Histograms (LBPH) – cv2.face.LBPHFaceRecognizer_create()

The LBPH Face Recognizer Process It takes a 3×3 window and move it across one image. At each move (each local part of the picture), compare the pixel at the center, with its surrounding pixels. Denote the neighbors with intensity value less than or equal to the center pixel by 1 and the rest by 0. After consuming the whole image data, list of local binary patterns is created. The histogram obtained is unique for each label. The algorithm also keeps track of which histogram belongs to which person. Later during recognition, the process is as follows: 

1. Feed a new image to the recognizer for face recognition. 

2. The recognizer generates a histogram for that new picture. 

3. It then compares that histogram with the histograms it already has. 4. Finally, it finds the best match and returns the person label associated with that best match.


Coding Face Recognition using Python and OpenCV The Face Recognition process is divided into three steps: 

1. Prepare Training Data: Read train data and assign an integer label to each image data. 

2. Train Face Recognizer: Train OpenCV's LBPH recognizer by feeding it the data we prepared in step 1. 

3. Prediction: Introduce some test images to face recognizer and see if it predicts them correctly. 

Now uploading the model to Django server:

The Server model is as follows: 

1.Create an admin panel where he can train the model and start the video detection. 

2.An employee subplot where each user can upload their image and save it for training.

3. A log page where he/she can see at what timestamp he/she was captured by our model. 

4.It can work on multiple devices. 


Required Modules The following modules are needed to be imported in Python 3.5 codebase: 

1. OpenCV 3.2.0 (cv2): This module is used for face detection and face recognition. 

2. os: This module deals in fetching and listing directories. 

3. Numpy: This module deals in computation of vectors and performs scientific calculations. 

4. Django: Python framework for hosting servers based on python backend. 

5. Sql: Default database handler in Django.


Outcome:

The solution detects a face and recognizes it from the training data set of the images stored in the server for hassle free entry and exit in different types of communities. The solution recognizes the face displays the name of the person along with their current image on the display screen. The solution also keeps the count of the number of times a person has entered and exited though the system where the solution is implemented.


Limitations:

The following are the current limitations to the solution:

1. A fair quality of images is required for training the data set and recognition of the face.

2. If multiple faces are very close to each other, it is difficult to extract each face from the image for recognition.

The above limitations can be resolved by:

1.The quality of the images can be made better by using a high-res camera.

2.The size of image in the training data set can be compressed for faster training of the data.

3.Subject spacing should be properly gapped.



Technology: Python | Python Django | OpenCV | Machine Learning | Computer Vision
