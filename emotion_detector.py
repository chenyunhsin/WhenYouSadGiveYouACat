import cv2
import numpy as np
from deepface import DeepFace    # 載入 deepface
import requests
IS_SMILING = 0.5 # 如果你微笑的角度比較小，偵測不到你在笑，就調小一點0.0
TOKEN = ''
CAT_URL = "https://api.thecatapi.com/v1/images/search"
cap = cv2.VideoCapture(0)        # 讀取攝影鏡頭

# 發送東西到line notify
def lineNotifyMessage(token, msg):
    response = requests.get(CAT_URL)
    if response.status_code == 200:
        # 將回應資料轉換為 JSON 格式
        data = response.json()
        image_url = data[0]["url"]
    else:
        print('貓貓api掛了')
        return
    headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }

    payload = {
    "message": "你的貓貓！",
    "imageThumbnail": image_url,
    "imageFullsize": image_url
    }   
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return r.status_code

# 定義在畫面中放入文字的函式
def putText(source, x, y, text, scale=2.5, color=(255,255,255)):
    org = (x,y)
    fontFace = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = scale
    thickness = 5
    lineType = cv2.LINE_AA
    cv2.putText(source, text, org, fontFace, fontScale, color, thickness, lineType)

happy = 0    # 是否有 happy 的變數

if not cap.isOpened():
    print("打不開你的相機，開個權限吧")
    exit()
while True:
    ret, img = cap.read()               # 讀取影片的每一幀
    if not ret:
        print("Cannot receive frame")   # 如果讀取錯誤，印出訊息
        break
    img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)   # 轉換成 BGRA，目的為了和白色圖片組合
    w = int(img.shape[1]*0.5)           # 取得圖片寬度的 1/2
    h = int(img.shape[0]*0.5)           # 取得圖片高度的 1/2
    img = cv2.resize(img,(w,h))         # 縮小圖片尺寸 ( 加快處理速度 )
    white = 255 - np.zeros((h,w,4), dtype='uint8')   # 產生全白圖片

    key = cv2.waitKey(1)                # 每隔一毫秒取得鍵盤輸入資訊

    try:
        emotion = DeepFace.analyze(img, actions=['emotion']) # verbose=False隱藏 
        if emotion[0]['emotion']['happy'] <IS_SMILING:
            lineNotifyMessage(TOKEN, "貓貓！")
           
    except Exception as e:
        print(f'error: {e}')
        pass


    if key == ord('q'):    # 按下 q 結束
        break
    output = img.copy()  
    
    cv2.imshow('emotion_detector', output)               # 顯示圖片

cap.release()                           # 所有作業都完成後，釋放資源
cv2.destroyAllWindows()                 # 結束所有視窗
