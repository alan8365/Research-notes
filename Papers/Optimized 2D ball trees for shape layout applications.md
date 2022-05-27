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
As mentioned in Section 2.2, the RDMA algorithm introduced in [19] is an efficient algorithm for producing a ball collection approximating a given shape rasterized as a binary image. In order to determine the fidelity of this approximation to the original shape, we devised the following procedure: (1) the same shape is rasterized again into a larger image; (2) the ball collection is also rasterized into a binary image of the same size; (3) different pixels are counted (see Fig. 3).

![[Pasted image 20220526212630.png]]

We propose a new algorithm that, like the RDMA approach, starts from the circles of the squared distance transform (SDT).

Rather than computing a medial axis, though, these circles are first sorted by size in decreasing order, and tested for approximate containment in any of the circles previously considered. Circles that pass the test are discarded

This new algorithm, which we call _SDT_ + _filter_, runs slower than the RDMA approach, since every element of the SDT must be tested against all others.

Fortunately, it is possible to use an online ball tree (see Section 4.2) to speed up the search for containing balls, i.e., only balls intersecting the query ball expanded by $\epsilon$ have to be tested

Fig. 5e shows the result of the algorithm for $\epsilon=2$ , containing 144 balls and yielding 6350 different pixels, or 4.6% of the total. We note that this result contains less balls and yields a smaller error than the one obtained with the RDMA approach (Fig. 5d),

![[Pasted image 20220526213512.png]]

![[Pasted image 20220526214517.png]]
> error rate的公式呢???

## 4. Ball tree construction

we focus on their use in tasks such as collision detection and assorted Euclidean distance-related queries, using Omohundro’s seminal work on ball tree construction [1] as a yardstick.

Six ball tree construction algorithms were implemented [34]. The first three follow the discussion of Omohundro [1] and we refer to them as the KD construction, Online and Bottom up algorithms.

Next, we present a quadratic algorithm (Q) and two others that use Voronoi neighborhoods [35], [36], which we call V0 and V1.

- KD
	- $O(n \log n)$
	- EL: $O(n^2)$
- Online
	- $O(n(\log n)^2)$
	- $O(n^2)$
- Bottom up
	- $O(n^2(\log n^2))$
- Q
	- $O(n^2)$
- V0
	- $O(n^2 \log(n))$
- V1
	- $O(n^2 \log(n))$

## 5. Query algorithms
The evaluation of a particular ball tree [construction algorithm](https://www-sciencedirect-com.nutc.idm.oclc.org/topics/computer-science/construction-algorithm "Learn more about construction algorithm from ScienceDirect's AI-generated Topic Pages"), in addition to an analysis of its time and space complexity, typically includes measurements of certain characteristics of trees built from assorted inputs.

> 看完決定要不要講，有點細又不講距離怎麼算

## 6. Construction and query experiments

## Reference
