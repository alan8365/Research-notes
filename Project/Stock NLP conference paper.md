- 事件驅動意見分類股市預測研究
- 融合新聞情緒和社群意見預測
	- TheLion作為意見分類訓練集
	- 看選隨便一個社群媒體當意見來源
	- 拿新聞內容的情緒也當作推論依據
	- 將兩個推論合起來蹦蹦蹦
- 選擇幾檔公司的股票和評論，把公司名稱mask起來
	- 訓練模型推出是哪間公司
	- 將模型用於新聞的encode

Fin-BERT: 用於股市情緒的預訓練語言模型

## TODO
#todo
- [ ] Training mask model
	- [ ] Bert (optional)
	- [ ] Fin-Bert
- [ ] Training head model
	- [ ] Bert
	- [ ] Fin-Bert

## Abstract

股票和相關金融衍生品的價格、走勢、變化率是由許多變量共同交織互相影響而成的結果，找出各變量如何影響股市是許多人的追求。

在影響股市的眾多變量中，人為情感因素對股市的影響雖可能只在短期相關卻不可忽視。但在探討情感因素對股市的影響前需先能夠取得情感因素的有效來源。

過往許多研究透過對網路大量資料的蒐集和訓練在自然語言處理領域取得優秀成績，BERT便是其中的佼佼者。但BERT的資料來源是維基百科和新聞文章，其中格式、用語、文法和網路上許多投資人討論並嶄露情緒的領域有落差。

有些文章為解決上述問題自創字典重新對各式用詞重新評分和編撰金融領域專屬辭典，但如此需具高度領域知識且曠日費時。

因此，本文提出針對股票討論處理的BERT變體fin-BERT，使用和BERT一樣的架構，但將BERT預訓練時所使用的資料來源改為從Stocktwits蒐集並重新訓練的新策略。

其中將Stocktwits特有的公司名稱和各種符號作為新token加入辭典中，以期獲得更適切貼合下游任務領域的編碼器。

本文將fin-BERT用於網路資訊對股票漲跌的意見分類上，並與原始版本BERT比較，預期本文模型在各項指標表現上會優於原始BERT。

本文貢獻在於對網路不同樣態資訊進行再處理，並重新適配於所需任務中，其中過程只需對領域的初級知識便能夠彌平預訓練模型間的領域差距。


股票和相關金融衍生品的價格、走勢、變化率是由許多變量共同交織互相影響而成的結果，找出各變量如何影響股市是許多人的追求。在影響股市的眾多變量中，人為情感因素對股市的影響雖可能只在短期相關卻不可忽視。但在探討情感因素對股市的影響前需先能夠取得情感因素的有效來源。過往許多研究透過對網路大量資料的蒐集和訓練在自然語言處理領域取得優秀成績，BERT便是其中的佼佼者。但BERT的資料來源是維基百科和新聞文章，其中格式、用語、文法和網路上許多投資人討論並嶄露情緒的領域有落差。有些文章為解決上述問題自創字典重新對各式用詞重新評分和編撰金融領域專屬辭典，但如此需具高度領域知識且曠日費時。因此，本文提出針對股票討論處理的BERT變體fin-BERT，使用和BERT一樣的架構，但將BERT預訓練時所使用的資料來源改為從Stocktwits蒐集並重新訓練的新策略。其中將Stocktwits特有的公司名稱和各種符號作為新token加入辭典中，以期獲得更適切貼合下游任務領域的編碼器。本文將fin-BERT用於網路資訊對股票漲跌的意見分類上，並與原始版本BERT比較，預期本文模型在各項指標表現上會優於原始BERT。本文貢獻在於對網路不同樣態資訊進行再處理，並重新適配於所需任務中，其中過程只需對領域的初級知識便能夠彌平預訓練模型間的領域差距。


茶葉歷史脈絡演進，一再顯示人們持續追求飲用高品質的茶葉，因此經常舉辦茶葉比賽。然而，茶葉比賽需要透過專業評審來進行評鑑評分，但透過人為評分，往往難以避免認知差異，進而產生評分的偏差。因此，本研究考量人為評審茶葉品質的評分過程所產生的問題，提出智慧化方法，透過智慧識別與多準則決策分析，期望協助降低以人為評分認知偏差的影響。本研究之實驗將蒐集茶葉比賽的資料與比賽過程中所產生的圖像。我們將採行評分準則中的『外觀（含水色）』和『葉底』圖像進行智慧辨識後產生評分，其餘『香氣』、『滋味』準則保持人為評審之評分。智慧辨識方法是透過OpenCV技術將茶葉比賽過程之圖像進行預處理，透過YOLOv4進行訓練並建模，接著進行辨識產生評分。而智慧辨識評分將與人為評審評分合併成評分矩陣，透過多準則決策之TOPSIS方法進行分析，取得實驗結果。最後，我們將本研究實驗結果跟所有準則評分皆由人為評審的結果進行比對，用以驗證本研究提出的實驗方法有效性。我們的貢獻在於使用混成準則，包含智慧辨識評分準則與人為評分準則，進行多準則決策分析，期望減少茶葉比賽完全由人為評分所產生認知差異的影響。

## Codes

- [ ] sentiment analysis downstream task

### Lib
- [🤗 Transformers (huggingface.co)](https://huggingface.co/docs/transformers/index)
- [Datasets (huggingface.co)](https://huggingface.co/docs/datasets/index)
## Reference
- BERTweet: A pre-trained language model for English Tweets
	- 跟現在方向很近的paper
- [[A Multimodal Event-Driven LSTM Model for Stock Prediction Using Online News]]
	- 參考內容是否可延伸為研究方向。
- Wikipedia and stock return: Wikipedia usage pattern helps to predict the individual stock movement
- Sentiment analysis algorithms and applications: A survey
	- 情緒分析的回顧
- Evaluation of Sentiment Analysis in Finance: From Lexicons to Transformers
	- 情緒分析在金融的超級比一比
- Text Mining of Stocktwits Data for Predicting Stock Prices
