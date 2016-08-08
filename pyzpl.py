from PIL import Image
import urllib.request
import io


class Element():

    def __init__(self, label, x=0, y=0, w=25, h=25, hide_border=False):
        self.label = label
        self.label.x = x
        self.label.y = y
        self.label.w = w
        self.label.h = h
        self.label.origin = '^FO{},{}'.format(
            int(x * self.label.dpmm),
            int(y * self.label.dpmm))
        self.label.font_origin = '^FO{},{}'.format(
            int(x * self.label.dpmm),
            int((y + 1) * self.label.dpmm))

        if not hide_border:
            self.draw_border()

        self.label.append(self.label.origin)
        # self.code += "^FO%i,%i" % (x * self.dpmm, y * self.dpmm)

    def draw_border(self):
        self.label.append(self.label.origin)
        self.label.append(
            '^GB{},{},1^FS'.format(
                self.label.w * self.label.dpmm,
                self.label.h * self.label.dpmm))
        self.label.append('^FS')

    def __enter__(self):
        return self.label

    def __exit__(self, type, value, traceback):
        self.label.append('^FS')


class Barcode():

    def __init__(self, label, ** kwargs):
        self.sub_label = label

        line_width = kwargs.get("line_width", self.sub_label.w)
        font = kwargs.get("font", 0)
        self.sub_label.append(self.sub_label.font_origin)
        self.sub_label.append('^BCN,25,Y,N,N'.format())
        # self.sub_label.append(code)

    def __enter__(self):
        return self.sub_label

    def __exit__(self, type, value, traceback):
        # self.sub_label.append('')
        pass


class Text():

    def __init__(self, label, ** kwargs):
        self.sub_label = label

        line_width = kwargs.get("line_width", self.sub_label.w)
        max_line = kwargs.get("max_line", 1)
        line_spaces = kwargs.get("line_spaces", 0)
        justification = kwargs.get("justification", "C")
        hanging_indent = kwargs.get("hanging_indent", 0)

        font = kwargs.get("font", 0)
        orientation = kwargs.get("orientation", 'N')
        font_height = kwargs.get("font_height", 20)
        font_width = kwargs.get("font_width", 20)

        self.highlighted = kwargs.get("highlighted", False)
        if self.highlighted:
            self.sub_label.append(self.sub_label.origin)
            self.sub_label.append('^GB{},{},{}^FS'.format(int(
                line_width * self.sub_label.dpmm), int(font_height + 6), int(font_height + 6)))
            self.sub_label.append('^FR')

        self.sub_label.append(self.sub_label.font_origin)
        self.sub_label.append('^A{},{},{},{}'.format(
            font, orientation, font_height, font_width))

        code = '^FB{},{},{},{},{}\n^FD'.format(
            int(line_width * self.sub_label.dpmm),
            max_line,
            line_spaces,
            justification,
            hanging_indent)

        self.sub_label.append(code)

    def __enter__(self):
        return self.sub_label

    def __exit__(self, type, value, traceback):
        self.sub_label.append('^LRN')


class Label(list):

    def __init__(self, height, width=110.0, dpmm=8.0):
        """
        Creates one (or more) ZPL2 labels.

        *height* and *width* are given in millimeters
        *dpmm* refers to dots per millimeter (e.g. 12 for 300dpi)
        """
        self.height = int(height)
        self.width = int(width)
        self.dpmm = int(dpmm)

        # self.append('^XA')

    @property
    def zpl(self):
        self._zpl = '^XA\n'
        self._zpl += '\n'.join(self)
        self._zpl += '\n^XZ'
        return self._zpl

    def preview(self, index=0):
        '''
        Opens rendered preview using Labelary API.

        Not all commands are supported, see http://labelary.com for more information.
        '''
        url = 'http://api.labelary.com/v1/printers/{}dpmm/labels/{}x{}/{}/'.format(
            self.dpmm, self.width / 25.4, self.height / 25.4, index)
        print(url)

        preview = None
        with urllib.request.urlopen(url, str.encode(self.zpl.replace('\n', ''))) as preview:
            preview = Image.open(io.BytesIO(preview.read()))
        preview.show()

if __name__ == '__main__':
    from create_label import Print_Label, Create_Label
    Create_Label()
