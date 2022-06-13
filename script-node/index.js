const puppeteer = require("puppeteer")
const csv = require("csv-writer")


// FONCTION POUR LA CREATION DU FICHIER CSV
function create_csv(data){
    let createCsvWriter = csv.createObjectCsvWriter
    let csvWriter = createCsvWriter({
        path : "../data/data-guinarshop.csv",
        header : [
            {id: 'nom', title: 'nom'},
            {id: 'prix', title: 'prix'},
            {id: 'poids', title: 'poids'},
            {id: 'image', title: 'image'},
            {id: 'site', title: 'site'},
        ]
    })

    csvWriter.writeRecords(data)
    .then( () => console.log("Fichier créé avec succès ! "))
}


// LA FONCTION POUR RECUPER LES DONNEES
async function getData(){
    
    const browser = await puppeteer.launch({headless:true})
    const page    = await browser.newPage()
    await page.goto("https://guinarshop.com/shop/")
    
    let data =  await page.evaluate( () => {  
        let results = []
        let ulItems =  document.querySelector('ul.products.columns-4')
        let items =  ulItems.querySelectorAll('li')

        items.forEach((item) => {

            let tabword = item.querySelector('h2').innerText.split(' ')
            
            results.push({
                'nom' : item.querySelector('h2').innerText,
                'prix' : item.querySelector('.woocommerce-Price-amount.amount bdi').innerText,
                'poids' : tabword[tabword.length -1 ].includes('kg') ? tabword[tabword.length -1 ] : null,
                'image': item.querySelector('img').src,
                'site' : window.location.hostname
            })

        })

        return results
    })

    console.log(data)
    create_csv(data)
    
    browser.close()
}

getData()