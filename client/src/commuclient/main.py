#encoding=utf-8
import Tkinter
from PIL import Image,ImageTk

#屏幕
class Screen(object):
    def __init__(self, parent=None, bg=''):
        image = Image.open(bg)
        self.bg_img =  ImageTk.PhotoImage(image)
        print(parent)
        self.canvas = Tkinter.Canvas(parent,
                width = 500,      # 指定Canvas组件的宽度
                height = 600,      # 指定Canvas组件的高度
                bg = 'white')      # 指定Canvas组件的背景色
        self.canvas.create_image(300,300,image = self.bg_img)      # 使用create_image将图片添加到Canvas组件中

#开始界面
class StartScreen(Screen):
    def __init__(self, parent, bg=''):
        Screen.__init__(self,parent,bg)

#验票界面
class InfoScreen(Screen):
    def __init__(self,parent, bg=''):
        Screen.__init__(self,parent,bg)
        self.title = ''
        self.detail = ''

class MainFrame(object):
    def __init__(self):
        self.tk = Tkinter.Tk()
        self.tk.bind("<F11>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.end_fullscreen)
        self.start_screen = StartScreen(self.tk,'/z/workspace/clound-checker/client/src/commuclient/bg.jpg')  #屏幕背景
        self.info_screen =  InfoScreen(self.tk,'/z/workspace/clound-checker/client/src/commuclient/bg1.jpg') #
        self.current_screen = None
        self.set_screen(self.start_screen)
    
    def toggle_fullscreen(self, event=None):
        self.tk.attributes("-fullscreen", True)

    def end_fullscreen(self, event=None):
        self.tk.attributes("-fullscreen", False)
    def set_screen(self, screen): 
        if self.current_screen :
            self.current_screen.canvas.pack_forget()
        self.current_screen = screen
        self.current_screen.canvas.pack()
    
    def set_text(self, x, y, text, **prop):
        pass
    def show(self):
        self.tk.mainloop()

mf = MainFrame()
mf.show()
        

