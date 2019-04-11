'use strict';
// Content Scriptからメッセージを受け取った時の処理をchrome.runtime.onMessage.addListenerで書く
// コールバック関数でメッセージを受け取った時の処理を書けばOK
chrome.runtime.onMessage.addListener(
    function(message, sender, callback){
        // 第一引数は受け取ったメッセージ
        // 第二引数はそれを送ってきたオブジェクト
        // 第三引数は受け取った後に実行したいコールバック関数を指定することができる

        // 今回はBrowserActionのバッジにリンクの数を指定する
        chrome.browserAction.setBadgeText({text: message.count + ""});
    }
);