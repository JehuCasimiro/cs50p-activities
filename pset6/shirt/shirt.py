import sys
from PIL import Image, ImageOps

def main():
    check_args()

    try:
        image_file = Image.open(sys.argv[1])
        shirt_file = Image.open("shirt.png")
        sizing = shirt_file.size
        resized_image = ImageOps.fit(image_file, sizing)
        resized_image.paste(shirt_file, shirt_file)
        resized_image.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit("Input does not exist")


def check_args():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few coomand-line arguments")
    else:
        pass

    file1_extension = sys.argv[1][-4:]
    file2_extension = sys.argv[2][-4:]

    if file1_extension != file2_extension:
        sys.exit("Input and output have different extensions")
    else:
        pass

    check_extension(sys.argv[1])
    check_extension(sys.argv[2])


def check_extension(file):
    extensions = (".jpg", ".jpeg", ".png")
    if file.endswith(extensions) == False:
        sys.exit("Invalid Output")
    else:
        pass


if __name__ == "__main__":
    main()