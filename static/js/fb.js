window.fbAsyncInit = function () {
  FB.init({
    appId: '2486509434954225',
    cookie: true,
    xfbml: true,
    version: 'v3.3'
  });
  FB.AppEvents.logPageView();
};

(function (d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) { return; }
  js = d.createElement(s); js.id = id;
  js.src = "https://connect.facebook.net/en_US/sdk.js";
  fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));


//3. Check Login Status
FB.getLoginStatus(function (response) {
  statusChangeCallback(response);
});


//4.Esta es la devolución de llamada. Llama a FB.getLoginStatus()
function checkLoginState() {
  FB.getLoginStatus(function (response) {
    statusChangeCallback(response);
  });
}

