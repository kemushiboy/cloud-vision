#!/usr/bin/python
#coding:utf-8
import base64
import json
from requests import Request, Session


# Cloud Vision APIで画像を分析
# CAPTCHAの分析
# CAPTCHA画像の読み込み
bin_captcha = open('demo-image.jpg', 'rb').read()
        
# base64でCAPTCHA画像をエンコード
str_encode_file = base64.b64encode(bin_captcha)
        
# APIのURLを指定
str_url = "https://vision.googleapis.com/v1/images:annotate?key="
        
# 事前に取得したAPIキー
str_api_key = "AIzaSyAh5zYBWfiPMDnt8GFPEye8fImsP7JStFs"
        
# Content-TypeをJSONに設定
str_headers = {'Content-Type': 'application/json'}
        
# Cloud Vision APIの仕様に沿ってJSONのペイロードを定義。
# CAPTCHA画像からテキストを抽出するため、typeは「TEXT_DETECTION」にする。
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
#return obj_response.text
else:
#return "error"
    print "error"