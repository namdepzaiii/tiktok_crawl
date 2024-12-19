import os, json
import requests, time
import telebot, requests,random
import threading


def varr():
    global tokentoken, id_telegram
    with open('config.txt','r') as f:
        configs = f.read().split('"')
        tokentoken= configs[11]
        id_telegram= configs[13]
    return id_telegram

varr()
bot = telebot.TeleBot(tokentoken,)

@bot.message_handler(commands=['start'])
def send_user_id(message):
    user_id = message.from_user.id 
    bot.reply_to(message, f"Your User ID is: {user_id}")
    
headers, data = {},{}
def head():
    global headers, data
    headers = {
            'Host': 'api16-normal-useast5.tiktokv.us',
            'rpc-persist-pyxis-policy-v-tnc': '1',
            'x-ss-stub': '9DB133727EBD9DD8371FD6079BA25905',
            'x-ss-req-ticket': '1734575336142',
            'x-api-version': '2;2;2',
            'x-tt-dm-status': 'login=1;ct=1;rt=1',
            'x-tt-pba-enable': '1',
            'x-tt-pba-enable': '1',
            'x-bd-kmsv': '0',
            'x-bd-client-key': '#VLl1db1V2Y+oKFlK8WRXnRAqCxa5wQWhgQ1I7TA0J3d6psROvVki8SkGuMy2VMnby8XiPRiUpPG2E4YH',
            'passport-sdk-version': '6031890',
            'x-tt-token': '04cf999e7ac01c6abd846303bc648a1fe200823cd678f758dd430cd3d62be869662387417ff5a841d90c337c94e5a175f6d5ce15d5f537f96a2f167498f9a66e4f42c97e0674b48eadab0bdea79c39419d1926e042dbdf0faa76b67c93c1c2f5b2906-CkAzMDdiOGUyZDkwNjA5YTUyYjMzMDJmOWMxZGY1ZmQyMTU3MjdiYzVjODdjM2E4ZjRmNzg2MzFhY2NkYmZmZDg3-2.0.0',
            'sdk-version': '2',
            'oec-vc-sdk-version': '3.0.4.i18n',
            'x-vc-bdturing-sdk-version': '2.3.8.i18n',
            'x-tt-request-tag': 'n=0;nr=000;bg=0',
            'x-tt-store-region': 'us',
            'x-tt-store-region-src': 'uid',
            'user-agent': 'com.ss.android.ugc.trill/370703 (Linux; U; Android 5.1.1; en_US; G011A; Build/LMY48Z;tt-ok/3.12.13.16)',
            'x-ladon': 'e6UIUAGnhZJk8ILIHwdfODZfdrG+LY4I6uGuQhlEBJKYyiNk',
            'x-khronos': '1734575336',
            'x-gorgon': '0404c0cd00007b4498036e768ce1ec8edd69f1d93f9c9aaf1bb2',
            'x-argus': 'lOzPAhhL0QXdXgfiUwNdp89H/hs3kVvKwxTkcgtzcwm12j8CkN/CoyvKc1Eez+BNEDd7Z3OjlHZQrJtKLdcV0NCpAvoZBrh32a1EjzxeKLRZEbbysnCffbAMq139lyQUHxgupFjnuv7ygZvHhxxBQqZ/GiQaGz8XweWFxwSrRDECOnus9WKM0MvyOGGF6q6JyOmZ4n0IhqyairPS30tYr4qh8n2Uii3QUUFCyZxFdDfwWkrSY/u0ssfRpkqyfgs+P5x6IxcXb1BEsT/c3ynEYVjAeLGd+epw72DgdAvLMXutH0ZMmbqFUNna1uCJL+J6iQA7PlodZILVq3TWVtIeFhAe5LVZcz1LcrHOnP/xkxBuB7TGIEaXMAaMFkhY2+Jpzs8laxsXK0+xnhjnucSLgfWP5M+xGtYmvyFUfVZwETMcFnCzbXq70eWxyjCQAof/qgI9q0j1zLmFMtuaKKlWECP1eEYmMT68TkqEDzNSm80M6bSse65DT3v3UZgMOkCgG55jbeREiyMJJJgG8dlH9Lh+Qrkokih1gX0si+qetOu38LbPrnXwwZ/0jfJ/FmT1Jg0PO33ThTPmZ9+dHjDAjCt+P7YIHOon3D4TU7T84iBbY4zb/PRY1hxFAiIUgGaMS3o=',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        }
    data = {
                'chunk_size_list': '[6, 6]',
                'search_channel': 'tiktok_mall',
                'keyword': "",
                'enter_from': 'homepage_mall',
                'count': '30',
                'hot_search': '0',
                'last_search_id': '20241216012754842599925C45C4B2B961',
                'source': 'mall',
                'search_source': 'normal_search',
                'query_correct_type': '1',
                'is_filter_search': '0',
                'filter_by': '0',
                'sort_type': '0',
                'search_context': f'[{{"channel":"tiktok_mall","query":"hoodies","search_id":"20241216012754842599925C45C4B2B961","source":"normal_search","time":1734312475000}}]',
                'traffic_source_list': '6',
                'cmpl_enc': 'AgICA6AAFikrPEDsvf3umVda3C9b0jjVuGD1F-RP_bbK-TG6Id0S_TycaUlNv6zZYNqWAg',
                'ec_search_session_id': '1734312411514',
                'search_session_id': '1734312411514',
                'ecom_user_actions': '{"video_view_action":[{"comment_button_click":false,"like":false,"is_dislike":0,"video_duration":8846,"has_good_anchor":false,"author_id":"6665994622126571521","timestamp":1734312408,"enter_from_merge":"homepage_hot","is_followed":0,"fav":false,"video_id":"7417718439298518279"}],"search_action":[{"query":"hoodies","channel":"tiktok_mall","search_method":"normal_search","timestamp":1734312474,"session_id":"1734312411514","has_effective_click":0,"browse_depth":0},{"query":"hoodies","channel":"tiktok_mall","search_method":"normal_search","timestamp":1734312436,"session_id":"1734312411514","has_effective_click":0,"browse_depth":0},{"query":"hoodies","channel":"tiktok_mall","search_method":"search_history","timestamp":1734312414,"session_id":"1734312411514","has_effective_click":0,"browse_depth":0}]}',
                'end_to_end_search_session_id': '7578343782979123433',
                'is_low_device': '0',
                'is_weak_network': '0',
                'use_new_filter_arch': '0',
                'is_non_personalized_search': '0',
                'dma_consent_status': '3',
                'edm_consent_status': '3',
                'search_keyword_strategy': '0',
                'search_promotion_params': '{"is_first_request":true,"source":"normal_search"}',
                'root_enter_from_type': '101',
                'client_request_id': '74481152467184205266f017d08-90d3-4b42-ac81-615d351099d51734312523426',
            }
    return headers, data

