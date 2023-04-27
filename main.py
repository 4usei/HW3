import time
from PIL import Image

# 读取图像
img = Image.open('B.jpg')

# 设定旋转角度
angle =eval(input("请输入旋转角度："))
# 记录开始时间
start_time = time.time()
n = 10
for i in range(n):
    # 进行旋转变换
    rotated = img.rotate(angle, expand=True)
# 记录结束时间
end_time = time.time()
# 计算代码执行时间
elapsed_time = end_time - start_time
print("代码执行时间：", elapsed_time/n, "秒")
# 显示旋转后的图像
rotated.show()

