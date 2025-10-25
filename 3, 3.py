import random
from PIL import Image

original = Image.open('1.png')
(width, height) = (original.width, original.height)
original = original.convert("1")
o_pixels = original.load()
first = Image.new("1", (original.size[0], original.size[1] * 4))
f_pixels = first.load()
second = Image.new("1", (original.size[0], original.size[1] * 4))
s_pixels = second.load()
third = Image.new("1", (original.size[0], original.size[1] * 4))
t_pixels = third.load()
w = 0
b = 0
int(w)
int(b)
for i in range(original.size[0]):
    for j in range(original.size[1]):
        if o_pixels[i, j] == 0:
            w = w + 1
            x = random.randint(1, 24)
            if x == 1:
                f_pixels[i, j * 4] = 0
                f_pixels[i, j * 4 + 1] = 0
                f_pixels[i, j * 4 + 2] = 1
                f_pixels[i, j * 4 + 3] = 1

                s_pixels[i, j * 4] = 1
                s_pixels[i, j * 4 + 1] = 0
                s_pixels[i, j * 4 + 2] = 1
                s_pixels[i, j * 4 + 3] = 0

                t_pixels[i, j * 4] = 0
                t_pixels[i, j * 4 + 1] = 1
                t_pixels[i, j * 4 + 2] = 1
                t_pixels[i, j * 4 + 3] = 0

            if x == 2:
                f_pixels[i, j * 4] = 0
                f_pixels[i, j * 4 + 1] = 0
                f_pixels[i, j * 4 + 2] = 1
                f_pixels[i, j * 4 + 3] = 1

                s_pixels[i, j * 4] = 0
                s_pixels[i, j * 4 + 1] = 1
                s_pixels[i, j * 4 + 2] = 0
                s_pixels[i, j * 4 + 3] = 1

                t_pixels[i, j * 4] = 1
                t_pixels[i, j * 4 + 1] = 0
                t_pixels[i, j * 4 + 2] = 0
                t_pixels[i, j * 4 + 3] = 1

            if x == 3:
                f_pixels[i, j * 4] = 1
                f_pixels[i, j * 4 + 1] = 1
                f_pixels[i, j * 4 + 2] = 0
                f_pixels[i, j * 4 + 3] = 0

                s_pixels[i, j * 4] = 1
                s_pixels[i, j * 4 + 1] = 0
                s_pixels[i, j * 4 + 2] = 1
                s_pixels[i, j * 4 + 3] = 0

                t_pixels[i, j * 4] = 1
                t_pixels[i, j * 4 + 1] = 0
                t_pixels[i, j * 4 + 2] = 0
                t_pixels[i, j * 4 + 3] = 1

            if x == 4:
                f_pixels[i, j * 4] = 1
                f_pixels[i, j * 4 + 1] = 1
                f_pixels[i, j * 4 + 2] = 0
                f_pixels[i, j * 4 + 3] = 0

                s_pixels[i, j * 4] = 0
                s_pixels[i, j * 4 + 1] = 1
                s_pixels[i, j * 4 + 2] = 0
                s_pixels[i, j * 4 + 3] = 1

                t_pixels[i, j * 4] = 0
                t_pixels[i, j * 4 + 1] = 1
                t_pixels[i, j * 4 + 2] = 1
                t_pixels[i, j * 4 + 3] = 0

            if x == 5:
                f_pixels[i, j * 4] = 0
                f_pixels[i, j * 4 + 1] = 1
                f_pixels[i, j * 4 + 2] = 1
                f_pixels[i, j * 4 + 3] = 0

                s_pixels[i, j * 4] = 1
                s_pixels[i, j * 4 + 1] = 0
                s_pixels[i, j * 4 + 2] = 1
                s_pixels[i, j * 4 + 3] = 0

                t_pixels[i, j * 4] = 0
                t_pixels[i, j * 4 + 1] = 0
                t_pixels[i, j * 4 + 2] = 1
                t_pixels[i, j * 4 + 3] = 1

            if x == 6:
                f_pixels[i, j * 4] = 1
                f_pixels[i, j * 4 + 1] = 0
                f_pixels[i, j * 4 + 2] = 0
                f_pixels[i, j * 4 + 3] = 1

                s_pixels[i, j * 4] = 0
                s_pixels[i, j * 4 + 1] = 1
                s_pixels[i, j * 4 + 2] = 0
                s_pixels[i, j * 4 + 3] = 1

                t_pixels[i, j * 4] = 0
                t_pixels[i, j * 4 + 1] = 0
                t_pixels[i, j * 4 + 2] = 1
                t_pixels[i, j * 4 + 3] = 1

            if x == 7:
                f_pixels[i, j * 4] = 1
                f_pixels[i, j * 4 + 1] = 0
                f_pixels[i, j * 4 + 2] = 0
                f_pixels[i, j * 4 + 3] = 1

                s_pixels[i, j * 4] = 1
                s_pixels[i, j * 4 + 1] = 0
                s_pixels[i, j * 4 + 2] = 1
                s_pixels[i, j * 4 + 3] = 0

                t_pixels[i, j * 4] = 1
                t_pixels[i, j * 4 + 1] = 1
                t_pixels[i, j * 4 + 2] = 0
                t_pixels[i, j * 4 + 3] = 0

            if x == 8:
                f_pixels[i, j * 4] = 0
                f_pixels[i, j * 4 + 1] = 1
                f_pixels[i, j * 4 + 2] = 1
                f_pixels[i, j * 4 + 3] = 0

                s_pixels[i, j * 4] = 0
                s_pixels[i, j * 4 + 1] = 1
                s_pixels[i, j * 4 + 2] = 0
                s_pixels[i, j * 4 + 3] = 1

                t_pixels[i, j * 4] = 1
                t_pixels[i, j * 4 + 1] = 1
                t_pixels[i, j * 4 + 2] = 0
                t_pixels[i, j * 4 + 3] = 0

            if x == 9:
                f_pixels[i, j * 4] = 1
                f_pixels[i, j * 4 + 1] = 0
                f_pixels[i, j * 4 + 2] = 1
                f_pixels[i, j * 4 + 3] = 0

                s_pixels[i, j * 4] = 0
                s_pixels[i, j * 4 + 1] = 0
                s_pixels[i, j * 4 + 2] = 1
                s_pixels[i, j * 4 + 3] = 1

                t_pixels[i, j * 4] = 0
                t_pixels[i, j * 4 + 1] = 1
                t_pixels[i, j * 4 + 2] = 1
                t_pixels[i, j * 4 + 3] = 0

            if x == 10:
                f_pixels[i, j * 4] = 0
                f_pixels[i, j * 4 + 1] = 1
                f_pixels[i, j * 4 + 2] = 0
                f_pixels[i, j * 4 + 3] = 1

                s_pixels[i, j * 4] = 0
                s_pixels[i, j * 4 + 1] = 0
                s_pixels[i, j * 4 + 2] = 1
                s_pixels[i, j * 4 + 3] = 1

                t_pixels[i, j * 4] = 1
                t_pixels[i, j * 4 + 1] = 0
                t_pixels[i, j * 4 + 2] = 0
                t_pixels[i, j * 4 + 3] = 1

            if x == 11:
                f_pixels[i, j * 4] = 1
                f_pixels[i, j * 4 + 1] = 0
                f_pixels[i, j * 4 + 2] = 1
                f_pixels[i, j * 4 + 3] = 0

                s_pixels[i, j * 4] = 1
                s_pixels[i, j * 4 + 1] = 1
                s_pixels[i, j * 4 + 2] = 0
                s_pixels[i, j * 4 + 3] = 0

                t_pixels[i, j * 4] = 1
                t_pixels[i, j * 4 + 1] = 0
                t_pixels[i, j * 4 + 2] = 0
                t_pixels[i, j * 4 + 3] = 1

            if x == 12:
                f_pixels[i, j * 4] = 0
                f_pixels[i, j * 4 + 1] = 1
                f_pixels[i, j * 4 + 2] = 0
                f_pixels[i, j * 4 + 3] = 1

                s_pixels[i, j * 4] = 1
                s_pixels[i, j * 4 + 1] = 1
                s_pixels[i, j * 4 + 2] = 0
                s_pixels[i, j * 4 + 3] = 0

                t_pixels[i, j * 4] = 0
                t_pixels[i, j * 4 + 1] = 1
                t_pixels[i, j * 4 + 2] = 1
                t_pixels[i, j * 4 + 3] = 0

            if x == 13:
                f_pixels[i, j * 4] = 1
                f_pixels[i, j * 4 + 1] = 0
                f_pixels[i, j * 4 + 2] = 1
                f_pixels[i, j * 4 + 3] = 0

                s_pixels[i, j * 4] = 0
                s_pixels[i, j * 4 + 1] = 1
                s_pixels[i, j * 4 + 2] = 1
                s_pixels[i, j * 4 + 3] = 0

                t_pixels[i, j * 4] = 0
                t_pixels[i, j * 4 + 1] = 0
                t_pixels[i, j * 4 + 2] = 1
                t_pixels[i, j * 4 + 3] = 1

            if x == 14:
                f_pixels[i, j * 4] = 0
                f_pixels[i, j * 4 + 1] = 1
                f_pixels[i, j * 4 + 2] = 0
                f_pixels[i, j * 4 + 3] = 1

                s_pixels[i, j * 4] = 1
                s_pixels[i, j * 4 + 1] = 0
                s_pixels[i, j * 4 + 2] = 0
                s_pixels[i, j * 4 + 3] = 1

                t_pixels[i, j * 4] = 0
                t_pixels[i, j * 4 + 1] = 0
                t_pixels[i, j * 4 + 2] = 1
                t_pixels[i, j * 4 + 3] = 1

            if x == 15:
                f_pixels[i, j * 4] = 1
                f_pixels[i, j * 4 + 1] = 0
                f_pixels[i, j * 4 + 2] = 1
                f_pixels[i, j * 4 + 3] = 0

                s_pixels[i, j * 4] = 0
                s_pixels[i, j * 4 + 1] = 1
                s_pixels[i, j * 4 + 2] = 1
                s_pixels[i, j * 4 + 3] = 0

                t_pixels[i, j * 4] = 1
                t_pixels[i, j * 4 + 1] = 1
                t_pixels[i, j * 4 + 2] = 0
                t_pixels[i, j * 4 + 3] = 0

            if x == 16:
                f_pixels[i, j * 4] = 0
                f_pixels[i, j * 4 + 1] = 1
                f_pixels[i, j * 4 + 2] = 0
                f_pixels[i, j * 4 + 3] = 1

                s_pixels[i, j * 4] = 1
                s_pixels[i, j * 4 + 1] = 0
                s_pixels[i, j * 4 + 2] = 0
                s_pixels[i, j * 4 + 3] = 1

                t_pixels[i, j * 4] = 1
                t_pixels[i, j * 4 + 1] = 1
                t_pixels[i, j * 4 + 2] = 0
                t_pixels[i, j * 4 + 3] = 0

            if x == 17:
                f_pixels[i, j * 4] = 0
                f_pixels[i, j * 4 + 1] = 0
                f_pixels[i, j * 4 + 2] = 1
                f_pixels[i, j * 4 + 3] = 1

                s_pixels[i, j * 4] = 0
                s_pixels[i, j * 4 + 1] = 1
                s_pixels[i, j * 4 + 2] = 1
                s_pixels[i, j * 4 + 3] = 0

                t_pixels[i, j * 4] = 1
                t_pixels[i, j * 4 + 1] = 0
                t_pixels[i, j * 4 + 2] = 1
                t_pixels[i, j * 4 + 3] = 0

            if x == 18:
                f_pixels[i, j * 4] = 0
                f_pixels[i, j * 4 + 1] = 0
                f_pixels[i, j * 4 + 2] = 1
                f_pixels[i, j * 4 + 3] = 1

                s_pixels[i, j * 4] = 1
                s_pixels[i, j * 4 + 1] = 0
                s_pixels[i, j * 4 + 2] = 0
                s_pixels[i, j * 4 + 3] = 1

                t_pixels[i, j * 4] = 0
                t_pixels[i, j * 4 + 1] = 1
                t_pixels[i, j * 4 + 2] = 0
                t_pixels[i, j * 4 + 3] = 1

            if x == 19:
                f_pixels[i, j * 4] = 1
                f_pixels[i, j * 4 + 1] = 1
                f_pixels[i, j * 4 + 2] = 0
                f_pixels[i, j * 4 + 3] = 0

                s_pixels[i, j * 4] = 1
                s_pixels[i, j * 4 + 1] = 0
                s_pixels[i, j * 4 + 2] = 0
                s_pixels[i, j * 4 + 3] = 1

                t_pixels[i, j * 4] = 1
                t_pixels[i, j * 4 + 1] = 0
                t_pixels[i, j * 4 + 2] = 1
                t_pixels[i, j * 4 + 3] = 0

            if x == 20:
                f_pixels[i, j * 4] = 1
                f_pixels[i, j * 4 + 1] = 1
                f_pixels[i, j * 4 + 2] = 0
                f_pixels[i, j * 4 + 3] = 0

                s_pixels[i, j * 4] = 0
                s_pixels[i, j * 4 + 1] = 1
                s_pixels[i, j * 4 + 2] = 1
                s_pixels[i, j * 4 + 3] = 0

                t_pixels[i, j * 4] = 0
                t_pixels[i, j * 4 + 1] = 1
                t_pixels[i, j * 4 + 2] = 0
                t_pixels[i, j * 4 + 3] = 1
            if x == 21:
                f_pixels[i, j * 4] = 0
                f_pixels[i, j * 4 + 1] = 1
                f_pixels[i, j * 4 + 2] = 1
                f_pixels[i, j * 4 + 3] = 0

                s_pixels[i, j * 4] = 0
                s_pixels[i, j * 4 + 1] = 0
                s_pixels[i, j * 4 + 2] = 1
                s_pixels[i, j * 4 + 3] = 1

                t_pixels[i, j * 4] = 1
                t_pixels[i, j * 4 + 1] = 0
                t_pixels[i, j * 4 + 2] = 1
                t_pixels[i, j * 4 + 3] = 0

            if x == 22:
                f_pixels[i, j * 4] = 1
                f_pixels[i, j * 4 + 1] = 0
                f_pixels[i, j * 4 + 2] = 0
                f_pixels[i, j * 4 + 3] = 1

                s_pixels[i, j * 4] = 0
                s_pixels[i, j * 4 + 1] = 0
                s_pixels[i, j * 4 + 2] = 1
                s_pixels[i, j * 4 + 3] = 1

                t_pixels[i, j * 4] = 0
                t_pixels[i, j * 4 + 1] = 1
                t_pixels[i, j * 4 + 2] = 0
                t_pixels[i, j * 4 + 3] = 1

            if x == 23:
                f_pixels[i, j * 4] = 1
                f_pixels[i, j * 4 + 1] = 0
                f_pixels[i, j * 4 + 2] = 0
                f_pixels[i, j * 4 + 3] = 1

                s_pixels[i, j * 4] = 1
                s_pixels[i, j * 4 + 1] = 1
                s_pixels[i, j * 4 + 2] = 0
                s_pixels[i, j * 4 + 3] = 0

                t_pixels[i, j * 4] = 1
                t_pixels[i, j * 4 + 1] = 0
                t_pixels[i, j * 4 + 2] = 1
                t_pixels[i, j * 4 + 3] = 0

            if x == 24:
                f_pixels[i, j * 4] = 0
                f_pixels[i, j * 4 + 1] = 1
                f_pixels[i, j * 4 + 2] = 1
                f_pixels[i, j * 4 + 3] = 0

                s_pixels[i, j * 4] = 1
                s_pixels[i, j * 4 + 1] = 1
                s_pixels[i, j * 4 + 2] = 0
                s_pixels[i, j * 4 + 3] = 0

                t_pixels[i, j * 4] = 0
                t_pixels[i, j * 4 + 1] = 1
                t_pixels[i, j * 4 + 2] = 0
                t_pixels[i, j * 4 + 3] = 1


        else:
            x = random.randint(1, 24)
            b = b + 1
            if x == 1:
                f_pixels[i, j * 4] = 0
                f_pixels[i, j * 4 + 1] = 0
                f_pixels[i, j * 4 + 2] = 1
                f_pixels[i, j * 4 + 3] = 1

                s_pixels[i, j * 4] = 1
                s_pixels[i, j * 4 + 1] = 0
                s_pixels[i, j * 4 + 2] = 1
                s_pixels[i, j * 4 + 3] = 0

                t_pixels[i, j * 4] = 1
                t_pixels[i, j * 4 + 1] = 0
                t_pixels[i, j * 4 + 2] = 0
                t_pixels[i, j * 4 + 3] = 1

            if x == 2:
                f_pixels[i, j * 4] = 0
                f_pixels[i, j * 4 + 1] = 0
                f_pixels[i, j * 4 + 2] = 1
                f_pixels[i, j * 4 + 3] = 1

                s_pixels[i, j * 4] = 0
                s_pixels[i, j * 4 + 1] = 1
                s_pixels[i, j * 4 + 2] = 0
                s_pixels[i, j * 4 + 3] = 1

                t_pixels[i, j * 4] = 0
                t_pixels[i, j * 4 + 1] = 1
                t_pixels[i, j * 4 + 2] = 1
                t_pixels[i, j * 4 + 3] = 0

            if x == 3:
                f_pixels[i, j * 4] = 1
                f_pixels[i, j * 4 + 1] = 1
                f_pixels[i, j * 4 + 2] = 0
                f_pixels[i, j * 4 + 3] = 0

                s_pixels[i, j * 4] = 1
                s_pixels[i, j * 4 + 1] = 0
                s_pixels[i, j * 4 + 2] = 1
                s_pixels[i, j * 4 + 3] = 0

                t_pixels[i, j * 4] = 0
                t_pixels[i, j * 4 + 1] = 1
                t_pixels[i, j * 4 + 2] = 1
                t_pixels[i, j * 4 + 3] = 0

            if x == 4:
                f_pixels[i, j * 4] = 1
                f_pixels[i, j * 4 + 1] = 1
                f_pixels[i, j * 4 + 2] = 0
                f_pixels[i, j * 4 + 3] = 0

                s_pixels[i, j * 4] = 0
                s_pixels[i, j * 4 + 1] = 1
                s_pixels[i, j * 4 + 2] = 0
                s_pixels[i, j * 4 + 3] = 1

                t_pixels[i, j * 4] = 1
                t_pixels[i, j * 4 + 1] = 0
                t_pixels[i, j * 4 + 2] = 0
                t_pixels[i, j * 4 + 3] = 1

            if x == 5:
                f_pixels[i, j * 4] = 1
                f_pixels[i, j * 4 + 1] = 0
                f_pixels[i, j * 4 + 2] = 0
                f_pixels[i, j * 4 + 3] = 1

                s_pixels[i, j * 4] = 1
                s_pixels[i, j * 4 + 1] = 0
                s_pixels[i, j * 4 + 2] = 1
                s_pixels[i, j * 4 + 3] = 0

                t_pixels[i, j * 4] = 0
                t_pixels[i, j * 4 + 1] = 0
                t_pixels[i, j * 4 + 2] = 1
                t_pixels[i, j * 4 + 3] = 1

            if x == 6:
                f_pixels[i, j * 4] = 0
                f_pixels[i, j * 4 + 1] = 0
                f_pixels[i, j * 4 + 2] = 1
                f_pixels[i, j * 4 + 3] = 1

                s_pixels[i, j * 4] = 0
                s_pixels[i, j * 4 + 1] = 1
                s_pixels[i, j * 4 + 2] = 0
                s_pixels[i, j * 4 + 3] = 1

                t_pixels[i, j * 4] = 0
                t_pixels[i, j * 4 + 1] = 0
                t_pixels[i, j * 4 + 2] = 1
                t_pixels[i, j * 4 + 3] = 1

            if x == 7:
                f_pixels[i, j * 4] = 0
                f_pixels[i, j * 4 + 1] = 1
                f_pixels[i, j * 4 + 2] = 1
                f_pixels[i, j * 4 + 3] = 0

                s_pixels[i, j * 4] = 1
                s_pixels[i, j * 4 + 1] = 0
                s_pixels[i, j * 4 + 2] = 1
                s_pixels[i, j * 4 + 3] = 0

                t_pixels[i, j * 4] = 1
                t_pixels[i, j * 4 + 1] = 1
                t_pixels[i, j * 4 + 2] = 0
                t_pixels[i, j * 4 + 3] = 0

            if x == 8:
                f_pixels[i, j * 4] = 1
                f_pixels[i, j * 4 + 1] = 0
                f_pixels[i, j * 4 + 2] = 0
                f_pixels[i, j * 4 + 3] = 1

                s_pixels[i, j * 4] = 0
                s_pixels[i, j * 4 + 1] = 1
                s_pixels[i, j * 4 + 2] = 0
                s_pixels[i, j * 4 + 3] = 1

                t_pixels[i, j * 4] = 1
                t_pixels[i, j * 4 + 1] = 1
                t_pixels[i, j * 4 + 2] = 0
                t_pixels[i, j * 4 + 3] = 0

            if x == 9:
                f_pixels[i, j * 4] = 1
                f_pixels[i, j * 4 + 1] = 0
                f_pixels[i, j * 4 + 2] = 1
                f_pixels[i, j * 4 + 3] = 0

                s_pixels[i, j * 4] = 0
                s_pixels[i, j * 4 + 1] = 0
                s_pixels[i, j * 4 + 2] = 1
                s_pixels[i, j * 4 + 3] = 1

                t_pixels[i, j * 4] = 1
                t_pixels[i, j * 4 + 1] = 0
                t_pixels[i, j * 4 + 2] = 0
                t_pixels[i, j * 4 + 3] = 1

            if x == 10:
                f_pixels[i, j * 4] = 0
                f_pixels[i, j * 4 + 1] = 1
                f_pixels[i, j * 4 + 2] = 0
                f_pixels[i, j * 4 + 3] = 1

                s_pixels[i, j * 4] = 0
                s_pixels[i, j * 4 + 1] = 0
                s_pixels[i, j * 4 + 2] = 1
                s_pixels[i, j * 4 + 3] = 1

                t_pixels[i, j * 4] = 0
                t_pixels[i, j * 4 + 1] = 1
                t_pixels[i, j * 4 + 2] = 1
                t_pixels[i, j * 4 + 3] = 0

            if x == 11:
                f_pixels[i, j * 4] = 1
                f_pixels[i, j * 4 + 1] = 0
                f_pixels[i, j * 4 + 2] = 1
                f_pixels[i, j * 4 + 3] = 0

                s_pixels[i, j * 4] = 1
                s_pixels[i, j * 4 + 1] = 1
                s_pixels[i, j * 4 + 2] = 0
                s_pixels[i, j * 4 + 3] = 0

                t_pixels[i, j * 4] = 0
                t_pixels[i, j * 4 + 1] = 1
                t_pixels[i, j * 4 + 2] = 1
                t_pixels[i, j * 4 + 3] = 0

            if x == 12:
                f_pixels[i, j * 4] = 0
                f_pixels[i, j * 4 + 1] = 1
                f_pixels[i, j * 4 + 2] = 0
                f_pixels[i, j * 4 + 3] = 1

                s_pixels[i, j * 4] = 1
                s_pixels[i, j * 4 + 1] = 1
                s_pixels[i, j * 4 + 2] = 0
                s_pixels[i, j * 4 + 3] = 0

                t_pixels[i, j * 4] = 1
                t_pixels[i, j * 4 + 1] = 0
                t_pixels[i, j * 4 + 2] = 0
                t_pixels[i, j * 4 + 3] = 1

            if x == 13:
                f_pixels[i, j * 4] = 1
                f_pixels[i, j * 4 + 1] = 0
                f_pixels[i, j * 4 + 2] = 1
                f_pixels[i, j * 4 + 3] = 0

                s_pixels[i, j * 4] = 1
                s_pixels[i, j * 4 + 1] = 0
                s_pixels[i, j * 4 + 2] = 0
                s_pixels[i, j * 4 + 3] = 1

                t_pixels[i, j * 4] = 0
                t_pixels[i, j * 4 + 1] = 0
                t_pixels[i, j * 4 + 2] = 1
                t_pixels[i, j * 4 + 3] = 1

            if x == 14:
                f_pixels[i, j * 4] = 0
                f_pixels[i, j * 4 + 1] = 1
                f_pixels[i, j * 4 + 2] = 0
                f_pixels[i, j * 4 + 3] = 1

                s_pixels[i, j * 4] = 0
                s_pixels[i, j * 4 + 1] = 1
                s_pixels[i, j * 4 + 2] = 1
                s_pixels[i, j * 4 + 3] = 0

                t_pixels[i, j * 4] = 0
                t_pixels[i, j * 4 + 1] = 0
                t_pixels[i, j * 4 + 2] = 1
                t_pixels[i, j * 4 + 3] = 1

            if x == 15:
                f_pixels[i, j * 4] = 1
                f_pixels[i, j * 4 + 1] = 0
                f_pixels[i, j * 4 + 2] = 1
                f_pixels[i, j * 4 + 3] = 0

                s_pixels[i, j * 4] = 0
                s_pixels[i, j * 4 + 1] = 1
                s_pixels[i, j * 4 + 2] = 1
                s_pixels[i, j * 4 + 3] = 0

                t_pixels[i, j * 4] = 1
                t_pixels[i, j * 4 + 1] = 1
                t_pixels[i, j * 4 + 2] = 0
                t_pixels[i, j * 4 + 3] = 0

            if x == 16:
                f_pixels[i, j * 4] = 0
                f_pixels[i, j * 4 + 1] = 1
                f_pixels[i, j * 4 + 2] = 0
                f_pixels[i, j * 4 + 3] = 1

                s_pixels[i, j * 4] = 1
                s_pixels[i, j * 4 + 1] = 0
                s_pixels[i, j * 4 + 2] = 0
                s_pixels[i, j * 4 + 3] = 1

                t_pixels[i, j * 4] = 1
                t_pixels[i, j * 4 + 1] = 1
                t_pixels[i, j * 4 + 2] = 0
                t_pixels[i, j * 4 + 3] = 0

            if x == 17:
                f_pixels[i, j * 4] = 0
                f_pixels[i, j * 4 + 1] = 0
                f_pixels[i, j * 4 + 2] = 1
                f_pixels[i, j * 4 + 3] = 1

                s_pixels[i, j * 4] = 1
                s_pixels[i, j * 4 + 1] = 0
                s_pixels[i, j * 4 + 2] = 0
                s_pixels[i, j * 4 + 3] = 1

                t_pixels[i, j * 4] = 1
                t_pixels[i, j * 4 + 1] = 0
                t_pixels[i, j * 4 + 2] = 1
                t_pixels[i, j * 4 + 3] = 0

            if x == 18:
                f_pixels[i, j * 4] = 0
                f_pixels[i, j * 4 + 1] = 0
                f_pixels[i, j * 4 + 2] = 1
                f_pixels[i, j * 4 + 3] = 1

                s_pixels[i, j * 4] = 0
                s_pixels[i, j * 4 + 1] = 1
                s_pixels[i, j * 4 + 2] = 1
                s_pixels[i, j * 4 + 3] = 0

                t_pixels[i, j * 4] = 0
                t_pixels[i, j * 4 + 1] = 1
                t_pixels[i, j * 4 + 2] = 0
                t_pixels[i, j * 4 + 3] = 1

            if x == 19:
                f_pixels[i, j * 4] = 1
                f_pixels[i, j * 4 + 1] = 1
                f_pixels[i, j * 4 + 2] = 0
                f_pixels[i, j * 4 + 3] = 0

                s_pixels[i, j * 4] = 0
                s_pixels[i, j * 4 + 1] = 1
                s_pixels[i, j * 4 + 2] = 1
                s_pixels[i, j * 4 + 3] = 0

                t_pixels[i, j * 4] = 1
                t_pixels[i, j * 4 + 1] = 0
                t_pixels[i, j * 4 + 2] = 1
                t_pixels[i, j * 4 + 3] = 0

            if x == 20:
                f_pixels[i, j * 4] = 1
                f_pixels[i, j * 4 + 1] = 1
                f_pixels[i, j * 4 + 2] = 0
                f_pixels[i, j * 4 + 3] = 0

                s_pixels[i, j * 4] = 1
                s_pixels[i, j * 4 + 1] = 0
                s_pixels[i, j * 4 + 2] = 0
                s_pixels[i, j * 4 + 3] = 1

                t_pixels[i, j * 4] = 0
                t_pixels[i, j * 4 + 1] = 1
                t_pixels[i, j * 4 + 2] = 0
                t_pixels[i, j * 4 + 3] = 1

            if x == 21:
                f_pixels[i, j * 4] = 1
                f_pixels[i, j * 4 + 1] = 0
                f_pixels[i, j * 4 + 2] = 0
                f_pixels[i, j * 4 + 3] = 1

                s_pixels[i, j * 4] = 0
                s_pixels[i, j * 4 + 1] = 0
                s_pixels[i, j * 4 + 2] = 1
                s_pixels[i, j * 4 + 3] = 1

                t_pixels[i, j * 4] = 1
                t_pixels[i, j * 4 + 1] = 0
                t_pixels[i, j * 4 + 2] = 1
                t_pixels[i, j * 4 + 3] = 0

            if x == 22:
                f_pixels[i, j * 4] = 0
                f_pixels[i, j * 4 + 1] = 1
                f_pixels[i, j * 4 + 2] = 1
                f_pixels[i, j * 4 + 3] = 0

                s_pixels[i, j * 4] = 0
                s_pixels[i, j * 4 + 1] = 0
                s_pixels[i, j * 4 + 2] = 1
                s_pixels[i, j * 4 + 3] = 1

                t_pixels[i, j * 4] = 0
                t_pixels[i, j * 4 + 1] = 1
                t_pixels[i, j * 4 + 2] = 0
                t_pixels[i, j * 4 + 3] = 1

            if x == 23:
                f_pixels[i, j * 4] = 0
                f_pixels[i, j * 4 + 1] = 1
                f_pixels[i, j * 4 + 2] = 1
                f_pixels[i, j * 4 + 3] = 0

                s_pixels[i, j * 4] = 1
                s_pixels[i, j * 4 + 1] = 1
                s_pixels[i, j * 4 + 2] = 0
                s_pixels[i, j * 4 + 3] = 0

                t_pixels[i, j * 4] = 1
                t_pixels[i, j * 4 + 1] = 0
                t_pixels[i, j * 4 + 2] = 1
                t_pixels[i, j * 4 + 3] = 0

            if x == 24:
                f_pixels[i, j * 4] = 1
                f_pixels[i, j * 4 + 1] = 0
                f_pixels[i, j * 4 + 2] = 0
                f_pixels[i, j * 4 + 3] = 1

                s_pixels[i, j * 4] = 1
                s_pixels[i, j * 4 + 1] = 1
                s_pixels[i, j * 4 + 2] = 0
                s_pixels[i, j * 4 + 3] = 0

                t_pixels[i, j * 4] = 0
                t_pixels[i, j * 4 + 1] = 1
                t_pixels[i, j * 4 + 2] = 0
                t_pixels[i, j * 4 + 3] = 1

