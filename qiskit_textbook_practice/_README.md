# 環境の構築方法
## 仮想環境を作成し、仮想環境をアクティブにする
```sh
# 仮想環境の作成
$ python -m venv venv

# 仮想環境をアクティブにする(Windows)
$ venv/Scripts/Activate
```

## pipを最新にする
```sh
$ python -m pip install --upgrade pip
```

## 必要なものを公式からインストールする。
https://qiskit.org/textbook/ja/ch-prerequisites/setting-the-environment.html

```sh
$ pip install git+https://github.com/qiskit-community/qiskit-textbook.git#subdirectory=qiskit-textbook-src
```

## その他必要なものをインストールする
* pylatexenc
  - draw("mpl")するのに必要