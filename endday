//Written by Stuart Anderson
//This script is for Foundry VTT, written in JavaScript
//This program requires the GM to setup group tokens and create flags to store variables to disk
//You can see I have example actor data like "BC Organization", which is the player's company.
//I also store world data in the company, because why not?
//This script will pull the data I want and message the players the day ended.
//It will then send all the information I want over my websocket to the python server
//My python server programs will process the data and send the data back
//This program then receives the message and processes the response data as I want
//The end result will be the day is advanced and the correct calendar day will be reported to the group and saved
//If you hit it on accident, use the setter script and change your variables to what you want


let company = game.actors.getName("BC Organization");
let days = parseInt(company.getFlag('world','days'));
let olddays = parseInt(company.getFlag('world','old'));
let wine = parseInt(company.getFlag('world','wine'));
let rum = parseInt(company.getFlag('world','rum'));
let storage = parseInt(company.getFlag('world','storage'));
let cash = parseInt(company.getFlag('world','cash'));
var socket = new WebSocket('ws://localhost:8089');

//var mes = [days,olddays,wine,rum,storage,cash];
var mes = [days,olddays,wine,rum,storage,cash];
let msg = 'Day '+days+' ended.';

ChatMessage.create({
        speaker: {
            alias: 'Day End'
    },
        content: msg
});

days++;
socket.onopen = function () {
  socket.send(mes);
  console.log('SENT: '+mes);
};
socket.onmessage = function (e) {
  console.log('RECEIVED: '+e.data);
  var arry = e.data.split(',');
  company.setFlag('world','days',days);
  company.setFlag('world','old',parseInt(arry[0]));
  company.setFlag('world','wine',parseInt(arry[1]));
  company.setFlag('world','rum',parseInt(arry[2]));
  company.setFlag('world','cash',parseInt(arry[3]));
  var msg = arry[4];
  msg+="\nAdventure Day: "+days;
  ChatMessage.create({
        speaker: {
            alias: 'Daily Report'
    },
        content: msg
});
};
