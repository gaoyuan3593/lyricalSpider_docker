(function () {
    $("a").on("mousedown click contextmenu", function () {
        var b = Math.floor(100 * Math.random()) + 1,
            a = this.href.indexOf("url="),
            c = this.href.indexOf("&k=");
        -1 !== a && -1 === c && (a = this.href.substr(a + 4 + parseInt("26") + b, 1), this.href += "&k=" + b + "&h=" + a)
    })
})();


var server_url = ("undefined" != typeof httpsUtil && httpsUtil.isHttps ? "https" : "http") + "://www.sogou.com/",
    pingBackUrl = "undefined" != typeof httpsUtil ? httpsUtil.getPingbackHost() : "http://pb.sogou.com";

function suggWxClick(e, t, i) {
    if ("undefined" != typeof WX_SUGG_PAGE_FROM && "undefined" != typeof SugPara) {
        var n = 1e3 * (new Date).getTime() + Math.round(1e3 * Math.random());
        $(function () {
            var o = 1 == $(i).attr("history") ? 1 : -1;
            setSuggType(o);
            var s = {
                uigs_productid: "wxsugg",
                frompage: WX_SUGG_PAGE_FROM,
                sugType: SugPara.sugType,
                uigs_t: n,
                w: e,
                k: t,
                act: "clk",
                suggestionid: o,
                pos: $(i).attr("lid"),
                num: $(i).parent().find("li").size()
            };
            $.ajax({url: pingBackUrl + "/cl.gif", data: s})
        })
    }
}

function setIsShowSuggAtLast(e) {
    try {
        $('[name="_sug_"]').val((e || 0) > 0 ? "y" : "n")
    } catch (e) {
    }
}

function setSuggType(e) {
    try {
        $('[name="_sug_type_"]').val(e)
    } catch (e) {
    }
}

function sugTemplate() {
}

if (window.navigator.appName.toUpperCase().indexOf("MICROSOFT") >= 0 && document.execCommand) try {
    document.execCommand("BackgroundImageCache", !1, !0)
} catch (e) {
}
var isIe6 = window.navigator.userAgent && window.navigator.userAgent.indexOf("MSIE 6.0") >= 0;

function uigs_sugg_pv(e, t, i, n) {
    try {
        if (!e) return;
        var o = [pingBackUrl + "/pv.gif?uigs_productid=wapapp&uigs_t="];
        if (o.push((new Date).getTime()), "undefined" != typeof uigs_para) {
            var s = uigs_para;
            for (var r in s) s.hasOwnProperty(r) && "uigs_productid" != r && "type" != r && "stype" != r && o.push("&" + r + "=" + encodeURIComponent(s[r]))
        }
        o.push("&type="), o.push(e), o.push("&stype=", t), o.push("&pos="), o.push(0 == i ? i : i || ""), o.push("&"), o.push(n || ""), o.push("&_t="), o.push((new Date).getTime()), (new Image).src = o.join("")
    } catch (e) {
    }
}

function uigs_sugg_cl(e, t, i, n) {
    try {
        if (!e) return;
        var o = [pingBackUrl + "/cl.gif?uigs_productid=wapapp&uigs_t="];
        if (o.push((new Date).getTime()), "undefined" != typeof uigs_para) {
            var s = uigs_para;
            for (var r in s) s.hasOwnProperty(r) && "uigs_productid" != r && "type" != r && "stype" != r && o.push("&" + r + "=" + encodeURIComponent(s[r]))
        }
        o.push("&type="), o.push(e), o.push("&uigs_cl="), o.push(t, "_"), o.push(0 == i ? i : i || ""), o.push("&"), o.push(n || ""), o.push("&_t="), o.push((new Date).getTime()), (new Image).src = o.join("")
    } catch (e) {
    }
}

