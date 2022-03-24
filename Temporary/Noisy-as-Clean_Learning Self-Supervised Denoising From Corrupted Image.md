###### tags: #Paper

## Metadata

Author: 

[source](https://ieeexplore-ieee-org.nutc.idm.oclc.org/document/9210208)

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
- [[Seminar (II) (1102)]]
### Judgment

## I.Introduction
> denoising problem intro

Image denoising is an ill-posed inverse problem to recover a clean image x from the observed noisy image y=x+no

Previously supervised denoising networks unavoidably suffer from a domain gap problem: both the image priors and noise statistics in training are different from those of the real-world test images.

> Paper strategy

We propose a “Noisy-As-Clean” (NAC) strategy for training self-supervised denoising networks. In our NAC, we directly train an image-specific network by taking the corrupted image y=x+no as the “clean” target.

Our work reveals that, when the noise is “weak”, a self-supervised network trained directly on the corrupted image can obtain comparable or even better performance than supervised networks on image denoising.

![[Pasted image 20220324013215.png]]

## II.Related Work



## III.Theoretical Background of “Noisy-As-Clean”
![[Pasted image 20220324015324.png]]

![[Pasted image 20220324015009.png]]

## IV.Learning Self-Supervised Denoising Networks by “Noisy-as-Clean”

## V.Experiments

### A. Synthetic Noise Removal With Known Noise

![[Pasted image 20220324020220.png]]

### C. Practice on Real Photographs

![[Pasted image 20220324020809.png]]

### D. Ablation Study

#### 1) Differences From DIP
![[Pasted image 20220324021255.png]]

#### 3) Comparison With Oracle:
![[Pasted image 20220324021744.png]]

## VI.Conclusion

We observed that it is possible to learn a self-supervised network only with the corrupted image, approximating the optimal parameters of a supervised network learned with a pair of noisy and clean images.

As a potential future work, we will apply our NAC strategy on noisy document text images, since it is difficult to obtain their clean counterparts.

## Reference
