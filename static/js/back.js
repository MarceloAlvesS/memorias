const extra = document.getElementById('extra')
location.reload()
extra.addEventListener('click', function(e) {
    if (e.target == this){
        history.back()
    }
})