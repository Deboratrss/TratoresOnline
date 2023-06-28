
function createCardElement(cardObj) {
    const imagemTrator = document.createElement('img')
    imagemTrator.setAttribute('src', cardObj.imagem)
    imagemTrator.setAttribute('alt', cardObj.title)

    const cardTitulo = document.createElement('h4')
    cardTitulo.innerText = cardObj.titulo

    const cardDescricao = document.createElement('p')
    cardDescricao.setAttribute('class', 'descricao')
    cardDescricao.innerText = cardObj.descricao

    const cardPreco = document.createElement('p')
    cardPreco.innerText = cardObj.preco

    const comprarAnchor = document.createElement('a')
    comprarAnchor.innerText = 'Comprar'
    comprarAnchor.setAttribute('href', `formulario.html?id=${cardObj.id}`)

    const container = document.createElement('div')
    container.setAttribute('class', 'card')
    container.appendChild(imagemTrator)
    container.appendChild(cardTitulo)
    container.appendChild(cardDescricao)
    container.appendChild(cardPreco)
    container.appendChild(comprarAnchor)

    return container
}

let scrollS = 1
let scrollsLimit = 0;

function mexerSlider(d) {
    if(d === 'direita') {
        aplicarMexida(scrollS * 500)
        if(scrollS < scrollsLimit - 1) {
            scrollS++
        }
    } else {
        if(scrollS > 0) {
            scrollS--
        }
        aplicarMexida(scrollS * 500)
    }
}

function aplicarMexida(position) {
    const slider = document.getElementById('produtos')
    slider.scrollTo(position, 0)
}

function formatTrator(trator) {
    return {
        titulo: trator['Item'],
        descricao: trator['Descricao'],
        preco: trator['Preço unitário']
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const img = 'https://static5.depositphotos.com/1001587/440/i/450/depositphotos_4402644-stock-photo-yellow-tractor.jpg'
    const descricao = `
        Apresentamos nosso trator verde,
        uma máquina potente e versátil, com
        um design moderno e resistente, possui
        motor eficiente, transmissão suave
        e estrutura durável. Proporcionando
        assim um desempenho excepcional e eficiência
    `

    fetch('http://localhost:8000/tratores', { method: 'GET' })
    .then(response => response.json()).then(
        response => {
            console.log(response)
            for(let trator in response) {
                scrollsLimit++

                const card = createCardElement({
                    id: trator,
                    imagem: img,
                    ...formatTrator(response[trator])
                })
                
                document.getElementById('produtos').appendChild(card)
            }
        }
    )
})
