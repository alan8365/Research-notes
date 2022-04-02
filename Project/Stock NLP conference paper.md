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

## 摘要

股票和相關金融衍生品的價格、走勢、變化率是由許多變量共同交織互相影響而成的結果，找出各變量如何影響股市是許多人的追求。

在影響股市的眾多變量中，人為情感因素對股市的影響雖可能只在短期相關卻不可忽視。但在探討情感因素對股市的影響前需先能夠取得情感因素的有效來源。

過往許多研究透過對網路大量資料的蒐集和訓練在自然語言處理領域取得優秀成績，BERT便是其中的佼佼者。但BERT的資料來源是維基百科和新聞文章，其中格式、用語、文法和網路上許多投資人討論並嶄露情緒的領域有落差。

有些文章為解決上述問題自創字典重新對各式用詞重新評分和編撰金融領域專屬辭典，但如此需具高度領域知識且曠日費時。 

因此，本文提出針對股票討論處理的BERT變體fin-BERT，使用和BERT一樣的架構，但將BERT預訓練時所使用的資料來源改為從美國股票討論社群媒體Stocktwits蒐集並重新訓練的新策略。

其中將Stocktwits特有的公司名稱和各種符號作為新token加入辭典中，以使其更適切貼合後續的分析應用。

本文將fin-BERT用於網路資訊對股票漲跌的意見分類上，並與原始版本BERT比較，預期本文模型在各項指標表現上得出較佳的結果。

本文貢獻在於對網路不同樣態資訊進行再處理，並重新適配於所需任務中，其中過程只需對領域的入門知識便能夠彌平預訓練模型間的領域差距。

## Outlines
- 介紹
- 文獻探討
	- 情緒對股市影響
		- 金融指標和網路來源出現的情緒差別優劣，為什麼要用網路來源(暫定)
		- [[Intraday online investor sentiment and return patterns in the U.S. stock market (2017)]]
	- 網路情緒蒐集
		- 回顧和分析其他挖掘手段或來源，如yahoo新聞和google搜尋量
		- [[Which sentiment index is more informative to forecast stock market volatility Evidence from China (2020)]]
			- 關於網路情緒有用的相關證據
	- BERT
		- 看要寫這邊還是要寫在第三章
		- 參考容易公式放在第三章，介紹放在第二章
	- 意見分類
		- 看看Bertweet怎麼放的
		- [[Emotion space model for classifying opinions in stock message board (2016)]]
- 方法
- 案例探討
- 結論

## Codes
[Stocktwit_sentiment_analysis Workspace – Weights & Biases (wandb.ai)](https://wandb.ai/alan8365/Stocktwit_sentiment_analysis?workspace=user-alan8365)
- [ ] sentiment analysis downstream task

### Lib
- [🤗 Transformers (huggingface.co)](https://huggingface.co/docs/transformers/index)
- [Datasets (huggingface.co)](https://huggingface.co/docs/datasets/index)
## Reference

### Reading later
![[Paper list#for stock NLP conference]]