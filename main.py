import l_leg
import r_leg
import l_arm
import r_arm
import standarddataset as sds
from threading import Thread
from tkinter import *

def connect():
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


def check():
    if abs(l_leg.q[1] - sds.leg_down) < sds.error_range:
        if abs(r_leg.q[1] - sds.leg_up) < sds.error_range:
            if abs(l_arm.q[0] - sds.l_arm_up) < sds.error_range:
                if abs(r_arm.q[0] - sds.r_arm_down) < sds.error_range:
                    lb.config(text="动作合格")
                else:
                    lb.config(text="右臂不合格")
            else:
                lb.config(text="左臂不合格")
        elif r_leg.q[1] < sds.leg_up - sds.error_range:
            lb.config(text="右腿动作幅度过大")
        else:
            lb.config(text="右腿动作幅度过小")
    elif abs(l_leg.q[1] - sds.leg_up) < sds.error_range:
        if abs(r_leg.q[1] - sds.leg_down) < sds.error_range:
            if abs(l_arm.q[0] - sds.l_arm_down) < sds.error_range:
                if abs(r_arm.q[0] - sds.r_arm_up) < sds.error_range:
                    lb.config(text="动作合格")
                else:
                    lb.config(text="右臂不合格")
            else:
                lb.config(text="左臂不合格")
        else:
            lb.config(text="右腿不合格")
    else:
        lb.config(text="左腿不合格")

connect()

flag = 1

def start():
    if flag:
        check()
        win.after(200, start)  # 在200毫秒（0.2秒）后再次调用hello函数

# 重新开始检测
def start_again():
    global flag
    flag = 1
    start()

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
#win.config(background="#009933")
# 透明度，1到0
# win.attributes("-alpha",0.5)
# 视窗置顶
win.attributes("-topmost", 1)

bg_image = PhotoImage(file="bg.png")

bg_label = Label(win, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# 按钮
btn_start = Button(text="开始检测",font=('华文楷体', 15))
btn_start.config(bg="skyblue")
btn_start.config(width=15, height=3)

# 调用函数
btn_start.config(command=start_again)
btn_start.place(x=360,y=450)
#btn_start.pack(side="bottom")

btn_end = Button(text="停止检测",font=('华文楷体', 15))
btn_end.config(bg="skyblue")
btn_end.config(width=15, height=3)
btn_end.config(command=end_start)
btn_end.place(x=560,y=450)
#btn_end.pack(side="bottom")

# label
lb = Label(text="开始正步检测",font=('华文楷体', 30))
lb.config(width=15, height=3)
lb.place(x=360,y=100)
#lb.pack()

win.mainloop()