import subprocess
import multiprocessing
import pandas as pd
import numpy as np
import time

def run_subprocess():
    proc = subprocess.Popen(['echo', 'Hello from the child!'], stdout=subprocess.PIPE, shell=True)
    out, err = proc.communicate()
    print(out.decode("utf-8"))

def poll_subprocess():
    import time
    # 子プロセスsubp.pyを実行する
    proc = subprocess.Popen(["python", "subp.py"], shell=True)
    while proc.poll() is None:
        # 子プロセスが終了するまで実行し続ける
        print("Working...")
        time.sleep(0.5)

def run_multisleep():
    """ 複数の子プロセスでrun_sleep.pyを実行する """
    def run_sleep():
        proc = subprocess.Popen(["python", "run_sleep.py"])
        return proc

    start = time.time()
    procs = []
    for _ in range(10):
        procs.append(run_sleep())

    for proc in procs:
        proc.communicate()

    end = time.time()
    print("Finished in {} seconds.".format(end-start))


def run_multisubp():
    """ 複数の子プロセスでfib.pyを実行する """
    def run_fib():
        proc = subprocess.Popen(["python", "fib.py"])
        return proc

    start = time.time()
    procs = []
    for _ in range(10):
        procs.append(run_sleep())

    for proc in procs:
        proc.communicate()

    end = time.time()
    print("Finished in {} seconds.".format(end-start))

def run_excel2csv_single():
    """ 大阪市のJR各駅の乗車人員情報のエクセルファイルから、
    駅名,総数,定期,定期外
    の情報を抜き出して、年度ごとのcsvファイルを作成する
    """
    FILENAME = "12-7.xls"
    excel = pd.ExcelFile(FILENAME)
    for sheet_name in excel.sheet_names:
        is_skip = True # 行をスキップするか
        text = ""     # ファイルに書き込む文字列
        df = pd.read_excel(FILENAME, sheet_name=sheet_name)
        for index, row in df.iterrows():
            # 関係ない行はスキップする
            if is_skip:
                if str(row[1]).replace(" ", "") == "総数":
                    is_skip = False
                else:
                    continue
            if row[5] is np.nan:
                continue

            # 駅名を取得する
            if row[3] is not np.nan:
                station = str(row[3])
            elif row[2] is not np.nan:
                station = str(row[2])
            else:
                station = str(row[1])

            try:
                text += "{},{},{},{}\n".format(station.replace(" ", ""), row[21], row[26], row[31])
            except:
                text += "{},{},{},{}\n".format(station.replace(" ", ""), row[8], row[9], row[10])
        # ファイルに書き込む
        filename = "H" + str(int(sheet_name[1:])-1) + ".csv"
        f = open(filename, "w", encoding="utf-8")
        f.write(text)
        f.close()


def run_excel2csv_multi():
    """ 大阪市のJR各駅の乗車人員情報のエクセルファイルから、
    駅名,総数,定期,定期外
    の情報を抜き出して、年度ごとのcsvファイルを作成する
    """
    def run_excel2csv(sheet_name):
        is_skip = True # 行をスキップするか
        text = ""     # ファイルに書き込む文字列
        df = pd.read_excel(FILENAME, sheet_name=sheet_name)
        for index, row in df.iterrows():
            # 関係ない行はスキップする
            if is_skip:
                if str(row[1]).replace(" ", "") == "総数":
                    is_skip = False
                else:
                    continue
            if row[5] is np.nan:
                continue

            # 駅名を取得する
            if row[3] is not np.nan:
                station = str(row[3])
            elif row[2] is not np.nan:
                station = str(row[2])
            else:
                station = str(row[1])

            try:
                text += "{},{},{},{}\n".format(station.replace(" ", ""), row[21], row[26], row[31])
            except:
                text += "{},{},{},{}\n".format(station.replace(" ", ""), row[8], row[9], row[10])
        # ファイルに書き込む
        filename = "H" + str(int(sheet_name[1:])-1) + ".csv"
        f = open(filename, "w", encoding="utf-8")
        f.write(text)
        f.close()


    FILENAME = "12-7.xls"
    excel = pd.ExcelFile(FILENAME)
    procs = []
    for sheet_name in excel.sheet_names:
        p = multiprocessing.Process(target=run_excel2csv, args=(sheet_name))
        p.start()
        procs.append(p)



if __name__ == "__main__":
    #run_multisubp()
    #run_multisleep()
    start = time.time()
    run_excel2csv_single()
    run_excel2csv_multi()
    end = time.time()
    print("Finished in {} seconds.".format(end-start))
