setTimeout(function() {
    var button = document.getElementById('edit-button');
    if (button) {
        button.style.display = 'none';
    }
    var butt = document.getElementById('delete-button');
    if (butt) {
        butt.style.display = 'none';
    }
}, 24 * 60 * 60 * 1000); 
