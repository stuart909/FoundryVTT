//Writen by: Stuart Anderson
//This is a simple java script web socket that will target a server running locally on port 8089.
//This particular example sends text strings retrieved from character data, obviously alcohol related.
//This program was written to facilitate alcohol production and sales in the back ground when
//The day was ended.  I placed this script within an "end day" script that executed the production
//and trade automagically.

var socket = new WebSocket('ws://localhost:8089');
let company = game.actors.getName("BC Organization");
var mes = [148,137,0,4000,50000,258000];
var msg = '';
socket.onopen = function () {
  socket.send(mes);
  console.log('SENT: '+mes);
};
socket.onmessage = function (e) {
  console.log('RECEIVED: '+e.data);
  var arry = e.data.split(',');
  company.setFlag('world','old',parseInt(arry[0]));
  company.setFlag('world','wine',parseInt(arry[1]));
  company.setFlag('world','rum',parseInt(arry[2]));
  company.setFlag('world','cash',parseInt(arry[3]));
  msg=arry[4];
};
