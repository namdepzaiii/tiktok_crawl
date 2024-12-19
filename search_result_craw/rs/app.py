from api import *
from pymongo.mongo_client import MongoClient
from pystyle import Colors

g = Colors.light_green
b = Colors.light_blue
y = Colors.yellow
o = Colors.orange
r = Colors.red
w = Colors.white

with open('config.txt','r') as f:
    configs = f.read().split('"')
    uri= configs[1]
    dtb= configs[3]
    clt= configs[5]
    rs_clt= configs[7]
    time_reload= int(configs[9])

STATUS_PENDING = "PENDING"
STATUS_RUNING = "RUNING"
STATUS_COMPLETE = "COMPLETE"
STATUS_ERROR = "ERROR"

client = MongoClient(uri)
db = client[dtb]
collection = db[clt]
collection_crawl = db[rs_clt]
def home():
    while 1:
        lst_data_keyw = []
        data1 = collection.find()
        for key in data1:
            if 'status' not in key or key['status'] == STATUS_RUNING:
                lst_data_keyw.append(key)
        if lst_data_keyw :
                for k in lst_data_keyw:
                    print(f'{w}Đang xử lí keyword : {k["keyword"]}')
                    collection.update_one({'_id': k["_id"]}, {'$set': {"status": STATUS_RUNING}} )
                    try:
                        result = request_tts(k['keyword'])
                        if result :
                            arr_js = []
                            for ree in result['e_com_items']:
                                if 'shop_view_data' in ree:
                                    reee = ree['shop_view_data']['init_state']
                                    print(f"{g}+1 : {y}{reee['title_text']}")
                                    arr_js.append({
                                        "title": reee['title_text'],
                                        "sold": reee['sold_count_burying_point'],
                                        "shop_id": reee['shop_id'],
                                        "search_keyword": reee['search_keyword'],
                                        "sales_price": reee['sales_price'],
                                        "product_intelligent_sellingpoint_text_num": reee['product_intelligent_sellingpoint_text_num'],
                                        "main_image": reee['main_image'],
                                        "cover": reee['cover'],
                                        "product_id": reee['product_id'],
                                    })
                            if arr_js:
                                collection_crawl.insert_many(arr_js)
                                print(f"\n\n{g}result collection inserted  :{y} +{len(arr_js)}")
                                collection.update_one({'_id': k["_id"]}, {'$set': {"status": STATUS_COMPLETE}} )
                
                    except Exception as e:
                        print(f'{r}error kxd: {y}{e}')
                        collection.update_one({'_id': k["_id"]}, {'$set': {"status": STATUS_ERROR}} )
                time.sleep(5)
        else :
            print(f'{r}Chưa có keyword nào cần xử lí >> sleep {time_reload} min')
            time.sleep(60*time_reload)
while 1:
    try:
        home()
    except :
        time.sleep(10)
        
        