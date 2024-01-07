const data = document.currentScript.dataset
const fotos_escolhidas = data.fotos_escolhidas.split(' ')
const ids_escolhidos = data.ids_escolhidos.split(' ')
const celulas = document.getElementsByClassName('coracao')
const quantidade_fotos = fotos_escolhidas.length

for (let i = 0; i < quantidade_fotos; i++) {
    celulas[i].innerHTML = `<a href="${ids_escolhidos[i]}"><img src="/static/images/${fotos_escolhidas[i]}" alt="${ids_escolhidos[i]}"></a>`
}
