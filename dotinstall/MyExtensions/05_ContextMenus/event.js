'use strict';

/*
右クリックで表示されるメニューを作っていく
*/
chrome.runtime.onInstalled.addListener(function(){
    // 最初の一回だけやればよいので、この拡張機能がインストールされたときのイベントを使う

    // 階層的なメニューにしてやりたいので、まずは親となるメニューを作成する
    var parent = chrome.contextMenus.create({
        id: 'parent',
        title: 'Choose Background Color'  // 右クリックメニューに表示される
    });
    // 子階層のメニューを作っていく
    chrome.contextMenus.create({
        id: 'red',
        parentId: parent,
        title: 'Red'
    });
    chrome.contextMenus.create({
        id: 'blue',
        parentId: parent,
        title: 'Blue'
    });
    chrome.contextMenus.create({
        id: 'green',
        parentId: parent,
        title: 'Green'
    });

});

// 右クリックメニューが選択されたときのイベントを作成する
chrome.contextMenus.onClicked.addListener(function(item){
    // 右クリックメニューで選択された項目はitemに入っている
    chrome.tabs.executeScript({
        // 背景色を変更する
        code: 'document.body.style.backgroundColor = "' + item.menuItemId + '"'
    });
});