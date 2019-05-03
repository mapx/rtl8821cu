import json
import requests as requests



# 获取网络数据
def getUrlData():
    try:
        url = 'https://api.spacexdata.com/v3/launches'
        space_data = requests.get(url)
        result = json.loads(space_data.text)
    except Exception:
        print('获取数据失败')
    yield result
# 将数据写入文件
# print(result)
def writeFile(result):
    with open('space_data1.txt','w') as f:
        for value in result:
            json.dump(value,f,indent=4)
# 处理数据
    with open('space_data1.txt','r') as f:
        data = f.read()
        print(data)
        # 分析数据发现两个数据间缺少逗号,添加上
        a = data.replace('}{','},{')

        list_data = json.loads(a)

        with open('data1.json','w') as f:

            for value in list_data:

                json.dump(value,f)
                f.write('\n')
                print(value)

if __name__ == '__main__':
    data = getUrlData()
    writeFile(data)

