[[A Multimodal Event-Driven LSTM Model for Stock Prediction Using Online News]]

## Abstract
- 此研究將影響市場的訊息分為基本面和新聞面。
- 以訊息預測股票由兩類訊息形塑為多模態問題。
- 此問題有兩個明顯的挑戰
	- 如何處理不同類訊息間的相互作用。
	- 如何處理採樣時間存在的異質性。
- 此研究透過張量和事件驅動解決以上兩個問題。
## 1. Introduction
- 效率市場假說指出股價由非情緒化投資人推動。
- 行為經濟學研究中股價則被歸為投資人的認知和感情偏差。
- 理論假設雖不同但都同意波動源於訊息。
- 股市同時受基本面(開盤價、交易量等等)和新聞面影響。
- 因此股市預測是多模態問題。
- 第一個挑戰在於確定基本面和新聞面的相互作用。
	- 傳統將訊息串聯為向量，但卻無法捕捉內在聯繫。
	- 而將訊息張量化則能解決上述問題。
- 第二個挑戰是採樣時間異質性
	- 基本面資料採樣時間為天。
	- 新聞面資料因隨機性而分布不均。
	- 以事件驅動解決異質性問題
## 2. Related Work
### 2.1 Information and Stock Volatility
- 股市訊息的分類
	- 基本資料
	- 媒體資料
- 投資人的決策可能受網路意見影響，導致羊群效應。
### 2.2 Stock Comovements
- 研究波動的主流方法分類
	- 基本面角度
	- 投資人行為角度
- Rashes發現兩個只有名字相似的股票會存在高度正向關，顯見是由非理性情緒產生。
### 2.3 The approaches for quantifying such media-aware movements.
- 股市預測模型可分為三個類別
	- 統計模型
	- 回歸模型
	- 機器學習模型
- 統計模型研究單一特徵與股市的相關性。
- 回歸模型研究特定特徵和市場運動的因果性。
- 然而這兩種類型都難以處理資料源間的聯繫。
- 傳統RNN模型通過向量簡化市場資訊，同樣也忽略了資料源間的聯繫。
## 3. Model Architecture
- 過往研究常將異質資料源串聯為向量。
- 基於向量的特徵忽略了資料源間的聯繫。
### 3.1 Tensor Representation
- 本章介紹如何透過張量表示股市資料。
### 3.2 Tensor Decomposition and Reconstruction
- 本章說明如何透過塔克分解捕捉不同資料源的聯繫。
### 3.3 Stock Relatedness

### 3.4 Multimodal Event-Driven LSTM Model

#### 3.4.1 Event-Driven LSTM Model

#### 3.4.2 Tensor-Based Convolution Operation

## 4. Experimental Evaluation

### 4.1 Experimental Data

### 4.2 Evaluation Settings

### 4.3 Model Parameters

### 4.4 Comparison

### 4.5 Effectiveness of the Proposed Approach

#### 4.5.1 Effectiveness of the Tensor Representation

#### 4.5.2 Effectiveness of the Event-Driven Mechanism

#### 4.5.3 Effectiveness of Stock Relatedness

### 4.6 Investment Simulation

## 5. Conclusion and Future Work