from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import json
options = Options()
options.binary_location = r"E:\\wbdownload\\chrome-win64\\chrome.exe"
options.add_argument("--ignore-certificate-errors")
options.add_argument("--disable-logging")
options.add_argument("--log-level=3")
options.add_argument("--silent")
options.add_argument("--no-sandbox")
service = Service(r"E:\\wbdownload\\chromedriver-win64\\chromedriver.exe")
pubchem_url = 'https://pubchem.ncbi.nlm.nih.gov/#query=Anti-inflammatory'
wd = webdriver.Chrome(service=service, options=options)
actions = ActionChains(wd)
wd.implicitly_wait(3)
wd.get(pubchem_url)
# 读取数据保存文件
with open(r'E:\code\python\Spider_Pubchem\cid_data.json', 'r', encoding="utf-8") as file:
    cid_data = json.load(file)

data = []
#  翻页（搜索总数不一样记得每次更改）
for i in range(1,111):
    # 记录每页10个数据
    for t in range(1,11):
        try:
            element = wd.find_element(By.XPATH, f'//a[@data-ga-label="Result Secondary Link; Position:{t}; Page:{i}"]')
            cid = element.find_element(By.XPATH, './*')
            cid = cid.text
            print(cid)
            data.append(cid)
        except Exception as e:
            print(e)
            print(f"{i} page,{t}poi not found")
    try:
        wd.get(pubchem_url + f"&page={i + 1}")
    except:
        continue
cid_data["Anti-inflammatory"] = data
with open(r'E:\code\python\Spider_Pubchem\cid_data.json', 'w', encoding="utf-8") as files:
    json.dump(cid_data, files, indent=4, ensure_ascii=False)
# 总共1096个