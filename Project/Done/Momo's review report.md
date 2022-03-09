[[A recent overview of the state-of-the-art elements of text classification]]

將文章依照outline拆成數段，每一段描述內容

- [x] 1. Introduction (3889 chars, 3 cycle)
- [x] 2. Related work (7933 chars, 3 cycle)
- [x] 3. Overview of a review method
	- [x] 3.1 Text classification framework (1770 chars, 2 cycle)
	- [x] 3.2. Review method (6137 chars, 2 cycle)
- [x] 4. Qualitative analysis of text classification studies
	- [x] 4.1. Problem and objectives of text classification (2410 chars, 2 cyclee)
	- [x] 4.2. Qualitative analysis of studies
		- [x] 4.2.1. Data acquisition (817 chars)
		- [x] 4.2.2. Data analysis and labelling
		- [x] 4.2.3. Feature construction and weighting (2806 chars, 1 cycle)
		- [x] 4.2.4. Dimensionality reduction (5481 chars, 2 cycle)
		- [x] 4.2.5. Training of classification models (3707 chars, 1 cycle)
		- [x] 4.2.6. Solution evaluation (1845 chars, 1 cycle)
	- [x] 4.3. Summary of qualitative analysis (3316 chars, 1 cycle)
- [x] 5. Quantitative analysis of studies
	- [x] 5.1. Research questions (1236 chars, 1 cycle)
	- [x] 5.2. Research topics (2478 chars, 1 cycle)
	- [x] 5.3. Publication time (1134 chars, 1 cycle)
	- [x] 5.4. Journals (1910 chars, 1 cycle)
	- [x] 5.5. Distribution of publications by countries and a cooperation network (2735 chars, 1 cycle)
	- [x] 5.6. Distribution of the number of authors in publications (649, 1 cycle)
	- [x] 5.7. Summary of quantitative analysis (3498 chars, 1 cycle)
- [x] 6. Conclusions (6591 chars, 2 cycle)
## TODO
- Paragraph modify
## Abstract
資料蒐集 (data collection)
標籤資料分析 (data analysis for labelling)
特徵建構和加權 (feature construction and weighing)
特徵篩選和投影 (feature selection and projection)
分類模型訓練 (training of a classification model)
解決方案評估 (solution evaluation)
## 1. Introduction
描述文本分類定義。說明文本分類不單關於模型訓練，還包含了資料前處理、轉換、維度縮減等。在文本分類的研究中研究人員或開發新分類系統或改進現有分類系統中元素。

過去的文本分類回顧論文因指出關鍵問題時至今日依舊有用，但也因不包含最新研究而過時。並且過去的回顧只強調機器學習技術和演算法，或專注於特定領域。這導致這些研究無法負荷對文本分類越來越大的興趣。

此研究旨在克服上述困難。此研究對文本分類進行了整體回顧，並產生研究地圖。此研究目標如下
1. 提取並呈現文本分類的必要過程，其中包括常見用語，以此作為基本框架。該框架可被稱為文本分類地圖。
2. 列舉各階段所用之新舊技術。透過質性分析系統性地確定這些技術。
3. 透過量化分析展示領域研究趨勢

研究團隊認為沒有類似的過往研究。此研究系統化的增強了分類系統建模知識。此研究表明識別、發現、開發文本分類的新面向或升級既有部分是可能的。
## 2. Related work
能接觸到的回顧研究多關注於五項元素：
(1)文本預處理，例如tokenisation、stop-word移除
(2)文本建模，例如將文本表示為適合被處理的形式
(3)特徵篩選和投影
(4)機器學習建模
(5)評估方法

列表說明四篇回顧論文是否涉及某項元素和底下特定項目。

## 3. Overview of a review method

### 3.1 Text classification framework
介紹前面提到的框架如何被定義

