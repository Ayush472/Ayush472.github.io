console.log('Js Loaded');
var countdownElement = document.getElementById('countdown');
var backImgElement =document.getElementById('bg-img');


var initialCountdownval = countdownElement.innerHTML;

setInterval(function () {
    initialCountdownval =initialCountdownval > 0 ? initialCountdownval-1:0;

    countdownElement.innerHTML = initialCountdownval;
       
    countdownElement.style.fontSize =   initialCountdownval*100 +"px"
    backImgElement.style.width = initialCountdownval * 10 + "%"
    console.log(initialCountdownval * 100 +"px")
    if (initialCountdownval <= 0) {
        clearInterval(interval);    
    }
    
},1000)