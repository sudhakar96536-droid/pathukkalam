/* ==========================================
   PATHUKKALAM PWA INSTALL / OPEN APP
========================================== */

(function () {

    let deferredPrompt = null;

    const isStandalone =
        window.matchMedia("(display-mode: standalone)").matches ||
        window.navigator.standalone === true;

    /*
       If already running as installed PWA,
       don't show any banner.
    */

    if (isStandalone) {
        return;
    }


    /* ==========================================
       PWA INSTALL PROMPT
    ========================================== */

    window.addEventListener(
        "beforeinstallprompt",
        function (event) {

            event.preventDefault();

            deferredPrompt = event;

            showPwaBanner("install");

        }
    );


    /* ==========================================
       AFTER APP IS INSTALLED
    ========================================== */

    window.addEventListener(
        "appinstalled",
        function () {

            deferredPrompt = null;

            removePwaBanner();

        }
    );


    /* ==========================================
       CREATE BANNER
    ========================================== */

    function showPwaBanner(type) {

        if (document.getElementById("pathukkalamPwaBanner")) {
            return;
        }


        const banner =
            document.createElement("div");

        banner.id =
            "pathukkalamPwaBanner";


        banner.innerHTML = `

            <div class="pwa-banner-icon">
                <img
                    src="/static/icon-192.png"
                    alt="Pathukkalam">
            </div>

            <div class="pwa-banner-content">

                <div class="pwa-banner-title">
                    Pathukkalam App
                </div>

                <div class="pwa-banner-text">
                    ${type === "install"
                        ? "Install for a faster app-like experience"
                        : "Open Pathukkalam in the app"}
                </div>

            </div>

            <div class="pwa-banner-actions">

                ${
                    type === "install"

                    ?

                    `
                    <button
                        id="pwaInstallBtn"
                        class="pwa-primary-btn">
                        Install App
                    </button>
                    `

                    :

                    `
                    <button
                        id="pwaOpenBtn"
                        class="pwa-primary-btn">
                        Continue with App
                    </button>

                    <button
                        id="pwaBrowserBtn"
                        class="pwa-secondary-btn">
                        Browser
                    </button>
                    `
                }

                <button
                    id="pwaCloseBtn"
                    class="pwa-close-btn"
                    aria-label="Close">
                    ×
                </button>

            </div>

        `;


        document.body.prepend(banner);


        /*
           Close
        */

        document
            .getElementById("pwaCloseBtn")
            .addEventListener(
                "click",
                removePwaBanner
            );


        /*
           Install
        */

        const installButton =
            document.getElementById(
                "pwaInstallBtn"
            );


        if (installButton) {

            installButton.addEventListener(
                "click",
                async function () {

                    if (!deferredPrompt) {
                        return;
                    }


                    deferredPrompt.prompt();


                    const result =
                        await deferredPrompt.userChoice;


                    console.log(
                        "PWA install result:",
                        result.outcome
                    );


                    deferredPrompt = null;

                    removePwaBanner();

                }
            );

        }


        /*
           Continue with App
        */

        const openButton =
            document.getElementById(
                "pwaOpenBtn"
            );


        if (openButton) {

            openButton.addEventListener(
                "click",
                function () {

                    /*
                       Opening the same PWA start URL.
                       Supported browsers may hand this
                       to the installed PWA.
                    */

                    window.location.href =
                        "https://pathukkalam.in/";

                }
            );

        }


        /*
           Continue with Browser
        */

        const browserButton =
            document.getElementById(
                "pwaBrowserBtn"
            );


        if (browserButton) {

            browserButton.addEventListener(
                "click",
                removePwaBanner
            );

        }

    }


    /* ==========================================
       REMOVE BANNER
    ========================================== */

    function removePwaBanner() {

        const banner =
            document.getElementById(
                "pathukkalamPwaBanner"
            );


        if (banner) {

            banner.remove();

        }

    }


    /* ==========================================
       BANNER CSS
    ========================================== */

    const style =
        document.createElement("style");


    style.innerHTML = `

        #pathukkalamPwaBanner {

            position:fixed;

            top:10px;
            left:50%;

            transform:translateX(-50%);

            width:calc(100% - 20px);

            max-width:650px;

            background:white;

            border-radius:16px;

            padding:12px;

            display:flex;

            align-items:center;

            gap:12px;

            box-shadow:
                0 5px 25px
                rgba(0,0,0,0.18);

            z-index:99999;

            border:1px solid #eee;

        }


        .pwa-banner-icon {

            flex-shrink:0;

        }


        .pwa-banner-icon img {

            width:48px;
            height:48px;

            border-radius:12px;

            object-fit:cover;

        }


        .pwa-banner-content {

            flex:1;

            min-width:0;

        }


        .pwa-banner-title {

            font-size:15px;

            font-weight:bold;

            color:#222;

        }


        .pwa-banner-text {

            margin-top:3px;

            font-size:12px;

            color:#777;

        }


        .pwa-banner-actions {

            display:flex;

            align-items:center;

            gap:6px;

        }


        .pwa-primary-btn {

            border:none;

            background:#1877f2;

            color:white;

            padding:9px 13px;

            border-radius:9px;

            font-size:13px;

            font-weight:bold;

            cursor:pointer;

            white-space:nowrap;

        }


        .pwa-secondary-btn {

            border:none;

            background:#f0f2f5;

            color:#333;

            padding:9px 11px;

            border-radius:9px;

            font-size:13px;

            cursor:pointer;

            white-space:nowrap;

        }


        .pwa-close-btn {

            width:28px;
            height:28px;

            border:none;

            border-radius:50%;

            background:#f0f2f5;

            color:#555;

            font-size:20px;

            line-height:20px;

            cursor:pointer;

        }


        @media(max-width:600px) {

            #pathukkalamPwaBanner {

                top:8px;

                width:calc(100% - 16px);

                padding:10px;

                gap:9px;

            }


            .pwa-banner-icon img {

                width:42px;
                height:42px;

            }


            .pwa-banner-title {

                font-size:14px;

            }


            .pwa-banner-text {

                font-size:11px;

            }


            .pwa-primary-btn {

                padding:8px 10px;

                font-size:12px;

            }


            .pwa-secondary-btn {

                padding:8px 9px;

                font-size:12px;

            }

        }

    `;


    document.head.appendChild(style);

})();
