(function(){
    // 即時関数で囲む
    'use strict';
    // リンク数をカウントする
    var links = document.getElementsByTagName('a');
    //alert(links.length);

    // Content Scriptからchrome.runtime.sendMessage()を使ってメッセージを投げる
    // 第一引数にはメッセージのキーと値を指定する
    // 第二引数はうまくいったときのコールバック関数
    chrome.runtime.sendMessage(
        {count: links.length},
        function(){
            console.log("message sent!");
        }    
    );    
})();
