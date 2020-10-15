# 利用百度OCR在线识别图片文本
from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '你的 App ID'
API_KEY = '你的 Api Key'
SECRET_KEY = '你的 Secret Key'

""" 待识别图片的路径 """
filepath = 'tmp.PNG'

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

if __name__ == "__main__":
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    
    image = get_file_content(filepath)

    """ 调用通用文字识别, 图片参数为本地图片 """
    res = client.basicGeneral(image);
    text = get_text_concat(res)
    print( text)
