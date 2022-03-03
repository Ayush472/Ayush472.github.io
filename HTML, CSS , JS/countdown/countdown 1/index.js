console.log('Js Loaded');
var countdownElement = document.getElementById('countdown');
var backImgElement =document.getElementById('bg-img');


var initialCountdownval = countdownElement.innerHTML;

setInterval(function () {
    initialCountdownval =initialCountdownval > 0 ? initialCountdownval-1:0;

    countdownElement.innerHTML = initialCountdownval;
    var backImgPath =initialCountdownval %2 === 0 ? 'img/12c4897507a99bf3586852606ecece52.jpg':'img/hand-painted-watercolor-pastel-sky-background_23-2148902771.jpg'  
    backImgElement.src = backImgPath;
    
    backImgElement.className='BackImage';
    console.log(backImgElement);
},1000)

