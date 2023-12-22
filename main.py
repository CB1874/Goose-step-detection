import l_leg
import r_leg
import l_arm
import r_arm
from threading import Thread
from tkinter import *

if __name__ == "__main__":
    t_pool = []
    imu_instances = []
    imu_order = []
    # 连接传感器
    for device_info in l_leg.imu_devices:
        imu = l_leg.ble_server(device_info["address"], device_info["name"])
        # print(imu.get_latest_data())
        imu_instances.append(imu)
        imu_order.append(device_info["name"])
        t_pool.append(Thread(target=imu.start))

    print("imu的次序是：", imu_order)

    for t in t_pool:
        t.start()

if __name__ == "__main__":
    t_pool = []
    imu_instances = []
    imu_order = []
    # 连接传感器
    for device_info in r_leg.imu_devices:
        imu = r_leg.ble_server(device_info["address"], device_info["name"])
        # print(imu.get_latest_data())
        imu_instances.append(imu)
        imu_order.append(device_info["name"])
        t_pool.append(Thread(target=imu.start))

    print("imu的次序是：", imu_order)

    for t in t_pool:
        t.start()

if __name__ == "__main__":
    t_pool = []
    imu_instances = []
    imu_order = []
    # 连接传感器
    for device_info in l_arm.imu_devices:
        imu = l_arm.ble_server(device_info["address"], device_info["name"])
        # print(imu.get_latest_data())
        imu_instances.append(imu)
        imu_order.append(device_info["name"])
        t_pool.append(Thread(target=imu.start))

    print("imu的次序是：", imu_order)

    for t in t_pool:
        t.start()

if __name__ == "__main__":
    t_pool = []
    imu_instances = []
    imu_order = []
    # 连接传感器
    for device_info in r_arm.imu_devices:
        imu = r_arm.ble_server(device_info["address"], device_info["name"])
        # print(imu.get_latest_data())
        imu_instances.append(imu)
        imu_order.append(device_info["name"])
        t_pool.append(Thread(target=imu.start))

    print("imu的次序是：", imu_order)

    for t in t_pool:
        t.start()




flag = 1

def start():
    if flag:
        if 40 <= l_leg.q[1] <= 60 and 80 <= r_leg.q[1] <= 100 and -30 <= l_arm.q[0] <= -10 and -85 <= r_arm.q[0] <= -65:
            lb.config(text="符合")
            print("符合")
        else:
            if 40 <= r_leg.q[1] <= 60 and 60 <= l_leg.q[1] <= 100 and 60 <= l_arm.q[0] <= 80 and 0 <= r_arm.q[0] <= 20:
                lb.config(text="符合")
                print("符合")
            else:
                lb.config(text="不符合")
                print("不符合:",l_leg.q[1],r_leg.q[1],l_arm.q[0],r_arm.q[0])
        win.after(500, start)  # 在1000毫秒（1秒）后再次调用hello函数

def end_start():
    global flag
    flag = 0

win = Tk()
# 标题名字
win.title("正步检测")
# 视窗大小
win.geometry("1200x600")
# win.minsize(width=1200,height=600)
# win.maxsize(width=1200,height=600)
win.resizable(False, False)
win.config(background="#009933")
# 透明度，1到0
# win.attributes("-alpha",0.5)
# 视窗置顶
win.attributes("-topmost", 1)

# 按钮
btn_start = Button(text="开始检测")
btn_start.config(bg="skyblue")
btn_start.config(width=15, height=3)

# 调用函数
btn_start.config(command=start)

btn_start.pack(side="bottom")

btn_end = Button(text="停止检测")
btn_end.config(bg="skyblue")
btn_end.config(width=15, height=3)
btn_end.config(command=end_start)

btn_end.pack(side="bottom")

# label
lb = Label(text="开始你的正步检测之旅吧！")
lb.config(width=25, height=3)
lb.pack()

win.mainloop()