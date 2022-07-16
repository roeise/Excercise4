


function switchToNugette(){
    document.getElementById("blintchess").src="../static/blintchessChoc.jpg";
}

function switchTocheese(){
    document.getElementById("blintchess").src="../static/blintchessFruit.jpg";
}

function switchToCream(){
    document.getElementById("blintchess").src="../static/blintchessCream.jpg";
}


// Wait for entire page to load first.
window.onload = function () {
    //Get the current page path.
    var patharray = location.pathname.split("/");
    var foldername = patharray[1];
    // If on the root folder of the site, highlight the first link.
    if (foldername == "" || foldername == "Home_Page.html") {
        document.getElementById("home").className = "currentpage";
    } else {
        //Otherwise, loop through the links and put classname on
        // the one whose folder name matches foldername variable.
        var nav = document.getElementById("sidenav");                
        var links = nav.getElementsByTagName("a");
        for ( i = 1; i < links.length; i++ ){
            if (links[i].getAttribute("href").indexOf(foldername) > -1){
                links[i].className = "currentpage";
            }
        }
    }
}

function totalIt() {
    var input = document.getElementsByName("product");
    var total = 0;
    for (var i = 0; i < input.length; i++) {
      if (input[i].checked) {
        total += parseFloat(input[i].value);
      }
    }
    document.getElementsByName("total")[0].value = "₪" + total.toFixed(2);
  }