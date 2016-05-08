#!/usr/bin/python
#coding:utf-8
import base64
import json

import cv2
import time

from requests import Request, Session


# Cloud Vision APIで画像を分析
# CAPTCHAの分析
# CAPTCHA画像の読み込み
#bin_captcha = open('demo-image.jpg', 'rb').read()
        
# base64でCAPTCHA画像をエンコード
#str_encode_file = base64.b64encode(bin_captcha)
        
# APIのURLを指定
str_url = "https://vision.googleapis.com/v1/images:annotate?key="
        
# 事前に取得したAPIキー
str_api_key = "AIzaSyAh5zYBWfiPMDnt8GFPEye8fImsP7JStFs"
        
# Content-TypeをJSONに設定
str_headers = {'Content-Type': 'application/json'}
        
    
capture = cv2.VideoCapture(0)
while True:
    ret, frame = capture.read()
    buf = cv2.cv.EncodeImage(".jpeg",cv2.cv.fromarray(frame)).tostring()#frameをjpeg文字列に変換
    str_encode_file = base64.b64encode(buf)#jpeg文字列からバイナリに変換
    cv2.imshow('frame',frame)
    if cv2.waitKey(10) == 27:#escを押したら
      break
        
      # Cloud Vision APIの仕様に沿ってJSONのペイロードを定義。
    str_json_data = {
          'requests': [
                       {
                       'image': {
                       'content': str_encode_file
                       },
                       'features': [
                                    {
                                    'type': "SAFE_SEARCH_DETECTION",
                                    'maxResults': 10
                                    }
                                    ]
                       }
                       ]
                       }

    # リクエスト送信
    obj_session = Session()
    obj_request = Request("POST",str_url + str_api_key,
                                        data=json.dumps(str_json_data),
                                        headers=str_headers
                                        )
    obj_prepped = obj_session.prepare_request(obj_request)
    obj_response = obj_session.send(obj_prepped,verify=True,timeout=60)
          
      # 分析結果の取得
    if obj_response.status_code == 200:
      print obj_response.text
      jsonData = json.loads(obj_response.text)
      params = jsonData["responses"][0]["safeSearchAnnotation"]
      if params["adult"] == "VERY_LIKELY":
        print "out"
      if params["adult"] == "LIKELY":
        print "out"
      if params["adult"] == "POSSIBLE":
        print "seout"

        #return obj_response.text
    else:
      #return "error"
      print "error"  

    time.sleep(5)
    #break

capture.release()
cv2.destroyAllWindows()#事後処理

