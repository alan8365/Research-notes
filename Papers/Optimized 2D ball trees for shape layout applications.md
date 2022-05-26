###### tags: #Paper

## Metadata

Author: 

[source](https://www-sciencedirect-com.nutc.idm.oclc.org/science/article/pii/S0097849322000231)

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
- [[Computer vision (1102)]] report
### Judgment

## 1. Introduction
> need more

In common off-the-shelf authoring software, elements such as text, pictures and diagrams are approximated by bounding box proxies

![[Pasted image 20220515200527.png]]

### 1.1. Contributions

## 2. Fundamentals
### 2.1. Shape layout
object groups are created either by individually clicking on their elements or by selecting all elements contained or overlapping a given shape drawn by the user—typically a rectangular window.

When groups are allowed to overlap, selecting one or more shapes for additional operations may also become problematic. A typical remedy is to organize content in layers or to allow the user to explicitly manipulate the stacking order between elements or groups.

In Section 7 we deal with these problems by presenting techniques for automatically grouping shapes hierarchically by distance and shifting shapes on the page to avoid overlaps

### 2.2. Shape approximation
Simplified representations for complex objects are useful in scenarios where sacrificing shape fidelity is acceptable in order to increase computation efficiency.

~~A 2D shape  can be represented by a polygon with an arbitrary number of sides. Another alternative is to compute a minimal set of balls  such that the distance from a point to  is bounded by the distance from that point to , within a given error margin .~~

![[Pasted image 20220523213504.png]]

Although the RDMA approach is very efficient and produces good approximations, it may miss some thin features on the image. Another shortcoming is that it cannot be adjusted to produce finer or coarser approximations. In Section 3 we describe another algorithm based on the SDT that addresses these issues.

### 2.3. Ball trees
Ball trees belong to a class of data structures called bounding volume hierarchies (BVH). Clearly, other kinds of BVH could also be used for the same purposes, but we have settled on ball trees because (1) they match our choice for ball collections as geometrical proxies; (2) they provide a convenient way to depict shape clusters (see Section 7.2), and (3) they simplify the computation of penetration depth and direction (see Section 7.3). 

> A ball tree is a binary tree where each node is associated with a portion of space bounded by a ball

![[Pasted image 20220523214353.png]]

## 3. Shape approximation with sets of balls

## Reference
