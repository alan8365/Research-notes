- 事件驅動意見分類股市預測研究
- 融合新聞情緒和社群意見預測
	- TheLion作為意見分類訓練集
	- 看選隨便一個社群媒體當意見來源
	- 拿新聞內容的情緒也當作推論依據
	- 將兩個推論合起來蹦蹦蹦
- 選擇幾檔公司的股票和評論，把公司名稱mask起來
	- 訓練模型推出是哪間公司
	- 將模型用於新聞的encode

## TODO
#todo
- [ ] Coding v1 model
- [ ] Reading Multimodal

## Abstract

如何預測股票價格一直是備受關注的主題，其中股價如何受網路資訊影響也是許多研究探討的關鍵。本文提出針對金融領域處理的BERT變體fin-BERT，將BERT預訓練時所使用的資料來源改為從Stocktwits蒐集並處理後重新訓練。

## Reference
- [[A Multimodal Event-Driven LSTM Model for Stock Prediction Using Online News]]
	- 參考內容是否可延伸為研究方向。
- Wikipedia and stock return: Wikipedia usage pattern helps to predict the individual stock movement
- Sentiment analysis algorithms and applications: A survey
	- 情緒分析的回顧
- Evaluation of Sentiment Analysis in Finance: From Lexicons to Transformers
	- 情緒分析在金融的超級比一比
- Text Mining of Stocktwits Data for Predicting Stock Prices
