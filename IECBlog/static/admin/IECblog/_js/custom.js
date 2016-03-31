/**
 * Created by Vizards on 16/3/16.
 * Contact me via E-mail: vizards@front.dog.
 */

/* 给每一个pre标签加上prettyprint的class属性,让prettify.js渲染 */

var code = document.getElementsByTagName("pre");
for (var i=0; i<code.length; i++){
    var codeEach = code[i];
    var att = document.createAttribute("class");
    att.value = "prettyprint";
    codeEach.setAttributeNode(att);
}

/* 给每一个table标签hack上cellspacing与cellpadding,避免出现table边框有缝隙的出现 */

var table = document.getElementsByTagName("table");
for (var i=0; i<table.length; i++){
    var tableEach = table[i];
    var attSpacing = document.createAttribute("cellspacing");
    attSpacing.value = "0";
    tableEach.setAttributeNode(attSpacing);

    var attPadding = document.createAttribute("cellpadding");
    attPadding.value = "0";
    tableEach.setAttributeNode(attPadding);
}


/*
 * 封装的一个淡入淡出的方法,供下面两个事件调用,可以复用~
 *
 */

var iBase = {
    Id: function(name){
        return document.getElementById(name);
    },
    // 设置元素透明度,透明度值按IE规则计,即0~100
    SetOpacity: function(ev, v){
        ev.filters ? ev.style.filter = 'alpha(opacity=' + v + ')' : ev.style.opacity = v / 100;
    }
};
// 淡入效果(含淡入到指定透明度)
function fadeIn(elem, speed, opacity){
    /*
     * 参数说明
     * elem==>需要淡入的元素
     * speed==>淡入速度,正整数(可选)
     * opacity==>淡入到指定的透明度,0~100(可选)
     */
    speed = speed || 20;
    opacity = opacity || 100;
    // 显示元素,并将元素值为0透明度(不可见)
    elem.style.display = 'block';
    iBase.SetOpacity(elem, 0);
    // 初始化透明度变化值为0
    var val = 0;
    // 循环将透明值以1递增,即淡入效果
    (function(){
        iBase.SetOpacity(elem, val);
        val += 1;
        if (val <= opacity) {
            setTimeout(arguments.callee, speed)
        }
    })();
}
// 淡出效果(含淡出到指定透明度)
function fadeOut(elem, speed, opacity){
    /*
     * 参数说明
     * elem==>需要淡入的元素
     * speed==>淡入速度,正整数(可选)
     * opacity==>淡入到指定的透明度,0~100(可选)
     */
    speed = speed || 20;
    opacity = opacity || 0;
    // 初始化透明度变化值为0
    var val = 100;
    // 循环将透明值以1递减,即淡出效果
    (function(){
        iBase.SetOpacity(elem, val);
        val -= 1;
        if (val >= opacity) {
            setTimeout(arguments.callee, speed);
        }else if (val < 0) {
            // 元素透明度为0后隐藏元素
            elem.style.display = 'none';
        }
    })();
}

/* 左右导航在网页滚动时不显示,在网页停止滚动后淡入显示 */
/* mac上chrome自带的平滑滚动让导航在滚动时会出现闪烁,暂时还没想到怎么解决 */

window.onload = function () {
    var nav = document.getElementsByClassName("nav-fillpath")[0];

    window.onscroll = function () {
        if (nav.style.display = "block") {
            nav.style.display = "none";
        }
        setTimeout(function(){
            fadeIn(iBase.Id('nav'),5,0);
        })
    };
};


/*
 * 原生JavaScript实现的图片弹窗
 * 自动捕获img标签上的点击事件并弹出大图(非原图大小但保持比例),无论该img标签处于页面上的什么位置
 * 点击弹出图片的左边或右边,切换前一张后一张图片,图片顺序根据img标签HTML代码的上下位置决定
 * cursor图标采用base64编码,避免了需要引入外部图片
 * 已经插件化,引入后无需任何设置,即可使用
 * 还在完善中……
 */

