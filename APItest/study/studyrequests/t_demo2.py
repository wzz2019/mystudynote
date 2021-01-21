from bs4 import BeautifulSoup

#解析html
#pip install beautifulsoup4
file='a.html'
data = open(file)  # 读取全部
soup = BeautifulSoup(data,'html.parser')
# 就是在find_all报了错，因此我想这样遍历应该是递归遍历，层数太深
# result = soup.find_all('strong', text=True)
# print(result)
# result = soup.find_all(name='div', attrs={"class": "zhengwen"}, limit=1)


for link in soup.find_all('a'):
    print(str(link.string)+"¥"+link.get('href'))