first.save("(3, 3) share1.png")
second.save("(3, 3) share2.png")
third.save("(3, 3) share3.png")

im1 = Image.open("(3, 3) share1.png")
im1 = im1.resize((width, height))
im1.save("(3, 3) share1.png")
im1.show()

im2 = Image.open("(3, 3) share2.png")
im2 = im2.resize((width, height))
im2.save("(3, 3) share2.png")
im2.show()

im3 = Image.open("(3, 3) share3.png")
im3 = im3.resize((width, height))
im3.save("(3, 3) share3.png")
im3.show()

first = Image.open("(3, 3) share1.png")
f_pixels = first.load()

second = Image.open("(3, 3) share2.png")
s_pixels = second.load()

third = Image.open("(3, 3) share3.png")
t_pixels = third.load()

result_3 = Image.new("1", (int(first.size[0]), int(first.size[1]/4)))
r3_pixels = result_3.load()

for i in range(result_3.size[0]):
    for j in range(result_3.size[1]):
        if (f_pixels[i, j * 4] + s_pixels[i, j * 4] + t_pixels[i, j * 4] == 0) or\
                (f_pixels[i, j * 4 + 1] + s_pixels[i, j * 4 + 1] + t_pixels[i, j * 4 + 1] == 0) or\
                (f_pixels[i, j * 4 + 2] + s_pixels[i, j * 4 + 2] + t_pixels[i, j * 4 + 2] == 0) or\
                (f_pixels[i, j * 4 + 3] + s_pixels[i, j * 4 + 3] + t_pixels[i, j * 4 + 3] == 0):

            r3_pixels[i, j] = 1
        else:
            r3_pixels[i, j] = 0

