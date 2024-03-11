# The TKHTMLview change for the desktop script not to get overloaded
# with buffer data of images.

# The error is because in TKHTMLview library the images used by the TKinter are
# saved as deepcopies. When the images are rotating they stay in the memory and
# overload it.



#~ line 487 / C:\Users\lenovo\Desktop\virtual_env\Lib\site-packages\tkhtmlview\html_parser.py
# Fixed here!
        elif tag == HTML.Tag.IMG and attrs[HTML.Attrs.SRC]:
            #-------------------------------------------------------------------- [ UNSTYLED_TAGS ]
            print("What runs 10.")
            image = None
            #print(attrs[HTML.Attrs.SRC] , self.cached_images)
            if attrs[HTML.Attrs.SRC].startswith(("https://" , "ftp://" , "http://")):
                if attrs[HTML.Attrs.SRC] in self.cached_images.keys():
                    print("What runs 11.")
                    # image = deepcopy(self.cached_images[attrs[HTML.Attrs.SRC]])
                else:
                    try:
                        print("What runs 12.")
                        image = Image.open(BytesIO(requests.get(attrs[HTML.Attrs.SRC]).content))
                        # self.cached_images[attrs[HTML.Attrs.SRC]] = deepcopy(image)
                    except :
                        pass

