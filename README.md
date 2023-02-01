# WhenYouSadGiveYouACat


> 如同標題，當你不開心時，透過line notify給你一隻貓貓
主要是透過line notify實作此功能

## 用途

```javascript
閒暇時做的小玩具，最近AI很紅，也試著參考相關程式做了一個小project，靈感來自於之前看到的相關project，但當時沒有成功啟動該project，因此自己做了一個，環境是用mac os，也會附上踩到的坑
```


## 使用方法(硬體為mac os)
先參考這邊申請一個line notify token，並替換掉emotion_detector.py的TOKEN變數數值
https://ithelp.ithome.com.tw/articles/10234115

創建虛體環境+下載需要的檔案

```shell
pip3 install virtualenv
python3 -m venv venv
source ./venv/bin/activate
pip3 install -r requirements.txt
```


## 參考
大部分人臉辨識的程式碼是參考這邊，順便改了一些變數名稱和一些bug，可能現在版本的回傳有差，因此跑起來有bug 0.0
https://steam.oxxostudio.tw/category/python/ai/ai-smile-photo.html

貓咪api
https://api.thecatapi.com/v1/images/search

line notify使用參考
https://ithelp.ithome.com.tw/articles/10234115

希望大家玩得開心 啦:D

