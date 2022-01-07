# Assembly-Line-Object-Detector
Here I develope a model to be used for an automated quality assurance unit in the manufacturing assembly. 

The [folder](https://drive.google.com/drive/folders/1NPSe6jSGzYp8Xd81uxs9kF1o5BPGgz7p?usp=sharing
) with all relevent files.


I utilize transfer learning with pretrained mobile_net deep neural network because the final trained neural network will run on a rasperry PI and hence needs to be light weight. 

## Example of detection

| Sample Input        | Output Detection           |
| :---------------------: |:-------------------------:| 
| <img src="https://github.com/AbdulRahmanSilmy/Machine-Assembly-Object-Detector/blob/main/images/input/bluecoverpcbtopfuse_16.jpeg" width="200" height="200" />| <img src="https://github.com/AbdulRahmanSilmy/Machine-Assembly-Object-Detector/blob/main/images/output/download%20(2).png" width="200" height="200" /> | 
| <img src="https://github.com/AbdulRahmanSilmy/Machine-Assembly-Object-Detector/blob/main/images/input/empty_25.jpeg" width="200" height="200" /> | <img src="https://github.com/AbdulRahmanSilmy/Machine-Assembly-Object-Detector/blob/main/images/output/download%20(3).png" width="200" height="200" /> |  
