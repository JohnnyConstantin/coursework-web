document.getElementById('laptop').onclick = function() {
    // access properties using this keyword
    if ( this.checked ) {
        // Returns true if checked
        alert( this.value );
    } else {
        // Returns false if not checked
    }
};