result_3.save("result (3 , 3).png")
result_3 = Image.open("result (3 , 3).png")
result_3 = result_3.resize((width, height))
result_3.save("result (3 , 3).png")
result_3.show()

s2_s3 = Image.new("1", (int(third.size[0]), int(third.size[1] / 4)))
r_pixels = s2_s3.load()
for i in range(s2_s3.size[0]):
    for j in range(s2_s3.size[1]):
        if (s_pixels[i, j * 4] + t_pixels[i, j * 4] == 0) or (s_pixels[i, j * 4 + 1] + t_pixels[i, j * 4 + 1] == 0) or\
                (s_pixels[i, j * 4 + 2] + t_pixels[i, j * 4 + 2] == 0) or\
                (s_pixels[i, j * 4 + 3] + t_pixels[i, j * 4 + 3] == 0):
            r_pixels[i, j] = 1
        else:
            r_pixels[i, j] = 0

s2_s3.save("result_s2+s3 (3 , 3).png")
s2_s3 = Image.open("result_s2+s3 (3 , 3).png")
s2_s3 = s2_s3.resize((width, height))
s2_s3.save("result_s2+s3 (3 , 3).png")
s2_s3.show()

s1_s2 = Image.new("1", (int(first.size[0]), int(first.size[1] / 4)))
r1_pixels = s1_s2.load()
for i in range(s1_s2.size[0]):
    for j in range(s1_s2.size[1]):
        if (f_pixels[i, j * 4] + s_pixels[i, j * 4] == 0) or (f_pixels[i, j * 4 + 1] + s_pixels[i, j * 4 + 1] == 0) or\
                (f_pixels[i, j * 4 + 2] + s_pixels[i, j * 4 + 2] == 0) or\
                (f_pixels[i, j * 4 + 3] + s_pixels[i, j * 4 + 3] == 0):
            r1_pixels[i, j] = 1
        else:
            r1_pixels[i, j] = 0