function sogouSugg(newPara) {
    function getSuggCookie(e) {
        var t = document.cookie, i = e + "=", n = t.indexOf("; " + i);
        if (-1 == n) {
            if (0 != (n = t.indexOf(i))) return null
        } else n += 2;
        var o = document.cookie.indexOf(";", n);
        return -1 == o && (o = t.length), unescape(t.substring(n + i.length, o))
    }

    function getAbtestId() {
        return getSuggCookie("ABTEST") && getSuggCookie("ABTEST").split("|").length > 0 ? getSuggCookie("ABTEST").split("|")[0] : ""
    }

    "object" != typeof SugPara && (SugPara = {});
    var isIe = -1 != navigator.userAgent.indexOf("MSIE") && !window.opera,
        isIe8 = -1 != navigator.userAgent.indexOf("MSIE 8") && !window.opera, that = this, tophint,
        MAX_RETRY_FETCH_SITE = 3, handleRetry = MAX_RETRY_FETCH_SITE - 1, template = new sugTemplate,
        myPara = newPara || SugPara, on = newPara ? 0 : 1, d = document, inputid = myPara.inputid || "query",
        sugType = myPara.sugType || "web", bigsize = myPara.bigsize || !1, productId = myPara.productId || sugType,
        postFix = myPara.postFix || "", preFix = myPara.preFix || "", revsd = myPara.revsd || 0,
        suggestRid = myPara.suggestRid || "", normalRid = myPara.normalRid || "", enableSug = !0,
        useParent = myPara.useParent || 0, abtestid = myPara.abtestid || getAbtestId(), ipn = myPara.ipn || "",
        frpage = myPara.frpage || "", domain = myPara.domain || "https://weixin.sogou.com",
        uri = myPara.uri || "/sugg/su.jsp", suggUri = "/sugg/ajaj_json.jsp", firstRun = 1, suggDiv, suggIfm = null,
        suggLis = [], suggOText = [], input_elem, input_form, mousedown_ontr = 0, noneed_query = "",
        lastinput_query = "", sending_timer = 0, highlight_li = -1, jsonData = [], jsonDataTongji = [],
        jsonDataTongji0 = [], jsonDataTongji1 = [], jsonDataTongji2 = [], goTongjiId = [], hasPersonal = 0,
        hasPersonal1 = 0, userInputString = "", cache = {}, sitecache = {}, ajaj = null, ajaj2 = null,
        ajajPinyin = null, originalQuery = "", suggestWordId = -1, input_time = 0, oldfunc = function () {
        }, oldfunc2 = function () {
        }, contentDiv, siteTimer, setTimer1, setTimer2, setTimer3, hideTimer, $c = sugTemplate.prototype.$c,
        handleFlag = handleRetry, vrFlag = {}, sugData = {}, cur_li = -1, isKeyTime = !1, mouseTime_li = -1,
        suggDivReqCount = 0, suggDivShowCount = 0, suggHisShowCount = 0, sugHisClk = 0, sugVrWordCount = 0,
        timeOutTimer, loadingTimer, badSuggMap = {}, hoverClassReg = new RegExp("\\bover\\b"), version = "1.0",
        sogouSearchSugPinyinN = "sogouSearchSugPinyin@" + version, showHistoryFlag = !1, searchType = "direct",
        clkSrc = "default", hisDisCount = 0, hisItemClk = 0, disCount = 0, hisClkAdd = 0, position = 0, disCount = 0,
        tpos = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], noresult = 0, hisPos = [0, 0], hisPosClk = [0, 0];

    function localStorageMap() {
        if (window.localStorage) for (var e = window.localStorage, t = 0; t < e.length; t++) {
            var i = e.key(t);
            if (i.indexOf("sogouSearchSugPinyin") >= 0) {
                var n = i.split("@");
                n[1] && n[1] == version || localStorage.removeItem(i)
            }
        }
    }

    function $(e) {
        return d.getElementById(e)
    }

    function bind(e, t, i) {
        if (e) return e.addEventListener ? e.addEventListener(t, i, !1) : e.attachEvent("on" + t, i)
    }

    function getElesByClass(e, t) {
        for (var i = t.getElementsByTagName("*"), n = new RegExp("\\b" + e + "\\b"), o = [], s = 0; s < i.length; s++) n.test(i[s].className) && o.push(i[s]);
        return o
    }

    function removeClass(e, t) {
        if (e) {
            var i = e.className, n = new RegExp("\\b" + t + "\\b");
            i = i.replace(n, ""), e.className = i
        }
    }

    function addClass(e, t) {
        if (e) {
            var i = e.className;
            if (new RegExp("\\b" + t + "\\b").test(e.className)) return;
            i = i + " " + t, e.className = i
        }
    }

    function pingback(e) {
        var t = new Date, i = 1e3 * t.getTime() + Math.round(1e3 * Math.random()), n = "";
        "" != sugType && (n = "sugg" + sugType);
        var o = [pingBackUrl + "/pv.gif", "?uigs_productid=", encodeURIComponent(n), "&uigs_t=", i, "&w=", encodeURIComponent(input_elem.value), "&k=", encodeURIComponent(userInputString), "&s="];
        o.push(-1 != suggestWordId ? "t" : "f"), -1 != suggestWordId && (o.push("&stj0=" + jsonDataTongji0[suggestWordId]), o.push("&stj1=" + jsonDataTongji1[suggestWordId])), o.push("&hp=" + hasPersonal), o.push("&hp1=" + hasPersonal1), -1 != suggestWordId && (o.push("&cline="), o.push(suggestWordId)), "sb" == e && (o.push("&c_s_req=" + suggDivReqCount), o.push("&c_s_show=" + suggDivShowCount), o.push("&c_s_h_show=" + suggHisShowCount), suggHisShowCount > 0 && o.push("&s_his_clk=" + sugHisClk), o.push("&c_s_vr_word=" + sugVrWordCount)), e && (o.push("&act="), o.push(encodeURIComponent(e))), o.push("&r=" + t.getSeconds()), o.push("&abtestid=" + encodeURIComponent(abtestid)), o.push("&uk=" + (useKey ? 1 : 0)), o.push("&sbby=" + submitby), (new Image).src = o.join("")
    }

    function init() {
        if ($(inputid)) {
            for (input_elem = $(inputid), input_form = input_elem.parentNode; input_form && "form" !== input_form.tagName.toLowerCase();) input_form = input_form.parentNode;
            input_form && (myPara.reset && input_form.reset(), input_elem.setAttribute("autocomplete", "off"), bind(input_elem, "mousedown", mousedown), bind(input_elem, "keyup", keydown), noneed_query = input_elem.value, checkQuery())
        } else setTimeout(init, 50)
    }

    function mousedown() {
        showHistoryFlag = !1, firstRun && start(), myPara.oms && (noneed_query = "", lastinput_query = ""), showtop = !1
    }

    function positionDiv() {
        var e = getPositionAndSize(useParent ? input_elem.parentNode : input_elem),
            t = !(location.href.indexOf("query=") > 0) && !bigsize;
        e[1], e[3], e[0];
        isIe8 && useParent && "home" != frpage && 1
    }

    function getPositionAndSize(e) {
        var t = 0, i = 0, n = (e.offsetWidth, e.offsetHeight);
        return e && (t += e.offsetLeft, i += e.offsetTop, e = e.offsetParent), [t, i, 578, n]
    }

    function getQuery() {
        return input_elem.value
    }

    function suggSaveQuery() {
        if (window.localStorage && window.JSON) {
            var e = trimStr(getQuery());
            if (e && e.length < 40) {
                var t = getLocalStoragePinyin(e);
                t ? localStoragePinyin(e, t) : httpRequestPinyin(e)
            }
        }
    }

    function checkQuery() {
        if (getQuery() !== noneed_query) return showtop = !1, void start();
        setTimeout(checkQuery, 10)
    }

    function checkQuery2() {
        var e = getQuery();
        e && noneed_query != e && lastinput_query == e ? sending_timer || (sending_timer = setTimeout(function () {
            noneed_query = "", suggestWordId = -1, needData(e)
        }, 100)) : (clearTimeout(sending_timer), sending_timer = 0, e || showtop || (userInputString = "", jsonData = [], window.localStorage && localStorage.getItem(sogouSearchSugPinyinN) && JSON.parse(localStorage.getItem(sogouSearchSugPinyinN)).length > 0 ? showHistory(JSON.parse(localStorage.getItem(sogouSearchSugPinyinN))) : hideDiv()), lastinput_query = e), e && (showtop = !1), setTimeout(checkQuery2, 10)
    }

    function showHistory(e) {
        showHistoryFlag = !0, highlight_li = -1, showtop = !0, suggLis = [], suggOText = [];
        for (var t, i, n, o = suggDiv.getElementsByTagName("ul")[0]; o.childNodes.length > 0;) o.removeChild(o.childNodes[0]);
        (n = (i = e.length) > 10 ? i - 10 : 0) > 0 && (clkSrc = "history", disCount = 1, hisDisCount++, position = 0);
        for (var s = 0, r = i - 1, a = 0; r >= n; r--, a++) {
            (t = d.createElement("li")).style.color = "rgb(122, 119, 200)", t.setAttribute("history", "1"), t.setAttribute("origin_sugg_query", e[r].oq), t.onmouseover = mouseOver, t.onmouseout = mouseOut, t.onmousedown = mouseDown, t.onclick = mouseClick, t.setAttribute("lid", r), t.setAttribute("qid", s++), t.innerHTML = e[r].oq.replace(/</gi, "&lt;").replace(/>/gi, "&gt;");
            var u = e[r].arr2.split(";")[2];
            (u && 1 == u || 2 == u) && (t.innerHTML += "<span></span>", sugVrWordCount++), suggLis.push(t), suggOText.push(t.innerHTML), o.appendChild(t), jsonData[r] = e[r].oq, vrFlag[e[r].oq] = {type: u}
        }
        for (r = 0; r < s; r++) tpos[r] = 1;
        positionDiv(), showDiv(isShowing()), contentDiv && (contentDiv.style.display = "none", suggDiv.className = "suggestion nobg")
    }

    localStorageMap(), that.sw = function (e, t) {
        if (!t) try {
            handleData(["", []])
        } catch (e) {
        }
        on = t || !1, noneed_query = e || "", showtop = !0, suggDiv && hideDiv()
    }, that.sugTypeChange = function (e) {
        sugType = e, cache = {}
    };
    var sctop, toptimer, showtop = !1;

    function showTopWord() {
        if (clearTimeout(toptimer), "undefined" == typeof sogou_top_words) return sctop || ((sctop = d.createElement("script")).charset = "gb2312", sctop.src = "/suggnew/hotwords?v=" + (new Date).getTime(), d.body.appendChild(sctop)), void (toptimer = setTimeout(showTopWord, 50));
        if (!getQuery()) {
            if (!sogou_top_words.length) return void hideDiv();
            showtop = !0, userInputString = "";
            for (var e, t = suggDiv.getElementsByTagName("ul")[0]; t.childNodes.length > 0;) t.removeChild(t.childNodes[0]);
            suggLis = [], suggOText = [], jsonData = sogou_top_words;
            for (var i = location.protocol.toLowerCase(), n = 0; n < jsonData.length && n < 10; n++) (e = d.createElement("li")).style.height = "27px", e.onmouseover = mouseOver, e.onmouseout = mouseOut, e.onmousedown = mouseDown, e.onclick = mouseClick, e.setAttribute("lid", n), e.innerHTML = "<em class='n0' style='background:url(" + i + "//www.sogou.com/sug/images/n_" + (n + 1) + ".gif) no-repeat;'></em>" + jsonData[n] + (0 == n ? ' <img src="/sug/images/new2.gif" align="absmiddle" />' : ""), vrFlag[jsonData[n]] = {
                type: 0,
                tupu_key: ""
            }, suggLis.push(e), suggOText.push(e.innerHTML), t.appendChild(e);
            positionDiv(), showDiv(isShowing()), tophint.style.display = "", contentDiv && (contentDiv.style.display = "none", suggDiv.className = "suggestion nobg")
        }
    }

    function needData(e) {
        if (input_time || (input_time = (new Date).getTime()), cache[e] && "function" != typeof cache[e]) handleData(cache[e]); else {
            try {
                d.body.removeChild(ajaj)
            } catch (e) {
            }
            (ajaj = d.createElement("script")).charset = "gb2312", ajaj.src = suggUri + "?key=" + encodeURIComponent(e) + "&type=" + sugType + "&pr=" + productId + "&t=" + input_time, d.body.appendChild(ajaj)
        }
    }

    function escapeForSpecialChars(e) {
        return null != e ? e.replace(/&/g, "&amp;").replace(/ /g, "&nbsp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;") : ""
    }

    function bold(e, t) {
        var i = e;
        return 0 == e.indexOf(t) && (i = t + "<b>" + e.substr(t.length) + "</b>"), i
    }

    function unbold(e) {
        if (void 0 !== e) return e.replace("<b>", "").replace("</b>", "")
    }

    function handleData(e) {
        if (!firstRun && getQuery()) {
            var t;
            if (userInputString = e[0] || userInputString, showHistoryFlag = !1, window.localStorage && window.JSON) {
                var i = getLocalStorageOq(e[0]);
                try {
                    t = i.length
                } catch (e) {
                }
                reorganizeResults(e = JSON.parse(JSON.stringify(e)), i)
            }
            if (jsonData = e[1], e.length > 2) {
                jsonDataTongji = e[2], "on" == getParam("sugdbg", "off") && (jsonDataTongji[0] = "0;0;1;0"), jsonDataTongji0 = [], jsonDataTongji1 = [], jsonDataTongji2 = [], goTongjiId = [];
                for (var n = 0; n < jsonDataTongji.length; ++n) {
                    var o = jsonDataTongji[n].split(";");
                    vrFlag[e[1][n]] = {type: o[2], tupu_key: e[3][n]}, sugData[e[1][n]] = {
                        arr2: e[2][n],
                        arr3: e[3][n]
                    }, null != o && o.length >= 3 ? (jsonDataTongji0.push(o[0]), jsonDataTongji1.push(o[1]), jsonDataTongji2.push(o[2])) : (jsonDataTongji0.push(-1), jsonDataTongji1.push(0), jsonDataTongji2.push("0")), goTongjiId.push(0)
                }
            }
            e.length > 3 && (hasPersonal1 = e[3][0]);
            var s = 0;
            clearHighlight(), highlight_li = -1, positionDiv();
            var r = isShowing();
            showDiv("show");
            for (var a, u = suggDiv.getElementsByTagName("ul")[0]; u.childNodes.length > 0;) u.removeChild(u.childNodes[0]);
            suggLis = [], suggOText = [];
            for (s = 0; s < jsonData.length && s < 10; s++) a = d.createElement("li"), t && s < t && (a.style.color = "rgb(122, 119, 200)", a.setAttribute("history", "1"), a.setAttribute("origin_sugg_query", jsonData[s]), hisPos[s] = 1), a.onmouseover = mouseOver, a.onmouseout = mouseOut, a.onmousedown = mouseDown, a.onclick = mouseClick, a.setAttribute("lid", s), a.innerHTML = bold(escapeForSpecialChars(jsonData[s]), escapeForSpecialChars(userInputString)), 0 == s && "3" == jsonDataTongji2[0] && (a.innerHTML = '<strong style="color:red">���Ƿ�Ҫ�ң�</strong><strong>' + a.innerHTML + "</strong>"), !vrFlag[jsonData[s]] || 1 != vrFlag[jsonData[s]].type && 2 != vrFlag[jsonData[s]].type || sugVrWordCount++, suggLis.push(a), suggOText.push(a.innerHTML), u.appendChild(a), sugTemplate.prototype.cutTitle(a, a.innerHTML), tpos[s] = 1;
            hideDiv(), (jsonData.length > 0 || newPara) && on && suggLis.length > 0 && (clkSrc = "common", disCount = 1, addClass(suggLis[0], "first"), positionDiv(), showDiv(r), suggDivShowCount++, t && t > 0 && suggHisShowCount++, handleFlag = handleRetry, selectItem(0)), position = 0, suggDivReqCount++, 0 != jsonData.length && on || hideDiv(), setIsShowSuggAtLast(jsonData.length)
        }
    }

    function getParam(e, t) {
        var i = location.href, n = i.indexOf("?");
        if (-1 == n) return t;
        for (var o = i.substring(n + 1).split("&"), s = o.length, r = 0; r < s; r++) {
            var a = o[r].split("=");
            if (!(a.length < 2)) {
                var u = a[0], g = a[1];
                if (u == e) return g
            }
        }
        return r == s ? t : void 0
    }

    function stopEvent(e) {
        return e.preventDefault && e.preventDefault(), e.cancelBubble = !0, e.returnValue = !1
    }

    "object" == typeof window.sogou && null != window.sogou || (window.sogou = {}), void 0 !== window.sogou.sug && (oldfunc = window.sogou.sug), window.sogou.sug = function (e) {
        try {
            oldfunc(e)
        } catch (e) {
        }
        badSuggMap = {}, e[0] == getQuery() ? (e.length > 1 && e[1].length > 0 && (cache[e[0]] = e), handleData(e)) : hideDiv()
    }, void 0 !== window.sogou.site && (oldfunc2 = window.sogou.site), window.sogou.site = function (e) {
        clearTimeout(setTimer1), clearTimeout(setTimer2), clearTimeout(setTimer3);
        try {
            oldfunc2(e)
        } catch (e) {
        }
        if (e) if (0 != e.doc_num) handleFlag = handleRetry, sitecache[decodeURIComponent(e.query)] = e, handleSiteData(e); else {
            for (var t = null, i = 0; i < suggLis.length; i++) hoverClassReg.test(suggLis[i].className) && (t = jsonData[i]);
            handleFlag > 0 && t == decodeURIComponent(e.query) && handleSiteData(e, --handleFlag)
        }
    };
    var useKey = !1, submitby = "default";

    function keydown(e) {
        if (e = e || window.event, firstRun) {
            if (27 == e.keyCode) return;
            start()
        }
        if (input_time || (input_time = (new Date).getTime()), 27 == e.keyCode) isShowing() && (hideDiv(), noneed_query = input_elem.value, setTimeout(function () {
            noneed_query = input_elem.value
        }, 1)); else if (13 == e.keyCode) ; else if (isShowing()) {
            if (38 == e.keyCode) return useKey = !0, upKey(e), position--, stopEvent(e);
            if (9 == e.keyCode || 40 == e.keyCode) return useKey = !0, downKey(e), position++, stopEvent(e)
        } else 38 != e.keyCode && 40 != e.keyCode || (useKey = !0, getQuery() && needData(getQuery()))
    }

    function timeoutSubmit() {
        setTimeout(function () {
            input_form.submit()
        }, 100);
        var e = input_elem.value;
        if (e && vrFlag[e] && (1 == vrFlag[e].type || 2 == vrFlag[e].type)) {
            var t = sitecache[e];
            if (t) {
                for (var i = 0, n = -1; i < jsonData.length; i++) if (jsonData[i] == decodeURIComponent(t.query)) {
                    n = i;
                    break
                }
                template.pv(t.query, t.type || "-1", n, t.doc_num || 0, "suggvrcl", "", t.vrtype)
            }
        }
    }

    function trimStr(e) {
        return e.replace(/^\s+|\s+$/gm, "")
    }

    function downKey(e) {
        suggDiv.onmousemove || (suggDiv.onmousemove = mouseMove), isKeyTime = !0, clearTimeout(setTimer3), needRemoveHistoryCloseIcon(suggLis[highlight_li], e) && removeHistoryCloseIcon(suggLis[highlight_li]), ++highlight_li == Math.min(jsonData.length, 10) && (highlight_li = -1), highlight(e)
    }

    function upKey(e) {
        suggDiv.onmousemove || (suggDiv.onmousemove = mouseMove), isKeyTime = !0, clearTimeout(setTimer3), clearHighlight(), needRemoveHistoryCloseIcon(suggLis[highlight_li], e) && removeHistoryCloseIcon(suggLis[highlight_li]), -2 == --highlight_li && (highlight_li = Math.min(jsonData.length, 10) - 1), highlight(e)
    }

    function highlight(e) {
        clearHighlight(), highlight_li >= 0 ? (addClass(suggLis[highlight_li], "over"), input_elem.value = unbold(showHistoryFlag ? jsonData[jsonData.length - highlight_li - 1] : jsonData[highlight_li]), handleFlag = handleRetry, selectItem(highlight_li), needAddHistoryCloseIcon(suggLis[highlight_li], e) && addHistoryCloseIcon(suggLis[highlight_li])) : input_elem.value = userInputString, suggestWordId = highlight_li, noneed_query = input_elem.value
    }

    function listHighlight() {
        clearHighlight(), highlight_li >= 0 && addClass(suggLis[highlight_li], "over")
    }

    function clearHighlight() {
        for (var e = 0; e < suggLis.length; e++) removeClass(suggLis[e], "over")
    }

    function mouseMove() {
        suggDiv.onmousemove = null, isKeyTime = !1, clearTimeout(hideTimer), hideTimer = setTimeout(function () {
            var e = null;
            mouseTime_li >= 0 && (e = suggLis[mouseTime_li]) && (clearHighlight(), addClass(e, "over"), handleFlag = handleRetry, selectItem(highlight_li = mouseTime_li)), mouseTime_li = -1
        }, 50)
    }

    function mouseOut(e) {
        needRemoveHistoryCloseIcon(this, e = e || window.event) && removeHistoryCloseIcon(this), clearTimeout(hideTimer)
    }

    function mouseOver(e) {
        if (e = e || window.event, mouseTime_li = parseInt(this.getAttribute("lid")), !isKeyTime) {
            clearHighlight(), addClass(this, "over"), clearTimeout(setTimer3), clearTimeout(hideTimer);
            var t = needAddHistoryCloseIcon(this, e), i = this;
            hideTimer = setTimeout(function () {
                clearHighlight(), addClass(i, "over"), highlight_li = parseInt(i.getAttribute("lid")), handleFlag = handleRetry, selectItem(highlight_li), t && addHistoryCloseIcon(i)
            }, 100)
        }
    }

    function mouseDown(e) {
        return e && e.stopPropagation ? e.stopPropagation() : window.event.cancelBubble = !0, mousedown_ontr = 1, !1
    }

    function mouseClick() {
        suggestWordId = parseInt(this.getAttribute("lid"));
        var e = input_elem.value, t = input_elem.value = jsonData[suggestWordId];
        try {
            suggWxClick(e, t, this)
        } catch (e) {
        }
        noneed_query = t, hideDiv(), submitby = "mouse", "history" == clkSrc ? (position = parseInt(this.getAttribute("qid")), hisItemClk = 1) : (position = suggestWordId, "1" == this.getAttribute("history") && (sugHisClk = 1, 0 == position ? (hisPosClk[0] = 1, clkSrc = "his") : 1 == position && (hisPosClk[1] = 1, clkSrc = "his"))), input_form.onsubmit && 0 == input_form.onsubmit() || timeoutSubmit()
    }

    function needAddHistoryCloseIcon(e, t) {
        var i = t.relatedTarget || t.fromElement;
        if (!i || i.parentNode == e || i == e) {
            var n = e.getElementsByTagName("a");
            if (9 != t.keyCode && 38 != t.keyCode && 40 != t.keyCode && 1 == n.length) return !1
        }
        return !0
    }

    function addHistoryCloseIcon(e) {
        if (window.localStorage && (e && e.getAttribute("history"))) {
            var t = d.createElement("a");
            t.href = "javascript:void(0);", t.onclick = function (t) {
                if (stopEvent(t = t || window.event), removeLocalStoragePy(e.getAttribute("origin_sugg_query")), e.parentNode.childNodes.length > 1) e.parentNode.removeChild(e); else {
                    var i = e.parentNode.parentNode.parentNode;
                    i.parentNode.removeChild(i)
                }
                uigs_sugg_cl("zh_sugg_remove", "hisremove", 0, "fr=" + frpage)
            }, t.setAttribute("class", "close"), e.appendChild(t)
        }
    }

    function needRemoveHistoryCloseIcon(e, t) {
        var i = t.relatedTarget || t.toElement;
        return !!(i && i.parentNode != e && i != e || 9 == t.keyCode || 38 == t.keyCode || 40 == t.keyCode)
    }

    function removeHistoryCloseIcon(e) {
        if (window.localStorage && (e && e.getAttribute("history"))) {
            var t = e.getElementsByTagName("a");
            t && t[0] && e.removeChild(t[0])
        }
    }

    function isShowing() {
        return suggDiv && "block" == suggDiv.style.display
    }

    function showDiv(e) {
        e || pingback("show_s"), tophint.style.display = "none", suggDiv.style.display = "block", suggIfm && (suggIfm.style.display = "block");
        try {
            useParent ? (input_elem.parentNode.offsetParent.appendChild(suggDiv), input_elem.parentNode.offsetParent.appendChild(suggIfm)) : (input_elem.offsetParent.appendChild(suggDiv), input_elem.offsetParent.appendChild(suggIfm))
        } catch (e) {
        }
    }

    function selectItem(e) {
        clearTimeout(timeOutTimer), clearTimeout(loadingTimer), setThroughResult(!1), vrFlag[jsonData[e]] && 0 != vrFlag[jsonData[e]].type || "none" !== contentDiv.style.display && (contentDiv.style.display = "none", suggDiv.className = "suggestion nobg", template.cutAllTitle(suggLis, suggOText))
    }

    function hideDiv() {
        suggDiv.style.display = "none", suggIfm && (suggIfm.style.display = "none");
        try {
            useParent ? (input_elem.parentNode.offsetParent.removeChild(suggDiv), input_elem.parentNode.offsetParent.removeChild(suggIfm)) : (input_elem.offsetParent.removeChild(suggDiv), input_elem.offsetParent.removeChild(suggIfm))
        } catch (e) {
        }
    }

    function initStyle() {
        var e = $c("link");
        e.setAttribute("rel", "stylesheet"), e.setAttribute("type", "text/css"), e.setAttribute("href", server_url + "sug/css/m3.min.v.4.css"), d.getElementsByTagName("head")[0].appendChild(e)
    }

    function computePersonal() {
        var e = 0;
        if (null == jsonDataTongji1 || jsonDataTongji1.length < 1) return 0;
        for (var t = 0; t < jsonDataTongji1.length; ++t) {
            e += parseInt(jsonDataTongji1[t])
        }
        return e
    }

    function start() {
        if (firstRun) {
            firstRun = 0, noneed_query = input_elem.value, normalRid = normalRid || (input_form.w && input_form.w.value ? input_form.w.value : normalRid), input_form.onsubmit = function (e) {
                return !(e = e || window.event) || "submit" != e.type || (setTimeout(function () {
                    0 == input_form.onsubmit() || timeoutSubmit()
                }, 100), !1)
            };
            var e = input_form.onsubmit || function () {
            };
            input_form.onsubmit = function (t, i, n) {
                if ("function" == typeof e && 0 == e(t, i, n)) return !1;
                increaseSct(), hasPersonal = computePersonal();
                var o = {w: normalRid};
                if (-1 != suggestWordId && (o = {
                    w: suggestRid,
                    oq: userInputString,
                    ri: suggestWordId,
                    sourceid: "sugg"
                }, jsonDataTongji.length > 0 && (o = {
                    w: suggestRid,
                    oq: userInputString,
                    ri: suggestWordId,
                    sourceid: "sugg",
                    stj: jsonDataTongji[suggestWordId],
                    stj2: goTongjiId[suggestWordId],
                    stj0: jsonDataTongji0[suggestWordId],
                    stj1: jsonDataTongji1[suggestWordId],
                    hp: hasPersonal,
                    hp1: hasPersonal1
                })), o.sut = input_time ? (new Date).getTime() - input_time : 0, o.sst0 = (new Date).getTime(), o.lkt = keypressNum_lead + "," + time1_lead + "," + time2_lead, showtop && (o.p = "01019900" == normalRid ? "40040108" : "40240100"), !(location.href.indexOf("query=") > 0 || bigsize)) {
                    var s = function (e, t) {
                        var i = location.href, n = i.indexOf("?");
                        if (-1 == n) return t;
                        for (var o = i.substring(n + 1).split("&"), s = o.length, r = 0; r < s; r++) {
                            var a = o[r].split("=");
                            if (!(a.length < 2)) {
                                var u = a[0], g = a[1];
                                if (u == e) return g
                            }
                        }
                        return r == s ? t : void 0
                    }("pid", "");
                    s.length > 0 && (o.pid = s)
                }
                var r, a, u = input_form.getElementsByTagName("input");
                for (var g in o) {
                    for (r = 0; r < u.length; r++) if (u[r].getAttribute("name") == g) {
                        u[r].value = o[g];
                        break
                    }
                    r == u.length && ((a = d.createElement("input")).type = "hidden", a.name = g, a.value = o[g], input_form.appendChild(a))
                }
                return suggSaveQuery(), pingback("sb"), suggDivReqCount = 0, suggDivShowCount = 0, suggHisShowCount = 0, sugHisClk = 0, sugVrWordCount = 0, !0
            }, function () {
                if (isIe) {
                    input_elem.offsetParent.style.position = "relative";
                    for (var e = input_elem.offsetParent; e;) parseInt(e.currentStyle.zIndex) || (e.style.zIndex = "2000"), e = e.offsetParent
                }
                if ((suggDiv = $c("div", null, "suggestion nobg")).id = "vl", window.isIpad) {
                    var t = {768: "455", 1024: "711", 1366: "1053"};
                    suggDiv.style.cssText = "top: 62px;left: 193px;width: " + t[document.body.clientWidth] + "px !important;", bind(window, "orientationchange", function () {
                        var e = document.body.clientWidth;
                        suggDiv.style.cssText = "top: 62px;left: 193px;width: " + t[e] + "px !important;"
                    })
                }
                var i, n = $c("div", suggDiv, "suginner"), o = $c("p", n, "s_title"), s = $c("ul", n, "suglist");
                (tophint = o).innerHTML = "�����ȴ�", tophint.style.display = "none", tophint.style.margin = "0", suggLis = [];
                for (var r = 0; r < 10; r++) (i = d.createElement("li")).onmouseover = mouseOver, i.onmouseout = mouseOut, i.onmousedown = mouseDown, i.onclick = mouseClick, i.setAttribute("lid", r), suggLis.push(i), s.appendChild(i);
                (contentDiv = $c("div", n, "sugc")).id = "sugc", contentDiv.onmouseover = function () {
                    mouseTime_li = -1
                }, contentDiv.style.display = "none", s.onmouseout = listHighlight
            }(), bind(d, "click", function (e) {
                for (var t = (e = e || window.event).srcElement || e.target; t;) {
                    if (t == contentDiv || t == input_elem) return;
                    t = t.parentNode
                }
                hideDiv()
            }), bind(input_elem, "beforedeactivate", function () {
                mousedown_ontr && (window.event.cancelBubble = !0, window.event.returnValue = !1, mousedown_ontr = 0)
            }), checkQuery2()
        }
    }

    function getCookie() {
        var e = d.cookie, t = e.indexOf("; sct=");
        if (-1 == t) {
            if (0 != (t = e.indexOf("sct="))) return null
        } else t += 2;
        var i = e.indexOf(";", t);
        return -1 == i && (i = e.length), e.substring(t + "sct=".length, i)
    }

    function increaseSct() {
        var e = parseInt(getCookie() || 0) || 0;
        document.cookie = "sct=" + (e + 1) + "; expires=Thu, 21-Jul-2020 00:00:00 GMT; path=/;domain=sogou.com;"
    }

    var oldclick = d.onclick || function () {
    };

    function page_click(e) {
        if (!(e && 0 != e.button || !e && 0 != window.event.button)) for (var t, i = (e = e || window.event).target ? e.target : e.srcElement; i && i.tagName;) {
            if ("A" == i.tagName.toUpperCase()) return void ((0 == (t = i.href || "").indexOf("http://www.sogou.com/") || 0 == t.indexOf("https://www.sogou.com/")) && t.indexOf("query=") > 0 && increaseSct());
            i = i.parentNode
        }
    }

    function setThroughResult(e) {
        for (var t = getElesByClass("suglist", suggDiv)[0], i = t.getElementsByTagName("span"), n = (getElesByClass("over", t)[0] || t.getElementsByTagName("li")[0]).getElementsByTagName("span")[0], o = 0, s = i.length; o < s; o++) "sugg-loading" === i[o].className && (i[o].className = "");
        if (n) return n.className = e ? "sugg-loading" : "", n
    }

    function getSiteData(e, t, i) {
        if (contentDiv.style.display = "", suggDiv.className = "suggestion", i = i || 0, (e = unbold(e || "")) && !badSuggMap[t]) {
            sitecache[e];
            if (clearTimeout(loadingTimer), clearTimeout(timeOutTimer), loadingTimer = setTimeout(function () {
                clearTimeout(loadingTimer), setThroughResult(!0)
            }, 100), timeOutTimer = setTimeout(function () {
                clearTimeout(timeOutTimer);
                var e = setThroughResult(!1);
                e && e.parentNode.removeChild(e), suggOText[t] = suggOText[t].replace("<span></span>", "")
            }, 3e3), contentDiv && 0 == i && (contentDiv.innerHTML = ""), sitecache[e]) handleSiteData(sitecache[e]); else {
                var n = 2 == vrFlag[e].type ? 1 : 0;
                e = encodeURIComponent(e);
                try {
                    d.body.removeChild(ajaj2)
                } catch (e) {
                }
                ajaj2 = d.createElement("script");
                var o = null;
                if (document.cookie.length > 0 && document.cookie.indexOf("IPLOC=") >= 0) {
                    var s = document.cookie.indexOf("IPLOC=") + 6,
                        r = -1 == document.cookie.indexOf(";", s) ? document.cookie.length : document.cookie.indexOf(";", s);
                    o = document.cookie.substring(s, r)
                }
                for (/CN[0-9]{4,6}/.exec(o) || (o = "CN110000"); o.legnth < 6;) o += "0";
                ajaj2.charset = "gb2312", ajaj2.src = ["http://go.sugg.sogou.com/", e, "?", (new Date).getTime(), "&rid=", e.toLowerCase().charCodeAt(e.length - 1) % 6, "&IPLOC=", o, "&type=", n].join(""), d.body.appendChild(ajaj2)
            }
        }
    }

    function httpRequestPinyin(e) {
        (ajajPinyin = d.createElement("script")).charset = "gb2312", ajajPinyin.src = "/sugg/ajaj_json.jsp?type=getpinyin&key=" + encodeURIComponent(e), d.body.appendChild(ajajPinyin)
    }

    function sleep(e) {
        for (var t = +new Date; !(+new Date - t > e);) ;
    }

    function getLocalStorageOq(e) {
        if (e = trimStr(e), window.localStorage) {
            if (!e || !localStorage.getItem(sogouSearchSugPinyinN)) return !1;
            for (var t = [], i = JSON.parse(localStorage.getItem(sogouSearchSugPinyinN)), n = i.length - 1; n > -1; n--) {
                var o = i[n];
                if (0 == o.py.indexOf(e) ? t.push(o) : 0 == o.oq.indexOf(e) && t.push(o), t.length > 1) break
            }
            return t
        }
    }

    function reorganizeResults(e, t) {
        if (!t || 0 == t.length) return e;
        for (var i = e[1], n = e[2], o = e[3], s = 0; s < i.length; s++) for (var r = i[s], a = 0; a < t.length; a++) {
            if (r == (g = t[a]).oq) {
                !0, i.splice(s, 1), n.splice(s, 1), o.splice(s, 1), s--;
                break
            }
        }
        for (var u = t.length - 1; u >= 0; u--) {
            var g = t[u];
            i.unshift(g.oq), n.unshift(g.arr2), o.unshift(g.arr3)
        }
        for (; i.length > 10;) i.pop(), n.pop(), o.pop()
    }

    function getLocalStoragePinyin(e) {
        try {
            if (!window.localStorage) return;
            if (!e || !localStorage.getItem(sogouSearchSugPinyinN)) return !1;
            for (var t = JSON.parse(localStorage.getItem(sogouSearchSugPinyinN)), i = 0; i < t.length; i++) {
                var n = t[i];
                if (n.oq == e) return n.py
            }
            return !1
        } catch (i) {
        }
    }

    function localStoragePinyin(e, t) {
        if (!e || !t) return !1;
        var i, n = {};
        if (window.localStorage) {
            i = localStorage.getItem(sogouSearchSugPinyinN) ? JSON.parse(localStorage.getItem(sogouSearchSugPinyinN)) : [];
            for (var o = 0; o < i.length; o++) {
                i[o].oq == e && i.splice(o, 1)
            }
            n.oq = e, n.py = t;
            var s = sugData[e];
            for (n.arr2 = s ? s.arr2 : "0;0;0;0", n.arr3 = s ? s.arr3 : "", i.push(n); i.length > 100;) i.shift();
            return localStorage.setItem(sogouSearchSugPinyinN, JSON.stringify(i)), !0
        }
    }

    function removeLocalStoragePy(e) {
        if (e = trimStr(e), window.localStorage) {
            if (!e || !localStorage.getItem(sogouSearchSugPinyinN)) return !1;
            for (var t = JSON.parse(localStorage.getItem(sogouSearchSugPinyinN)), i = 0; i < t.length; i++) {
                if (t[i].oq == e) {
                    t.splice(i, 1);
                    break
                }
            }
            return localStorage.setItem(sogouSearchSugPinyinN, JSON.stringify(t)), !0
        }
    }

    function handleSiteData(e, t) {
        var i = -1;
        if (contentDiv) if (0 == (t || 0) && (contentDiv.innerHTML = ""), template.build(contentDiv, e, jsonData, goTongjiId, vrFlag)) clearTimeout(timeOutTimer), clearTimeout(loadingTimer), setThroughResult(!1), suggDiv.className = "suggestion", "none" == contentDiv.style.display ? (contentDiv.style.display = "", template.cutAllTitle(suggLis, suggOText)) : contentDiv.style.display = ""; else if (suggDiv.className = "suggestion", contentDiv.style.display = "none", clearTimeout(setTimer1), clearTimeout(setTimer3), e.query) {
            for (var n = 0; n < jsonData.length; n++) if (jsonData[n] == decodeURIComponent(e.query)) {
                i = n, 0 === t && (badSuggMap[i] = !0);
                break
            }
            setTimer3 = setTimeout(function () {
                getSiteData(decodeURIComponent(e.query), i, MAX_RETRY_FETCH_SITE - 1)
            }, 500)
        }
    }

    d.onclick = function (e) {
        var t = oldclick(e);
        return page_click(e), t
    }, window.sogou.sugpy = function (e) {
        var t = e[0];
        if (!/^\?+\?$/.test(t.trim())) {
            var i = e[1][0];
            localStoragePinyin(trimStr(getQuery()), i)
        }
    }, template.getSiteData = getSiteData, isIe6 || init(), sugTemplate.prototype.buildZhiDaLoopSection = function (context, tempCode) {
        for (var loopPtn = /<!--\s*LOOP\s+SET=\$\{(.*?)\}.*?-->/, endPtn = /<!--\s*ENDLOOP\s*-->/, loopMat = null, endMat = null; loopMat = loopPtn.exec(tempCode);) {
            var leftContent = RegExp.leftContext, setCode = loopMat[1];
            endMat = endPtn.exec(tempCode);
            var rightContent = RegExp.rightContext,
                loopCode = tempCode.substring(loopMat.index + loopMat[0].length, endMat.index), loopContent = "";
            with (context) var setVar = eval(setCode);
            for (var i = 0; i < setVar.length; i++) {
                var item = setVar[i];
                context.item = item, context.i = i, loopContent += this.replaceZhidaTemp(loopCode, context)
            }
            tempCode = leftContent + loopContent + rightContent
        }
        return tempCode
    }, sugTemplate.prototype.replaceZhidaTemp = function (code, context) {
        for (var varPtn = /\$\{(.*?)\}|\$%7B(.*?)%7D/g, varMat = null, head = 0, tail = 0, k = 0, content = ""; varMat = varPtn.exec(code);) {
            with (tail = varMat.index, content += code.substring(head, tail), context) content += eval(varMat[1] ? varMat[1] : varMat[2]);
            head = tail + varMat[0].length
        }
        return content += code.substring(head, code.length), content
    }, sugTemplate.prototype.buildZhiDaHtml = function (e, t) {
        return t = this.buildZhiDaLoopSection(e, t), this.replaceZhidaTemp(t, e)
    }, sugTemplate.prototype.buildZhiDa = function (e, t, i) {
        e.innerHTML = this.buildZhiDaHtml(t, i)
    }, suggSaveQuery()
}

