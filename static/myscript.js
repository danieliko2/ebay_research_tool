$(document).ready(function(){ 
    console.log("mainscript up");

    document.getElementById("productSearchSubmit").addEventListener("click", function() {
        console.log("updating listen");
        document.getElementById("ip_list").style.display="block";
        document.getElementById("ip_scan_spinner").style.display="block";  
    });

});

