from tkinter import *
from PIL import ImageTk, Image
import time
import ad_timeing
import os

# Start the tkinter object.
root = Tk()


# Create a container class for the all tkinter object functionality.
class YouScreen:

    def __init__(self, master):

        # 'master' here is used as the main tkinter object instead of 'root'.
        self.master = master

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

        # Lists for resized and ready for their frames graphics.
        self.monitor_1 = []
        self.monitor_2 = []
        self.monitor_3 = []
        self.monitor_4 = []
        self.monitor_5 = []
        self.monitor_6 = []

        # Create a frame and place a label into it.
        self.frame_1 = LabelFrame(master, bd=0, height=315, width=350)
        self.frame_1.grid(row=0, column=0, padx=50, pady=50)
        self.frame_1.grid_propagate(False)

        self.label_1 = Label(self.frame_1)
        self.label_1.grid(row=0, column=0)

        # Create a list of picture files from a folder as default ads if the paid slots are empty.
        self.fold_files = os.listdir(r'C:\Users\Lenovo\PycharmProjects\adWall\default_pictures')
        self.fold_files = [file for file in self.fold_files if file[-4:] == '.jpg']

        # Create a number variable to be used in changing the graphics on the screen.
        self.x = 0

    # Create a paid ad pictures list.
    def p_sql_adds(self):
        self.paid_pic_paths_1 = []
        paid_paths = ad_timeing.paid_ad_paths('you_screen.screen_1')

        if len(paid_paths) > 0:
            for path in paid_paths:
                if path not in self.paid_pic_paths_1:
                    self.paid_pic_paths_1.append(path)

    # Create all the 15 picture paths to circulate for a given hour.
    def all_15_paths(self):
        self.fifteen_paths = []
        for ad_num in range(15):  # 0 to 14.
            if ad_num < len(self.paid_pic_paths_1):
                self.fifteen_paths.append(self.paid_pic_paths_1[ad_num])
            else:  # TODO create a function generating a picture for the unpaid slots.
                self.fifteen_paths.append(r'C:\Users\Lenovo\PycharmProjects\adWall\default_pictures\%s'
                                          % self.fold_files[ad_num])

    #  Transform all the pictures to Tkinter resized pictures.
    def image_transform(self):
        self.monitor_1 = []
        for image in self.fifteen_paths:
            self.monitor_1.append(ImageTk.PhotoImage(Image.open(image)
                                                     .resize((350, 315), Image.ANTIALIAS)))

    #  Change the picture on the first monitor by changing frame/label picture.
    def change_only(self, im):
        self.label_1.configure(image=self.monitor_1[im])

    #  Wait for a pre-set time and call the functions above.
    #  Call the function inside itself and make a cycle.
    def calling(self):

        self.master.after(20, lambda: self.change_only(self.x))
        self.master.after(6000, self.calling)
        self.x = self.x + 1
        print(self.x)
        print('list length tk_im:', len(self.monitor_1))
        print('list 15 paths:', len(self.fifteen_paths))

        #  Check for new ads and add them to the image cycle at the 8th spin.
        if self.x == 8:
            self.p_sql_adds()
            self.all_15_paths()
            self.image_transform()

        #  When self.x reaches the 15th picture it's changed back to 0 to start the new cycle.
        elif self.x == len(self.monitor_1):
            self.x = 0


def function_call():
    y_screen = YouScreen(root)
    y_screen.p_sql_adds()
    y_screen.all_15_paths()
    y_screen.image_transform()

    #  Start the self calling cycle 'calling()'.
    y_screen.calling()

    #  Make the widow full-screen.
    root.attributes('-fullscreen', True)
    root.mainloop()


if __name__ == '__main__':
    function_call()