sugTemplate.prototype.getSuggCdnImgLink = function (e) {
    if (!e) return "";
    if (!("https:" == location.protocol.toLowerCase()) || -1 == e.indexOf("http://") || 0 == e.indexOf("https://")) return e;
    var t = "https://img0" + (Math.abs(function (e) {
            var t = 0;
            if (0 == e.length) return t;
            for (var i = 0; i < e.length; i++) t = (t << 5) - t + e.charCodeAt(i), t &= t;
            return t
        }(e) % 4) + 1) + ".sogoucdn.com", i = /^\s*http:\/\/www\.sogou\.com/g, n = /^\s*http:\/\/img\d*\.sogoucdn\.com/g,
        o = /^\s*http:\/\/img\d*\.store\.sogou\.com/g, s = /^\s*http:\/\/imgstore\d*\.cdn\.sogou\.com/g,
        r = /^\s*http:\/\/cmc\.imgstore\.cdn\.sogou\.com/g, a = /^\s*http:\/\/pic\d*\.sogoucdn\.com/g;
    return i.test(e) ? e.replace(i, "") : n.test(e) ? e.replace(n, t) : o.test(e) ? e.replace(o, t) : s.test(e) ? e.replace(s, t) : r.test(e) ? e.replace(r, t) : a.test(e) ? e.replace(a, t) : t + "/v2/thumb?t=2&url=" + encodeURIComponent(e) + "&appid=200580"
}, sugTemplate.prototype.vmap = {
    21: ".v.1",
    60: ".v.4",
    69: ".v.1",
    91: ".v.1",
    97: ".v.5",
    113: ".v.2",
    117: ".v.1",
    125: ".v.2",
    137: ".v.1",
    145: ".v.3",
    163: ".v.2",
    164: ".v.2",
    166: ".v.2",
    191: ".v.5",
    206: ".v.1",
    210: ".v.3",
    244: ".v.4",
    273: ".v.1",
    312: ".v.3",
    317: ".v.3",
    320: ".v.2",
    328: ".v.2",
    338: ".v.1",
    344: ".v.2",
    376: ".v.6",
    322: ".v.1",
    330: ".v.1",
    349: ".v.2",
    406: ".v.1",
    411: ".v.1",
    446: ".v.1",
    2040: ".v.1",
    2140: ".v.2",
    2098: ".v.1",
    3005: ".v.1",
    10001: ".v.3",
    10002: ".v.3",
    10003: ".v.1",
    10004: ".v.2",
    10005: ".v.2"
}, sugTemplate.prototype.cutTitle = function (e, t) {
    var i, n = -1 != navigator.userAgent.indexOf("MSIE 6") && !window.opera,
        o = /^(.*?)(<b>(.*?)<\/b>)?(<span><\/span>)?$/i.exec(t), s = [o[1], o[3], o[4] ? o[4] : ""],
        r = s[0].length + (s[1] ? s[1].length : 0);
    for (n && (e.style.height = null), e.innerHTML = "��", i = e.offsetHeight, e.innerHTML = t; e.offsetHeight > 5 * i / 4;) e.innerHTML = s[0].substring(0, r) + (r > s[0].length ? "<b>" + s[1].substring(0, r - s[0].length) + "...</b>" : "...") + s[2], r--;
    n && (e.style.height = "27px")
}, sugTemplate.prototype.cutAllTitle = function (e, t) {
    for (var i = 0; i < e.length; i++) this.cutTitle(e[i], t[i])
}, sugTemplate.prototype.revertAllTitle = function (e, t) {
    for (var i = 0; i < e.length; i++) e[i].innerHTML = t[i]
}, sugTemplate.prototype.len = function (e) {
    return e && e.replace ? e.replace(/\[\/?em\]/g, "").replace(/[^\x00-\xff]/g, "rr").length : ""
}, sugTemplate.prototype.cutLength = function (e, t, i, n) {
    if (i = i || "...", n = n || 3, this.len(e) > t) {
        do {
            e = e.lastIndexOf("[em]") == e.length - 4 ? e.substring(0, e.length - 4) : e.lastIndexOf("[/em]") == e.length - 5 ? e.substring(0, e.length - 5) : e.substring(0, e.length - 1)
        } while (e && this.len(e) + n > t);
        return e.lastIndexOf("[/em]") < e.lastIndexOf("[em]") && (e = e.substring(0, e.lastIndexOf("[em]")) + e.substring(e.lastIndexOf("[em]") + 4)), e + i
    }
    return e
}, sugTemplate.prototype.$c = function (e, t, i) {
    var n = document.createElement(e);
    return t && t.appendChild(n), i && (n.className = i), n
}, sugTemplate.prototype.$ = function (e) {
    return document.getElementById(e)
}, sugTemplate.prototype.parseXML = function (e) {
    return window.DOMParser ? (tmp = new DOMParser, xml = tmp.parseFromString(e, "text/xml")) : (xml = new ActiveXObject("Microsoft.XMLDOM"), xml.async = "false", xml.loadXML(e)), xml.documentElement
}, sugTemplate.prototype.selectNodes = function (e, t) {
    function i(e, t) {
        for (var i = [], n = 0; n < e.length; n++) for (var o = 0; o < e[n].childNodes.length; o++) e[n].childNodes[o].nodeName == t && (i[i.length] = e[n].childNodes[o]);
        return i
    }

    for (var n = [e], o = t.split("/"), s = 0; s < o.length; s++) if (null == (n = i(n, o[s]))) return [];
    return n
}, sugTemplate.prototype.buildTitle = function (e, t, i, n, o) {
    var s = this.$c("h3", e, o || "sugtype");
    return s.innerHTML = ['<a id="sgtitle" onfocus="this.blur();" href="', i ? i + '" target="_blank' : "/sogou?ie=utf8&query=" + t.query, '">', this.cutLength(n || decodeURIComponent(t.query), 44), "</a>"].join(""), s
}, sugTemplate.prototype.buildMoreHint = function (e, t) {
    var i = this.$c("div", e, "morehint"), n = this.$c("a", i);
    n.innerHTML = "������ؽ��&gt;&gt;", n.href = "/web?query=" + t.query, n.target = "_blank", n.setAttribute("hideFocus", "hidefocus")
}, sugTemplate.prototype.markRed = function (e, t, i) {
    return t = t || "<em>", i = i || "</em>", e.indexOf(t) > 0 ? e : (e.indexOf("[em]") >= 0 && (e = e.replace(/\[em\]/g, t).replace(/\[\/em\]/g, i)), e)
}, sugTemplate.prototype.escape = function (e) {
    return e.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
}, sugTemplate.prototype.cutRed = function (e) {
    return e.replace(/\[\/?em\]/g, "")
}, sugTemplate.prototype.buildVRTitle = function (e, t, i) {
    var n = this.$c("a", this.$c("h3", e, "se_embed_title")), o = t.title;
    return o = this.cutLength(o, i), o = this.escape(o), o = this.cutRed(o), n.href = t.url, n.target = "_blank", n.title = this.cutRed(t.title), n.innerHTML = o, n
}, sugTemplate.prototype.buildContent = function (e, t) {
    for (var i = this.$c("div", e, "querylist"), n = 0; n < 2; n++) {
        var o = this.$c("a", i, "qitem");
        o.target = "_blank", o.href = t.docs[n].url, o.onfocus = function () {
            this.blur()
        };
        var s = this.$c("strong", o, "qtitle"), r = this.$c("span", s, "siteico");
        if (t.docs[n].favicon && (r.style.background = "url(" + t.docs[n].favicon + ") no-repeat scroll 6px 50% transparent"), r.innerHTML = this.cutLength(t.docs[n].title, 54), t.docs[n].content) this.$c("span", o, "qsummary").innerHTML = this.cutLength(this.escape(t.docs[n].content), 106);
        var a = this.$c("span", o, "qcite");
        t.docs[n].url && t.docs[n].url.indexOf("://") > 0 ? a.innerHTML = decodeURIComponent(t.docs[n].url.split("://")[1].split("/")[0]) : a.innerHTML = "www.sogou.com"
    }
    this.buildMoreHint(e, t)
}, sugTemplate.prototype.build = function (e, t, i, n, o) {
    if (!t) return !1;
    for (var s = this, r = -1, a = 0; a < i.length; a++) if (i[a] == decodeURIComponent(t.query)) {
        r = a;
        break
    }
    if (s.pv(t.query, t.type || "-1", r, t.doc_num || 0, null, null, t.vrtype || "-1"), n[r] = t.type || "-1", !t.doc_num || !t.docs) return !1;
    if (e.onclick = function (e) {
        if (!(e && 0 != e.button || !e && 0 != window.event.button)) try {
            for (var i, n = (e = e || window.event).target ? e.target : e.srcElement; n && n.tagName && ("A" == (i = n.tagName.toUpperCase()) && s.pv(t.query, t.type, r, t.doc_num, n.id || "sgcontent", n.href, t.vrtype), "DIV" != i);) n = n.parentNode
        } catch (e) {
        }
    }, t.type && 100 != t.type) {
        if (1e4 == t.type) try {
            var u = this.parseXML(t.docs[0].xml).getAttribute("type");
            t.qaType = parseInt(u), t.type = 1e4 + t.qaType, t.qaTag = o[decodeURIComponent(t.query)].tupu_key
        } catch (e) {
        }
        if (!this["build" + t.type]) {
            if (("317" == t.type || "60" == t.type) && !s.curtime) {
                if (window.standardtime) {
                    var g = window.standardtime;
                    window.standardtime = function (e, t) {
                        return s.curtime = e, g(e, t)
                    }
                } else window.standardtime = function (e, t) {
                    s.curtime = e
                };
                var l = document.createElement("script");
                l.charset = "gb2312", l.src = "websearch/features/standardtimeadjust.jsp?a=" + Math.random(), document.body.appendChild(l)
            }
            var c = document.createElement("script");
            c.charset = "gb2312", c.src = server_url + "js/sugtemp/build" + t.type + (this.vmap[t.type] || "") + ".js", document.body.appendChild(c)
        }
        this.buildVR(e, t, 0)
    } else e.innerHTML = "", this.buildTitle(e, t), this.buildContent(e, t);
    return !0
}, sugTemplate.prototype.buildVR = function (e, t, i) {
    if ("function" == typeof this["build" + t.type]) try {
        var n = t.docs, o = n[0], s = n[0].xml;
        s && ("https:" == location.protocol.toLowerCase() && (s = (s = (s = (s = s.replace(/http:\/\/www\.sogou\.com/g, "")).replace(/http:\/\/img\d+\.sogoucdn\.com/g, "https://img.store.sogou.com")).replace(/http:\/\/img\d+\.store\.sogou\.com/g, "https://img.store.sogou.com")).replace(/http:\/\/imgstore\.cdn\.sogou\.com/g, "https://img.store.sogou.com")), s = this.parseXML(s));
        try {
            o.url = this.selectNodes(s, "url")[0].firstChild.nodeValue
        } catch (e) {
        }
        try {
            o.title = this.selectNodes(s, "title")[0].firstChild.nodeValue
        } catch (e) {
        }
        try {
            o.domain = o.url.split("://")[1].split("/")[0]
        } catch (e) {
        }
        e.innerHTML = "", this["build" + t.type](e, t, o, s)
    } catch (e) {
    } else if (i <= 10) {
        var r = this;
        setTimeout(function () {
            r.buildVR(e, t, i + 1)
        }, 30)
    } else e.innerHTML = "", this.buildTitle(e, t), this.buildContent(e, t)
}, sugTemplate.prototype.reg = new RegExp("{{(.*?)}}", "g"), sugTemplate.prototype.pv = function (e, t, i, n, o, s, r) {
    try {
        if (imgurl = [pingBackUrl, o ? "/cl.gif" : "/pv.gif", "?uigs_productid=webgo"], imgurl.push("&query="), imgurl.push(encodeURIComponent(e)), imgurl.push("&type="), imgurl.push(t), r && imgurl.push("&vrtype=" + r), imgurl.push("&pos="), imgurl.push(i), imgurl.push("&num="), imgurl.push(n), o) imgurl.push("&uigs_cl="), imgurl.push(o), imgurl.push("&"), imgurl.push("href=" + encodeURIComponent(s)); else {
            if (this.lastpv == imgurl.join("")) return;
            this.lastpv = imgurl.join("")
        }
        imgurl.push("&uigs_t="), imgurl.push((new Date).getTime()), (new Image).src = imgurl.join("")
    } catch (e) {
    }
}, sugTemplate.prototype.buildTemplate = function (e, t) {
    var i = this;
    return e.replace(this.reg, function (e, n) {
        n = n.split("@");
        var o = i.selectNodes(t, "" + n[0]);
        return o.length > 0 ? n.length > 1 ? o[0].getAttribute(n[1]) : o[0].firstChild.nodeValue.replace(/\ue40a/g, "").replace(/\ue40b/g, "") : ""
    })
};
var smugg = new sogouSugg;

