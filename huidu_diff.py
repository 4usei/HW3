from PIL import Image

# 打开图片并转换为灰度模式
image1 = Image.open("A.jpg").convert("L")
image2 = Image.open("C.jpg").convert("L")

# 将图片转换为像素值列表
pixels1 = list(image1.getdata())
pixels2 = list(image2.getdata())

# 计算像素值差异并求平均值
diff = sum(abs(p1 - p2) for p1, p2 in zip(pixels1, pixels2)) / len(pixels1)

# 输出结果
print("灰度值差异值为:", diff)