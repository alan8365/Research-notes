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
- 傳統金融中使用皮爾森相關係數計算股票間關聯性。
- 此研究將新聞中同時提及的股票作關聯，提及新聞越多關聯愈強。
### 3.4 Multimodal Event-Driven LSTM Model
- 新聞隨機時間出現的特性會使LSTM的長期依賴機制失效。
#### 3.4.1 Event-Driven LSTM Model
- 主要透過在LSTM的output gate加上新聞事件資訊來實現事件驅動。
#### 3.4.2 Tensor-Based Convolution Operation
- 合併張量間關係的方式是使用卷積對各張量和權重運算，所以是卷積式LSTM。
## 4. Experimental Evaluation
### 4.1 Experimental Data
- 基本面資料蒐集2015整年度的CSI100公司資料。
- 新聞面從中國財經新聞網站蒐集了CSI100有關的45021條新聞。
### 4.2 Evaluation Settings
- 模型評估的指標為方向準確率(DA)跟馬修斯相關係數(MCC)。
- DA只與正確數量佔總數的多少有關，無法評估不平衡資料的情況。
- MCC則考慮了所有四個象限的指標。
- 同時也使用夏普率評估模型所做出的投資穩健性。
### 4.3 Model Parameters
略
### 4.4 Comparison
- 在針對股票方向的預測上此研究贏過諸多經典模型和當時最先進的TeSLA模型。
### 4.5 Effectiveness of the Proposed Approach
#### 4.5.1 Effectiveness of the Tensor Representation
- 此節比較向量和張量對於模型的好壞，在傳統LSTM的三項實驗中張量贏過兩項，在事件驅動LSTM中則張量全贏。
- 作者推測張量有一場失敗的原因在於該實驗同時考慮開盤和收盤價，這為模型帶來額外的資訊。
- 說的好像只有向量享受到額外資訊張量沒有似的。
#### 4.5.2 Effectiveness of the Event-Driven Mechanism
- 此節比較事件驅動的有無，在向量和張量根基兩種模型中事件驅動都贏過傳統LSTM。
#### 4.5.3 Effectiveness of Stock Relatedness
- 此節比較如何處理新聞對多支股票的影響而非只是處理傳統一對一影響。
- 第一種方式是參考媒體企業網路中的聯繫為參考。
- 第二種是本研究的方法，將新聞中重複提及的公司做連結。
- 第一種方式好過不考慮對多支股票的影響，第二種方式好過第一種。
### 4.6 Investment Simulation
- 此節實驗模型用於交易的表現，若預測股票將上漲則買入或放空後六天結算，實驗三個月。
- 該模型表現超過TeSLA和大盤指數等等交易策略。
- 同時模型的夏普率也最高，代表在風險和報酬間的權衡得當。
- 實驗時間有夠短，還沒有考慮在熊市和牛市情況下分別長期實驗，公信力欠缺。
## 5. Conclusion and Future Work
- 此研究所提出的張亮表示方法可推廣於更多多模態問題中，例如醫療保健監測等等。