function sugg_go_imgresize(e, t, i) {
    var n = e.width || 0, o = e.height || 0;
    if (0 == n || 0 == o) {
        !0;
        var s = e.cloneNode(!0);
        s.style.visibility = "hidden", document.body.appendChild(s), n = s.width, o = s.height, document.body.removeChild(s)
    }
    n > t && o > i && (n / o <= t / i ? (e.style.width = t + "px", e.style.height = "auto") : (e.style.height = i + "px", e.style.width = "auto"))
}

var keypressNum_lead = 0, time1_lead = 0, time2_lead = 0;
!function () {
    var e, t, n, o, s = "browerV", r = "osV", a = function () {
            var e = window.navigator.userAgent.toLowerCase(), t = {};
            if (window.opera) t.opera = !0; else if (-1 != e.indexOf("msie")) {
                t.ie = !0;
                var i = /msie\s+(.)/.exec(e);
                i && (t["ie" + i[1]] = !0)
            } else -1 != e.indexOf("webkit") ? (t.webkit = !0, -1 != e.indexOf("chrome") ? t.chrome = !0 : -1 != e.indexOf("ipad") ? (t.ipad = !0, t.ios = !0) : -1 != e.indexOf("safari") && (t.safari = !0)) : -1 != e.indexOf("gecko") ? (t.gecko = !0, -1 != e.indexOf("firefox") && (t.firefox = !0)) : window.openDatabase && (t.safari = !0);
            return -1 != e.indexOf("se 2.x") && (t.se = !0), -1 != e.indexOf("360ee") ? t.s60ee = !0 : -1 != e.indexOf("360se") ? t.s60se = !0 : -1 != e.indexOf("aoyou") || -1 != e.indexOf("maxthon") ? t.aoyou = !0 : -1 != e.indexOf("theworld") ? t.world = !0 : -1 != e.indexOf("worldchrome") ? t.worldchrome = !0 : -1 != e.indexOf("greenbrowser") ? t.greenbrowser = !0 : -1 != e.indexOf("qqbrowser") ? t.qqbrowser = !0 : -1 != e.indexOf("baidu") || -1 != e.indexOf("bidu") ? t.baidu = !0 : -1 != e.indexOf("ucweb") && (t.ucweb = !0), t
        }(),
        u = (e = window.navigator.userAgent.toLowerCase(), t = {}, -1 != e.indexOf("windows") ? t.window = !0 : -1 != e.indexOf("mac") ? t.mac = !0 : -1 != e.indexOf("linux") ? t.linux = !0 : -1 != e.indexOf("x11") ? t.unix = !0 : -1 != e.indexOf("solaris") && (t.solaris = !0), e.match(/AppleWebKit.*Mobile.*/) || e.match(/AppleWebKit/) ? t.mobile = !0 : -1 != e.indexOf("ios") ? t.mobile = !0 : -1 != e.indexOf("ipad") ? t.ipad = !0 : -1 != e.indexOf("android") ? t.android = !0 : -1 != e.indexOf("iphone") && (t.iphone = !0), t);

    function g(e, t, i, n, o, s) {
        var r = new Date;
        r.setTime(r.getTime());
        var a = new Date(r.getTime() + i);
        document.cookie = e + "=" + t + (i ? "; expires=" + a.toGMTString() : "") + (n ? "; path=" + n : "") + (o ? "; domain=" + o : "") + (s ? "; secure" : "")
    }

    function l(e) {
        var t = document.cookie, i = e + "=", n = t.indexOf("; " + i);
        if (-1 == n) {
            if (0 != (n = t.indexOf(i))) return null
        } else n += 2;
        var o = document.cookie.indexOf(";", n);
        return -1 == o && (o = t.length), unescape(t.substring(n + i.length, o))
    }

    l(s), l(r), n = function (e) {
        if (e) {
            if (e.s60ee) return 6;
            if (e.s60se) return 7;
            if (e.aoyou) return 9;
            if (e.world) return 10;
            if (e.worldchrome) return 11;
            if (e.greenbrowser) return 12;
            if (e.qqbrowser) return 13;
            if (e.baidu) return 14;
            if (e.se) return 8;
            if (e.opera) return 4;
            if (e.chrome) return 3;
            if (e.safari) return 5;
            if (e.ie) return 1;
            if (e.firefox) return 2
        }
        return 0
    }(a), g(s, n, 94608e4, "/", "www.sogou.com", ""), o = function (e) {
        if (e) {
            if (e.mobile) return 6;
            if (e.android) return 7;
            if (e.iphone) return 8;
            if (e.ipad) return 9;
            if (e.window) return 1;
            if (e.linux) return 3;
            if (e.solaris) return 4;
            if (e.unix) return 5;
            if (e.mac) return 2
        }
        return 0
    }(u), g(r, o, 94608e4, "/", "www.sogou.com", "");
    var c = document.getElementsByTagName("input");
    for (var d in c) for (i = 0; i < c.length; i++) "query" == c[i].name && (c[i].onkeypress = function () {
        keypressNum_lead++, 0 == time1_lead && (time1_lead = (new Date).getTime()), time2_lead = (new Date).getTime()
    })
}();