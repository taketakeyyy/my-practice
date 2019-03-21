'use strict';

/*
オプションで保存した値を最初に選択されるようにする

(1) option.htmlが読み込まれた時のイベントを仕込む
*/
document.addEventListener("DOMContentLoaded", function(){
    // chrome.storage.sync.getは、chrome.storageに保存した値を読み込む
    //   - 第一引数は、取得する値のキーを指定する
    //     - キーで検索した値が見つからなかったときのデフォルト値は"red"にしておく
    //   - 
    chrome.storage.sync.get({
        color: "red"
    }, function(item){
        // 読み込みがうまくいった場合のコールバック関数
        // 読み込まれた値はitemで取得できる
        // 読み込んだitemを使ってセレクトボックスの値を設定する
        document.getElementById("colors").value = item.color;
    });
});

/*
Saveをクリックしたときの処理
*/
document.getElementById("save").addEventListener("click",
function(){
    // セレクトボックスの値を取得する
    var color = document.getElementById("colors").value;
    // colorの値をchromeのstorage機能で保存する
    //   - chrome.storage.sync.setで保存することができる
    //   - 第一引数で、key:value形式で値を保存する
    //   - 第二引数は、処理が終わったあとに実行するコールバック関数を指定できる。
    chrome.storage.sync.set({
        color: color
    }, function(){
        console.log("saved: " + color);
    });
});


/*
popup.htmlのselect要素にイベントを仕込む
(1) まずは、要素を取得する
(2) addEventListenerを仕込み、値が変わったときに次の処理をしなさい…とする
(3) ページ内にJSを埋め込んで実行するには、chrome.tabs.executeScriptが使える
*/
/*
document.getElementById("colors").addEventListener("change",
function(){
    chrome.tabs.executeScript({
        code: 'document.body.style.backgroundColor = "' + this.value + '"'
    });
});
*/
