# LuLu's proposal report

###### tags: `Research method`

## 1. Introduction

- 背景
    - 神經網路對圖片任務的表現
    - 神經網路對標籤數量的依賴性
    - 許多任務無法獲得大量標籤
        - 可能因為預算、標籤難度、太冷門
- 動機
    - 自監督式學習能夠改善無標籤的狀況
- 目的
    - 使用自監督式學習讓模型學會區分區塊
- 方法
    - 透過圖片內相似性和圖片間相似性

## 2. Related work

- 圖片自監督式學習
- 圖片相似性

## 3. Method

- 資料蒐集
- 模型設計
	- 將圖片中某些區塊複製貼上到其他部分
	- GAN貼貼
- 實驗方法

## Reference

### Self-supervised

- [[A Survey on Contrastive Self-Supervised Learning (2021)]]
	- 關於對比學習的回顧論文，其中包含許多種自監督式學習方法
- [[Self-Supervised Visual Feature Learning With Deep Neural Networks A Survey]]
	- 純血自監督回顧論文
- [[Overview of deep learning in medical imaging]]
	- 關於深度學習如何應用在醫學上的回顧論文
- [[Self-supervised learning for medical image analysis using image context restoration (2019)]]
	- 使用context對醫學影像自監督式學習
	- Related work就決定是你了
- [[Unsupervised visual representation learning by context prediction]]
	- 使用圖片背景進行自監督式學習
- [[Twin self-supervision based semi-supervised learning (TS-SSL) Retinal anomaly classification in SD-OCT images]]
	- 說是結合了兩種自監督式方法並融合半監督式學習
- [[Self-supervised video object segmentation using integration-augmented attention]]
	- 透過自監督學習加強影片中的物件特徵做語意切割
- [[CR-SSL A closely related self-supervised learning based approach for improving breast ultrasound tumor segmentation]]
	- 自監督來進行邊緣偵測並區分出腫瘤位置
- [[Self-Supervised Variational Auto-Encoders]]
	- 透過自監督的VAE完成降維或邊緣偵測等工作
- [[Structure-Driven Unsupervised Domain Adaptation for Cross-Modality Cardiac Segmentation]]
	- 透過邊緣切割心臟的無監督式學習
- [[Selfie Self-supervised Pretraining for Image Embedding]]
	- 自監督的圖像embedding方法
- [[Context Encoders Feature Learning by Inpainting]]
	- 透過挖空重建來自監督
- [[Self-supervised Learning for Spinal MRIs]]
	- 同一病人的連續MRI掃描來自監督學習
- [[Using Self-Supervised Learning Can Improve Model Robustness and Uncertainty]]
	- 證明自監督學習能夠增加Robustness和對異常點的抗性

### Image similarity

- [[Overview on subjective similarity of images for content-based medical image retrieval]]
	- 醫學圖片相似性計算的回顧論文
- [[Overview on subjective similarity of images for content-based medical image retrieval]]
	- 圖片相似性的回顧論文
- [[Local Diagonal Maxima-Minima Pattern-based Edge Detection Technique for Ultrasound and Digital Radiography Images]]
	- 傳新的邊緣濾波器，在各項指標上都有優勢
- [[Unsupervised Discovery of Object Landmarks as Structural Representations]]
	- 跟我的結果有87%相似度的paper，讀爛
### Just cite
- Unsupervised representation learning by predicting image rotations
	- 旋轉型的自監督學習
- Colorful image colorization
	- 把灰階圖片上色


## Dark Theme CSS

{%hackmd theme-dark %}