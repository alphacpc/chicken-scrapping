let tbody =  document.querySelector('.divTabItem tbody')
let btnAuchan = document.querySelector('.btn-auchan')
let btnBaayguins = document.querySelector('.btn-baayguins')
let btnGuinarshop = document.querySelector('.btn-guinarshop')
let btnAll = document.querySelector('.btn-all')

let generate_tr = (data) => {

    tbody.innerHTML = ''

    for(let product of data){
        let tr = document.createElement('tr')
        
        let td_image = document.createElement('td')
        let img = document.createElement('img')
        td_image.setAttribute('class', 'trImg')
        img.setAttribute('src', `${product.image}`)
        img.setAttribute('alt', `${product.nom}`)
        td_image.appendChild(img)

        let td_title = document.createElement('td')
        if( product['nom'].length > 25){
            product.nom =  product['nom'].slice(0,25) + '...'
        }
        td_title.innerText = product.nom

        let td_price = document.createElement('td')
        let strong = document.createElement('strong')
        strong.innerText = product.prix
        td_price.appendChild(strong)

        let td_poids = document.createElement('td')
        td_poids.innerText = product.poids
        let td_origine = document.createElement('td')

        td_origine.innerText = product.origine

        tr.appendChild(td_image)
        tr.appendChild(td_title)
        tr.appendChild(td_price)
        tr.appendChild(td_poids)
        tr.appendChild(td_origine)
        tbody.appendChild(tr)
    }

}

let getter_data = async () =>{

    let response = await fetch('http://localhost:5000/api/data')
    let data = await response.json()

    generate_tr(data)

}

btnAuchan.addEventListener('click', async() => {

    let response = await fetch('/api/data/auchan',)
    let data = await response.json()

    generate_tr(data)
})


btnBaayguins.addEventListener('click', async() => {

    let response = await fetch('/api/data/baayguins',)
    let data = await response.json()

    generate_tr(data)
})


btnGuinarshop.addEventListener('click', async() => {

    let response = await fetch('/api/data/guinarshop',)
    let data = await response.json()

    generate_tr(data)
})


btnAll.addEventListener('click', async() => {

    let response = await fetch('/api/data',)
    let data = await response.json()

    generate_tr(data)
})


getter_data()