import re
str1 = """
http://www.flvcd.com/parse.php?kw=http%3A%2F%2Ftv.sohu.com%2F20080504%2Fn256652702.shtml&flag=
http://www.flvcd.com/parse.php?kw=http%3A%2F%2Fsports.sina.com.cn%2Fg%2Fbn%2F2007-08-30%2F01364215.shtml
http://www.flvcd.com/parse.php?flag=&kw=http%3A%2F%2Fwww.56.com%2Fw55%2Fplay_album.phtml%3Faid%3D3497210%26vid%3DOTk2OTQxNA
http://www.flvcd.com/parse.php?kw=http%3A%2F%2Fwww.joy.cn%2Fspecial-page.jsp%3Fzt%3D7
http://www.flvcd.com/parse.php?kw=http://www.pinshan.com/topiclist/instyle6453.html
http://www.flvcd.com/url.php
https://baike.baidu.com/item/URL%E6%A0%BC%E5%BC%8F/10056474?fr=aladdin
https://mbd.baidu.com/newspage/data/landingsuper?context=%7B%22nid%22%3A%22news_8827900506114302782%22%7D&n_type=0&p_from=1
"""
# rel = "http[s]*://\w+\.\w+\.\w+/\w+\.\w+"
rel = "http[s]*://(?:\w+\.)+(?:\w+)+"
print(re.findall(rel,str1,re.S))
