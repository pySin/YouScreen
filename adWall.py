from tkinter import *
from PIL import ImageTk, Image
import ad_timing
import os
import random
from tkhtmlview import HTMLLabel
import time

# Start the tkinter object.
root = Tk()
root.configure(background='pink')


# Add image file
bg = PhotoImage(file = "background_4.png")

# Show image using label
label1 = Label( root, image = bg)
label1.place(x = 0, y = 0, relwidth=1, relheight=1)


# Create a container class for the all tkinter object functionality.
class YouScreen:

    def __init__(self, master, monitor):

        # 'master' here is used as the main tkinter object instead of 'root'.
        self.master = master

        # Choose a monitor.
        self.monitor = monitor

        # A list for the paid graphics.
        self.paid_pic_paths_1 = []
        self.paid_pic_paths_2 = []
        self.paid_pic_paths_3 = []
        self.paid_pic_paths_4 = []
        self.paid_pic_paths_5 = []
        self.paid_pic_paths_6 = []

        # A list for all the non-resized graphics.
        self.fifteen_paths_1 = []
        self.fifteen_paths_2 = []
        self.fifteen_paths_3 = []
        self.fifteen_paths_4 = []
        self.fifteen_paths_5 = []
        self.fifteen_paths_6 = []


        # Create a frame and place a label into it.
        self.frame_1 = LabelFrame(master, bd=0, height=315, width=350)
        self.frame_1.grid(row=0, column=0, padx=50, pady=40)
        self.frame_1.grid_propagate(False)

        self.label_1 = HTMLLabel(self.frame_1, background='white')
        self.label_1.grid(row=0, column=0)

        # Frame 2.
        self.frame_2 = LabelFrame(master, bd=0, height=315, width=350)
        self.frame_2.grid(row=0, column=1, padx=50, pady=40)
        self.frame_2.grid_propagate(False)

        self.label_2 = HTMLLabel(self.frame_2, background='white')
        self.label_2.grid(row=0, column=0)

        # Frame 3.
        self.frame_3 = LabelFrame(master, bd=0, height=315, width=350)
        self.frame_3.grid(row=0, column=2, padx=50, pady=40)
        self.frame_3.grid_propagate(False)

        self.label_3 = HTMLLabel(self.frame_3, background='white')
        self.label_3.grid(row=0, column=0)

        # Frame 4.
        self.frame_4 = LabelFrame(master, bd=0, height=315, width=350)
        self.frame_4.grid(row=1, column=0, padx=50, pady=40)
        self.frame_4.grid_propagate(False)

        self.label_4 = HTMLLabel(self.frame_4, background='white')
        self.label_4.grid(row=0, column=0)

        # Frame 5.
        self.frame_5 = LabelFrame(master, bd=0, height=315, width=350)
        self.frame_5.grid(row=1, column=1, padx=50, pady=40)
        self.frame_5.grid_propagate(False)

        self.label_5 = HTMLLabel(self.frame_5, background='white')
        self.label_5.grid(row=0, column=0)

        # Frame 6.
        self.frame_6 = LabelFrame(master, bd=0, height=315, width=350)
        self.frame_6.grid(row=1, column=2, padx=50, pady=40)
        self.frame_6.grid_propagate(False)

        self.label_6 = HTMLLabel(self.frame_6, background='white')
        self.label_6.grid(row=0, column=0)

        # Get image paths from a text file
        m_path_2 = "https://youscreen.co.uk/static/default_images/"
        o_file_2 = open("default_images_3.txt", 'r')
        r_lines_2 = o_file_2.readlines()
        self.fold_files = [m_path_2 + x[:-1] for x in r_lines_2 if len(x) > 4 and x[-1] == '\n']

        # Create a number variable to be used in changing the graphics on the screen.
        self.x = 0

    # Create a paid ad pictures list.
    def p_sql_adds(self):
        paid_paths_1 = ad_timing.paid_ad_paths('youscree_app.ads_show', self.monitor, 1)
        paid_paths_2 = ad_timing.paid_ad_paths('youscree_app.ads_show', self.monitor, 2)
        paid_paths_3 = ad_timing.paid_ad_paths('youscree_app.ads_show', self.monitor, 3)
        paid_paths_4 = ad_timing.paid_ad_paths('youscree_app.ads_show', self.monitor, 4)
        paid_paths_5 = ad_timing.paid_ad_paths('youscree_app.ads_show', self.monitor, 5)
        paid_paths_6 = ad_timing.paid_ad_paths('youscree_app.ads_show', self.monitor, 6)

        self.paid_pic_paths_1 = []
        if len(paid_paths_1) > 0:
            for path in paid_paths_1:
                if path not in self.paid_pic_paths_1:
                    self.paid_pic_paths_1.append(path)

        self.paid_pic_paths_2 = []
        if len(paid_paths_2) > 0:
            for path in paid_paths_2:
                if path not in self.paid_pic_paths_2:
                    self.paid_pic_paths_2.append(path)

        self.paid_pic_paths_3 = []
        if len(paid_paths_3) > 0:
            for path in paid_paths_3:
                if path not in self.paid_pic_paths_3:
                    self.paid_pic_paths_3.append(path)

        self.paid_pic_paths_4 = []
        if len(paid_paths_4) > 0:
            for path in paid_paths_4:
                if path not in self.paid_pic_paths_4:
                    self.paid_pic_paths_4.append(path)

        self.paid_pic_paths_5 = []
        if len(paid_paths_5) > 0:
            for path in paid_paths_5:
                if path not in self.paid_pic_paths_5:
                    self.paid_pic_paths_5.append(path)

        self.paid_pic_paths_6 = []
        if len(paid_paths_6) > 0:
            for path in paid_paths_6:
                if path not in self.paid_pic_paths_6:
                    self.paid_pic_paths_6.append(path)

    # Create all the 15 picture paths to circulate for a given hour.
    def all_15_paths(self):

        self.label_1.destroy()
        self.label_1 = HTMLLabel(self.frame_1, background='white')
        self.label_1.grid(row=0, column=0)

        self.label_2.destroy()
        self.label_2 = HTMLLabel(self.frame_2, background='white')
        self.label_2.grid(row=0, column=0)

        self.label_3.destroy()
        self.label_3 = HTMLLabel(self.frame_3, background='white')
        self.label_3.grid(row=0, column=0)

        self.label_4.destroy()
        self.label_4 = HTMLLabel(self.frame_4, background='white')
        self.label_4.grid(row=0, column=0)

        self.label_5.destroy()
        self.label_5 = HTMLLabel(self.frame_5, background='white')
        self.label_5.grid(row=0, column=0)

        self.label_6.destroy()
        self.label_6 = HTMLLabel(self.frame_6, background='white')
        self.label_6.grid(row=0, column=0)
        time.sleep(2)


        # Default pictures length
        default_length = len(self.fold_files) - 1
        
        self.fifteen_paths_1 = []
        for ad_num in range(15):  # 0 to 14.
            if ad_num < len(self.paid_pic_paths_1):
                self.fifteen_paths_1.append("https://youscreen.co.uk/static/images/"+self.paid_pic_paths_1[ad_num])
            else:
                rand = random.randint(0, default_length)
                self.fifteen_paths_1.append(self.fold_files[rand])

        self.fifteen_paths_2 = []
        for ad_num in range(15):  # 0 to 14.
            if ad_num < len(self.paid_pic_paths_2):
                self.fifteen_paths_2.append("https://youscreen.co.uk/static/images/"+self.paid_pic_paths_2[ad_num])
            else:
                rand = random.randint(0, default_length)
                self.fifteen_paths_2.append(self.fold_files[rand])

        self.fifteen_paths_3 = []
        for ad_num in range(15):  # 0 to 14.
            if ad_num < len(self.paid_pic_paths_3):
                self.fifteen_paths_3.append("https://youscreen.co.uk/static/images/"+self.paid_pic_paths_3[ad_num])
            else:
                rand = random.randint(0, default_length)
                self.fifteen_paths_3.append(self.fold_files[rand])

        self.fifteen_paths_4 = []
        for ad_num in range(15):  # 0 to 14.
            if ad_num < len(self.paid_pic_paths_4):
                self.fifteen_paths_4.append("https://youscreen.co.uk/static/images/"+self.paid_pic_paths_4[ad_num])
            else:
                rand = random.randint(0, default_length)
                self.fifteen_paths_4.append(self.fold_files[rand])

        self.fifteen_paths_5 = []
        for ad_num in range(15):  # 0 to 14.
            if ad_num < len(self.paid_pic_paths_5):
                self.fifteen_paths_5.append("https://youscreen.co.uk/static/images/"+self.paid_pic_paths_5[ad_num])
            else:
                rand = random.randint(0, default_length)
                self.fifteen_paths_5.append(self.fold_files[rand])

        self.fifteen_paths_6 = []
        for ad_num in range(15):  # 0 to 14.
            if ad_num < len(self.paid_pic_paths_6):
                self.fifteen_paths_6.append("https://youscreen.co.uk/static/images/"+self.paid_pic_paths_6[ad_num])
            else:
                rand = random.randint(0, default_length)
                self.fifteen_paths_6.append(self.fold_files[rand])

    #  Change the picture on the first monitor by changing frame/label picture.
    def change_only(self, im):
        # time.sleep(2)
        self.label_1.set_html(html='<img src=%s width=350 height=315>' % self.fifteen_paths_1[im])
        self.label_1.place(x = 0, y = 0, relwidth=1, relheight=1)

        self.label_2.set_html(html='<img src=%s width=350 height=315>' % self.fifteen_paths_2[im])
        self.label_2.place(x = 0, y = 0, relwidth=1, relheight=1)

        self.label_3.set_html(html='<img src=%s width=350 height=315>' % self.fifteen_paths_3[im])
        self.label_3.place(x = 0, y = 0, relwidth=1, relheight=1)

        self.label_4.set_html(html='<img src=%s width=350 height=315>' % self.fifteen_paths_4[im])
        self.label_4.place(x = 0, y = 0, relwidth=1, relheight=1)

        self.label_5.set_html(html='<img src=%s width=350 height=315>' % self.fifteen_paths_5[im])
        self.label_5.place(x = 0, y = 0, relwidth=1, relheight=1)

        self.label_6.set_html(html='<img src=%s width=350 height=315>' % self.fifteen_paths_6[im])
        self.label_6.place(x = 0, y = 0, relwidth=1, relheight=1)

    #  Wait for a pre-set time and call the functions above.
    def calling(self):

        self.master.after(20, lambda: self.change_only(self.x))
        self.master.after(20000, self.calling)
        self.x = self.x + 1
        print('list length tk_im:', len(self.fifteen_paths_1))
        print('list 15 paths:', len(self.fifteen_paths_1))

        #  Check for new ads and add them to the image cycle at the 4th spin.
        if self.x == 4:
            self.p_sql_adds()
            self.all_15_paths()

        #  When self.x reaches the 15th picture it's changed back to 0 to start the new cycle.
        elif self.x == 15:
            self.x = 0


def function_call():
    y_screen = YouScreen(root, 'monitor1')
    y_screen.p_sql_adds()
    y_screen.all_15_paths()

    y_screen.calling()
    #  Make the window full-screen.
    root.attributes('-fullscreen', True)
    root.mainloop()


if __name__ == '__main__':
    function_call()
