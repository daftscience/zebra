

class Label_Text():

    def __init__(self, label, x=0, y=0):
        self.label = label
        self.label.append(
            '^FO{},{}'.format(
                x * self.label.dpmm,
                y * self.label.dpmm))
        # self.code += "^FO%i,%i" % (x * self.dpmm, y * self.dpmm)

    def __enter__(self):

        return self.label

    def __exit__(self, type, value, traceback):
        self.label.append('^FS')


class Label(list):

    def __init__(self, height, width=110.0, dpmm=8.0):
        """
        Creates one (or more) ZPL2 labels.

        *height* and *width* are given in millimeters
        *dpmm* refers to dots per millimeter (e.g. 12 for 300dpi)
        """
        self.height = height
        self.width = width
        self.dpmm = dpmm

        self.append('^XA')

    @property
    def zpl(self):
        self._zpl = "\n".join(self)
        return self._zpl
