import pandas as pd
import random
from datetime import datetime, timedelta

# 設定資料筆數
NUM_RECORDS = 300
OUTPUT_FILENAME = 'taiwan_tourism_data_300.csv'

# 基礎資料庫
attractions_db = [
    {"name": "台北101", "type": "地標/購物", "city": "台北市", "region": "北部"},
    {"name": "太魯閣國家公園", "type": "自然景觀", "city": "花蓮縣", "region": "東部"},
    {"name": "日月潭", "type": "自然景觀", "city": "南投縣", "region": "中部"},
    {"name": "墾丁大街", "type": "海邊/夜市", "city": "屏東縣", "region": "南部"},
    {"name": "九份老街", "type": "歷史/文化", "city": "新北市", "region": "北部"},
    {"name": "阿里山森林遊樂區", "type": "自然景觀", "city": "嘉義縣", "region": "南部"},
    {"name": "駁二藝術特區", "type": "藝文特區", "city": "高雄市", "region": "南部"},
    {"name": "澎湖花火節", "type": "離島/活動", "city": "澎湖縣", "region": "離島"},
    {"name": "奇美博物館", "type": "博物館", "city": "台南市", "region": "南部"},
    {"name": "清境農場", "type": "自然景觀", "city": "南投縣", "region": "中部"},
    {"name": "故宮博物院", "type": "博物館", "city": "台北市", "region": "北部"},
    {"name": "逢甲夜市", "type": "夜市/美食", "city": "台中市", "region": "中部"},
    {"name": "知本溫泉", "type": "溫泉", "city": "台東縣", "region": "東部"},
    {"name": "陽明山國家公園", "type": "自然景觀", "city": "台北市", "region": "北部"},
    {"name": "鹿港老街", "type": "歷史/文化", "city": "彰化縣", "region": "中部"},
    {"name": "野柳地質公園", "type": "自然景觀", "city": "新北市", "region": "北部"},
    {"name": "赤崁樓", "type": "歷史/文化", "city": "台南市", "region": "南部"},
    {"name": "六福村主題遊樂園", "type": "遊樂園", "city": "新竹縣", "region": "北部"},
    {"name": "蘭嶼", "type": "離島/自然", "city": "台東縣", "region": "離島"},
    {"name": "武陵農場", "type": "自然景觀", "city": "台中市", "region": "中部"},
    {"name": "宜蘭傳藝中心", "type": "文化/體驗", "city": "宜蘭縣", "region": "北部"},
    {"name": "小琉球", "type": "離島/海邊", "city": "屏東縣", "region": "離島"},
    {"name": "高美濕地", "type": "自然景觀", "city": "台中市", "region": "中部"},
    {"name": "金門戰地遺跡", "type": "歷史/文化", "city": "金門縣", "region": "離島"},
    {"name": "淡水老街", "type": "老街/美食", "city": "新北市", "region": "北部"},
    {"name": "義大世界", "type": "遊樂園/購物", "city": "高雄市", "region": "南部"},
    {"name": "馬祖藍眼淚", "type": "離島/自然", "city": "連江縣", "region": "離島"},
    {"name": "麗寶樂園", "type": "遊樂園", "city": "台中市", "region": "中部"},
    {"name": "華山1914文創園區", "type": "藝文特區", "city": "台北市", "region": "北部"},
    {"name": "安平古堡", "type": "歷史/文化", "city": "台南市", "region": "南部"}
]

member_types = ["家庭", "情侶", "朋友", "公司", "個人", "學生", "夫妻"]
transports_land = ["自行開車", "火車", "高鐵", "客運", "包車"]
transports_city = ["捷運", "公車", "自行開車", "計程車", "單車"]
transports_island = ["航空", "船運"]

data = []

start_date = datetime(2023, 1, 1)
end_date = datetime(2024, 6, 1)
days_diff = (end_date - start_date).days

print(f"正在生成 {NUM_RECORDS} 筆旅遊模擬資料...")

for _ in range(NUM_RECORDS):
    # 1. 隨機選擇景點
    attraction = random.choice(attractions_db)
    
    # 2. 決定成員與人數
    member = random.choice(member_types)
    if member == "個人":
        people = 1
    elif member == "情侶" or member == "夫妻":
        people = 2
    elif member == "家庭":
        people = random.randint(3, 6)
    elif member == "公司":
        people = random.randint(10, 40)
    else: # 朋友/學生
        people = random.randint(2, 8)
        
    # 3. 決定天數與交通 (加入邏輯)
    is_island = attraction["region"] == "離島"
    
    if is_island:
        days = random.randint(3, 5)
        transport = random.choice(transports_island)
    else:
        # 如果是都會區景點(台北/高雄)，天數可能較短
        if attraction["city"] in ["台北市", "高雄市"] and random.random() > 0.3:
            days = random.randint(1, 3)
            # 交通工具邏輯
            transport = random.choice(transports_city) if attraction["city"] in ["台北市", "高雄市"] else random.choice(transports_land)
        else:
            days = random.randint(1, 4)
            transport = random.choice(transports_land)

    # 4. 隨機日期
    random_days = random.randint(0, days_diff)
    travel_date = (start_date + timedelta(days=random_days)).strftime("%Y-%m-%d")
    
    # 5. 計算合理花費 (邏輯：基礎花費 + (住宿 * 天數 * 人數) + 交通費)
    # 假設每人每日平均食宿雜支
    daily_cost_per_person = random.randint(1500, 4000) 
    transport_cost_per_person = 0
    
    if transport in ["航空"]: transport_cost_per_person = 4000
    elif transport in ["高鐵"]: transport_cost_per_person = 2500
    elif transport in ["自行開車", "包車"]: transport_cost_per_person = 1000 # 油錢分攤概念
    elif transport in ["捷運", "公車", "火車"]: transport_cost_per_person = 500
    else: transport_cost_per_person = 1500
    
    total_cost = (daily_cost_per_person * days * people) + (transport_cost_per_person * people)
    
    # 微調花費
    if member == "公司": total_cost *= 1.2
    if member == "學生": total_cost *= 0.7
    
    # 取整數
    total_cost = int(round(total_cost, -2))

    record = {
        "景點": attraction["name"],
        "景點類型": attraction["type"],
        "景點縣市": attraction["city"],
        "區域": attraction["region"],
        "旅遊天數": days,
        "旅遊日期": travel_date,
        "旅遊人數": people,
        "成員類型": member,
        "總花費(元)": total_cost,
        "交通工具": transport
    }
    data.append(record)

# 建立 DataFrame
df = pd.DataFrame(data)

# 輸出為 CSV 檔案
try:
    df.to_csv(OUTPUT_FILENAME, index=False, encoding='utf-8-sig')
    print(f"成功！檔案已儲存為：{OUTPUT_FILENAME}")
    print(f"檔案路徑通常位於您的 Python 腳本同層目錄下。")
except Exception as e:
    print(f"儲存失敗：{e}")