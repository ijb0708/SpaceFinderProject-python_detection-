from tkinter import *
from tkinter.ttk import *
import cv2
import os

# _test()


class customWindow:

    def __init__(self, title="noTitle", width=920, height=640, initX=50, initY=50):
        self.window = Tk()  # create new instance

        self.window.title(title)  # title name setting
        self.window.geometry(
            str(width) + "x" + str(height) + "+" + str(initX) + "+" + str(initY)
        )
        self.window.resizable(False, False)  # use that x, y resizing
        self.window.resizable(False, False)  # use that x, y resizing
        self.window.mainloop()  # gui start


# test = customWindow()

# 주차공간인식 기능
# 자동차 주차확인
# 글자인식 기능(상황보고 글자인식부분에서 teserect부분 딥러닝으로 교체)

# find Camera
camera_ports = []
for port in range(1, 100):
    camera = cv2.VideoCapture(port)
    if not camera.isOpened():
        break
    else:
        camera_ports.append(port)
        # is_reading, img = camera.read()
        # w = camera.get(3)
        # h = camera.get(4)

# 테스트용 주석
# if len(camera_ports) == 0:
#     messagebox.showwarning(title="error", message="not found the camera")
#     os._exit(os.EX_OK)

app = Tk()  # create new instance
app.title("carDtectMan")  # title name setting
app.geometry("920x640+50+50")
app.resizable(False, False)  # use that x, y resizing
app.resizable(False, False)  # use that x, y resizing

app.bind("<Escape>", lambda e: app.quit())


topFrame = Frame(app)
topFrame.pack(side="top", fill="x")

button = Button(topFrame, text="capture")
button.grid(column=1, row=0, sticky="w")

datas = ["1번 카메라", "2번 카메라", "3번 카메라"]
comboBox = Combobox(topFrame, values=datas)
comboBox.set("select camera")
comboBox.grid(column=0, row=0, sticky="w")

# mainFrame = Frame(app)
# mainFrame.pack(expand=True)

label_widget = Label(
    app,
    text="camera",
    foreground="red",
    background="white",
)
label_widget.pack(side="left", expand=True)

controlFrame = Frame(app)
controlFrame.pack(side="right")

detectCarLineBtn = Button(controlFrame, text="detect car line")
detectCarLineBtn.grid(row=0, column=0)

detectSpaceBtn = Button(controlFrame, text="check space")
detectSpaceBtn.grid(row=1, column=0)

readTextBtn = Button(controlFrame, text="read Text")
readTextBtn.grid(row=2, column=0)

app.mainloop()

os._exit(os.EX_OK)
