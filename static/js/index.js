window.onload = function () {

    document.querySelector("#submit_button").onclick = function () {
        document.querySelector("#searching").innerHTML = "Идет поиск...";
    }


    // document.querySelector("#cheapest").onclick = function () {
    //     var paras = document.getElementsByClassName('item');
    //     console.log("here");
    //             for (var i = 0; i < paras.length; i++) {
    //                 console.log("got item");
    //               paras[i].setAttribute("style", "display:none")
    //             }
    // }
}