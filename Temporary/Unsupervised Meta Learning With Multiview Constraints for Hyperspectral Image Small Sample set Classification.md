###### tags: #Paper

## Metadata

Author: Gao, Kuiliang, Bing Liu, Xuchu Yu, and Anzhu Yu.

[source](https://ieeexplore-ieee-org.nutc.idm.oclc.org/document/9769872)

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
- The point is the method, not the success about problem solveing

### Judgment

## I. Introduction
> Background
> HSI是地球觀測拍攝中很重要的部分

Since the 1970s, remote sensing technology has become one of the most important technical means to obtain earth observation information. 

Compared with panchromatic and multispectral images, HSIs contain both rich spectral details and spatial structure information, providing the possibility for accurate identification and classification [1].

> Motivation
> 樣本蒐集困難

As we all know, collecting a large number of high-quality HSI labeled samples is very laborious and time-consuming in practice.

To improve the accuracy of HSI small sample set classification, meta learning methods are introduced and has achieved encouraging results.

> Method
> Meta learning description

Different from conventional deep learning methods, meta learning methods take tasks containing support sets and query sets as the basic units for training, enabling the model to acquire the ability of learning how to learn [38]–[39][40]. 

Typically, meta learning methods first learn more general-purpose knowledge on the source data sets, and then fine-tune the model using a few labeled samples in the target HSIs, to quickly adapt to new classification tasks [41], [42].

> Purpose

The above meta learning-based methods can effectively improve the accuracy of HSI small sample set classification, but they all carry out supervised learning on a labeled source data set, which means that a large number of labeled samples are still required in advance.

We can quickly collect a large number of unlabeled HSIs. Therefore, how to utilize unlabeled HSIs for unsupervised meta learning, to further reduce the number of requisite labeled samples and improve the performance of HSI small sample set classification, is more meaningful in practical application.

## II. Meta Learning-Based HSI Small Sample Set Classification

### A. Supervised Meta Learning

![[Pasted image 20220713160410.png]]

### C. Unsupervised Meta Learning

![[Pasted image 20220713161647.png]]

## III. The Proposed Method

### A. Workflow

![[Pasted image 20220713161920.png]]


## IV. Experiments and Discussion

### A. Experimental Data Sets

![[Pasted image 20220713164034.png]]

### C. Cross-Domain HSI Small Sample set Classification

> 在PC数据集上，UM2L的分类精度略低于有监督元学习方法。在UP、SA和IP数据集上，UM2L的分类精度高于有监督元学习方法。

![[Pasted image 20220713164818.png]]

![[Pasted image 20220713164643.png]]

### E. Hyperparameters Analysis

## V. Conclusion

## Reference
