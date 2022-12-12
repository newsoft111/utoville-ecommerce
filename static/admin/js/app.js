! function() {
    "use strict";
    var e, t, a = localStorage.getItem("language"),
        n = "eng";

    function o(t) {
        document.getElementById("header-lang-img") && ("eng" == t ? document.getElementById("header-lang-img").src = "/static/images/flags/us.jpg" : "sp" == t ? document.getElementById("header-lang-img").src = "/static/images/flags/spain.jpg" : "gr" == t ? document.getElementById("header-lang-img").src = "/static/images/flags/germany.jpg" : "it" == t ? document.getElementById("header-lang-img").src = "/static/images/flags/italy.jpg" : "ru" == t && (document.getElementById("header-lang-img").src = "/static/images/flags/russia.jpg"), localStorage.setItem("language", t), a = localStorage.getItem("language"), function() {
            null == a && o(n);
            var t = new XMLHttpRequest;
            t.open("GET", "/static/lang/" + a + ".json"), t.onreadystatechange = function() {
                var a;
                4 === this.readyState && 200 === this.status && (a = JSON.parse(this.responseText), Object.keys(a).forEach(function(e) {
                    document.querySelectorAll("[data-key='" + e + "']").forEach(function(t) {
                        t.textContent = a[e]
                    })
                }))
            }, t.send()
        }())
    }

    function s() {
        var t = document.querySelectorAll(".counter-value");
        t && t.forEach(function(o) {
            ! function t() {
                var e = +o.getAttribute("data-target"),
                    a = +o.innerText,
                    n = e / 250;
                n < 1 && (n = 1), a < e ? (o.innerText = (a + n).toFixed(0), setTimeout(t, 1)) : o.innerText = e
            }()
        })
    }

    function i() {
        setTimeout(function() {
            var t, e, a = document.getElementById("side-menu");
            a && (a = a.querySelector(".mm-active .active"), 300 < (t = a ? a.offsetTop : 0) && (t -= 100, (e = document.getElementsByClassName("vertical-menu") ? document.getElementsByClassName("vertical-menu")[0] : "") && e.querySelector(".simplebar-content-wrapper") && setTimeout(function() {
                e.querySelector(".simplebar-content-wrapper").scrollTop = t
            }, 0)))
        }, 0)
    }

    function l() {
        for (var t = document.getElementById("topnav-menu-content").getElementsByTagName("a"), e = 0, a = t.length; e < a; e++) "nav-item dropdown active" === t[e].parentElement.getAttribute("class") && (t[e].parentElement.classList.remove("active"), t[e].nextElementSibling.classList.remove("show"))
    }

    function r(t) {
        var e = document.getElementById(t);
        e.style.display = "block";
        var a = setInterval(function() {
            e.style.opacity || (e.style.opacity = 1), 0 < e.style.opacity ? e.style.opacity -= .2 : (clearInterval(a), e.style.display = "none")
        }, 200)
    }

    function d() {
        var t, e;
        feather.replace(), window.sessionStorage && ((e = sessionStorage.getItem("is_visited")) ? null !== (t = document.querySelector("#" + e)) && (t.checked = !0, e = e, 1 == document.getElementById("layout-direction-ltr").checked && "layout-direction-ltr" === e ? (document.getElementsByTagName("html")[0].removeAttribute("dir"), document.getElementById("layout-direction-rtl").checked = !1, document.getElementById("bootstrap-style").setAttribute("href", "/static/css/bootstrap.min.css"), document.getElementById("app-style").setAttribute("href", "/static/css/app.min.css"), sessionStorage.setItem("is_visited", "layout-direction-ltr")) : 1 == document.getElementById("layout-direction-rtl").checked && "layout-direction-rtl" === e && (document.getElementById("layout-direction-ltr").checked = !1, document.getElementById("bootstrap-style").setAttribute("href", "/static/css/bootstrap-rtl.min.css"), document.getElementById("app-style").setAttribute("href", "/static/css/app-rtl.min.css"), document.getElementsByTagName("html")[0].setAttribute("dir", "rtl"), sessionStorage.setItem("is_visited", "layout-direction-rtl"))) : sessionStorage.setItem("is_visited", "layout-direction-ltr"))
    }

    function c(t) {
        document.getElementById(t) && (document.getElementById(t).checked = !0)
    }

    function u() {
        document.webkitIsFullScreen || document.mozFullScreen || document.msFullscreenElement || document.body.classList.remove("fullscreen-enable")
    }! function() {
        let t = document.querySelectorAll("#username, #username1, #email,#email1, #password, #password1, #password2,#password3, #password4, #password5, #password6 ,#password7");
        t.forEach(t => {
            t.addEventListener("keypress", function(t) {
                if (" " == t.key) return t.preventDefault(), !1
            })
        })
    }(), window.onload = function() {
            document.getElementById("preloader") && (r("pre-status"), r("preloader"))
        }, d(), document.addEventListener("DOMContentLoaded", function(t) {
            document.getElementById("side-menu") && new MetisMenu("#side-menu")
        }), s(),
        function() {
            var e = document.body.getAttribute("data-sidebar-size");
            /*window.onload = function() {
                1024 <= window.innerWidth && window.innerWidth <= 1366 && (document.body.setAttribute("data-sidebar-size", "sm"), c("sidebar-size-small"))
            };
            for (var t, a = document.getElementsByClassName("vertical-menu-btn"), n = 0; n < a.length; n++) a[t = n] && a[t].addEventListener("click", function(t) {
                t.preventDefault(), document.body.classList.toggle("sidebar-enable"), 992 <= window.innerWidth ? null == e ? null == document.body.getAttribute("data-sidebar-size") || "lg" == document.body.getAttribute("data-sidebar-size") ? document.body.setAttribute("data-sidebar-size", "sm") : document.body.setAttribute("data-sidebar-size", "lg") : "md" == e ? "md" == document.body.getAttribute("data-sidebar-size") ? document.body.setAttribute("data-sidebar-size", "sm") : document.body.setAttribute("data-sidebar-size", "md") : "sm" == document.body.getAttribute("data-sidebar-size") ? document.body.setAttribute("data-sidebar-size", "lg") : document.body.setAttribute("data-sidebar-size", "sm") : i()
            });*/
        }(), setTimeout(function() {
            var t = document.querySelectorAll("#sidebar-menu a");
            t && t.forEach(function(t) {
                var e = window.location.href.split(/[?#]/)[0];
                t.href == e && (t.classList.add("active"), (t = t.parentElement) && "side-menu" !== t.id && (t.classList.add("mm-active"), (t = t.parentElement) && "side-menu" !== t.id && (t.classList.add("mm-show"), t.classList.contains("mm-collapsing") && console.log("has mm-collapsing"), (t = t.parentElement) && "side-menu" !== t.id && (t.classList.add("mm-active"), (t = t.parentElement) && "side-menu" !== t.id && (t.classList.add("mm-show"), (t = t.parentElement) && "side-menu" !== t.id && t.classList.add("mm-active"))))))
            })
        }, 0), (t = document.querySelectorAll(".navbar-nav a")) && t.forEach(function(t) {
            var e = window.location.href.split(/[?#]/)[0];
            t.href == e && (t.classList.add("active"), (t = t.parentElement) && (t.classList.add("active"), (t = t.parentElement).classList.add("active"), (t = t.parentElement) && (t.classList.add("active"), (t = t.parentElement) && (t.classList.add("active"), (t = t.parentElement) && (t.classList.add("active"), (t = t.parentElement) && t.classList.add("active"))))))
        }), (t = document.querySelector('[data-toggle="fullscreen"]')) && t.addEventListener("click", function(t) {
            t.preventDefault(), document.body.classList.toggle("fullscreen-enable"), document.fullscreenElement || document.mozFullScreenElement || document.webkitFullscreenElement ? document.cancelFullScreen ? document.cancelFullScreen() : document.mozCancelFullScreen ? document.mozCancelFullScreen() : document.webkitCancelFullScreen && document.webkitCancelFullScreen() : document.documentElement.requestFullscreen ? document.documentElement.requestFullscreen() : document.documentElement.mozRequestFullScreen ? document.documentElement.mozRequestFullScreen() : document.documentElement.webkitRequestFullscreen && document.documentElement.webkitRequestFullscreen(Element.ALLOW_KEYBOARD_INPUT)
        }), document.addEventListener("fullscreenchange", u), document.addEventListener("webkitfullscreenchange", u), document.addEventListener("mozfullscreenchange", u),
        function() {
            if (document.getElementById("topnav-menu-content")) {
                for (var t = document.getElementById("topnav-menu-content").getElementsByTagName("a"), e = 0, a = t.length; e < a; e++) t[e].onclick = function(t) {
                    "#" === t.target.getAttribute("href") && (t.target.parentElement.classList.toggle("active"), t.target.nextElementSibling.classList.toggle("show"))
                };
                window.addEventListener("resize", l)
            }
        }(), [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]')).map(function(t) {
            return new bootstrap.Tooltip(t)
        }), [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]')).map(function(t) {
            return new bootstrap.Popover(t)
        }), [].slice.call(document.querySelectorAll(".toast")).map(function(t) {
            return new bootstrap.Toast(t)
        }),
        function() {
            "null" != a && a !== n && o(a);
            var t = document.getElementsByClassName("language");
            t && t.forEach(function(e) {
                e.addEventListener("click", function(t) {
                    o(e.getAttribute("data-lang"))
                })
            })
        }(), e = document.body, document.getElementById("right-bar-toggle") && (document.getElementById("right-bar-toggle").addEventListener("click", function(t) {
            e.classList.toggle("right-bar-enabled")
        }), e.addEventListener("click", function(t) {
            !t.target.parentElement.classList.contains("right-bar-toggle-close") && t.target.closest(".right-bar-toggle, .right-bar") || document.body.classList.remove("right-bar-enabled")
        }), (e = document.getElementsByTagName("body")[0]).hasAttribute("data-layout") && "horizontal" == e.getAttribute("data-layout") ? (c("layout-horizontal"), document.getElementById("sidebar-setting").style.display = "none") : c("layout-vertical"), e.hasAttribute("data-layout-mode") && "dark" == e.getAttribute("data-layout-mode") ? c("layout-mode-dark") : c("layout-mode-light"), e.hasAttribute("data-layout-size") && "boxed" == e.getAttribute("data-layout-size") ? c("layout-width-boxed") : c("layout-width-fluid"), e.hasAttribute("data-layout-scrollable") && "true" == e.getAttribute("data-layout-scrollable") ? c("layout-position-scrollable") : c("layout-position-fixed"), e.hasAttribute("data-topbar") && "dark" == e.getAttribute("data-topbar") ? c("topbar-color-dark") : c("topbar-color-light"), e.hasAttribute("data-sidebar-size") && "sm" == e.getAttribute("data-sidebar-size") ? c("sidebar-size-small") : e.hasAttribute("data-sidebar-size") && "md" == e.getAttribute("data-sidebar-size") ? c("sidebar-size-compact") : c("sidebar-size-default"), e.hasAttribute("data-sidebar") && "brand" == e.getAttribute("data-sidebar") ? c("sidebar-color-brand") : e.hasAttribute("data-sidebar") && "dark" == e.getAttribute("data-sidebar") ? c("sidebar-color-dark") : c("sidebar-color-light"), document.getElementsByTagName("html")[0].hasAttribute("dir") && "rtl" == document.getElementsByTagName("html")[0].getAttribute("dir") ? c("layout-direction-rtl") : c("layout-direction-ltr"), document.querySelectorAll("input[name='layout'").forEach(function(t) {
            t.addEventListener("change", function(t) {
                t && t.target && t.target.value && (window.location.href = "vertical" == t.target.value ? "../" : "/layouts/horizontal")
            })
        }), document.querySelectorAll("input[name='layout-mode']").forEach(function(t) {
            t.addEventListener("change", function(t) {
                t && t.target && t.target.value && ("light" == t.target.value ? (document.body.setAttribute("data-layout-mode", "light"), document.body.setAttribute("data-topbar", "light"), document.body.setAttribute("data-sidebar", "light"), e.hasAttribute("data-layout") && "horizontal" == e.getAttribute("data-layout") || document.body.setAttribute("data-sidebar", "light"), c("topbar-color-light"), c("sidebar-color-light")) : (document.body.setAttribute("data-layout-mode", "dark"), document.body.setAttribute("data-topbar", "dark"), document.body.setAttribute("data-sidebar", "dark"), e.hasAttribute("data-layout") && "horizontal" == e.getAttribute("data-layout") || document.body.setAttribute("data-sidebar", "dark"), c("topbar-color-dark"), c("sidebar-color-dark")))
            })
        }), document.querySelectorAll("input[name='layout-direction']").forEach(function(t) {
            t.addEventListener("change", function(t) {
                t && t.target && t.target.value && ("ltr" == t.target.value ? (document.getElementsByTagName("html")[0].removeAttribute("dir"), document.getElementById("bootstrap-style").setAttribute("href", "/static/css/bootstrap.min.css"), document.getElementById("app-style").setAttribute("href", "/static/css/app.min.css"), sessionStorage.setItem("is_visited", "layout-direction-ltr")) : (document.getElementById("bootstrap-style").setAttribute("href", "/static/css/bootstrap-rtl.min.css"), document.getElementById("app-style").setAttribute("href", "/static/css/app-rtl.min.css"), document.getElementsByTagName("html")[0].setAttribute("dir", "rtl"), sessionStorage.setItem("is_visited", "layout-direction-rtl")))
            })
        })), i()
}();