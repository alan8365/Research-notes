###### tags: #Paper

## Metadata

Author: 

[source]()

## Abstract

| Type       | Description |
| ---------- | ----------- |
| Background |             |
| Problem    |             |
| Method     |             |
| Steps      |             |
| Exception  |             |
| Contribute |             |
| Limitation |             |

### Reading purpose
- [[Monthly paper report]]
- [[Dentist CV project]]
### Judgment

## 1. Introduction
### Background
> small object is 0x0 to 32x32

With the rapid development of deep learning, the method of image feature extraction has changed from hand-engineered features to automatic extraction by convolution neural network, which provided major improvements for object detection [1]. 

Despite the remarkable progress, there is a typical dilemma, the detectors often underperform with the small objects.

For instance, the result of FPN equipped with ResNet-50 released in [10] is (mAP:36.7%, APs:21.1%, APm:39.9%, APl:48.1%), accuracy on the small objects (APs) is almost half of that on the middle size (APm) or large size (APl)

### Motivation

![[Pasted image 20220518100930.png]]

we propose a novel Feedback-driven loss function which can train the detectors in a more balanced way and bridge the gap between small object detection and common object detection.

The core idea is that the less the loss for small objects, the larger the computational loss gain of the small objects, during the training iterations.

## 2. Related work
> one stage and two stage

Object detectors can be mainly divided into two categories: single-stage detectors (YOLO, SSD, Retina Net, etc.) and two-stage detectors (Faster R-CNN, Cascade R-CNN, R-FCN, etc.).

Single-stage detectors directly predict object labels and bounding box coordinates within one image based on the default anchor boxes, which is fast but not accurate enough.

In contrast, two-stage detectors firstly generate a large number of region proposals based on the CNN features and then recognize the proposals with a heavy head.

> small object alleviate strategies.

Whether single-stage object detectors or two-stage object detectors, the performance on the small objects is unsatisfying. Researchers have proposed many strategies to alleviate this problem.

Piotr Dollár et al. presented the FPN (Feature Pyramid Networks) [18], a top-down architecture with lateral connections which is developed for building high-level semantic feature maps at all scales. 

 [19] further proposed a novel network called Image Pyramid Guidance Network (IPG-Net) to make sure both the spatial information and semantic information are abundant for each layer.

Much effort has been put into the network structure, scale variation, and augmentation of the object detectors to bridge the gap between the small object detection and common object detection, but limited work has been done to improve the loss function of the detectors.


## 3. Methodology
### 3.1. Location loss in original Yolo
![[Pasted image 20220518103650.png]]
![[Pasted image 20220518103555.png]]

![[Pasted image 20220518104328.png]]

### 3.2. Feedback-driven loss function in this paper

![[Pasted image 20220518104533.png]]

![[Pasted image 20220518105128.png]]

![[Pasted image 20220518105825.png]]

## 4. Experiments
## 5. Conclusion

## Reference
