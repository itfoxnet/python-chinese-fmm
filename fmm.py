#coding:utf-8
#中文注释
import re
import sys 
reload(sys) 
sys.setdefaultencoding('utf8') 

word_dict   = ['新华网','日本','记者','行政','改革','二战','靖国神社','内阁','东京','中国','韩国','亚洲','国家']
test_str    = '''    新华网东京电记者吴谷丰据日本共同社28日报道，日本行政改革担当大臣稻田朋美当天参拜了供
奉有二战甲级战犯牌位的靖国神社。她成为第四个参拜靖国神社的安倍内阁成员。    靖国神社位于东京千代田区，供奉
有包括东条英机在内的14名第二次世界大战甲级战犯的牌位。长期以来，日本部分政客参拜靖国神社，导致日本与中国、韩国等亚洲国家关系


'''

#获取分词
def getSeg(text):

    if not text:
        return ''

    if len(text) == 1:
        return text

    if text in word_dict:
        return text 
    else:
        small = len(text) - 1
        text  = text[0:small]
        return getSeg(text)


def main():
    global test_str
    test_str     = test_str.decode('utf8').strip()
    #sub_list    = re.split(u"[\（），。]+",test_str)
    str_len      = len(test_str)
    #正向最大匹配分词测试 最大长度5
    max_len      = 5 
    result_str   = ''   #保存分词结果
    i = 0
    result_len = 0
    print 'input :',test_str
    while test_str:
        
        tmp_str      = test_str[0:max_len]
        seg_str      = getSeg(tmp_str)
        seg_len      = len(seg_str)
        result_len   = result_len + seg_len 
        
        if  seg_str.strip() :        
            result_str   = result_str + seg_str + ' / '
        test_str     = test_str[seg_len:]
        #exit()
        
    print 'output :',result_str

if __name__ == '__main__':
    main()
