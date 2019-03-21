'use strict';

/*
全てのウィンドウのタブの情報を取得する
chrome.tabs.query({}, function(tabs){
    // 第一引数は空のオブジェクトを渡す
    // tabsには、開いているすべてのタブ情報が入っている
*/

/* 
現在開いているウィンドウだけのタブを取得する
chrome.tabs.query({lastFocusedWindow: true}, function(tabs){
*/

/*
現在見ているタブのタイトルだけを取得する
*/
chrome.tabs.query({active: true, lastFocusedWindow: true}, function(tabs){
    var i;
    var results = document.getElementById("results");
    var titles = [];

    for(i=0; i<tabs.length; i++){
        console.log(tabs[i].title);
        titles.push(tabs[i].title);
    }
    // results.valueは、textareaのvalueのこと
    results.value = titles.join("\n");
    // 選択状態にする
    results.select();
});
