###### tags: #Paper

## Metadata

Author: 

[source](https://www-sciencedirect-com.nutc.idm.oclc.org/science/article/pii/S1361841518304699)

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
- Study self-supervised learning for medical image.
### Judgment

## 1. Introduction
> Point out how important CNN and data are.

In medical image analysis, CNNs have also demonstrated significant improvement when applied to challenging tasks such as disease classification and organ segmentation

Large amounts of training data with manual labels have been crucial in many of these successes.

Crowd sourcing has limited applicability in medical imaging because annotation usually requires expert knowledge.

> What is SSL and How to use in medical image.

Self-supervised learning aims at supervised feature learning where the supervision tasks are generated from data itself.

Therefore, self-supervised learning is a good option to explore the unlabelled images to improve the CNN performance in case where only limited labelled data is available.

> Identify 2 SSL method 

Two existing self-supervised learning strategies are applicable in our cases, namely, the prediction of the relative positions of image patches (Doersch et al., 2015) (the RP method) and local context prediction (Pathak et al., 2016) (the CP method).
![[Pasted image 20220222145936.png]]

> What is the paper's proposed method.

We propose a novel self-supervised learning strategy for medical imaging.

Specifically, given an image, two small patches are randomly selected and swapped. Repeating this operation a number of times leads to a new image for which the intensity distribution is preserved but its spatial information is altered.

A CNN is then trained to restore the altered image back to its original version.

> How many advantages the method has.

The proposed context restoration strategy has three advantages

1) CNNs trained on this task focus on learning useful semantic features
2) CNN features learned in this task are useful for different types of subsequent tasks including classification, localization, and segmentation
3) Implementation is simple and straightforward. 

We evaluate our novel self-supervised learning strategy in three different common problems in medical image analysis, namely classification, localization, and segmentation. 

In all three tasks, the pretraining based on our context restoration strategy is superior to other self-supervised learning strategies, as well as no self-supervised training.

## 2. Related work

> RP method

In the RP method, it was proposed to predict the relative positions between a central patch and its surrounding patches in a 3 × 3 patch grid (Doersch et al., 2015).

First, the relative position between two patches could have multiple correct answers.

Second, it was reported that CNNs could complete the self-supervised learning tasks by learning trivial features, instead of semantic features that are useful in other discriminative tasks such as classification and segmentation. 

Third, the RP method is based on patches, which do not convey information about the global context of images.

> CP method

They proposed an idea which trains CNNs to learn how to inpaint missing information in images with patchy context removed.

They reported that if the removed patch is always in the centre of an image and in the square shape (Fig. 1(c)), CNNs would only focus on the central context.

The removal of context changes the image intensity distribution. Thus the resulting images belong to another domain and the learned features may not be useful for images in the original domain.

## 3. Self-supervision based on context restoration
### 3.1. Context restoration

![[Pasted image 20220222155407.png]]

Inspired by existing self-supervised learning strategies, a good self-supervised learning strategy should exhibit three key features: 
1) Features learned in the self-supervised training stage should be representative of the image semantics.
2) Self-supervised pretraining is useful for different types of subsequent tasks. 
3) The implementation should be simple. 

### 3.2. Network architectures

![[Pasted image 20220222162049.png]]

## 4. Experiments and results
### 4.1. Context restoration results

![[Pasted image 20220222162850.png]]

### 4.2. Fetal standard scan plane classification

 2D US imaging is the most widely used medical imaging modality to assess the health of the fetus. 

US images often have low quality because of noise, artefacts, shadows, etc. Therefore, interpreting fetal US images is challenging. 

![[Pasted image 20220223203640.png]]

![[Pasted image 20220222164124.png]]

### 4.3. Abdominal multi-organ localization

In many medical image analysis problems, localization anatomical structures is a prerequisite.

However, manual cropping requires expert knowledge and costly.

![[Pasted image 20220223204650.png]]

![[Pasted image 20220222165330.png]]

### 4.4. Brain tumour segmentation
Gliomas are the major brain tumours occurring in adults. They are routinely assessed using MR imaging (Bakas et al., 2017b).

Accurate segmentation of gliomas on MR image is a key step for quantification.

![[Pasted image 20220223204706.png]]

![[Pasted image 20220222165754.png]]

## 5. Discussion and conclusion

### Contribution

In this paper, we proposed a novel self-supervised learning strategy based on context restoration. This enables CNNs to learn useful image semantics without any labels.

We have validated the proposed context restoration pretraining on three types of representative tasks in medical image analysis,

In our experiments, we found that if the reduction of training data causes significant performance decrease, the context restoration pretraining can offer significant performance improvement over the baselines.

## Reference