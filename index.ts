import fetch from "node-fetch";
import jsdom from "jsdom";
const { JSDOM } = jsdom;

(async () => {
    const res = await fetch("http://example.com");
    const body = await res.text(); // HTMLをテキストで取得
    const dom = new JSDOM(body); // パース
    const h1Text = dom.window.document.querySelector("h1")?.textContent; // JavaScriptと同じ書き方ができます。
    if(h1Text){
        console.log(h1Text); // Example Domain


    }
})();