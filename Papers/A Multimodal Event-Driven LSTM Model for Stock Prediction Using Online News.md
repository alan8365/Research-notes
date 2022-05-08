###### tags: #Paper

## Metadata

Author: 

DOI: 
Cited: 

[source](https://ieeexplore-ieee-org.nutc.idm.oclc.org/abstract/document/8966989)

## Abstract

| Type       | Description                                                                                                                                |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Background | In finance, it is believed that market information, namely, fundamentals and news information, affects stock movements.                    |
| Problem    | The strategy ignores the interactions among different modes;The heterogeneity of the data in terms of sampling time.                       |
| Method     | tensor-based event-driven LSTM model to address these challenges.                                                                          |
| Steps      |                                                                                                                                            |
| Exception  |                                                                                                                                            |
| Contribute | Experiments performed on the China securities market demonstrate the superiority of the proposed approach over state-of-the-art algorithms |
| Limitation |                                                                                                                                            |

### Reading purpose
- [[Monthly paper report#MOMO 202203xx week 3]]
- Study how to model online news to stock prediction.
### Judgment

## 1. Introduction

### Background

> 股票價格的影響理論，好像有點冗，值得砍掉

A company's stock price reflects investor perception of its ability to earn and grow profits in the future.

The traditional efficient market hypothesis (EMH) states that the price of a stock is always driven by ‘unemotional’ investors [1], [2]. 

In behavioral finance studies, stock movements are attributed to investors’ cognitive and emotional biases [4].

Although the two theories are based on different views regarding how information shapes stock movements, both agree that the volatility of stock markets stems from the release, dissemination and absorption of information [5].

> 股市受何影像的實證論文

In previous studies, scholars have found that stock movements are affected by various sources of information, including transaction data, news, social media, and search behavior [6], [7], [8].

Essentially, stock markets are affected by multiple information sources, fundamentals (e.g., turnover, opening prices, and trading volumes) and financial news [12].

Thus, the problem of modeling stock movements is essentially a multimodal learning problem.

### Motivation

> 為什麼要用tensor

The first challenge lies in identifying the joint effects of fundamental data and news information on stock markets.

The traditional strategy is to concatenate these information into a compound vector and utilize various learning models.

However, such vector-based models may ignore the inherent links among multiple sources of information and thus fail to capture their interconnections.

To overcome this challenge, some scholars have modeled multidimensional information with tensors to achieve better performance [16], [17].

> 甚麼是heterogeneity of the sampling times

Another important issue facing multimodal models is the heterogeneity of the sampling times among different modes.

The fundamental data are characterized by continuous values sampled at equal time intervals (i.e., one day). 

By contrast, news information consists of discrete values sampled at nonequal time intervals because of the randomness of the occurrence of news events.

In previous studies, this problem has typically been solved by using only a portion of the available data;

In addition, previous studies on media-aware stock movements have focused on only the one-to-one problem, in which news articles about a company are assumed to affect only that company

### 

> 貢獻啦

To address the above challenges, we propose a multimodal event-driven long short-term memory (LSTM) model with several unique contributions, as follows.

We first represent the complicated market information space with tensors to preserve the interconnections among different information modalities.

We then propose an event-driven LSTM model to address the heterogeneity of the sampling times in different modes.

We also consider the indirect influence of related companies on media-aware stock movements by constructing a media-based enterprise network to reshape the market information space represented by tensors.

Experiments performed on one full year of data on the China securities market demonstrate the superiority of the proposed approach over state-of-the-art algorithms

## 2. Related Work

### 2.1 Information and Stock Volatility

> 股市訊息種類和訊息影響波動

Stock market information can be roughly categorized into three subgroups: fundamental data, media information and a combination of the two [12].

In particular, investors’ decisions can be influenced by the opinions of others as expressed via online media, which may result in herd behavior in investment. 

For example, Schumaker and Chen experimented with several textual news representation approaches to study the effects of breaking news on stock movements [10].

### 2.2 Stock Comovements

> 基本面和投資人行為如何共同影響股市波動。

There are two mainstream methods of studying stock comovements: from the perspective of fundamentals and from the perspective of investor behavior.

in modern behavioral finance, it is believed that irrational behaviors of investors cause the comovements of related stocks. 

For example, Rashes found a highly abnormal positive correlation between two companies with similar names but nothing else in common, caused by the irrational feelings of investors [31].

Web media provide a platform for expressing the options of experts and the public moods of investors, which inevitably affect investor behavior and can even elicit herd behavior [9].

### 2.3 The approaches for quantifying such media-aware movements.

> 各種方法預測股市的彙整

There are three mainstream classes of such models: statistical models (originating from statistics), regression models (originating from econometrics) and machine learning models (originating from computer science).

![[Pasted image 20220228105155.png]]

> 非機器學習方法的回顧和缺點

Statistical models emphasize the correlations between a single feature and stock markets [7], [8].

For example, Moat et al. applied the Wilcoxon test to identify the linkage between a company's browsing frequency on Wikipedia and its stock fluctuations.

Econometric models focus on the causal relationships between specific features and market movements [12], [32], [33].

However, both statistical models and econometric models often have difficulty preserving the interconnections among multiple data sources and thus fail to capture their joint effects on stock performance.

> DNN應用回顧

Inspired by the application of recurrent neural networks (RNNs) to time-series problems, LSTM models have been widely applied to study media-aware stock movements [21], [41]. 

However, these approaches simplify the market information space by adopting a vector representation, which ignores the interconnections among different information modes.

## 3. Model Architecture

A common strategy in previous studies has been to concatenate information from these heterogeneous data sources into a compound vector. 

However, these vector-based models treat different information sources as independent features, ignoring the inherent links between them and thus failing to properly capture stock movements [16].

![[Pasted image 20220308151354.png]]

### 3.1 Tensor Representation

![[Pasted image 20220308151708.png]]

$$
\begin{equation*}
{ P_{t}^{+}=\frac{N_{t}^{+}}{N_{t}^{+}+N_{t}^{-}}, P_{t}^{-}=\frac{N_{t}^{-}}{N_{t}^{+}+N_{t}^{-}}, D_{t}=\frac{N_{t}^{+}-N_{t}^{-}}{N_{t}^{+}+N_{t}^{-}}}, \tag{1} 
\end{equation*}
$$

### 3.2 Tensor Decomposition and Reconstruction

Tucker decomposition is applied to decompose the tensor $X$ into $C \times _{1}R_1 \times _{2}R_2$ [42]. Here, each factor matrix $R_k (k=1,2)$ describes one distinct facet of the information space of the stock market

The core tensor $C$ reflects the strength of the relations between these two facets.

### 3.3 Stock Relatedness

### 3.4 Multimodal Event-Driven LSTM Model

#### 3.4.1 Event-Driven LSTM Model

#### 3.4.2 Tensor-Based Convolution Operation

## 4. Experimental Evaluation

we conducted a series of experiments using actual market transaction data from January 1, 2015, to December 31, 2015.

### 4.1 Experimental Data

Fundamental data: This dataset contains the financial statuses of 100 companies listed on the China Securities Index (CSI 100) between January 1, 2015, and December 31, 2015.

Media data: We selected 45,021 news data points related to the 91 selected companies listed on the CSI 100 from www.eastmoney.com, which is one of the largest financial information websites in China.

![[Pasted image 20220507163810.png]]

### 4.2 Evaluation Settings

![[Pasted image 20220507164253.png]]

In addition, considering the financial scenario, the Sharpe ratio is applied to measure the investment robustness of the proposed multimodal event-driven LSTM framework.
![[Pasted image 20220507164341.png]]

We take the further step of evaluating the $k$-day-ahead influence of media information.
![[Pasted image 20220507164306.png]]

### 4.3 Model Parameters

### 4.4 Comparison

![[Pasted image 20220507164710.png]]

![[Pasted image 20220507164851.png]]

### 4.5 Effectiveness of the Proposed Approach

#### 4.5.1 Effectiveness of the Tensor Representation
![[Pasted image 20220507165005.png]]
#### 4.5.2 Effectiveness of the Event-Driven Mechanism
![[Pasted image 20220507165049.png]]
#### 4.5.3 Effectiveness of Stock Relatedness
![[Pasted image 20220507165122.png]]
### 4.6 Investment Simulation
![[Pasted image 20220507165312.png]]

![[Pasted image 20220507165328.png]]
## 5. Conclusion and Future Work

### Contribution
We proposed a tensor representation approach for modeling multimodal market information.

we proposed an event-driven memory mechanism to address the sampling heterogeneity among different data sources for multimodal learning.

Our method achieved a return of 136.42 percent in an investment simulation.
### Future work
the proposed tensor-based event-driven LSTM framework can be generalizable to many other multimodal learning problems in which the information space consists of several interacting data modes with sampling heterogeneity. 
	in health care monitoring, both daily monitoring indicators and random sickness records are applied to detect health abnormalities [47].
	the prediction of crop growth in agriculture based on daily growth indicators and uncertain conditions, including rainfall, wind and disasters [48].
## Reference

## Dark Theme CSS

{%hackmd theme-dark %}