s1_s2.save("result_s1+s2 (3 , 3).png")
s1_s2 = Image.open("result_s1+s2 (3 , 3).png")
s1_s2 = s1_s2.resize((width, height))
s1_s2.save("result_s1+s2 (3 , 3).png")
s1_s2.show()

s1_s3 = Image.new("1", (int(first.size[0]), int(first.size[1] / 4)))
r2_pixels = s1_s3.load()
for i in range(s1_s3.size[0]):
    for j in range(s1_s3.size[1]):
        if (f_pixels[i, j * 4] + t_pixels[i, j * 4] == 0) or (f_pixels[i, j * 4 + 1] + t_pixels[i, j * 4 + 1] == 0) or \
                (f_pixels[i, j * 4 + 2] + t_pixels[i, j * 4 + 2] == 0) or \
                (f_pixels[i, j * 4 + 3] + t_pixels[i, j * 4 + 3] == 0):
            r2_pixels[i, j] = 1
        else:
            r2_pixels[i, j] = 0

s1_s3.save("result_s1+s3 (3 , 3).png")
s1_s3 = Image.open("result_s1+s3 (3 , 3).png")
s1_s3 = s1_s3.resize((width, height))
s1_s3.save("result_s1+s3 (3 , 3).png")
s1_s3.show()

