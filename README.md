# lane-detection
lane detection system on highways


The artificial intelligence model architecture, which is planned to be used in the line tracking system, is based on the principles of fast semantic segmentation (fastseg). One of the main reasons for choosing the architecture in accordance with the Fastseg principle is that it is successful in obtaining real-time output. The fastai library, which was developed by using the Torch library, was used in the development of the artificial intelligence architecture. MobileV3Small architecture is used. The dataset was developed using the CARLA simulator. The dataset contains 600 data for validation, 600 for 5000 tests for training.
Since increasing the data in the dataset will increase the success of the model and prevent the risk of overfitting, noise and motionblur have been added to each photo. As a result, an increase of 200% was achieved in the data set used in training. The albumentations library was used for these operations. With the implementation of these procedures, the success rate increased by 7 points. The success and loss rates of the model are shown in Figure 1. In the model training, the number of epochs was determined as 10.

![image](https://user-images.githubusercontent.com/71135790/190428600-d8aeef13-0fe7-46a8-b1db-3d4a612e6975.png)
Figure 1

The visual given as input to the developed artificial intelligence model is shown in Figure 2. The photo taken as output is detailed in figure 3 and figure 4.

![image](https://user-images.githubusercontent.com/71135790/190429254-ff84520a-1358-4361-bb5e-b51658c80e59.png)

Figure 2

![image](https://user-images.githubusercontent.com/71135790/190429312-b054dcb4-0483-424f-bf74-e0af0b8ac9e2.png)

Figure 3

![image](https://user-images.githubusercontent.com/71135790/190429660-8179deb4-15e8-4751-8173-8800f15b21e0.png)

Figure 4

Result
In the test results I made, the artificial intelligence model is quite suitable for real use. One of the main reasons for reaching such a conclusion is because the prediction speed of my model is 14.7 ms. This corresponds to approximately 68 fps. Figure 5 shows how many seconds of delay my model creates in each recall.

![image](https://user-images.githubusercontent.com/71135790/190430647-0b97b8d2-0b06-4ddc-893e-0ca75749f6e6.png)

Figure 5

The images taken from the interface developed on the Qt platform are shown in Figure 6.

![image](https://user-images.githubusercontent.com/71135790/190430827-1168fb70-1e77-4905-9f58-71e9fac1df27.png)

![image](https://user-images.githubusercontent.com/71135790/190430863-e2853e09-3784-4ba6-9c90-0dc61a4f970b.png)

Figure 6


