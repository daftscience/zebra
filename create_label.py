from pyzpl import Label, Element, Text, Barcode
from printer import Printer


def Create_Label():
    label = Label(50, 50)
    with Element(label, 0, 0, w=50) as l:
        with Text(l) as t:
            t.append("Label 1")
    with Element(label, 0, 25) as l:
        with Text(l, font_height=30) as t:
            t.append('Label 2')
    with Element(label, 25, 25) as l:
        with Text(l, highlighted=True, font_height=15) as t:
            t.append('Label 3')
    with Element(label, 25, 35) as l:
        with Barcode(l,) as t:
            t.append('Label 3')

    label.preview()
    return label.zpl

if __name__ == '__main__':

    # Printer(Create_Label())
    Create_Label()
