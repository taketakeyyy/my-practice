'use strict';

/*
popup.htmlのselect要素にイベントを仕込む
(1) まずは、要素を取得する
(2) addEventListenerを仕込み、値が変わったときに次の処理をしなさい…とする
(3) ページ内にJSを埋め込んで実行するには、chrome.tabs.executeScriptが使える
*/
document.getElementById("colors").addEventListener("change",
function(){
    chrome.tabs.executeScript({
        code: 'document.body.style.backgroundColor = "' + this.value + '"'
    });
});
