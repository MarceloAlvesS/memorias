const extra = document.getElementById('extra')
extra.addEventListener('click', function(e) {
    if (e.target == this){
        history.back()
    }
})