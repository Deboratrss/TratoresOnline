
function salvarDados(event) {
    event.preventDefault()
    let forme = document.getElementById('forme')
    const params = new URLSearchParams(window.location.search)
    const id = params.get('id')
    
    const nome = forme.nome.value
    const telefone = forme.telefone.value
    const endereco = forme.endereco.value
    const email = forme.email.value

    const body = {
        nome,
        telefone,
        endereco,
        email
    }

    fetch('http://localhost:8000/informacoes_pessoais', {
        method: 'POST',
        headers: {
            'Content-type': 'application/json'
        },
        body: JSON.stringify(body)
    }).then(r => {
        if(r.status === 200) window.location.href = `pagamentos.html?id=${id}`
    })
}

document.addEventListener('DOMContentLoaded', () => {
    // pega o parametro da url
    const params = new URLSearchParams(window.location.search)
    const id = params.get('id')

    /*
        1 -> requisita os dados
        2 -> cria o elemento
        3 -> adiciona o elemento na tela
    */
  
    fetch(`http://localhost:8000/vendas/${id}`,{method: 'GET' })
    .then(response => response.json()).then(
        response => {
         console.log(response)
            const produto = document.getElementById('produto')
            produto.innerHTML = `
                <p>${response['Item']}</p>
                <p>${response['Preço unitário']}</p>
            `
        }
    )


    let forme = document.getElementById('forme')
    forme.addEventListener('submit', salvarDados)

})
