# WhenYouSadGiveYouACat


如同標題，當你不開心時，透過line notify給你一隻貓貓

## 用途


閒暇時做的小玩具，最近AI很紅，也試著參考相關程式做了一個小project，靈感來自於之前看到的相關project，
但當時沒有成功啟動該project，因此自己做了一個，環境是用mac os，踩到的坑:mac os 下載的tensorflow原來不同包...



## 使用方法(硬體為mac os)
#### 1. 先到這邊申請一個line notify token，先進此網站並登入
https://notify-bot.line.me/my/

#### 2. 拉到最下面會有**發行權杖按鈕**按下去

<img width="543" alt="截圖 2023-02-01 下午2 06 07" src="https://user-images.githubusercontent.com/58776036/215964719-3034e6c3-19f3-4744-8ec4-cf7b213c94c3.png">

#### 3. 接著選擇要訂閱貓圖的人或群組，如圖：
<img width="952" alt="ImotionDefeetorToken" src="https://user-images.githubusercontent.com/58776036/215964020-c8a3b812-0bdc-40cc-9a01-287d4bb91258.png">

#### 4. 接著按下複製按鈕
<img width="761" alt="取權村拷貝" src="https://user-images.githubusercontent.com/58776036/215964040-c1b1d68f-ca71-42f4-96f1-84ddfce09d1a.png">

#### 5. 將複製的值替換掉emotion_detector.py的TOKEN變數數值

#### 6. 創建虛體環境+下載需要的檔案

```shell
pip3 install virtualenv
python3 -m venv venv
source ./venv/bin/activate
pip3 install -r requirements.txt
```

#### 7. 接著啟動，就能玩了～

```shell
python3 emotion_detector.py
```

#### 一個簡單的Demo



https://user-images.githubusercontent.com/58776036/217727938-488c7382-6345-4411-917f-49304cc9d4bd.mp4



## 感謝這些參考對象~
大部分人臉辨識的程式碼是參考這邊，順便改了一些變數名稱和一些bug，可能現在版本的回傳有差，因此跑起來有bug 0.0
https://steam.oxxostudio.tw/category/python/ai/ai-smile-photo.html

貓咪api
https://api.thecatapi.com/v1/images/search

line notify使用參考
https://ithelp.ithome.com.tw/articles/10234115

## 希望大家玩得開心 啦:D

