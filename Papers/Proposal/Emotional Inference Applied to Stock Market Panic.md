# Emotional Inference Applied to Stock Market Panic

###### tags: `Paper draft`

## 緒論

- 背景
    - 股票受到市場的情緒影響
- 動機
    - 本研究認為辨識市場情緒有助於預測股價
- 目的
    - 尋找出市場情緒和股價間的關係
    - 尋找出容易受影響的股票種類
    - 尋找出容易受影響的時間特徵
- 方法
    - 蒐集網路論壇討論股票的貼文
    - 分析貼文內的情緒或情緒變化
    - 透過情緒和股價資訊預測股價

## 文獻回顧

- 股市恐慌 (待定
- 情緒識別
- 意見分類
- 股市預測

做了一個叫ESM的低維模型，裡面有憤怒、厭惡、恐懼、悲傷、驚訝、快樂，六種分類。它是基於Ekman心理學理論的意見分類，並且設計了兩種方法來擴展情感詞的數量，並通過有效的權重計算將信息向量到情感空間。
在TheLion股票論壇上進行實驗。

## 方法

- 資料集和爬蟲
- 模型說明
- 訓練說明
- 驗證指標說明 (湊字數
- 預期效果說明 (湊字數

## 參考文獻

### Reading later

- WALKING DOWN WALL STREET WITH A TABLET: A SURVEY OF STOCK MARKET PREDICTIONS USING THE WEB
    - Important

- Sentiment analysis of Twitter feeds for the prediction of stock market movement(2013)
    - http://cs229.stanford.edu/proj2011/ChenLazer-SentimentAnalysisOfTwitterFeedsForThePredictionOfStockMarketMovement.pdf
- Do Internet stock message boards influence trading? Evidence from heavily discussed stocks with no fundamental news(2011)
- Knowledge in memetic algorithms for stock classification(2014)
    - https://www.igi-global.com/article/knowledge-in-memetic-algorithms-for-stock-classification/103853
- Sentiment analysis in Twitter with lightweight discourse analysis(2012)
    - https://aclanthology.org/C12-1113.pdf

### Done

- [[Is All That Talk Just Noise The Information Content of Internet Stock Message Boards (2004)]]
    - 遠古論文網路情緒影響股市的論文
    - Antweiler, W., & Frank, M. Z. (2004). Is all that talk just noise? The information content of internet stock message boards. The Journal of finance, 59(3), 1259-1294.
- [[Mining opinion and sentiment for stock return prediction based on Web-forum messages (2013)]]
    - 文獻回顧
        - 意見分類
	- Duan, J., & Zeng, J. (2013, July). Mining opinion and sentiment for stock return prediction based on web-forum messages. In _2013 10th International Conference on Fuzzy Systems and Knowledge Discovery (FSKD)_ (pp. 984-988). IEEE.
    - [ ] 可以找找還有沒有可以放緒論的東西
- [[Investor sentiment from internet message postings and the predictability of stock returns (2014)]]
    - 背景
    - 認為網路上的情緒對股票價值沒有影響
    - Kim, S. H., & Kim, D. (2014). Investor sentiment from internet message postings and the predictability of stock returns. _Journal of Economic Behavior & Organization_, _107_, 708-729.
- [[Emotion space model for classifying opinions in stock message board (2016)]]
    - 文獻回顧
        - 意見分類
	- Luo, B., Zeng, J., & Duan, J. (2016). Emotion space model for classifying opinions in stock message board. _Expert Systems with Applications_, _44_, 138-146.
    - [ ] 可以找找還有沒有可以放緒論的東西
- [[Intraday online investor sentiment and return patterns in the U.S. stock market (2017)]]
    - 緒論非常值得參考
    - 發現在一天內的短期波動中情緒可以預測股價
    - Renault, T. (2017). Intraday online investor sentiment and return patterns in the US stock market. _Journal of Banking & Finance_, _84_, 25-40.
- [[Walking down wall street with a tablet A survey of stock market predictions using the web (2016)]]
    - 內容偏少，找時間讀四五章
    - Nardo, M., Petracco‐Giudici, M., & Naltsidis, M. (2016). Walking down wall street with a tablet: A survey of stock market predictions using the web. _Journal of Economic Surveys_, _30_(2), 356-369.
- [[The impact of sentiment and attention measures on stock market volatility (2020)]]
    - 最新的研究注意力和情緒對波動性影響的論文
    - Audrino, F., Sigrist, F., & Ballinari, D. (2020). The impact of sentiment and attention measures on stock market volatility. _International Journal of Forecasting_, _36_(2), 334-357.
- [[Fear of the coronavirus and the stock markets (2020)]]
    - 使用google趨勢作為恐慌指數研究恐慌對股票市場的影響
    - Lyócsa, Š., Baumöhl, E., Výrost, T., & Molnár, P. (2020). Fear of the coronavirus and the stock markets. _Finance research letters_, _36_, 101735.
- [[Which sentiment index is more informative to forecast stock market volatility Evidence from China (2020)]]
    - 研究傳統媒體、網路媒體、網路論壇建構的情緒指數對波動率的影響，只有傳統媒體沒有用。
    - Liang, C., Tang, L., Li, Y., & Wei, Y. (2020). Which sentiment index is more informative to forecast stock market volatility? Evidence from China. _International Review of Financial Analysis_, _71_, 101552.

### Just cite

- Infectious disease pandemic and permanent volatility of international stock markets: A long-term perspective
	- 發現只要有傳染病發生股市波動性就會上升。
	- https://doi.org/10.1016/j.frl.2020.101709
- Can Internet Search Queries Help to Predict Stock Market Volatility?
	- 股市中當搜索量上升則隔天波動率就會上升，在高波動率時期尤其明顯。
	- https://doi.org/10.1111/eufm.12058
- Constructing a Global Fear Index for the COVID-19 Pandemic
	- 基於確診和死亡數構建恐慌指數，並發現融合恐慌指數的模型預測效果較好。
	- https://doi.org/10.1080/1540496X.2020.1785424
- Pandemic-induced fear and stock market returns: Evidence from China (2021)
	- 基於搜尋引琴搜索量構建疫情恐慌指數，並發現恐慌指數對中國股市回報率有負面影響
	- [Pandemic-induced fear and stock market returns: Evidence from China - ScienceDirect (oclc.org)](https://www-sciencedirect-com.nutc.idm.oclc.org/science/article/pii/S1044028321000429#s0070)
- Noise trader risk in financial markets (1990)
    - 說明市場中交易會受情緒影響
    - De Long, J. B., Shleifer, A., Summers, L. H., & Waldmann, R. J. (1990). Noise trader risk in financial markets. Journal of political Economy, 98(4), 703-738.
- Investor sentiment in the stock market (2007)
    - 透過代理情緒指數研究情緒和市場波動的關係
    - Baker, M., & Wurgler, J. (2007). Investor sentiment in the stock market. Journal of economic perspectives, 21(2), 129-152.
- Enhancing emotion inference in conversations with commonsense knowledge (2021)
    - Seminar偷吃步
    - Li, D., Zhu, X., Li, Y., Wang, S., Li, D., Liao, J., & Zheng, J. (2021). Enhancing emotion inference in conversations with commonsense knowledge. Knowledge-Based Systems, 232, 107449.
- BERT rediscovers the classical NLP pipeline (2019)
    - Bert的原始論文(?
    - Tenney, I., Das, D., & Pavlick, E. (2019). BERT rediscovers the classical NLP pipeline. arXiv preprint arXiv:1905.05950.
- BERT Post-Training for Review Reading Comprehension and Aspect-based Sentiment Analysis (2019)
    - Bert用來情感分析
    - Xu, H., Liu, B., Shu, L., & Yu, P. S. (2019). BERT post-training for review reading comprehension and aspect-based sentiment analysis. arXiv preprint arXiv:1904.02232.
- SpanEmo: Casting Multi-label Emotion Classification as Span-prediction
    - Transfomer來情感分析，而且是Multi-label
    - Alhuzali, H., & Ananiadou, S. (2021). SpanEmo: Casting Multi-label Emotion Classification as Span-prediction. arXiv preprint arXiv:2101.10038.
- Random walks in stock market prices (1995)
    - 討論神秘的股票預測方法
    - Fama, E. F. (1995). Random walks in stock market prices. Financial analysts journal, 51(1), 75-80.
- Stock market analysis: A review and taxonomy of prediction techniques
    - 股票預測的回顧論文
    - Shah, D., Isah, H., & Zulkernine, F. (2019). Stock market analysis: A review and taxonomy of prediction techniques. International Journal of Financial Studies, 7(2), 26.
- Equity forecast: Predicting long term stock price movement using machine learning
    - 經典模型股市預測效果超級比比看
    - Milosevic, N. (2016). Equity forecast: Predicting long term stock price movement using machine learning. arXiv preprint arXiv:1603.00751.
- IEMOCAP: interactive emotional dyadic motion capture database
	- 六人行的情緒訓練資料集
	- Busso, C., Bulut, M., Lee, C. C., Kazemzadeh, A., Mower, E., Kim, S., ... & Narayanan, S. S. (2008). IEMOCAP: Interactive emotional dyadic motion capture database. _Language resources and evaluation_, _42_(4), 335-359.
- Constants across cultures in the face and emotion.
	- 情緒分六類的論文
	- Ekman, P., & Friesen, W. V. (1971). Constants across cultures in the face and emotion. _Journal of personality and social psychology_, _17_(2), 124.
- Twitter sentiment classification using distant supervision
	- Go, A., Bhayani, R., & Huang, L. (2009). Twitter sentiment classification using distant supervision. _CS224N project report, Stanford_, _1_(12), 2009.
- Attention is all you need
	- Transformer origin
	- Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., ... & Polosukhin, I. (2017). Attention is all you need. In _Advances in neural information processing systems_ (pp. 5998-6008).
- Long short-term memory
	- LSTM origin
	- Hochreiter, S., & Schmidhuber, J. (1997). Long short-term memory. _Neural computation_, _9_(8), 1735-1780.

## Dark Theme CSS

{%hackmd theme-dark %}