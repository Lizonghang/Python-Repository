var toolbar_start="<ul class='stuff'>";
var toolbar_add="<li><a href='javascript:void(0);' onclick='editQ(this);' title='鎮ㄤ篃鍙互鍙屽嚮棰樼洰鏉ヨ繘琛岀紪杈�'><span class='design-icon design-edit'></span><span>缂栬緫</span></a></li>";
var toolbar_copy="<li><a href='javascript:void(0);' onclick='curover.copyQ();' title='澶嶅埗姝ら'><span class='design-icon design-copy'></span><span>澶嶅埗</span></a></li>";
var toolbar_moveup="<li><a href='javascript:void(0);' onclick='curover.moveUp();'  title='灏嗘棰樹笂绉�'><span class='design-icon design-up'></span><span>涓婄Щ</span></a></li>";
var toolbar_movedown="<li><a href='javascript:void(0);' onclick='curover.moveDown();'  title='灏嗘棰樹笅绉�'><span class='design-icon design-down'></span><span>涓嬬Щ</span></a></li>";
var toolbar_movefirst="<li><a href='javascript:void(0);' onclick='curover.moveFirst();'  title='灏嗘棰樼Щ鍔ㄥ埌绗竴棰�'><span class='design-icon design-first'></span><span>鏈€鍓�</span></a></li>";
var toolbar_movelast="<li><a href='javascript:void(0);' onclick='curover.moveLast();'  title='灏嗘棰樼Щ鍔ㄥ埌鏈€鍚庝竴棰�'><span class='design-icon design-last'></span><span>鏈€鍚�</span></a></li>";
var toolbar_del="<li><a href='javascript:void(0);' onclick='curover.deleteQ();'  title='鍒犻櫎姝ら'><span class='design-icon design-delete'></span><span>鍒犻櫎</span></a></li>";
var toolbar_del_move=toolbar_del+toolbar_moveup+toolbar_movedown+toolbar_movefirst+toolbar_movelast;
var toolbar_end="<div style='clear:both;'></div></ul>";
Array.prototype.indexOf=function(c){
    for(var b=0,a=this.length;b<a;b++){
        if(this[b]==c){
            return b;
        }
    }
    return -1;
};
Array.prototype.moveUp=function(b){
    var a=this.indexOf(b);
    return this._moveElement(a,-1);
};
Array.prototype.moveFirst=function(b){
    var a=this.indexOf(b);
    while(this._moveElement(a--,-1)){}
};
Array.prototype.moveDown=function(b){
    var a=this.indexOf(b);
    return this._moveElement(a,1);
};
Array.prototype.moveLast=function(b){
    var a=this.indexOf(b);
    while(this._moveElement(a++,1)){}
};
Array.prototype.moveTo=function(d,e){
    var a=this.indexOf(d);
    var c=Math.abs(e-a);
    if(a<e){
        for(var b=0;b<c;b++){
            this._moveElement(a++,1);
        }
    }
    else{
        for(var b=0;b<c;b++){
            this._moveElement(a--,-1);
        }
    }
};
Array.prototype._moveElement=function(a,d){
    var c,b;if(a<0||a>=this.length){
        return false;
    }
    c=a+d;
    if(c<0||c>=this.length||c==a){
        return false;
    }
    b=this[c];
    this[c]=this[a];
    this[a]=b;
    return true;
};
Array.prototype.insertAt=function(b,a){
    this.splice(a,0,b);
};
Array.prototype.insertBefore=function(b,a){
    this.insertAt(b,this.indexOf(a));
};
Array.prototype.remove=function(a){
    this.removeAt(this.indexOf(a));
    return a;
};
Array.prototype.removeAt=function(a){
    var b=this[a];
    if(b){this.splice(a,1);
    }
    return b;
};
function updateTopic(l){
    var a=1;
    var b=1;
    firstPage.divTopic.innerHTML="<span style='font-size:14px; font-weight:bold;'>绗�"+(b)+"椤�/鍏�"+total_page+"椤�</span>";
    b++;
    var g=new Object();
    for(var e=0;e<questionHolder.length;e++){
        var d=questionHolder[e].dataNode;
        var f=d._type;
        if(f!="page"&&f!="cut"){
            if(d._topic-a!=0){
                if(d._hasjump){
                    if(d._anytimejumpto-1>0){
                        d._anytimejumpto=parseInt(d._anytimejumpto)+(a-d._topic);
                        if(questionHolder[e].setAnyTimeJumpTo){
                            questionHolder[e].setAnyTimeJumpTo();
                        }
                    }
                    else{
                        if(d._select){
                            for(var n=1;n<d._select.length;n++){
                                if(d._select[n]._item_jump-1>0){
                                    d._select[n]._item_jump=parseInt(d._select[n]._item_jump)+(a-d._topic);
                                }
                            }
                            if(questionHolder[e].setItemJump){
                                questionHolder[e].setItemJump();
                            }
                        }
                    }
                }
                if(curNewQ!=questionHolder[e]){
                    g[d._topic]=a;
                }
            }
            d._topic=a;
            if(questionHolder[e].divTopic){
                questionHolder[e].divTopic.innerHTML=a;
                if(a-100<0){
                    questionHolder[e].divTopic.innerHTML=a+".";
                }
            }
            if(questionHolder[e]._referDivQ){
                if(questionHolder[e].createTableRadio){
                    questionHolder[e].createTableRadio();
                }
                else{
                    if(questionHolder[e].createSum){
                        questionHolder[e].createSum();
                    }
                }
                if(questionHolder[e].updateReferQ){
                    questionHolder[e].updateReferQ();
                    questionHolder[e].updateSelCheck();
                }
            }
            a++;
        }
        else{
            if(f=="page"){
                questionHolder[e].dataNode._topic=b;
                questionHolder[e].divTopic.innerHTML="<span style='font-size:14px; font-weight:bold;'>绗�"+b+"椤�/鍏�"+total_page+"椤�</span>";
                b++;
            }
        }
    }
    for(var e=0;e<questionHolder.length;e++){
        var d=questionHolder[e].dataNode;
        if(!d._relation){continue;}
        var k=d._relation.split(",");
        var j=parseInt(k[0]);
        if(g[j]){
            var a=g[j];
            var c=a+","+k[1];
            d._relation=c;
            var h=questionHolder[e].getRelation();
            var m=questionHolder[e].RelationIns;
            if(h){
                m.innerHTML=h[0];
                m.title=h[1];
            }
        }
    }
}
function recreateEditor(a){
    if(a.hasCreatedAttr){
        if(!KE.browser.IE){
            var b=a.titleId;
            if(!b){return;}
            KE.remove(b);
            KE.create(b);
            KE.util.focus(b);
        }
    }
}
function setMoveStyle(b){
    var a=b;
    setTimeout(function(){
        a.className="div_question div_question_move";
        if(prevcurmove&&prevcurmove!=a&&prevcurmove.className.toLowerCase()=="div_question div_question_move"){
            prevcurmove.className="div_question div_question_mouseout";
        }
        prevcurmove=a;
        prevcurmove.divTableOperation.style.visibility="hidden";
    },2);
}
function afterMove(b,a){
    recreateEditor(b);
    recreateEditor(a);
    updateTopic(b.dataNode._type);
    b.onmouseout();
    b.focus();
    setMoveStyle(b);
}
function moveUp(){
    var c=this.dataNode._type;
    var b=c=="page"||c=="cut";
    if(isMergeAnswer&&!b){
        alert("寰堟姳姝夛紝鍦ㄤ互鍚堝苟绛斿嵎妯″紡涓嬩慨鏀归棶鍗蜂负浜嗕繚鎸佹暟鎹竴鑷存€т笉鍏佽涓婄Щ棰樼洰锛�");
        return;
    }
    if(this._referDivQ){
        var e=parseInt(this.dataNode._topic)-1;
        var g=this._referDivQ.dataNode._topic;
        if(e<=g){
            var d="閫夐」";
            if(this.dataNode._type=="matrix"||this.dataNode._type=="sum"){
                d="琛屾爣棰�";
            }
            show_status_tip("姝ら"+d+"鏉ユ簮浜庣"+g+"棰樼殑閫変腑椤癸紝涓嶈兘鍐嶅皢姝ら绉诲埌绗�"+g+"棰樹笂鏂癸紒",4000);
            return;
        }
    }
    var a=questionHolder.indexOf(this);
    if(a>0){
        if(a==1&&isCepingQ){
            show_status_tip("涓嶈兘绉诲姩鍒拌娴嬭瘎瀵硅薄涓婇潰",3000);
        }
        var f=questionHolder[a-1];
        this.parentNode.insertBefore(this,f);
        questionHolder.moveUp(this);
        afterMove(this,f);
    }
    else{
        show_status_tip("绗�1棰樹笉鑳藉啀涓婄Щ",3000);
    }
}
function moveDown(){
    var e=this.dataNode._type;
    var g=e=="page"||e=="cut";
    if(isMergeAnswer&&!this.isMergeNewAdded&&!g){
        alert("寰堟姳姝夛紝鍦ㄤ互鍚堝苟绛斿嵎妯″紡涓嬩慨鏀归棶鍗蜂负浜嗕繚鎸佹暟鎹竴鑷存€т笉鍏佽涓嬬Щ棰樼洰锛�");
        return;
    }
    if(this._referedArray){
        var c="";
        var f=parseInt(this.dataNode._topic)+1;
        for(var d=0;d<this._referedArray.length;d++){
            var a=this._referedArray[d].dataNode._topic;
            if(f-a>=0){var j="閫夐」";
                if(this._referedArray[d].dataNode._type=="matrix"||this._referedArray[d].dataNode._type=="sum"){
                    j="琛屾爣棰�";
                }
                show_status_tip("绗�"+a+"棰樼殑"+j+"鏉ユ簮浜庢棰樼殑閫変腑椤癸紝涓嶈兘灏嗘棰樼Щ鍒扮"+a+"棰樹笅鏂癸紒",4000);
                return;
            }
        }
    }
    var h=questionHolder.indexOf(this);
    if(h<questionHolder.length-1){
        var b=questionHolder[h+1];
        this.parentNode.insertBefore(b,this);
        questionHolder.moveDown(this);
        afterMove(this,b);
    }
    else{show_status_tip("鏈€鍚�1棰樹笉鑳藉啀涓嬬Щ",3000);}
}
function moveFirst(){
    var c=this.dataNode._type;
    var b=c=="page"||c=="cut";
    if(isMergeAnswer&&!b){alert("寰堟姳姝夛紝鍦ㄤ互鍚堝苟绛斿嵎妯″紡涓嬩慨鏀归棶鍗蜂负浜嗕繚鎸佹暟鎹竴鑷存€т笉鍏佽涓婄Щ棰樼洰锛�");
        return;
    }
    if(this._referDivQ){
        var d="閫夐」";
        if(this.dataNode._type=="matrix"||this.dataNode._type=="sum"){
            d="琛屾爣棰�";
        }
        show_status_tip("姝ら"+d+"鏉ユ簮浜庣"+this._referDivQ.dataNode._topic+"棰樼殑閫変腑椤癸紝涓嶈兘灏嗘棰樼Щ鍔ㄦ渶鍓嶏紒",4000);
        return;
    }
    var a=questionHolder.indexOf(this);
    if(a>0){
        var e=questionHolder[0];
        this.parentNode.insertBefore(this,e);
        questionHolder.moveFirst(this);
        afterMove(this,e);
    }
    else{
        show_status_tip("绗�1棰樹笉鑳藉啀涓婄Щ",3000);
    }
}
function moveLast(){
    if(this._referedArray){
        var a="";
        for(var c=0;c<this._referedArray.length;c++){
            if(c>0){
                a+=",";
            }
            a+=this._referedArray[c].dataNode._topic;
        }
        show_status_tip("绗�"+a+"棰樼殑閫夐」鎴栬鏍囬鏉ユ簮浜庢棰樼殑閫変腑椤癸紝涓嶈兘灏嗘棰樼Щ鍔ㄥ埌鏈€鍚庯紒",4000);
        return;
    }
    var b=questionHolder.indexOf(this);
    if(b<questionHolder.length-1){
        var d=questionHolder[questionHolder.length-1];
        this.parentNode.insertBefore(this,d);
        this.parentNode.insertBefore(d,this);
        questionHolder.moveLast(this);
        afterMove(this,d);
    }
    else{
        show_status_tip("鏈€鍚�1棰樹笉鑳藉啀涓嬬Щ",3000);
    }
}
function insertQ(c){
    var a=curinsert==c;
    if(a){resetInsertQ();}
    else{
        curinsert=c;
        var b=$$("a",curinsert.divInsertOp)[0];
        if(b){
            b.innerHTML="鍙栨秷鎻掑叆鐐�";
        }
        setMoveStyle(curinsert);
        show_status_tip("璇峰湪椤甸潰涓婃柟閫夋嫨鐩稿簲鐨勯鍨嬫彃鍏ュ埌姝ら鐨勫悗闈�",10000);
    }
}
function resetInsertQ(){
    if(curinsert!=null){
        if(curinsert.className.toLowerCase()=="div_question div_question_move"){
            curinsert.className="div_question div_question_mouseout";
        }
        var a=$$("a",curinsert.divInsertOp)[0];
        if(a){a.innerHTML="鍦ㄦ棰樺悗鎻掑叆鏂伴";}
        curinsert=null;
    }
}
function change_dataNode(g,d){
    var b=new Object();
    b._isTouPiao=false;
    b._isCeShi=false;
    b._isCePing=false;
    var f=false;
    var e=false;
    if(d=="likert"){
        b._tag=2;
        b._type="radio";
    }
    else{
        if(d=="order"){
            b._tag=1;
            b._type="check";
            b._upLimit=b._lowLimit="-1";
        }
        else{
            if(d.indexOf("matrix")>-1){
                var h=d.split(",")[1];
                b._type="matrix";
                b._tag=h;
                b._rowtitle=g._rowtitle;
                b._rowtitle2=g._rowtitle2;
                if(g._columntitle){
                    b._columntitle=g._columntitle;
                }
                b._rowwidth=g._rowwidth;
                b._rowwidth2=g._rowwidth2;
                if(h=="202"||h=="301"){
                    b._minvalue=0;
                    b._maxvalue=10;
                }
                if(h-101<=0||h=="303"){e=true;}
            }
            else{
                if(d=="toupiaoradio"||d=="toupiaocheck"){
                    b._type=d=="toupiaoradio"?"radio":"check";
                    b._isTouPiao=true;
                    b._touPiaoWidth=g._touPiaoWidth||50;
                    b._displayTiao=g._displayTiao||true;b._displayNum=g._displayNum||true;b._displayPercent=g._displayPercent||true;
                }
                else{
                    if(d=="ceshiradio"||d=="ceshicheck"){
                        b._type=d=="ceshiradio"?"radio":"check";
                        b._isCeShi=true;
                        b._ceshiValue=5;
                        b._ceshiDesc="";
                        f=true;
                    }
                    else{
                        if(d=="cepingradio"||d=="cepingcheck"){
                            b._type=d=="cepingradio"?"radio":"check";
                            b._isCePing=true;
                        }
                        else{b._type=d;b._tag=0;}
                    }
                }
            }
        }
    }
    b._verify="0";
    b._topic=g._topic;
    b._title=g._title;
    b._requir=g._requir;
    b._ins=g._ins;
    b._hasjump=g._hasjump;
    b._anytimejumpto=g._anytimejumpto;
    b._keyword=g._keyword;
    if(g._type=="question"){
        b._hasvalue=false;
        b._randomChoice=false;
        b._isTouPiao=false;
        b._isCeShi=false;
        b._numperrow="1";
        b._select=new Array();
        for(var a=1;a<3;a++){
            b._select[a]=new Object();
            b._select[a]._item_title="閫夐」"+a;
            b._select[a]._item_radio=false;
            b._select[a]._item_value=0;
            b._select[a]._item_jump=0;
            b._select[a]._item_tb=false;
            b._select[a]._item_tbr=false;
            b._select[a]._item_img="";
            b._select[a]._item_imgtext=false;
            b._select[a]._item_desc="";
            b._select[a]._item_label="";
        }
        if(d=="likert"){
            b._hasvalue=true;
        }
        return b;
    }
    else{
        if(d=="question"){
            b._height="1";
            b._maxword="";
            b._minword="";
            b._width="";
            b._hasList=false;
            b._listId="";
            b._underline=false;
            b._norepeat=false;
            b._default="";
            return b;
        }
        else{
            b._hasvalue=false;
            if(b._isCePing){b._hasvalue=true;}
            if(d.indexOf("matrix")>-1){b._hasvalue=e;}
            b._randomChoice=g._randomChoice||false;
            b._numperrow=g._numperrow||0;
            b._select=g._select;
            if(g._type=="check"||d=="likert"||d=="order"||b._isCePing){
                for(var c=1;c<b._select.length;c++){
                    b._select[c]._item_radio=false;
                }
            }
            if(d=="order"){
                for(var c=1;c<b._select.length;c++){
                    b._select[c]._item_tb=false;
                    b._select[c]._item_tbr=false;
                }
            }
            if(d=="check"&&b._hasjump&&b._anytimejumpto=="0"){b._hasjump=false;}
            if(d=="likert"||e||d=="cepingradio"){
                for(var c=1;c<b._select.length;c++){
                    b._select[c]._item_value=c;
                }
                b._hasvalue=true;
            }
            if(f){
                b._hasvalue=false;
                b._hasjump=false;
                if(!g._isCeShi){
                    for(var c=1;c<b._select.length;c++){if(c==1){
                        b._select[c]._item_radio=true;
                    }
                    else{
                        b._select[c]._item_radio=false;
                    }
                        b._select[c]._item_tb=false;
                    }
                }
            }
            return b;
        }
    }
}
function changeQ(d){
    cur.validate();
    if(cur._referDivQ){
        var c="閫夐」";
        if(cur.dataNode._type=="matrix"||cur.dataNode._type=="sum"){c="琛屾爣棰�";}
        show_status_tip("姝ら"+c+"鏉ユ簮浜庣"+cur._referDivQ.dataNode._topic+"棰樼殑閫変腑椤癸紝涓嶈兘杞崲棰樺瀷锛�",4000);
        return;
    }
    if(cur._referedArray){
        var a="";
        for(var b=0;b<cur._referedArray.length;b++){
            if(b>0){a+=",";}
            a+=cur._referedArray[b].dataNode._topic;
        }
        show_status_tip("绗�"+a+"棰樼殑閫夐」鎴栬鏍囬鏉ユ簮浜庢棰樼殑閫変腑椤癸紝涓嶈兘杞崲棰樺瀷锛�",4000);
        return;
    }
    if(cur.checkValid()){
        var e=copyNode(cur.dataNode);
        var f=change_dataNode(e,d);
        f._topic=cur.dataNode._topic;
        createQ(f,true);
    }
}
function createFreQ(f,h,c){
    var b=createFreQdataNode(f,h,c);
    var e=createQ(b);
    if(firstPage){firstPage.style.display="";}
    var d=!b._tag&&(b._type=="radio"||b._type=="radio_down");
    var a=b._type=="check";
    var g=/^[a-zA-Z_]+$/.test(f);
    if((d||a)&&g){e.newAddQ=true;}
}
function createFromText(){
    if(isMergeAnswer){
        alert("寰堟姳姝夛紝鎮ㄦ鍦ㄤ互鍚堝苟绛斿嵎妯″紡缂栬緫闂嵎锛屼笉鑳戒娇鐢ㄦ鍔熻兘锛�");
    }
    else{
        if(confirm("鎮ㄧ‘瀹氳鏀惧純瀵规闂嵎鐨勬洿鏀瑰苟閲嶆柊鐢熸垚姝ら棶鍗峰悧锛�")){
            windowGotoUrl("/MySojump/DesignQbytxt.aspx?activity="+activityID);
        }
    }
}
function createFreQdataNode(G,B,v){
    var E;
    var f;
    var a="璇峰湪姝よ緭鍏ラ棶棰樻爣棰�";
    var q="question搂1搂";
    var i="搂0搂1搂搂false搂false搂搂搂false搂搂"+G;
    var r="";
    if(G=="check"&&v){r="-1";}
    var D="璇烽€夋嫨鎮ㄨ涓烘纭殑绛旀锛�";
    var o="2009鏈€鍙楀叧娉ㄧ殑涓枃缃戠珯/搴旂敤/鏈嶅姟";
    var J="娣樺疂缃戙€抐alse銆�0銆�0銆抐alse銆抐alse銆掋€抐alse銆掋€捖у紑蹇冪綉銆抐alse銆�1銆�0銆抐alse銆抐alse銆掋€抐alse銆掋€捖х櫨搴︺€抐alse銆�1銆�0銆抐alse銆抐alse銆掋€抐alse銆掋€捖ц吘璁€抐alse銆�1銆�0銆抐alse銆抐alse銆掋€抐alse銆掋€捖т汉浜虹綉銆抐alse銆�1銆�0銆抐alse銆抐alse銆掋€抐alse銆掋€�";
    var n="閫夐」"+(select_item_num+1)+"銆抐alse銆�1銆�0銆抐alse銆抐alse銆掋€抐alse銆掋€捖ч€夐」"+(select_item_num+2)+"銆抐alse銆�2銆�0銆抐alse銆抐alse銆掋€抐alse銆掋€�";
    var j="閫夐」1銆抰rue銆�0銆�0銆抐alse銆抐alse銆掋€抐alse銆掋€捖ч€夐」2銆抐alse銆�1銆�0銆抐alse銆抐alse銆掋€抐alse銆掋€�";
    var k="寰堜笉婊℃剰銆抐alse銆�1銆�0搂涓嶆弧鎰忋€抐alse銆�2銆�0搂涓€鑸€抐alse銆�3銆�0搂婊℃剰銆抐alse銆�4銆�0搂寰堟弧鎰忋€抐alse銆�5銆�0";
    var I="";
    var s=false;
    var u="搂搂搂搂200搂false搂";
    var m="";
    switch(G){
        case"鐢佃瘽":I="鎮ㄥ父鐢ㄧ殑鐢佃瘽鍙风爜锛�";
            s=true;
            m=u;
            break;
        case"Email":I="鎮ㄥ父鐢ㄧ殑Email鍦板潃锛�";
            s=true;
            m=u;
            break;
        case"鍩庡競鍗曢€�":
        case"鍩庡競澶氶€�":I="璇烽€夋嫨鍩庡競:";
            s=true;
            break;
        case"鐪佸競鍖�":I="璇烽€夋嫨鐪佷唤鍩庡競涓庡湴鍖�:";
            s=true;
            break;
        case"澶氱骇涓嬫媺":I="璇烽€夋嫨锛�";
            s=true;
            break;
        case"鐢熸棩":I="璇疯緭鍏ユ偍鐨勫嚭鐢熸棩鏈燂細";
            s=true;
            break;
        case"鎵嬫満":I="璇疯緭鍏ユ偍鐨勬墜鏈哄彿鐮侊細";
            s=true;
            m=u;
            break;
        case"鎵嬫満楠岃瘉":I="璇疯緭鍏ユ偍鐨勬墜鏈哄彿鐮侊細";
            s=true;
            m="搂false銆抰rue搂搂搂150搂false搂";
            i="搂0搂1搂搂true搂false搂搂搂false搂搂鎵嬫満";
            break;
        case"楂樻牎":I="鎮ㄦ墍鍦ㄦ垨鑰呮瘯涓氱殑楂樻牎鍚嶇О锛�";
            s=true;
            break;
        case"濮撳悕":I="鎮ㄧ殑濮撳悕锛�";
            s=true;
            i="搂0搂1搂搂true搂false搂搂搂false搂搂"+G;
            break;
        case"鎬у埆":E="radio搂3搂鎮ㄧ殑鎬у埆锛毬�0搂8搂false搂false搂搂true搂0000搂搂鎬у埆搂搂搂鐢枫€抐alse銆�0銆�0搂濂炽€抐alse銆�0銆�0";
            break;
        case"骞撮緞娈�":E="radio搂3搂鎮ㄧ殑骞撮緞娈碉細搂0搂8搂false搂false搂搂true搂0000搂搂骞撮緞娈德�18宀佷互涓嬨€抐alse銆�0銆�0搂18~25銆抐alse銆�0銆�0搂26~30銆抐alse銆�0銆�0搂31~40銆抐alse銆�0銆�0搂41~50銆抐alse銆�0銆�0搂51~60銆抐alse銆�0銆�0搂60浠ヤ笂銆抐alse銆�0銆�0";
            break;
        case"琛屼笟":E="radio_down搂10搂鎮ㄧ洰鍓嶄粠浜嬬殑琛屼笟锛毬�0搂1搂false搂false搂搂true搂0000搂搂琛屼笟搂搂搂";
            var e="IT/杞‖浠舵湇鍔�/鐢靛瓙鍟嗗姟/鍥犵壒缃戣繍钀�,蹇€熸秷璐瑰搧(椋熷搧/楗枡/鍖栧鍝�),鎵瑰彂/闆跺敭,鏈嶈/绾虹粐/鐨潻,瀹跺叿/宸ヨ壓鍝�/鐜╁叿,鏁欒偛/鍩硅/绉戠爺/闄㈡牎,瀹剁數,閫氫俊/鐢典俊杩愯惀/缃戠粶璁惧/澧炲€兼湇鍔�,鍒堕€犱笟,姹借溅鍙婇浂閰嶄欢,椁愰ギ/濞变箰/鏃呮父/閰掑簵/鐢熸椿鏈嶅姟,鍔炲叕鐢ㄥ搧鍙婅澶�,浼氳/瀹¤,娉曞緥,閾惰/淇濋櫓/璇佸埜/鎶曡祫閾惰/椋庨櫓鍩洪噾,鐢靛瓙鎶€鏈�/鍗婂浣�/闆嗘垚鐢佃矾,浠櫒浠〃/宸ヤ笟鑷姩鍖�,璐告槗/杩涘嚭鍙�,鏈烘/璁惧/閲嶅伐,鍒惰嵂/鐢熺墿宸ョ▼/鍖荤枟璁惧/鍣ㄦ,鍖荤枟/鎶ょ悊/淇濆仴/鍗敓,骞垮憡/鍏叧/濯掍綋/鑹烘湳,鍑虹増/鍗板埛/鍖呰,鎴垮湴浜у紑鍙�/寤虹瓚宸ョ▼/瑁呮舰/璁捐,鐗╀笟绠＄悊/鍟嗕笟涓績,涓粙/鍜ㄨ/鐚庡ご/璁よ瘉,浜ら€�/杩愯緭/鐗╂祦,鑸ぉ/鑸┖/鑳芥簮/鍖栧伐,鍐滀笟/娓斾笟/鏋椾笟,鍏朵粬琛屼笟";
            var d=e.split(",");
            var A="";
            for(var l=0;l<d.length;l++){
                if(l>0){A+="搂";}
                A+=d[l]+"銆抐alse銆�0銆�0";
            }
            E+=A;
            break;
        case"鑱屼笟":E="radio_down搂11搂鎮ㄧ洰鍓嶄粠浜嬬殑鑱屼笟锛毬�0搂1搂false搂false搂搂true搂0000搂搂鑱屼笟搂搂搂鍏ㄦ棩鍒跺鐢熴€抐alse銆�0銆�0搂鐢熶骇浜哄憳銆抐alse銆�0銆�0搂閿€鍞汉鍛樸€抐alse銆�0銆�0搂甯傚満/鍏叧浜哄憳銆抐alse銆�0銆�0搂瀹㈡湇浜哄憳銆抐alse銆�0銆�0搂琛屾斂/鍚庡嫟浜哄憳銆抐alse銆�0銆�0搂浜哄姏璧勬簮銆抐alse銆�0銆�0搂璐㈠姟/瀹¤浜哄憳銆抐alse銆�0銆�0搂鏂囪亴/鍔炰簨浜哄憳銆抐alse銆�0銆�0搂鎶€鏈�/鐮斿彂浜哄憳銆抐alse銆�0銆�0搂绠＄悊浜哄憳銆抐alse銆�0銆�0搂鏁欏笀銆抐alse銆�0銆�0搂椤鹃棶/鍜ㄨ銆抐alse銆�0銆�0搂涓撲笟浜哄＋(濡備細璁″笀銆佸緥甯堛€佸缓绛戝笀銆佸尰鎶や汉鍛樸€佽鑰呯瓑)銆抐alse銆�0銆�0搂鍏朵粬銆抐alse銆�0銆�0";
            break;
        case"鐪佷唤":E="radio搂19搂鎮ㄦ墍鍦ㄧ殑鐪佷唤锛毬�0搂8搂false搂false搂搂true搂0000搂搂鐪佷唤搂搂搂瀹夊窘銆抐alse銆�0銆�0搂鍖椾含銆抐alse銆�1銆�0搂閲嶅簡銆抐alse銆�1銆�0搂绂忓缓銆抐alse銆�1銆�0搂鐢樿們銆抐alse銆�1銆�0搂骞夸笢銆抐alse銆�1銆�0搂骞胯タ銆抐alse銆�1銆�0搂璐靛窞銆抐alse銆�1銆�0搂娴峰崡銆抐alse銆�1銆�0搂娌冲寳銆抐alse銆�1銆�0搂榛戦緳姹熴€抐alse銆�1銆�0搂娌冲崡銆抐alse銆�1銆�0搂棣欐腐銆抐alse銆�1銆�0搂婀栧寳銆抐alse銆�1銆�0搂婀栧崡銆抐alse銆�1銆�0搂姹熻嫃銆抐alse銆�1銆�0搂姹熻タ銆抐alse銆�1銆�0搂鍚夋灄銆抐alse銆�1銆�0搂杈藉畞銆抐alse銆�1銆�0搂婢抽棬銆抐alse銆�1銆�0搂鍐呰挋鍙ゃ€抐alse銆�1銆�0搂瀹佸銆抐alse銆�1銆�0搂闈掓捣銆抐alse銆�1銆�0搂灞变笢銆抐alse銆�1銆�0搂涓婃捣銆抐alse銆�1銆�0搂灞辫タ銆抐alse銆�1銆�0搂闄曡タ銆抐alse銆�1銆�0搂鍥涘窛銆抐alse銆�1銆�0搂鍙版咕銆抐alse銆�1銆�0搂澶╂触銆抐alse銆�1銆�0搂鏂扮枂銆抐alse銆�1銆�0搂瑗胯棌銆抐alse銆�1銆�0搂浜戝崡銆抐alse銆�1銆�0搂娴欐睙銆抐alse銆�1銆�0搂娴峰銆抐alse銆�1銆�0";
            break;
        case"閭瘎鍦板潃":E="matrix搂1搂璇疯緭鍏ユ偍鐨勮仈绯诲湴鍧€锛毬�201搂濮撳悕锛歕n鎵€鍦ㄥ湴鍖猴細\n琛楅亾鍦板潃:\n閭斂缂栫爜:\n鎵嬫満鎴栧浐璇濓細銆掋€捖alse搂false搂搂true搂15%銆掋€�0,,,;1,鐪佸競鍖�,,,50;2,,,,50;3,鏁板瓧,,;4,鐢佃瘽,,銆�10搂搂搂搂搂"+k;
            break;
        case"鍩烘湰淇℃伅":E="matrix搂1搂鍩烘湰淇℃伅锛毬�201搂濮撳悕锛歕n閮ㄩ棬锛歕n鍛樺伐缂栧彿:銆掋€捖alse搂false搂搂true搂15%銆掋€�0,,,;1,,,;2,,,銆�10搂搂搂搂搂"+k;
            break;
        case"radio":
        case"radio_down":
        case"check":
        case"qingjing":
        case"shop":
            var b=G=="check"?"true,"+r+","+r:"true";
            if(G=="qingjing"){
                b="true,1";
                G="radio";
                n="鎯呮櫙1銆抐alse銆�50銆�0搂鎯呮櫙2銆抐alse銆�50銆�0搂鎯呮櫙3銆抐alse銆�50銆�0搂鎯呮櫙4銆抐alse銆�50銆�0";
            }
            else{
                if(G=="shop"){
                    G="check";
                    a="璇烽€夋嫨鍟嗗搧锛�";
                    b="false,shop";
                    n="鍟嗗搧1銆抐alse銆�0銆捖у晢鍝�2銆抐alse銆�0銆捖у晢鍝�3銆抐alse銆�0銆�";
                }
            }
            if(B){n+="搂鍏跺畠銆抐alse銆�1銆�0銆抰rue銆抐alse銆掋€抐alse銆掋€�";}
            var H=v||0;
            E=G+"搂1搂"+a+"搂"+v+"搂1搂false搂false搂搂"+b+"搂搂搂搂搂搂"+n;
            break;
        case"toupiao":G=B==1?"radio":"check";
            E=G+"搂1搂"+o+"搂"+v+"搂1搂false搂false搂搂true搂true銆�50銆抐alse銆抰rue銆抰rue搂搂搂搂搂"+J;
            break;
        case"ceshi":
            if(B==3){
                E="question搂1搂"+a+"搂0搂1搂搂true搂false搂搂搂false搂搂搂false搂搂搂搂搂搂5銆掕璁剧疆绛旀";
            }
            else{
                if(B==4){
                    E="gapfill搂1搂鎮ㄧ殑闂锛�"+getFillStr(3)+"搂0搂true搂1搂搂false搂0搂搂搂1";
                }
                else{
                    if(B==5){
                        G="radio";
                        E=G+"搂1搂"+D+"搂"+v+"搂1搂true搂false搂搂true搂ceshi銆�5銆捖у銆抰rue銆�0銆�0銆抐alse銆抐alse銆掋€抐alse銆掋€捖ч敊銆抐alse銆�1銆�0銆抐alse銆抐alse銆掋€抐alse銆掋€�";
                    }
                    else{
                        G=B==1?"radio":"check";
                        E=G+"搂1搂"+D+"搂"+v+"搂1搂true搂false搂搂true搂ceshi銆�5銆捖�"+j;
                    }
                }
            }
            hasCeShiQ=true;
            showCeShiInfo();
            break;
        case"ceping":G=B==1?"radio":"check";
            E=G+"搂1搂"+a+"搂0搂1搂true搂false搂搂true搂ceping搂搂搂搂搂"+n;
            break;
        case"boolean":E=G+"搂1搂"+a+"搂0搂8搂true搂false搂搂true搂0000搂搂搂搂搂鏄€抐alse銆�1銆�0搂鍚︺€抐alse銆�0銆�0";
            break;
        case"likert":E="radio搂1搂"+a+"搂1搂1搂true搂false搂搂true搂0000搂搂搂搂搂"+k;
            break;
        case"matrix":
            var F=B||2;
            var c="";
            var z="";
            var C=10;
            if(F=="202"){C=100;}
            var h=F<102||F==303;
            var g=h?"true":"false";
            if(B-300>0){c="鐧惧害\n璋锋瓕\n鑵捐鎼滄悳\n缃戞槗鏈夐亾\n鎼滅嫄鎼滅嫍";}
            if(F==101){
                E="matrix搂1搂璇锋牴鎹偍鐨勫疄闄呮儏鍐甸€夋嫨鏈€绗﹀悎鐨勯」锛�1-->5琛ㄧず闈炲父涓嶆弧鎰�-->闈炲父婊℃剰搂"+F+"搂澶栬\n鍔熻兘銆掋€�"+c+"搂"+g+"搂false搂搂true搂"+z+"銆掋€�0銆�"+C+"搂搂搂搂搂1銆抐alse銆�1銆�0搂2銆抐alse銆�2銆�0搂3銆抐alse銆�3銆�0搂4銆抐alse銆�4銆�0搂5銆抐alse銆�5銆�0";
            }
            else{
                if(F==102){
                    var p="閫熷害蹇€抐alse銆�1銆�0搂鍑嗙‘鐜囬珮銆抐alse銆�2銆�0搂淇℃伅閲忓銆抐alse銆�3銆�0搂鐣岄潰鏇寸編瑙傘€抐alse銆�4銆�0";E="matrix搂1搂璇疯瘎璁笅闈㈢殑鎼滅储寮曟搸锛毬�"+F+"搂鐧惧害\nGoogle\n鎼滅嫍銆掋€�"+c+"搂"+g+"搂false搂搂true搂"+z+"銆掋€�0銆�"+C+"搂搂搂搂搂"+p;
                }
                else{
                    E="matrix搂1搂"+a+"搂"+F+"搂澶栬\n鎬ц兘銆掋€�"+c+"搂"+g+"搂false搂搂true搂"+z+"銆掋€�0銆�"+C+"搂搂搂搂搂"+k;
                }
            }
            break;
        case"question":
            var t=B||1;
            var x=v||false;
            E="question搂1搂"+a+"搂0搂"+t+"搂搂false搂false搂搂搂false搂搂搂"+x+"搂搂搂搂搂";
            break;
        case"gapfill":E="gapfill搂1搂濮撳悕锛�"+getFillStr(3)+"&nbsp;&nbsp;&nbsp;&nbsp;骞撮緞锛�"+GapFillStr+"宀�<br/>鐢佃瘽锛�"+getFillStr(4)+"搂0搂true搂1搂搂false搂0搂";
            break;
        case"slider":E="slider搂1搂"+a+"搂0搂true搂0搂100搂涓嶆弧鎰徛ф弧鎰徛alse搂0搂";
            break;
        case"sum":E="sum搂1搂"+a+"搂0搂true搂100搂澶栬\n鎬ц兘搂15%搂0搂搂false搂0搂";
            break;
        case"fileupload":E="fileupload搂1搂"+a+"搂0搂true搂200搂"+defaultFileExt+"搂4096搂搂false搂0搂";
            break;
        case"page":
            var w=B||"";
            E=G+"搂1搂搂搂"+w;
            break;
        case"cut":
            var I=B?B:"";
            E=G+"搂"+I+"搂";
            break;
    }
    if(s){E=q+I+i+m;}
    f=set_string_to_dataNode(E);
    return f;
}
var curNewQ=null;
function addNewQ(d,f,a,g){
    var e;
    var c=d._type;
    e=create_question(d);
    curNewQ=e;
    setQHandler(e);
    setAttrHander(e);
    if(curinsert!=null){g=curinsert;}
    if(a){g=curover;}
    if(!f){
        if((!isMergeAnswer||c=="page"||c=="cut")&&g){
            if(questions.lastChild==g){
                questions.appendChild(e);
            }
            else{
                questions.insertBefore(e,g.nextSibling);
            }
            if(g==firstPage){
                questionHolder.unshift(e);
            }
            else{
                questionHolder.insertBefore(e,g);
                questionHolder.moveUp(g);
            }
            updateTopic();
        }
        else{
            questions.appendChild(e);
            questionHolder.push(e);
            updateTopic();
        }
    }
    else{
        cur.parentNode.insertBefore(e,cur);
        e.isMergeNewAdded=cur.isMergeNewAdded;
        questionHolder[questionHolder.indexOf(cur)]=e;
        cur.deleteQ("noNeedConfirm");
        cur=null;
    }
    if(curinsert!=null){
        resetInsertQ();
    }
    if(a&&curover){
        if(curover._referDivQ){
            var b=curover._referDivQ;
            e._referDivQ=b;
            if(!b._referedArray){
                b._referedArray=new Array();
            }
            if(b._referedArray.indexOf(e)==-1){
                b._referedArray.push(e);
            }
            b._referedArray.sort(function(i,h){
                return i.dataNode._topic-h.dataNode._topic;
            }
            );
        }
    }
    curNewQ=null;
    return e;
}
function createQ(c,e,a){
    if(cur){
        cur.divTableOperation.style.visibility="hidden";
    }
    var d=addNewQ(c,e,a);
    if(!isMergeAnswer&&window.makeDrag){
        makeDrag(d);
    }
    d.createOp();
    var b=new Date().getTime();
    if(!useShortCutAddNewQ){
        if(lastAddNewQTime&&!e){
            var f=b-lastAddNewQTime;
            if(f>8000){d.ondblclick();}
            else{
                if(cur&&cur.isEditing){
                    qonclick.call(cur);
                }
                setMoveStyle(d);
            }
        }
        else{d.ondblclick();}
    }
    else{setMoveStyle(d);}
    d.focus();
    lastAddNewQTime=b;
    return d;
}
function copyQ(){
    if(this.validate){this.validate();}
    if(!this.checkValid||this.checkValid()){
        var a=copyNode(this.dataNode);
        a._hasjump=false;
        a._needOnly=false;
        a._hasList=false;
        a._listId=-1;
        a._referedTopics="";
        createQ(a,false,true);
        show_status_tip("澶嶅埗鎴愬姛锛�",4000);
    }
}
function copyNode(f){
    var a=new Object();
    for(var c in f){a[c]=f[c];}
    if(f._select){
        a._select=new Array();
        for(var b=1;b<f._select.length;b++){
            a._select[b]=new Object();
            for(var d in f._select[b]){
                a._select[b][d]=f._select[b][d];
            }
        }
    }
    if(f._rowVerify){
        a._rowVerify=new Array();
        for(var b=0;b<f._rowVerify.length;b++){
            a._rowVerify[b]=new Object();
            for(var d in f._rowVerify[b]){
                a._rowVerify[b][d]=f._rowVerify[b][d];
            }
        }
    }
    return a;
}
function deleteQ(b){
    var f=this.dataNode._type;
    var h=f=="page"||f=="cut";
    if(this._referedArray){
        var d="";
        for(var e=0;e<this._referedArray.length;e++){
            if(e>0){
                d+=",";
            }
            d+=this._referedArray[e].dataNode._topic;
        }
        show_status_tip("鎻愮ず锛氱"+d+"棰樼殑閫夐」鎴栬鏍囬鏉ユ簮浜庢棰樼殑閫変腑椤癸紝涓嶈兘鍒犻櫎姝ら锛�",4000);
        return;
    }
    if(!h){
        for(var e=0;e<questionHolder.length;e++){
            var c=questionHolder[e].dataNode;
            if(!c._relation){continue;}
            var k=c._relation.split(",");
            var l=parseInt(k[0]);
            if(this.dataNode._topic==l){
                var j=c._topic;
                if(WjxActivity._use_self_topic){
                    var m=c._title.match(/^\s*\d+[\.\-\_\(\/]?\d+?\)?/);
                    if(m){j=m;
                    }
                }
                show_status_tip("鎻愮ず锛氱"+j+"棰樺叧鑱斾簬姝ら鐨勭"+k[1]+"涓€夐」锛屼笉鑳藉垹闄ゆ棰橈紒",4000);
                return;
            }
        }
    }
    if(b!="noNeedConfirm"){
        if(isMergeAnswer&&!this.isMergeNewAdded&&!h){
            show_status_tip("寰堟姳姝夛紝鍦ㄤ互鍚堝苟绛斿嵎妯″紡涓嬩慨鏀归棶鍗蜂负浜嗕繚鎸佹暟鎹竴鑷存€т笉鍏佽鍒犻櫎鍘熷闂嵎涓殑棰樼洰锛�",4000);
            return;
        }
        show_status_tip("鍙互閫氳繃Ctrl+Z鎭㈠鍒犻櫎鐨勯棶棰�",4000);
    }
    if(f=="page"){total_page--;}
    else{
        if(f!="cut"){
            total_question--;
        }
    }
    showhidebatq();
    if(this.tabAttr){
        this.tabAttr.parentNode.removeChild(this.tabAttr);
        this.tabAttr=null;
        this.hasCreatedAttr=false;
    }
    if(this.clearReferQ){this.clearReferQ();}
    if(this.clearReferedQ){this.clearReferedQ();}
    if(b!="noNeedConfirm"){var g=questionHolder.indexOf(this);}
    this.className="div_question div_question_mouseout";
    this.parentNode.removeChild(this);
    questionHolder.remove(this);
    updateTopic(this.dataNode._type);
    if(b!="noNeedConfirm"){
        var a=firstPage;
        if(g>0){a=questionHolder[g-1];}
        new DeleteAction(this,a).exec();
    }
    if(cur==this){cur=null;}
}
function qSelect(){}
function qonclick(){
    if(this.isCepingQ){
        show_status_tip("琚祴璇勫璞￠涓嶈兘杩涜缂栬緫");
        return;
    }
    try{
        window.getSelection?window.getSelection().removeAllRanges():document.selection.empty();
    }catch(a){}
    this.className="div_question div_question_onclick";
    this.title="";
    resetInsertQ();
    this.divInsertOp.style.visibility="hidden";
    if(cur!=this||(cur==this&&cur.isEditing)){
        if(cur!=null){
            if(cur.updateItem){
                cur.updateItem();
            }
            cur.className="div_question";
            if(cur.hasCreatedAttr){cur.tabAttr.style.display="none";}
            cur.isEditing=false;
            cur.ondblclick=qonclick;
            cur.style.cursor="move";
            changeEditText(cur.editQLink,false);
        }
        if(cur&&cur.createAttr&&(cur.checkValid&&!cur.checkValid())){cur.validate();}
        if(cur==this){
            cur.focus();
            cancelInputClick(this);
            return false;
        }
    }
    cancelInputClick(this);
    cur=this;
    var b=this.dataNode;
    this.isEditing=true;
    this.ondblclick=null;
    hasDisplayEditTip=true;
    this.style.cursor="default";
    changeEditText(this.editQLink,true);
    if(this.hasCreatedAttr){
        this.tabAttr.style.display="";
        cancelDblClick(this);
        if(this.hasDisplaySelCheck){this.updateSelCheck();}
        this.focus();
        setQTopPos(this);
    }
    else{
        if(this.createAttr){
            var c=this;
            setTimeout(function(){
                c.createAttr();
                cancelDblClick(c);
                c.setDataNodeToDesign();
                setQTopPos(c);
            },0);
        }
        else{
            show_status_tip("姝ｅ湪鍔犺浇闂灞炴€э紝璇疯€愬績绛夊緟....",4000);
        }
    }
    return false;
}
function editQ(a){
    if(curover){
        qonclick.call(curover);
    }
}
function changeEditText(c,a){
    if(!c){return;}
    if(a){
        var b=c.nextSibling;
        if(b.nodeType==3){b=b.nextSibling;}
        b.innerHTML="瀹屾垚";
        c.className="design-icon design-finish";
    }
    else{
        c.className="design-icon design-edit";
        var b=c.nextSibling;
        if(b.nodeType==3){
            b=b.nextSibling;
        }
        b.innerHTML="缂栬緫";
    }
}
function createOp(){
    if(this.divTableOperation.OpCreated){
        this.divTableOperation.style.visibility="visible";
    }
    else{
        this.deleteQ=deleteQ;
        this.copyQ=copyQ;
        this.moveUp=moveUp;
        this.moveDown=moveDown;
        this.moveFirst=moveFirst;
        this.moveLast=moveLast;
        var c=this.divTableOperation;
        var a=this.dataNode._type;
        if(a=="page"){
            if(this.dataNode._topic>1){
                c.innerHTML=toolbar_start+toolbar_add+toolbar_del_move+toolbar_end;
            }
            else{
                c.innerHTML=toolbar_start+toolbar_add+toolbar_end;
            }
        }
        else{
            if(a=="cut"){
                c.innerHTML=toolbar_start+toolbar_add+toolbar_del_move+toolbar_end;
            }
            else{
                if(isMergeAnswer&&!this.isMergeNewAdded){
                    c.innerHTML=toolbar_start+toolbar_add+toolbar_copy+toolbar_end;
                }
                else{
                    if(isMergeAnswer){
                        c.innerHTML=toolbar_start+toolbar_add+toolbar_copy+toolbar_del+toolbar_movedown+toolbar_movelast+toolbar_end;
                    }
                    else{
                        c.innerHTML=toolbar_start+toolbar_add+toolbar_copy+toolbar_del_move+toolbar_end;
                    }
                }
            }
        }
        if(this.isCepingQ){c.innerHTML="";}
        c.OpCreated=true;
        this.divTableOperation.style.visibility="visible";
        var b=$$("span",c)[0];
        this.editQLink=b;
    }
}
var hasDisplayEditTipTimes=0;
function qonmouseover(c){
    if(!this.isEditing&&!isMergeAnswer){
        this.divInsertOp.style.visibility="visible";
    }
    var b=this.className.toLowerCase();
    if(b.indexOf("div_question_onclick")<0&&this!=curinsert){
        if(b.indexOf("div_question_error")<0){
            this.className="div_question div_question_mouseover";
        }
        else{
            this.className="div_question div_question_mouseover div_question_error";
        }
    }
    this.createOp();
    if(isMergeAnswer){
        this.style.cursor="default";
    }
    curover=this;
    var a=this;
    if(hasDisplayEditTipTimes<3){
        hasDisplayEditTipTimes++;
        toolTipLayer.innerHTML="鎻愮ず锛氭偍鍙互閫氳繃鈥滃弻鍑烩€濋鐩潵杩涜缂栬緫";
        sb_setmenunav(toolTipLayer,true,this,true);
        this.hasDisplayEditTip=true;
    }
}
function qonmouseout(b){
    this.divInsertOp.style.visibility="hidden";
    var a=this.className.toLowerCase();
    if(a.indexOf("div_question_onclick")<0&&this!=curinsert){
        if(a.indexOf("div_question_error")<0){
            this.className="div_question div_question_mouseout";
        }
        else{
            this.className="div_question div_question_mouseout div_question_error";
        }
    }
    if(this.hasDisplayEditTip){
        sb_setmenunav(toolTipLayer,false,this);
        this.hasDisplayEditTip=false;
    }
    if(this.divTableOperation){
        this.divTableOperation.style.visibility="hidden";
    }
}
function getObjPos(d){
    var a=y=0;
    if(d.getBoundingClientRect){
        var b=d.getBoundingClientRect();
        var c=document.documentElement;
        a=b.left+Math.max(c.scrollLeft,document.body.scrollLeft)-c.clientLeft;
        y=b.top+Math.max(c.scrollTop,document.body.scrollTop)-c.clientTop;
    }
    else{
        while(d&&d!=document.body){
            a+=d.offsetLeft;
            y+=d.offsetTop;
            d=d.offsetParent;
        }
    }
    return{x:a,y:y};
}
function getCurPos(b){
    b=b||window.event;
    var a=document.documentElement||document.body;
    if(b.pageX){return{x:b.pageX,y:b.pageY};}
    return{x:b.clientX+a.scrollLeft-a.clientLeft,y:b.clientY+a.scrollTop-a.clientTop};
}
function mouseOverout(a){
    a.onmouseover=qonmouseover;
    a.onmouseout=qonmouseout;
}
function setQHandler(a){
    mouseOverout(a);
    a.createOp=createOp;
    a.ondblclick=qonclick;
    a.deleteQ=deleteQ;
}
initEventHandler();
function initEventHandler(){
    var a=$("divId");
    a.onmouseover=function(){
        this.style.border="2px solid #FDB553";
    };
    a.onmouseout=function(){
        this.style.border="2px solid #ffffff";
    };
    firstPage.ondblclick=qonclick;
    mouseOverout(firstPage);
    firstPage.createOp=createOp;
    for(var c=0;c<questionHolder.length;c++){
        var b=questionHolder[c];setQHandler(b);
    }
}
function cancelDblClick(d){
    var a=d.tabAttr;
    if(a){
        var b=$$("input",a);
        for(var c=0;c<b.length;c++){
            b[c].ondblclick=function(f){
                f=window.event||f;
                if(f){
                    f.cancelBubble=true;
                    if(f.stopPropagation){f.stopPropagation();}
                }
            };
        }
    }
}
var actionStack=new Array();
var actionIndex=0;
function BaseAction(){}
BaseAction.prototype.exec=function(){actionStack[actionIndex++]=this;};
BaseAction.prototype.undo=function(){return false;};
BaseAction.prototype.redo=function(){return false;};
function DeleteAction(b,a){
    this.deleteDiv=b;
    this.prevDiv=a;
    this.status="done";
}
DeleteAction.prototype=new BaseAction();
DeleteAction.prototype.undo=function(){
    if(this.status!="done"){return;}
    this.prevDiv.parentNode.insertBefore(this.deleteDiv,this.prevDiv);
    this.prevDiv.parentNode.insertBefore(this.prevDiv,this.deleteDiv);
    if(this.prevDiv==firstPage){
        questionHolder.unshift(this.deleteDiv);
    }
    else{
        questionHolder.insertBefore(this.deleteDiv,this.prevDiv);
        questionHolder.moveUp(this.prevDiv);
    }
    updateTopic();
    this.deleteDiv.focus();
    this.status="undone";
};
DeleteAction.prototype.redo=function(){
    if(this.status!="undone"){return;}
    this.deleteDiv.deleteQ();
    this.status="done";
};
function undo(){
    if(actionIndex>0){
        actionStack[--actionIndex].undo();
    }
}
function redo(){
    if(actionIndex<actionStack.length){
        actionStack[actionIndex++].redo();
    }
}