# 利用百度OCR在线识别图片文本
from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '你的 App ID'
API_KEY = '你的 Api Key'
SECRET_KEY = '你的 Secret Key'

""" 待识别图片的路径 """
filepath = 'tmp.PNG'

# 是否保存结果到文件中，True为保存，False为不保存，直接输出
isFileSave = True
# 若保存，保存路径为
saveFilePath = 'OcrText.txt'
# 是否保留上次文件中的内容，True为保存之前的内容，并在之后添加本次内容
# False为删除上次的内容，只保留本次识别结果
isLastSave = True

""" 读取图片的编码 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

""" 将所有的文字都合并到一起 """ 
def get_text_concat(resdict):
    strx=""
    for tex in resdict["words_result"]:
        strx+=tex["words"]
    return(strx)

""" 将数据data保存到filePath中 """ 
def save_text(filePath, data, isLastSave = True):
    if(isLastSave):
        with open(filePath, 'a', encoding='utf-8') as f:
            f.write('\n'+ data)
    else:
        with open(filePath, 'w', encoding='utf-8') as f:
            f.write(data)

if __name__ == "__main__":
    print("OCR识别开始")
    """ 调用通用文字识别, 图片参数为本地图片 """
    try:
        client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
        image = get_file_content(filepath)
        res = client.basicGeneral(image)
        text = get_text_concat(res)
        if(isFileSave):
            save_text(saveFilePath, text, isLastSave)
            print("识别文字已保存到文件中")
        else:
            print( text)
        print("OCR识别成功，程序结束")
    except Exception as e:
        print("OCR识别失败！！！程序非正常结束\n详情：",e)