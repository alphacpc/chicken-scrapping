/************************************************************ */
/***************** DECLARATION DES VARIABLES *************** */
/********************************************************** */
let tbody =  document.querySelector('.divTabItem tbody')
let btnAuchan = document.querySelector('.btn-auchan')
let btnBaayguins = document.querySelector('.btn-baayguins')
let btnGuinarshop = document.querySelector('.btn-guinarshop')
let btnAll = document.querySelector('.btn-all')
let trs = document.querySelectorAll('th.tri')
let inputLoad = document.querySelector('.divLoader input')
let btnLoad = document.querySelector('.divLoader button')
let divMessage = document.querySelector('.divMessage')




/************************************************************** */
/******** POUR GENERER DE TR EN FONCTION DES DONNES ********** */
/************************************************************ */
let generate_tr = (data) => {

    tbody.innerHTML = ''
    localStorage.setItem('data', JSON.stringify(data))

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

/************************************************************************* */
/************ LA FONCTION QUI RECUPERE TOUT LES PRODUITS **************** */
/*********************************************************************** */
let getter_data = async () =>{

    let response = await fetch('http://localhost:5000/api/data')
    let data = await response.json()

    generate_tr(data)

}


/************************************************************ */
/*************** AU CLICK FAIRE DES ACTIONS **************** */
/********************************************************** */
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


/************************************************************ */
/************** TRIER EN FONCTION DES COLONNES ************* */
/********************************************************** */
trs.forEach((tr) => {



    tr.addEventListener('click', (e) => {
        let data = JSON.parse(localStorage.getItem('data'))
        console.log(data)

        let balise = e.target
        let columnName = balise.getAttribute('column-name')
        let order = balise.getAttribute('order')

        if( order == 'desc'){
            balise.setAttribute('order', 'asc')
            data = data.sort( (a,b) => {
                return a[columnName] > b[columnName] ? 1 : -1
            })
        }else{
            balise.setAttribute('order', 'desc')

            data = data.sort( (a,b) => {
                return a[columnName] < b[columnName] ? 1 : -1
            })
        }

        generate_tr(data)

    })

})


/************************************************************ */
/****************** AFFICHER QUELQUES PRODUTS ************** */
/********************************************************** */
function show_error(message){
    let p = document.createElement('p')
        p.innerText = message
        divMessage.appendChild(p)
        divMessage.classList.add('show')

        setTimeout(() => {
            p.innerText = ''
            p.remove()
            divMessage.classList.remove('show')
        }, 3000);
}


btnLoad.addEventListener('click', () => {
    console.log("hello word")
    console.log("Valeur de input", inputLoad.value)
    let data = JSON.parse(localStorage.getItem('data'))


    if( inputLoad.value){
        let valeur = inputLoad.value


        if( valeur > data.length){
            show_error(`Veuillez donner un nombre compris entre 1 à ${data.length }`)
            inputLoad.value = ''
        }
        
        else{

            generate_tr( data.slice(0, valeur) )
            inputLoad.value = ''
        }
    
    }
    
    else{
        show_error('Veuillez entrer un nombre positif !')
    }
})



getter_data()