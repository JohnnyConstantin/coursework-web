window.onload = function () {

    document.querySelector('#type_phones').onclick = function() {
       if ( this.checked ) {
           console.log("phone checked");
            document.querySelector('.type .fa-phone').onclick = function() {
                this.setAttribute("style", "font-size: 35px")
            }
        } else {
           document.querySelector('.type .fa-phone').onclick = function() {
                this.setAttribute("style", "border-radius: 40px; font-size: 30px; background-color: chocolate;")
           }
        }
    }

    document.querySelector('#type_laptops').onclick = function() {
        // access properties using this keyword
        if ( this.checked ) {
            document.querySelector('.type .fa-laptop').onclick = function() {
                this.setAttribute("style", "font-size: 35px")
            }
        } else {
        document.querySelector('.type .fa-laptop').onclick = function() {
                this.setAttribute("style", "border-radius: 40px; font-size: 30px; background-color: chocolate;")
             console.log("laptop checked")
            }
        }
    }
}