// 动态创建一个div弹出层
var fancyBoxDiv = document.createElement("div");
fancyBoxDiv.className = "fancy-box";
fancyBoxDiv.id = "fancy-box";
fancyBoxDiv.style.position = "fixed";
fancyBoxDiv.style.top = "0";
fancyBoxDiv.style.right = "0";
fancyBoxDiv.style.bottom = "0";
fancyBoxDiv.style.left = "0";
fancyBoxDiv.style.backgroundColor = "rgba(114,151,161,0.5)";
fancyBoxDiv.style.zIndex = "1000";
fancyBoxDiv.style.display = "none";
document.body.appendChild(fancyBoxDiv);
var fancyBox = document.getElementsByClassName("fancy-box")[0];

// 遍历所有的img标签,并给它们添加onclick事件,添加base64编码的cursor图片
var image = document.getElementsByTagName("img");
for (var i = 0; i < image.length; i++) {
    image[i].onclick = fancyIt;
    // 放大镜图片
    image[i].style.cursor = "url(\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAQAAADZc7J/AAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JQAAgIMAAPn/AACA6QAAdTAAAOpgAAA6mAAAF2+SX8VGAAAAAmJLR0QA/4ePzL8AAAAJcEhZcwAACxMAAAsTAQCanBgAAAGaSURBVEjHpZTfZ4JRGMc/JRERLyMiYuw2drebGNF/MMZuR3Q73tkf0OwvabqKXWQxJiKa7XY3jRFjSsTu5uzinN5O50frre/hVec553Oec87zPQnBfkpBQv8fcEaNAmXgjQld7pn5JovoI5UhZI4w2pyQjA8gNECeoTV52YbkfYCEkFsoMKCo+p/pMgMCalRU3ycnTPxbSEerjzldG1NlHGWR9m8hVIPaZK08s7RVNPQBckytNYR2umkGCARTcm7AuVqhbMYildWIuhvQQSDo2zFNfQSCjg1IAkcA9NgkGT22AylQd/yxuhn9lpClKqMHNiDJdvrVvhbgC4CSWk028/chAN9uwDsA1Y0ZyOiLIyLgYutrvDTnLgtJenDwTyEtfIW0bSk37exFZKZRZKbK2phKZCYPYGXnIQXV/0RP2blqePOWa+P8tMopbnhQhDuL9RcJMtw4nrQFjz6ECQAIaPDAK4IFI1rUCYCmG+EC+ORExAE4EfEADkRcgIm4ig+AOw3Q2gWgI2q7ASTih8YuZ7BUSfpSeWE//QFJeivVldQeggAAACV0RVh0ZGF0ZTpjcmVhdGUAMjAxNS0wNy0yNVQyMTo0OTozMCswODowMO6kBPkAAAAldEVYdGRhdGU6bW9kaWZ5ADIwMTItMDUtMjJUMjI6MDE6MTIrMDg6MDC4EzVtAAAATnRFWHRzb2Z0d2FyZQBJbWFnZU1hZ2ljayA2LjguOC0xMCBRMTYgeDg2XzY0IDIwMTUtMDctMTkgaHR0cDovL3d3dy5pbWFnZW1hZ2ljay5vcmcFDJw1AAAAGHRFWHRUaHVtYjo6RG9jdW1lbnQ6OlBhZ2VzADGn/7svAAAAF3RFWHRUaHVtYjo6SW1hZ2U6OkhlaWdodAAzMij0+PQAAAAWdEVYdFRodW1iOjpJbWFnZTo6V2lkdGgAMzLQWzh5AAAAGXRFWHRUaHVtYjo6TWltZXR5cGUAaW1hZ2UvcG5nP7JWTgAAABd0RVh0VGh1bWI6Ok1UaW1lADEzMzc2OTUyNzJN7FGaAAAAE3RFWHRUaHVtYjo6U2l6ZQAzLjI0S0JCFlxVrwAAAFp0RVh0VGh1bWI6OlVSSQBmaWxlOi8vL2hvbWUvd3d3cm9vdC93d3cuZWFzeWljb24ubmV0L2Nkbi1pbWcuZWFzeWljb24uY24vc3JjLzEwNjkxLzEwNjkxNjAucG5nTeD6swAAAABJRU5ErkJggg==\"),auto";
    image[i].id = i;
}