def request_tts(keyword):
    while not id_telegram:
        if not varr():
            print('Đợi bằng được id telegram !')
        time.sleep(3)
    try :
        headers, data
    except:
        headers, data = head()
    data.update({"keyword": keyword})
    try:
            response = requests.post('https://api16-normal-useast5.tiktokv.us/aweme/v1/search/stream/ecom/?device_platform=android&os=android&ssmix=a&_rticket=1734312523471&cdid=ad6b2414-d149-4f68-ab04-ea246e6f09b6&channel=googleplay&aid=1180&app_name=trill&version_code=370703&version_name=37.7.3&manifest_version_code=370703&update_version_code=370703&ab_version=37.7.3&resolution=720*1280&dpi=240&device_type=G011A&device_brand=google&language=en&os_api=22&os_version=5.1.1&ac=wifi&is_pad=0&current_region=US&app_type=normal&sys_region=US&last_install_time=1734151422&mcc_mnc=31070&timezone_name=America%2FChicago&residence=US&build_number=37.7.3&uoo=0&carrier_region=US&region=US&locale=en-GB&op_region=US&timezone_offset=-21600&ts=1734312522&app_language=en&ac2=wifi&host_abi=armeabi-v7a&iid=7448115473751705387&device_id=7448115246718420526&openudid=b62e78915044b36b',headers=headers, data=data)
            if 'product_intelligent_sellingpoint_text_num' in str(response.text):
                result = str(response.text).split('\n')[3]
                return json.loads(result)
            else :
                bot.send_message(id_telegram, f'Die token hoặc gì đó dẫn đến ko tìm thấy kết quả !')
                return None
    except Exception as e:
            bot.send_message(id_telegram, f'Xảy ra lỗi : {e}')
            return None
        
def bot_thr():
    bot.polling(none_stop=True)
threading.Thread(target=bot_thr).start()
