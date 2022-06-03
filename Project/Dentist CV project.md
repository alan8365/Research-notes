## Todo
#todo 
- [x] Point out the four canine teeth
- [ ] Reasoning why 43 special. 
- [ ] edge detection test.
	- [ ] test to bounding between 4-bound

## Meeting
### 2022/06/03
- 目前在處理ROI
- 使用邊緣偵測方法切出ROI
- 再從ROI中切出牙齒，使用牙齒來把問題改為分類不是定位
- 之前有用邊緣偵測
- post跟endo跟蛀牙一起解決
### 2022/05/14
- 蛀牙先解決
	- 蛀牙有缺角跟小灰點
- 一張標記三分鐘
- 有post一定會有endo
- filling、embedded可以不標
- 假設架在GCP上
### 2022/03/18
- 3月底300張標註
- 有牙無牙的標註

確認完成事項
- 牙位偵測
	- precision優先，recall0.9以上
- 牙齒狀態診斷、歸類
	- 透過標籤訓練框定12項類別
- API開發、協助串接
	- 輸入pano圖 ，tif跟jpg都要可以
	- 輸出12項類別有無和出現牙位的json檔案
	- 協助將程式部署於公司雲端

## Report
### 2022/05/13
- 臼齒牙位辨識準確率和虎牙大致一樣
- 牙位以外辨識只有lmp達到90%，其餘狀況分為以下三類：
- 第一類準確率50%以上：bridge、crown、embedded、endo、filling
- 第二類準確率50%以下：R.R、impacted、post
- 第三類準確率15%以下：caries

- 第三類狀況目前初步猜測是由於物件過小且對比不明顯所致
- 第二類和第一類狀況則尚未全部釐清，只能確定部分容易搞混的情況
	- impacted中有20%被判斷為embedded，相反的情況也有11%
	- post有10%被判斷為endo

- 目前打算將caries單獨一個model處理
- 其餘兩類狀況目前正同時實驗以下兩種方式
	- 加入其他前處理步驟觀察準確率變化
	- 測試其他架構的model是否適合

## Idea test
### Edge
- Sobel edge detection
- Gaussian filter (Bilateral filter)
	- Not just Gaussian filter by [OpenCV: Smoothing Images](https://docs.opencv.org/4.x/d4/d13/tutorial_py_filtering.html)
	- Inspire by [A review on lung boundary detection in chest X-rays | SpringerLink](https://link.springer.com/article/10.1007/s11548-019-01917-1) and [[2012.13666] PaXNet: Dental Caries Detection in Panoramic X-ray using Ensemble Transfer Learning and Capsule Classifier (arxiv.org)](https://arxiv.org/abs/2012.13666)
- Pooling to sharpening the edge
> Need to study more about ROI extracting before try myself.
> only teeth can not determined ROI, have to find the edge of mandible.

### SAHI
- 和絕對位置相關的不能使用
- 可能只能用在蛀牙上

### YOLOv5

detect test
```shell
python detect.py --weights .\dentist_cv\exp12\weights\best.pt --source .\datasets\pano630\val\images\202008250508501754_0950923A.jpg --save-txt --save-crop
```

## Idea collect
### Caries Detection
[[2012.13666] PaXNet: Dental Caries Detection in Panoramic X-ray using Ensemble Transfer Learning and Capsule Classifier (arxiv.org)](https://arxiv.org/abs/2012.13666)
[Classification of Dental Cavities from X-ray images using Deep CNN algorithm | IEEE Conference Publication | IEEE Xplore (oclc.org)](https://ieeexplore-ieee-org.nutc.idm.oclc.org/document/9143013)

### Small object detection
[Feedback-driven loss function for small object detection - ScienceDirect (oclc.org)](https://www-sciencedirect-com.nutc.idm.oclc.org/science/article/pii/S0262885621001025?casa_token=PQfGADMDursAAAAA:NCf66YL4Nzd-7eh61sKh0x_14Zub3kMK1I8QJJ0mtSXsn3sJcgtFYp4V1u-Dax6RBxBiP2m7)

### Edge detection
[MarkMoHR/Awesome-Edge-Detection-Papers: A collection of edge/contour/boundary detection papers and toolbox. (github.com)](https://github.com/MarkMoHR/Awesome-Edge-Detection-Papers)

### Optional
#### MLops
[MLflow - A platform for the machine learning lifecycle | MLflow](https://mlflow.org/)
[mlflow/mlflow: Open source platform for the machine learning lifecycle (github.com)](https://github.com/mlflow/mlflow)

## Reference
- [Deep Instance Segmentation of Teeth in Panoramic X-Ray Images | IEEE Conference Publication | IEEE Xplore (oclc.org)](https://ieeexplore-ieee-org.nutc.idm.oclc.org/document/8614355)
- [Automatic segmenting teeth in X-ray images: Trends, a novel data set, benchmarking and future perspectives - ScienceDirect (oclc.org)](https://www-sciencedirect-com.nutc.idm.oclc.org/science/article/pii/S0957417418302252)
	- 超級review
	- 超級dataset
- [A deep learning approach to automatic teeth detection and numbering based on object detection in dental periapical films | Scientific Reports (nature.com)](https://www.nature.com/articles/s41598-019-40414-y#Sec11)
	- 自己標了一堆資料，說如果想要要去找北京神秘醫院要。
	- 同樣種類的牙齒容易搞混，把位置pattern加進來很重要。

