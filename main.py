# -*- coding: utf-8 -*-
from PIL import Image
import sys


def LoadImage(ImageToAnalyze):
    htmlFile = open(ImageToAnalyze + ".html", "w", encoding="utf-8")
    im = Image.open(ImageToAnalyze)
    rgb_im = im.convert("RGB")

    htmlFile.write(
        '<!DOCTYPE html>' +
        '<html>' +

        '<head>' +
        '<meta charset="utf-8" />' +
        '<meta http-equiv="X-UA-Compatible" content="IE=edge">' +
        '<title>' + ImageToAnalyze + '</title>' +
        '<meta name="viewport" content="width=device-width, initial-scale=1">' +
        '</head>' +

        '<body>' +
        '<pre>\n'
    )

    for x in range(im.size[1]):
        for y in range(im.size[0]):
            r, g, b = rgb_im.getpixel((y, x))
            """sys.stdout.write(
                "<g style='color: rgb" +
                "(" + str(r) + ", " + str(g) + ", " + str(b) + ")" + " "
                + "'>\u2588\u2588</g>"
            )"""
            htmlFile.write(
                "<g style='color: rgb" +
                "(" + str(r) + ", " + str(g) + ", " + str(b) + ")" + " "
                + "'>\u2588\u2588</g>"
            )
        # sys.stdout.write("\n")
        htmlFile.write("\n")
    sys.stdout.flush()
    htmlFile.write(
        "\n</pre>" +
        "</body>" +
        "</html>"
    )
    htmlFile.close()


if __name__ == "__main__":
    try:
        LoadImage(sys.argv[1])
    except IndexError:
        LoadImage(input("Enter image name: "))
