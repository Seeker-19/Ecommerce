console.log("working");

if (localStorage.getItem("cart") == null) {
  var cart = {};
} else {
  cart = JSON.parse(localStorage.getItem("cart"));
 // document.getElementById("cart").innerHTML = Object.keys(cart).length;
  
 updateCart(cart);
   
}

$(".divpr").on("click", "button.cart", function () {
  
  console.log("clicked");

  var idstr = this.id.toString();
  console.log(idstr);

  if (cart[idstr] != undefined) {
    qty = cart[idstr][0] + 1;
    cart[idstr][0] = cart[idstr][0] + 1;
    //name="My Item";
  } else {
    qty = 1;
    //name="My Item";
    na= document.getElementById("name" + idstr).innerHTML;
    price = document.getElementById("price" + idstr).innerHTML;
    cart[idstr] = [qty, na, parseInt(price)];
  }

  console.log(cart);
  updateCart(cart);
  document.location = "/shop";
});

function updateCart(cart) {
  var sum = 0;
  for (var item in cart) {
    //console.log(cart)
    // console.log(item)
    sum += cart[item][0];
    
  }
  localStorage.setItem("cart", JSON.stringify(cart));
  document.getElementById("cart").innerHTML = sum;
  
}

