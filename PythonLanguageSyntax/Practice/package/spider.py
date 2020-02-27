from urllib import request 
import re

class Spider():
    url = 'https://www.huya.com/g/lol'
    roughing = '<span class="txt">([\s\S]*?)</li>'
    name_machining = '<i class="nick" title="([\w\W]*?)">'
    number_machining = '<i class="js-num">([\s\S]*?)</i>'
    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        return htmls
    
    def __analysise(self, htmls):
        root_html = re.findall(Spider.roughing, htmls)
        anchors = []
        for html in root_html:
            name = re.findall(Spider.name_machining, html)
            number = re.findall(Spider.number_machining,html)
            anchor = {"name": name,"number": number}
            anchors.append(anchor)
        return anchors
        
    def __refine(self, anchors):
        l = lambda anchor: {'name': anchor['name'][0],  'number': anchor['number'][0]}
        return map(l, anchors)

    def __sort_key(self, anchor):
        r = re.findall('\d*', anchor['number'])
        number = float(r[0])
        if '万' in anchor['number']:
            number *= 10000
        return number

    def __sort(self, anchors):
        anchors = sorted(anchors, key=self.__sort_key,  reverse=True)
        return anchors
    
    
    def __show(self, anchors):
        for rank in range(0, len(anchors)):
            print('排名'+str(rank+1)+'   '+'主播：'+anchors[rank]['name']+"    "+'人气:'+anchors[rank]['number'])

    def go(self):
        htmls = self.__fetch_content()
        anchors = self.__analysise(htmls)
        anchors = list(self.__refine(anchors))
        anchors = self.__sort(anchors)
        self.__show(anchors)

    






sipder = Spider()
sipder.go()
