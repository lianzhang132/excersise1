#安装 OpenCV
# pip3 install opencv-python
import cv2

# 待检测的图片路径 只能识别正脸
imagepath = './img/14.jpg'

# 这个xml文件，就是opencv在GitHub上共享出来的具有普适的训练好的数据。我们可以直接的拿来使用。
# https://github.com/opencv/opencv/tree/master/data/haarcascades
face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

# 读取图片
image = cv2.imread(imagepath)
#把普通图片转化为灰度图片供检测
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# 我们可根据scaleFactor和minNeighbors来达到不同精度下的识别。返回值就是opencv对图片的检测结果。
# scaleFactor表示在前后两次相继的扫描中，搜索窗口的比例系数。默认为1.1即每次搜索窗口依次扩大10%
# minNeighbors匹配成功所需要的周围矩形框的数目，每一个特征匹配到的区域都是一个矩形框，只有多个矩形框同时存在的时候，才认为是匹配成功
# minSize检索的范围
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor = 1.5,
    minNeighbors = 3,
    minSize = (5,5)
)

print("发现{0}个人脸!".format(len(faces)))

# 遍历检测到的结果 在检测到的人脸上绘制矩形
for (x, y, w, h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)#最后的两个参数表示颜色和线条宽度
# 输出图片
cv2.imshow("Find Faces!", image)
# 按任意键后关闭
cv2.waitKey(0)