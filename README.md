# Assembly-Line-Object-Detector
Here I developed a model to be used for an automated quality assurance unit in the manufacturing assembly. 

The [folder](https://drive.google.com/drive/folders/1NPSe6jSGzYp8Xd81uxs9kF1o5BPGgz7p?usp=sharing
) with all relevent files.


I utilize transfer learning with pretrained mobile_net deep neural network. The final trained neural network will run on a rasperry PI and needs to be light weight, hence the choice of mobine_net. 

Note this is still a work in progress, more information and improvements will be added.

## Example of detection

| Sample Input        | Output Detection           |
| :---------------------: |:-------------------------:| 
| <img src="https://github.com/AbdulRahmanSilmy/Machine-Assembly-Object-Detector/blob/main/images/input/bluecoverpcbtopfuse_16.jpeg" width="200" height="200" />| <img src="https://github.com/AbdulRahmanSilmy/Machine-Assembly-Object-Detector/blob/main/images/output/download%20(2).png" width="200" height="200" /> | 
| <img src="https://github.com/AbdulRahmanSilmy/Machine-Assembly-Object-Detector/blob/main/images/input/empty_25.jpeg" width="200" height="200" /> | <img src="https://github.com/AbdulRahmanSilmy/Machine-Assembly-Object-Detector/blob/main/images/output/download%20(3).png" width="200" height="200" /> |  


## The process

### Step1: Determine classes present

**Classes:**
-	Empty
-	Black Back Cover
-	Red Back Cover
-	Blue Back Cover
-	Grey Back Cover
-	Black Front Cover
-	Red Front Cover
-	Blue Front Cover
-	Grey Front Cover
-	PCB
-	Top Fuse
-	Rear Fuse

### Step2: Take pictures of classes

Before training the system it is important to gather images that the ML system will be trained on. To do this gather around 15-20 pictures of every image that the ML algorithm will see. This means that you take 15-20 pictures of just a black front cover. Then take another 15-20 pictures of a black front cover with a PCB. Another, 15-20 of the same combination with the top fuse, rear fuse and both fuses at the same time. Repeat this process for every colour front cover. Since the back cover hides everything underneath it, it doesn’t matter what is underneath it. Thus take 15-20 pictures of each colour of back cover present. 

### Step3: Label images
"""script to label images can be included here"""
 <img src="https://user-images.githubusercontent.com/79419793/149260690-0bc37b33-8626-4bf8-b610-5cd8dca9c102.png" width="800" height="400" />

### Step4: Training the machine learning system

The reason we use a pretrained model is that it makes it much easier to train custom images on a pretrained model rather than creating a fresh new algorithm. Due to the raspberry pi’s low processing power, we need to choose a model that has a low speed. A lower speed indicates a faster system due to lower processing required. Luckily these frameworks are easy to identify due to them having mobile in their name such as “CenterNet MobileNetV2 FPN 512x512”. For this guide we will use “SSD MobileNet v2 320x320”. 

Before training begins configuring the pipeline. We want num_classes to equal the number of classes we wrote in the labelImg in this case it would be 12. For batch_size set it to a value around 64-256. For num_steps set it to a value between 5,000 - 10,000 this is due to the fact that the simplicity of this system means that it doesn’t need a large amount of steps for a large training time. If your system is more complex you can use anywhere between 50,000 - 200,000 steps.


Training is best run on google colab because we can take advantage of googles gpus available over the cloud. This [ipynb_file](https://github.com/AbdulRahmanSilmy/Assembly-Line-Object-Detector/blob/main/assembly_line_object_detector.ipynb) walks through the rest of the training process.

#### Graph of training 
<img width="800" alt="image" src="https://user-images.githubusercontent.com/79419793/149263357-2aae6dfb-7ae7-45a4-a063-12485664bca8.png">


### Step4: Evaluation of Model 
""" develope script for model evaluation """


