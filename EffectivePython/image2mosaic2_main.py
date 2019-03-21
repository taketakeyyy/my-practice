import cv2
from pathlib import Path
import time
import subprocess

IMAGE_PATH = "../../../tmp/image"


def main():
    """ メモリ不足で動作に失敗する
    cv2.error: OpenCV(3.4.4) C:\projects\opencv-python\opencv\modules\core\src\alloc.cpp:55: error: (-4:Insufficient memory) Failed to allocate 1277946880 bytes in function 'cv::OutOfMemoryError'
    """
    files = Path(IMAGE_PATH + "/origin/").glob("*")
    procs = []
    for file in files:
        proc = subprocess.Popen(["python", "image2mosaic2_sub.py", str(file), file.name, IMAGE_PATH])
        procs.append(proc)

    # 子プロセスの終了を待つ
    for proc in procs:
        proc.communicate()


def main2():
    """ 100枚の画像から、100枚のモザイク処理した画像を生成する
    Popenを使って並列処理でモザイク画像を生成する
    """
    files = Path(IMAGE_PATH + "/origin/").glob("*")
    procs = []
    N = 5  # メモリ不足にならないようにNを適切に設定する必要がある
    for file in files:
        proc = subprocess.Popen(["python", "image2mosaic2_sub.py", str(file), file.name, IMAGE_PATH])
        procs.append(proc)

        if len(procs) == N:
            # メモリ不足で実行に失敗するので、
            # 子プロセスの数がNになったら、一旦全ての子プロセスの終了を待つ
            for proc in procs:
                proc.communicate()
            procs.clear()
    for proc in procs:
        proc.communicate()


if __name__ == "__main__":
    start = time.time()
    main2()
    end = time.time()
    print("Finished in {} seconds.".format(end-start))
