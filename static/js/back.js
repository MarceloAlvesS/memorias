const extra = document.getElementById('extra')
extra.style.cursor = 'pointer'
extra.addEventListener('click', function(e) {
    if (e.target == this){
        history.back()
    }
})