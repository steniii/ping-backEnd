// Exercice 1 :
// Déclarez une variable isDone et initialisez-la avec une valeur booléenne de votre choix.
// Affichez
// cette valeur dans la console.

let isDone : boolean = true
console.log(isDone)

// Exercice 2 :
// Déclarez une variable greeting et initialisez-la avec une chaîne de caractères de votre
// choix.
// Affichez cette chaîne dans la console.

let greeting : string = "Hello"
console.log(greeting)

// Exercice 3 :
// Déclarez une variable numbers et initialisez-la avec un tableau contenant les nombres
// de 1 à 5.
// Utilisez une boucle pour afficher chaque élément du tableau.

let nombres : number[]  = [1,2,3,4,5]
for (let i=0; i<nombres.length;i++ )
    console.log(nombres[i])

// Exercice 4 :
// Déclarez une variable person et initialisez-la avec un objet contenant les propriétés
// firstName
// et lastName de type chaîne de caractères. Affichez les valeurs de ces propriétés dans la
// console.

let person : {firstName: string, lastName: string}
person = {firstName:"Sten",lastName:"Mgz"}

console.log(person.firstName + " " + person.lastName)

// Exercice 5:
// Déclarez une variable status avec un type union pouvant être soit une chaîne de
// caractères
// "success", soit "error", soit "loading". Initialisez cette variable avec l'une de ces valeurs
// et
// affichez-la dans la console.

let statut : "success" | "error" | "loading"
statut = "success"
console.log(statut)