[[Self-supervised learning for medical image analysis using image context restoration]]


## Abstract
- 深度學習模型訓練需要大量的標記資料。
- 醫學圖像分析中經常缺乏標記並含有大量未標記資料。
- 使用自監督式學習能有效利用大量未標記資料並改進模型效能。
- 此文提出一種基於上下文恢復的自監督學習策略，其中有三個特點
	- 能夠學習圖像語意特徵
	- 學習到的特徵能夠用於後續任務
	- 實現簡單
## 1. Introduction
- CNN用於醫學圖像分析有著明顯的改進，但卻依賴於大量標記資料。
- 其他領域解決大量標記的方式在需要專業知識的醫療領域很難起到作用。
- 自監督學習指透過資料本身加工的資料進行監督學習。
- 有兩個既有的自監督策略能夠解決問題，後續會提到他們的缺點。
- 此文提出一個新的自監督策略，對於給定的圖片隨機選取其中兩個小塊互換，以此重複數次，訓練模型將混淆過的圖片還原。
- 此方法能夠學習到圖像中的語意特徵
- 此方法對後續任務如分類、定位、分割都有幫助
- 此方法的實現簡單明瞭
## 2. Related work
- 既有的RP方法將圖片分成3x3的小塊，訓練模型分辨出9個小塊的相對位置。
- 該方法的第一個缺點是對於對稱圖形等等狀況小塊位置可能有多個答案。
- 第二是該方法可能學習到小塊邊角的瑣碎特徵而非用於後續任務的語意特徵。
- 第三是此方法機器只接觸小塊而不能學習全局的背景資訊。
- 既有的CP方法是在圖像中選取一塊區域，將去與抹去後訓練模型將其還原。
- 該方法的缺點在於模型將只會關注抹去區域的上下文，也就是抹去區域周圍的資訊。
- 並且改變圖像強度分布將會轉變任務的領域，可能使學習到的特徵對原始任務沒用。
## 3. Self-supervision based on context restoration
### 3.1. Context restoration
略
### 3.2. Network architectures
略
## 4. Experiments and results
### 4.1. Context restoration results
略
### 4.2. Fetal standard scan plane classification
- 此節實驗自監督策略對分類圖像的效果，資料集選擇胎兒的超音波圖像。
- 結果在各個自監督策略中此文的策略獲得最好的結果。
- 並且在只使用25%資料時此文的策略幫助提升的效能最大。
- 並且在只有25%資料時單純使用資料增強提高的效能比部分自監督要來的高。
### 4.3. Abdominal multi-organ localization
- 此節實驗自監督策略對定位圖像的效果，資料集選擇腹部的CT斷層掃描圖像。
- 此文在50%資料時獲得最好的結果，但在25%資料辨識右腎上輸給了RP方法。
- 作者推測是由於區分兩個腎臟本身就很困難，兩個腎臟應合併辨識。
- 在這項實驗中資料增強幾乎沒有帶來任何提升，甚至有可能降低效能。
- 同時也發現RP方法經常優於JS方法，這可能是因為RP方法只使用兩個小塊訓練，相比於JS方法降低了學習到器官邊角的機會。
### 4.4. Brain tumour segmentation
- 此節實驗自監督策略對分割圖像的效果，資料集選擇大腦腫瘤的MRI斷層掃描圖像。
- 此文方法在大部分評估指標上都贏過其他方法，除了靈敏度和50%時的特異度。
- 資料增強幾乎都在降低分割準確度，可能是由於資料增強並沒有給腫瘤加入額外差異或增強改變了圖像強度。
- 同時資料量的下降對模型效能的下降並不明顯，這導致不同策略間的差異也不明顯。
## 5. Discussion and conclusion
- 實驗發現將實驗資料數量降低效能會明顯下降，但自監督方法所提升的效能也會明顯上升。