資料蒐集。文本分類的第一步，從各式來源蒐集原始資料組成資料集。
資料分析和標籤。分析資料以給定資料標籤。
特徵建構和加權。利用資料建構特徵並計算特徵加權。
特徵篩選和投影。將和標籤不相關的特徵移出，將互相相關的特徵投影至低維。
模型訓練。訓練模型找出特徵和標籤的關係。
解決方案評估。利用指標確認訓練模型的好壞。

### 3.2 Review method
說明回顧方法所包含的三個階段
- 文章蒐集
	- 選擇文章來源
		- 來源主要是Springer和Elsevier。
		- 少數ACM和IEEE因許可問題被忽略。
		- 排除arXiv因文章未經同儕審查，但有例外。
	- 選擇搜尋限制
		- 只搜尋期刊論文，排除書籍和研討會論文，但有例外。
	- 搜尋和蒐集 
		- 從框架內的六項流程獲得關鍵字。
		- 透過關鍵字從來源搜尋文章並依限制排除。
		- 將各流程中的關鍵字和搜尋結果列於表2。
- 文章質化分析
	- 人工審查每篇文章歸類於框架中
	- 某些情況下一篇文章可能有多個類別
- 文章量化分析
- 該文認為表2中各流程關鍵字等同於文本分類術語字典
## 4. Qualitative analysis of text classification studies
### 4.1. Problem and objectives of text classification
- 文本分類是指為無標籤文本給定標籤的問題
- 文中透過五個面向歸納出數個研究主體
	- 領域
		- 工業、金融、 醫療、網路、專利
	- 分類目的
		- 分類感情、情緒和意見
		- 分類網站中與目前網站相關的資料
		- 於網路爬取中輔助篩選網頁資料
		- 識別推文語言
		- 輔助自動文獻綜述
		- PDF文本段落分類
		- 諷刺偵測
		- 網路恐怖主義言論偵測
		- 分類應用
		- 透過研究贊助組織所對應的應用科學專案分類專案
		- 分類商業性網站
	- 分類任務
		- 二元分類、多元分類、多標籤分類、階層式分類
	- 通用方法
		- 調整單純貝式分類器 (Naive Bayes classifier)
		- 略
		- 新建輕量文本分類器 (lightweight text classifier)
		- 新建可解釋文本方法 (interpretable classification method)
		- 新建可擴展且有效的文本分類器 (scalable and an effective text classifier)
	- 專門方法
		- 暗網分類調查
		- 略
### 4.2. Qualitative analysis of studies
- 依照框架框定的六項流程逐一分析
#### 4.2.1. Data acquisition
> 列出幾個報社跟一組領域專門資料集而已

(資料集來源多來自公開資料集)
#### 4.2.2. Data analysis and labelling
- 公開資料集多為以標籤資料
- 標籤方法主要為分群標籤和逐一標籤
#### 4.2.3. Feature construction and weighting
- 此階段包含三子階段
- 選擇文本表示法
	- 向量空間表示法。將詞轉向量，文本即為向量組
	- 圖形表示法。將文本轉為圖，詞為節點、詞間關係為邊
- 特徵建立
	- 簡單特徵。如uni-grams、bi-grams、n-grams
	- 分類法或本體論特徵
	- 特定領域特徵。如意見、情緒和特定術語
	- 嵌入特徵。如Word2vec和GloVe
	- 簡單語意特徵。如命名實體
	- 主題建模提取特徵。如LSA、PLSA、LDA
	- 元資訊。如維基知識
- 特徵加權
	- 詞頻(tf)、逆文件頻率(idf)、tf-idf
#### 4.2.4. Dimensionality reduction
- 維度縮減可分為兩種，移除不重要特徵和轉換特徵空間
- 特徵篩選
	- filter。透過排序函數選出關聯最高的特徵。
	- wrapper。取特徵的子集合測試結果，擇優存留。
	- embedded。選擇對正確率貢獻最高的特徵，常隱含於學習過程中。
- 特徵投影
	- PCA、SVD、LDA等等
