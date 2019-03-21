import cv2
from pathlib import Path
import time

IMAGE_PATH = "../../../tmp/image"


def mosaic(src, ratio=0.1):
    small = cv2.resize(src, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    return cv2.resize(small, src.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)

def mosaic_area(src, x, y, width, height, ratio=0.1):
    dst = src.copy()
    dst[y:y + height, x:x + width] = mosaic(dst[y:y + height, x:x + width], ratio)
    return dst

def img2mosaic(src, ratio=0.1):
    """ 元画像srcを受け取り、モザイク処理した画像dstを返す """
    cascade_path = "".join(cv2.__path__) + "/data/haarcascade_frontalface_default.xml"
    cascade = cv2.CascadeClassifier(cascade_path)

    src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(src_gray)

    for x, y, w, h in faces:
        dst = mosaic_area(src, x, y, w, h, ratio)

    return dst


def main():
    """ 100枚の画像から、100枚のモザイク処理した画像を生成する """
    files = Path(IMAGE_PATH + "/origin/").glob("*")
    for file in files:
        src = cv2.imread(str(file))
        dst = img2mosaic(src, ratio=0.01)
        cv2.imwrite(IMAGE_PATH + "/mosaic/" + file.name, dst)

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Finished in {} seconds.".format(end-start))
