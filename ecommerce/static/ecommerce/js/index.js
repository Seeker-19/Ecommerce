var buton = document.getElementsByClassName("buton")[0];

buton.addEventListener("click", function () {
  document.getElementById("contain").style.display = "none";
  document.getElementsByClassName('inner-box')[0].style.display="block";
});

var div=document.getElementsByClassName('signup-header')[0];

div.addEventListener("click",function(){

    document.getElementById("contain").style.display = "flex";
    document.getElementsByClassName("inner-box")[0].style.display = "none";
})