// 图片弹出效果
function fancyIt() {
    // 获取当前点击的图片地址
    var currentImageSrc = this.src;
    var currentImageId = this.id;

    // 如果当前图片出于未弹出状态则弹出,反之同理
    if (fancyBox.style.display = "none") {
        // 使用了上面封装的淡入方法让大图渐显
        fadeIn(iBase.Id('fancy-box'),2,0);
        // 创建一个img标签,传入src值,创建一个id值以方便后续添加专有属性
        var img = new Image();
        img.src = currentImageSrc;
        img.className = "fancy-img";
        fancyBox.appendChild(img);

        // 在弹出层内动态创建一左一右两个span,用JavaScript动态控制宽度
        var leftSpan = document.createElement("span");
        var rightSpan = document.createElement("span");
        function adjustSpanWidth () {
            // 动态样式(封装)
            var fancyWidth = document.getElementsByClassName("fancy-img")[0].width;
            var clientWidth = document.documentElement.clientWidth;
            var spanWidth = (clientWidth - fancyWidth) / 2;
            leftSpan.style.width = spanWidth + "px";
            rightSpan.style.width = spanWidth + "px";
        }
        adjustSpanWidth();

        leftSpan.className = "left-span";
        leftSpan.id = "left-span";
        leftSpan.style.position = "fixed";
        leftSpan.style.height = "100%";
        leftSpan.style.left = "0";
        leftSpan.style.top = "0";
        leftSpan.style.zIndex = "1500";
        leftSpan.style.cursor = "url(\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAfCAQAAABXe8XLAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAAmJLR0QAAKqNIzIAAAAJcEhZcwAAASwAAAEsAHOI6VIAAAFYSURBVDjLldRJSxZQGIbhy+/LoVpmahMilkXgtmWKNBAulMKQQlr0K4IobOAjcBWFIELgul9Q0oi0CJEUkXYtWmRmk0NBwdtCcHvenvXz3DfncDj8Z6rpZrurdvmQK9c7b1Z4rD5T7/DAmjCjR12p3GDInPBVzf4yu9O4deG1s+XTNhr2Tlh1V1uZfdiEDeGl0ypl9iULwopbWsvsLpM2hef6yuwmIxaFz25qKbOPeeSXMK23fN87XbEkLLuuucw+bspv4YmTZXbFRe+Fj67ZU2az21Phj9u5h1X11ydHHdKtxZIfmREHjfkuvDWY87BDvzfCT/e15yYccM83YdYFDblJ1TkzwpqHOrKefWpWhTlDec8Zr4R14zqznjZ3fBHmDWvMTSpOeSFsmHAk62k1akVYcFlT1tPnmbBpUlfWs9cNy8KigfJb3kqdHtP5n28rzUacyNe38w8LrWRso9oY9QAAACV0RVh0ZGF0ZTpjcmVhdGUAMjAxNi0wMS0yM1QxNDo0NDowOSswODowMJY2lAYAAAAldEVYdGRhdGU6bW9kaWZ5ADIwMTYtMDEtMjNUMTQ6NDQ6MDkrMDg6MDDnayy6AAAATnRFWHRzb2Z0d2FyZQBJbWFnZU1hZ2ljayA2LjguOC0xMCBRMTYgeDg2XzY0IDIwMTUtMDctMTkgaHR0cDovL3d3dy5pbWFnZW1hZ2ljay5vcmcFDJw1AAAAGHRFWHRUaHVtYjo6RG9jdW1lbnQ6OlBhZ2VzADGn/7svAAAAGHRFWHRUaHVtYjo6SW1hZ2U6OkhlaWdodAAxOTnXj6jdAAAAF3RFWHRUaHVtYjo6SW1hZ2U6OldpZHRoADE1MwgeXpIAAAAZdEVYdFRodW1iOjpNaW1ldHlwZQBpbWFnZS9wbmc/slZOAAAAF3RFWHRUaHVtYjo6TVRpbWUAMTQ1MzUzMTQ0OeCZGmYAAAATdEVYdFRodW1iOjpTaXplADEuMDNLQkJm1C9fAAAAWnRFWHRUaHVtYjo6VVJJAGZpbGU6Ly8vaG9tZS93d3dyb290L3d3dy5lYXN5aWNvbi5uZXQvY2RuLWltZy5lYXN5aWNvbi5jbi9zcmMvMTE5OTEvMTE5OTE2My5wbmfA23aAAAAAAElFTkSuQmCC\"),auto";

        rightSpan.className = "right-span";
        rightSpan.id = "right-span";
        rightSpan.style.position = "fixed";
        rightSpan.style.height = "100%";
        rightSpan.style.right = "0";
        rightSpan.style.top = "0";
        rightSpan.style.zIndex = "1500";
        rightSpan.style.cursor = "url(\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAfCAQAAABXe8XLAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAAmJLR0QAAKqNIzIAAAAJcEhZcwAAASwAAAEsAHOI6VIAAAFaSURBVDjLndM/SNVhGMXxz/3dRG+FYCQYFEQggTU43cmhP0u4RA2XGro11FZbDYUt4RRN0SQu1lKb4GBDteQSDZcCG2xwKEFQsD9YFzGfFvf3qWc+33N4D+flH6+uMu6iFd+ySJ85oaOlNwfUnLIgbJoynE0ZMmldWNTWyCGVM14LXU+dyOYMmrAqLLlhf/Y9Y+bt2PLCaDZnwG1fhGW39Gehplnbts1qZpF+Ny0LX91xIAuNem7LjpfG1HLIPtctCavuG8zmjJjxW3jjrHoOabjio7DmbnZvtH0XOrkCDrpnRfjsmj0lceW0V0LXMyfL3kMeWBM+uWpvSVx3zlvhl2nHy96HPbQhfHCp3EyP894JPz1xrOx91GM/hPcu6CmJe7V0hA2PHCl7D5uyKSwYL/fd0LYorJt0qOw9YkZ3d2BVSVxp7U54IjfhPnP+mM9/kpqmywZy4v+4v/PIZd46XTKQAAAAJXRFWHRkYXRlOmNyZWF0ZQAyMDE2LTAxLTIzVDE0OjQ0OjEwKzA4OjAwzwTRSwAAACV0RVh0ZGF0ZTptb2RpZnkAMjAxNi0wMS0yM1QxNDo0NDoxMCswODowML5ZafcAAABOdEVYdHNvZnR3YXJlAEltYWdlTWFnaWNrIDYuOC44LTEwIFExNiB4ODZfNjQgMjAxNS0wNy0xOSBodHRwOi8vd3d3LmltYWdlbWFnaWNrLm9yZwUMnDUAAAAYdEVYdFRodW1iOjpEb2N1bWVudDo6UGFnZXMAMaf/uy8AAAAYdEVYdFRodW1iOjpJbWFnZTo6SGVpZ2h0ADE5OdePqN0AAAAXdEVYdFRodW1iOjpJbWFnZTo6V2lkdGgAMTUx5hA/vgAAABl0RVh0VGh1bWI6Ok1pbWV0eXBlAGltYWdlL3BuZz+yVk4AAAAXdEVYdFRodW1iOjpNVGltZQAxNDUzNTMxNDUwgF6TgwAAABF0RVh0VGh1bWI6OlNpemUAOTQzQkI+mbV7AAAAWnRFWHRUaHVtYjo6VVJJAGZpbGU6Ly8vaG9tZS93d3dyb290L3d3dy5lYXN5aWNvbi5uZXQvY2RuLWltZy5lYXN5aWNvbi5jbi9zcmMvMTE5OTEvMTE5OTE2NC5wbmdy+6qQAAAAAElFTkSuQmCC\"),auto";
        fancyBox.appendChild(leftSpan);
        fancyBox.appendChild(rightSpan);

        // 将居中显示和渐消封装为 fancyImg() 函数方便后续调用
        function fancyImg() {
            // HACK 将img有影响的样式重置到原始状态
            document.getElementsByClassName("fancy-img")[0].style.margin = "0";
            document.getElementsByClassName("fancy-img")[0].style.padding = "0";
            document.getElementsByClassName("fancy-img")[0].style.borderRadius = "0";
            // 缩小镜图片
            document.getElementsByClassName("fancy-img")[0].style.cursor = "url(\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAQAAADZc7J/AAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JQAAgIMAAPn/AACA6QAAdTAAAOpgAAA6mAAAF2+SX8VGAAAAAmJLR0QA/4ePzL8AAAAJcEhZcwAACxMAAAsTAQCanBgAAAGQSURBVEjHpZRNZwNRFIafiQghhKGEEELpNnTXTSgh/6CUbkvItkz1B6T6S1JZhS6ioVQIIdVuu0kpoVQihOzqdjF3ppP7MZ1JziWLc859zju5972OYL/IAjjRjMsZTcrUgDfmDLhnadsuQBDRkMdjhVDWCo98EkCJibY5WBNKZoAjgk8oM6Yi888MWAIuTeoy98kJc7uCXDh9xulWT4NZqCJnB3iyqUdB01mgJ6ueDVBkYZuBr2+MQLCgaAacywk163HXZEfLDOgjEIyIixECQV8FZAA4AmAYC/Crx2o6CyDP+CNQpYUTVg/UUoak8RP51QBfAFTlNH0BHALwbQa8A9CIVeBXX7S8QMBF4mO8VHcHF8n34Pifi7S2XaSkV7mj6/8z0zQ0U32rpx6ayQiI2nlCWeafGEo7NxRv3nJtVgBQiXlQhFmF/qTdGJ60NY82hAoAcGnzwCuCNVO6tHCBjhlhAtjCiEgDMCLSAQyItAAVcZUeAHcRQHcXQBTR3A3gIza0d/kPgqj6vpRe2Cd+ATlRIOJAAoZbAAAAJXRFWHRkYXRlOmNyZWF0ZQAyMDE1LTA3LTI1VDIxOjQ5OjMwKzA4OjAw7qQE+QAAACV0RVh0ZGF0ZTptb2RpZnkAMjAxMi0wNS0yMlQyMjowMToxMiswODowMLgTNW0AAABOdEVYdHNvZnR3YXJlAEltYWdlTWFnaWNrIDYuOC44LTEwIFExNiB4ODZfNjQgMjAxNS0wNy0xOSBodHRwOi8vd3d3LmltYWdlbWFnaWNrLm9yZwUMnDUAAAAYdEVYdFRodW1iOjpEb2N1bWVudDo6UGFnZXMAMaf/uy8AAAAXdEVYdFRodW1iOjpJbWFnZTo6SGVpZ2h0ADMyKPT49AAAABZ0RVh0VGh1bWI6OkltYWdlOjpXaWR0aAAzMtBbOHkAAAAZdEVYdFRodW1iOjpNaW1ldHlwZQBpbWFnZS9wbmc/slZOAAAAF3RFWHRUaHVtYjo6TVRpbWUAMTMzNzY5NTI3Mk3sUZoAAAATdEVYdFRodW1iOjpTaXplADMuMjJLQkIzNwpzAAAAWnRFWHRUaHVtYjo6VVJJAGZpbGU6Ly8vaG9tZS93d3dyb290L3d3dy5lYXN5aWNvbi5uZXQvY2RuLWltZy5lYXN5aWNvbi5jbi9zcmMvMTA2OTEvMTA2OTE2MS5wbmdwgNMDAAAAAElFTkSuQmCC\"),auto";

            // 使弹出层的图片居中显示
            var fancyHeight = document.getElementsByClassName("fancy-img")[0].height;
            var cilentHeight = document.documentElement.clientHeight;
            var paddingHeight = (cilentHeight - fancyHeight) / 2;
            fancyBox.style.paddingTop = paddingHeight + "px";

            // 使用上面封装的淡出方法让大图渐消
            document.getElementsByClassName("fancy-img")[0].onclick = function(){
                fadeOut(iBase.Id('fancy-box'),2,0);
                // 将fancyBox这个div中的图片移除,供下次点击时新的图片放入
                var img = document.getElementsByClassName("fancy-img")[0];
                fancyBox.removeChild(img);
                // 将fancyBox中的两个span移除,防止多次点击图片后出现多个span
                var leftSpan = document.getElementById("left-span");
                var rightSpan = document.getElementById("right-span");
                fancyBox.removeChild(leftSpan);
                fancyBox.removeChild(rightSpan);
            }
        }

        fancyImg();
    }

    function alertIt(content,height,width){
        var alertDiv = document.createElement("div");
        alertDiv.className = "alert-div";
        alertDiv.id = "alert-div";
        alertDiv.style.position = "fixed";
        alertDiv.style.textAlign = "center";
        alertDiv.style.width = 'width';
        alertDiv.style.height = 'height';
        alertDiv.style.backgroundColor = "rgba(0,0,0,0.2)";
        alertDiv.style.color = "#ffffff";
        alertDiv.style.fontSize = "24px";
        alertDiv.style.zIndex = "1500";
        alertDiv.style.borderRadius = "20px";
        alertDiv.style.paddingLeft = alertDiv.style.paddingRight = "20px";
        alertDiv.innerHTML = content;

        var clientWidth = document.documentElement.clientWidth;
        var clientHeight = document.documentElement.clientHeight;
        var top = (clientHeight - height) / 2;
        var left = (clientWidth - width) / 2;
        alertDiv.style.top = top + 'px';
        alertDiv.style.left = left + 'px';

        document.body.appendChild(alertDiv);

        fadeIn(iBase.Id('alert-div'),5,0);
        setTimeout("fadeOut(iBase.Id('alert-div'),5,0)",900);
        setTimeout('document.getElementById("alert-div").parentNode.removeChild(document.getElementById("alert-div"))',1500);
    }

    if(fancyBox.style.display = "block"){

        document.getElementById("left-span").onclick = function(){
            var prevImageId = currentImageId * 1 - 1;
            if (document.getElementById(prevImageId) == null){
                alertIt("已经是第一张辣!",100,200);
                return;
            }
            var prevImageSrc = document.getElementById(prevImageId).src;
            var img = document.getElementsByClassName("fancy-img")[0];
            fancyBox.removeChild(img);
            var img = new Image();
            img.src = prevImageSrc;
            img.className = "fancy-img";
            fancyBox.appendChild(img);
            adjustSpanWidth();
            fancyImg();
            currentImageId = prevImageId;
        };

        document.getElementById("right-span").onclick = function(){
            var nextImageId = currentImageId * 1 + 1;
            if (document.getElementById(nextImageId) == null ){
                alertIt("已经是最后一张辣!",100,200);
                return;
            }
            var nextImageSrc = document.getElementById(nextImageId).src;
            var img = document.getElementsByClassName("fancy-img")[0];
            fancyBox.removeChild(img);
            var img = new Image();
            img.src = nextImageSrc;
            img.className = "fancy-img";
            fancyBox.appendChild(img);
            adjustSpanWidth();
            fancyImg();
            currentImageId = nextImageId;
        }
    }
}

