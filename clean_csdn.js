// ==UserScript==
// @name         纯净版CSDN
// @description  【CSDN美化】自动展开+内容only


// @namespace    https://github.com/idejie
// @version      2.1
// @author       idejie
// @match        http*://blog.csdn.net/*/article/details/*
// @run-at       document-end
// @grant        none
// @license      CC-BY-NC-3.0
// @supportURL   https://github.com/idejie
// @date         29/11/2018
// @modified    29/11/2018
// ==/UserScript==

(function () {
    'use strict';
    document.querySelector('div.article_content').style='';
    var readmore=document.getElementById("btn-readmore").parentNode;
    readmore.parentNode.removeChild(readmore);
    var ef = document.querySelector('.hide-article-box');
    if (ef) {
        ef.remove();
        //document.querySelector('#article_content').style.height='auto';
    }
    //阅读全文
    $('#btn-readmore').click();
    //vip免广告 按钮
    $('.meau-gotop-box').remove();
    //未登录提示
    $('.unlogin-box').remove();
    //去除剪切板劫持
    csdn.copyright.init("", "", "");
    //移除左侧最新评论
    $('#asideNewComments').remove();
    //移除左侧CSDN联系方式
    $('.persion_article').remove();
    //移除右侧工具栏
    $('.tool-box').remove()
    //下部推荐
    $('.recommend-box').remove();
    //两栏处理
    $('.nodata .container').css({'width':'1318px !important'})
    $('.nodata .tool-box .meau-list .btn-like-box p').css({'display': 'block'})
    $('.recommend-right').css({'display':'none'})
    $('.container').css({'width':'1318px'})
    $('.container main').css({'width': '1010px'})
    $('.container main .recommend-box .type_blog .content .desc').css({'width': '81%'})
    $('.container main .recommend-box .type_blog .content .blog_title_box').css({'width': '18%'})
    $("#mainBox > main").css("float","left");  //感谢 ID:potoo 的反馈
    $("aside").remove();
    $('body').css({'min-width':'0'});
    $('.csdn-toolbar').css({'min-width':'0'});
    //去广告
    $('.pulllog-box').remove();
    $('.fourth_column').remove();
    $('.mb8').remove();
    $('newsfeed').remove();
    $('#asideFooter').remove();
    $("li:contains('赚零钱')").remove();
    $("aside").css({'display':'block'});
    $("#mainBox > main").css("width","100%");
    $('.container').css({'width':'100%'})
 
})();