#### 4.2.5. Training of classification models
- 此處列出文本分類所用學習策略
- 監督式學習。給定輸入輸出值(標籤資料)訓練函數。
- 半監督式學習。資料集內同時有標籤和未標籤資料訓練。
- 集成式學習。合併多個分類函數。
- 主動式學習。訓練中存在機制能夠改變資料標籤。
- 遷移式學習。將不同任務訓練結果用於新任務訓練
- 多視角學習。融合不同資料形成的特徵，強化函數一般性。
#### 4.2.6. Solution evaluation
- 此處列出解決方案評估的三道步驟
- 指標選擇
	- precision、recall、accuracy、_F_-score、specificity、area under the curve (AUC)和error rate。
	- 指標的選擇多與任務相關，即結果為二元、多元、多標籤。
	- 也有研究使用模型負荷相關指標，如CPU訓練時間、RAM訓練占用等等。
- 決定測量方法
	- 決定如何分配訓練集交叉實驗。
- 摘要並比較測量結果
	- 從研究中發現以下三種方法用於最後結果摘要。
	- 以統計圖表直觀比較表示結果。
	- 對結果進行統計檢定測量是否有顯著差異。
	- 使用多準則決策方法排名解決方案。
### 4.3. Summary of qualitative analysis
- 缺乏對於多實例標籤的廣泛討論和調查。
- 向量特徵表示比其圖形特徵表示更常被使用和討論。
- 新提出的特徵加權法優於標準而著名的加權法。
## 5. Quantitative analysis of studies
### 5.1. Research questions
- 列出八點研究問題。
- 框架中被研究的最多和最少的流程為何。
- 文章的分布情況為何。
- 各主題文章數量逐年變化量為何。
- 文章在期刊中的分布為何。
- 是否能突出文本分類中的頂級期刊。
- 是否能突出文本分類中出版最廣泛的國家。
- 國家間合作研究的狀況如何。
- 出版物中作者分布數量為何。
### 5.2. Research topics
- 文章被分成九項類別呈現於圖六，類別源於對框架流程的再次切割。
- 關於特徵處理的文章佔總數2/5。
- 圖七呈現九項類別歷年文章數變化。
- 特徵處理中特徵建構和篩選都保持高關注度。
- 特徵加權與特徵投影近年則缺乏關注。
### 5.3. Publication time
- 有2/5的文章發表於2016、2017年。
- 2015年佔比7.85%，2016年佔比21.9%，接近三倍。
- 2005年後發表數量整體呈線性成長趨勢，直至2016年翻倍。
### 5.4. Journals
- Expert System with Application、Knowledge Based-System、Information Processing and Management三本期刊佔文本分類1/3的出版。
- 只出版一篇文章和會議論文構成的其他期刊佔1/3的出版。
- 顯示文本分類領域出版物具分散性。
### 5.5. Distribution of publications by countries and a cooperation network
- 在所有文章中，中國作者佔所有作者的1/4，美國作者佔1/8。
- 在所有跨國合作文章中，中國和美國、中國和香港、中國和澳洲為合作發表數前三名。
- 作者認為此聯繫模式和地理或歷史因素皆無關，說明研究只考慮科學問題。
### 5.6. Distribution of the number of authors in publications
> 3/4 的研究為2~4人團隊進行，1/3是三人團隊，普通。 

略
### 5.7. Summary of quantitative analysis
> 真的總結，啥新東西都沒說

略
## 6. Conclusions
### Contribution
- 提取文本分類中最關鍵的流程。
- 對每個流程進行質化分析，確定其中常見技術。
- 對研究量化分析，觀察其中趨勢。
- 目前缺乏對過擬合問題相關研究。
- 概念飄移問題需要更多研究關注。
- 研究結果顯示當前最熱門的話題如下
	- cross-lingual text classification 
	- text stream analysis
	- opinions or sentiments analysis
	- ensemble learning method 
	- embedding features method
### Future work
- 雖然在文中因許可問題被排除，但ACM和IEEE仍是需要被參考的來源。
- 此文只針對機器學習相關技術回顧，但仍有如基於模糊邏輯的分類模型等等模型值得被討論。