from pyzpl import Label, Element, Text, Barcode
import socket


class Print_Label:
    TCP_IP = '10.20.12.99'
    TCP_PORT = 9100
    BUFFER_SIZE = 1024

    def __init__(self, zpl):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.TCP_IP, self.TCP_PORT))
        s.send(bytes(zpl, "utf-8"))
        # s.send(zpl)
        s.close()


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

    # Print_Label(Create_Label())
    Create_Label()
    # l.origin(0, 1)
    # l.write_text(
    #     "Label 1",
    #     char_height=8,
    #     char_width=8,
    #     line_width=50,
    #     justification='C')
    # l.endorigin()
    # l.origin(10, 10)
    # l.write_qr("Bar Code", justification='C')
    # l.endorigin()
    # # l.origin(0,0)
    # # l.draw_box(25, 25, thickness=1, color='B')
    # # l.endorigin()
    # l.origin(1, 40)
    # l.write_text(
    #     "Label 2",
    #     char_height=5,
    #     char_width=5,
    #     line_width=25,
    #     justification='C')
    # l.endorigin()
    # l.origin(26, 40)
    # l.write_text(
    #     "Label 3",
    #     char_height=5,
    #     char_width=5,
    #     line_width=25,
    #     justification='C')
    # l.endorigin()
    # # height += 10
    # # image_width = 10
    # # l.origin((l.width-image_width)/2, height)
    # # image_height = l.write_graphic(Image.open('trollface-large.png'), image_width)
    # # l.endorigin()

    # print(l.dumpZPL())
    # l.preview()
    # # test = Print_Label(l.dumpZPL())
