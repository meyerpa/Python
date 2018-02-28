"""
5.8 Draw Line
A monochrome screen is stored as a single array of bytes, allowing eight
consecutive pixels to be stored in one byte. The sceen has width w, where w
is divisible by 8 (that is, no byte will be split across rows). The height
of the screen, of course, can be derived from the length of the array and the
width. Implement a function that draws a horizontal line from (x1, y) to
(x2, y). The method signature should look something like:
    drawLine(byte[] screen, int width, int x1, int x2, int y)
"""

def drawLine(screen, width, x1, x2, y):
    """ not_colored: 0
        colored: 1
        Assuming x1 and x2 represents the horizontal bit
    """
    i_offset = y * (width / 8)
    for i in range(x1, x2+1):
        screen[i_offset + i//8][i % 8] = 1
    return screen
