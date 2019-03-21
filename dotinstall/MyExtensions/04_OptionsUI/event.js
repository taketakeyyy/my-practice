'use strict';

/*
Browser Actionがクリックされたときのイベントを記述する

*/
chrome.browserAction.onClicked.addListener(function(){
    chrome.storage.sync.get({
        color: "red"
    }, function(item){
        // 読み込みがうまくいった場合のコールバック関数
        // 読み込まれた値はitemで取得できる
        // 読み込んだitemを使って背景色を変更する
        chrome.tabs.executeScript({
            code: 'document.body.style.backgroundColor = "' + item.color + '"'
        });
    });
});