w1 = 0
int(w1)
b1 = 0
int(b1)
w2 = 0
int(w2)
b2 = 0
int(b2)
w3 = 0
int(w3)
b3 = 0
int(b3)
w4 = 0
int(w3)
b4 = 0
int(b3)

share_1 = Image.open("(3, 3) share1.png")
t1_pixels = share_1.load()
share_2 = Image.open("(3, 3) share2.png")
t2_pixels = share_2.load()
share_3 = Image.open("(3, 3) share3.png")
t3_pixels = share_3.load()
result2_2 = Image.open("result (3 , 3).png")
t4_pixels = result2_2.load()

for i in range(share_1.size[0]):
    for j in range(share_1.size[1]):
        if t1_pixels[i, j] == 0:
            w1 = w1 + 1
        else:
            b1 = b1 + 1

        if t2_pixels[i, j] == 0:
            w2 = w2 + 1
        else:
            b2 = b2 + 1

        if t3_pixels[i, j] == 0:
            w3 = w3 + 1
        else:
            b3 = b3 + 1

        if t4_pixels[i, j] == 0:
            w4 = w4 + 1
        else:
            b4 = b4 + 1

print("number of black pixel in secret image = ", w, "\n", "number of white pixel in secret image = ", b, "\n", 'total = ', w + b)
print("number of black pixel in share 1 = ", w1, "\n", "number of white pixel in share 1 = ", b1, "\n", 'total = ', w1 + b1)
print("number of black pixel in share 2 = ", w2, "\n", "number of white pixel in share 2 = ", b2, "\n", 'total = ', w2 + b2)
print("number of black pixel in share 3 = ", w3, "\n", "number of white pixel in share 3 = ", b3, "\n", 'total = ', w3 + b3)
print("number of black pixel in decoded image = ", w4, "\n", "number of white pixel in decoded image = ", b4, "\n", 'total = ', w4 + b4)