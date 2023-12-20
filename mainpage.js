import pokemon from 'pokemontcgsdk'
import { TOKEN } from './config.js'

pokemon.configure({apiKey: TOKEN})

// constants
pokemon.card.where({ supertype: 'Pokémon', pageSize: 1 })
    .then(result => {
        console.log(result.count) // 10000
    })

// examples
// Cards
// Get a single card by ID
pokemon.card.find('base1-4')
.then(card => {
    console.log(card.name) // "Charizard"
})
// Filter cards via the q parameter
pokemon.card.where({ q: 'name:blastoise' })
.then(result => {
    console.log(result.data[0].name) // "Blastoise"
})
// Filter cards via the q parameter and specific page
pokemon.card.where({ q: 'name:blastoise', pageSize: 10, page: 3 })
.then(result => {
    console.log(result.data[0].name) // "Blastoise"
})
// Automatically page through card data
pokemon.card.all({ q: 'name:blastoise' })
    .then((cards) => {
        console.log(cards[0].name) // "Blastoise"
    })

// Using the `all` function, pagination happens automatically, and the result will simply contain the data and no pagination info.

// Sets
// Get a single set by ID
pokemon.set.find('base1')
.then(set => {
    console.log(set.name) // "Base"
})
// Filter sets via the q 
parameterhere({ q: 'series:base' })
.then(result => {
    console.log(result.data[0].name) // "Base"
})
// Filter cards via the q parameter and specific page
pokemon.set.where({ q: 'series:base', pageSize: 1, page: 1 })
.then(result => {
    console.log(result.data[0].name) // "Base"
})
// Automatically page through card data
pokemon.set.all({ q: 'series:base' })
    .then((cards) => {
        console.log(cards[0].name) // "Base"
    })

// Using the `all` function, pagination happens automatically, and the result will simply contain the data and no pagination info.

// Supertypes
pokemon.supertype.all()
// Subtypes
pokemon.subtype.all()
// types
pokemon.type.all()
// Rarity
pokemon.rarity.all()