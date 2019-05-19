// ==UserScript==
// @name         国科大上网脚本
// @namespace    https://github.com/idejie/Scripts/blob/master/fuck_ucas_net.js
// @version      0.2
// @description  A script for F**king UCAS network
// @author       idejie
// @match        http://210.77.16.21/eportal/index.jsp*
// @supportURL   https://github.com/idejie
// @date         2019/05/19
// @modified    2019/05/19
// ==/UserScript==

(function() {
    'use strict';
    // Your code here...
    // init user infos
    var uname="请输入你的用户名";
    var psword="输入你的密码";
    //for remove the check  '/' in username
    checkForm=()=>true;
    //get elements for login
    var username = document.getElementById("username");
    var password = document.getElementById("pwd");
    //change elements value
    username.value = "e中国科学院\\"+uname;
    password.value = psword;
    //click login_btn
    var login_btn = document.getElementById('loginLink');
    login_btn.click();
})();
