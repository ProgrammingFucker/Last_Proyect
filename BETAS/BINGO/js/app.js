
var rango = _.range(1,90);
rango = _.shuffle(rango);
const cartonJugador = rango.slice(0, 100);

rango = _.shuffle(rango);
const cartonCpu = rango.slice(0, 100);

function crearCartonHTML(selector,array)
{ 
let parent = document.querySelector(`.${selector}`)

for(e of array)
{
let divcarton = document.createElement('div');
divcarton.className = 'numero n'+e;
divcarton.textContent = e;
parent.appendChild(divcarton);
}
}

crearCartonHTML('cartonJugador',cartonJugador);
crearCartonHTML('cartonCpu',cartonCpu);

function contarTachado()
{
let totalJugador = document.querySelectorAll('.cartonJugador .tachado').length;
let totalCpu = document.querySelectorAll('.cartonCpu .tachado').length;

if(totalJugador==90)
alert('FELICIDADES CARTON JUGADOR COMPLETADO');
if(totalCpu==90)
alert('FELICIDADES CARTON CPU COMPLETADO');

console.log(totalJugador + ' - ' + totalCpu);
}

function sacarBola()
{

let bola = Math.floor(Math.random() * rango.length);
  bola = rango[bola];



console.log(rango);

let divbola = document.querySelector('#bola');
  divbola.textContent = bola;
let numero = document.querySelectorAll(`.n${bola}`);
for (var i = 0; i < numero.length; ++i) {
 numero[i].classList.add('tachado');
}
}
