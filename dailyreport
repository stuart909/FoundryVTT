//Written by Stuart Anderson
//This is a simple script that will load and report a simple daily report
//I use this template to pull data and concat a string message and chat
//it to the players.  It's also useful to remind the GM what day it is :)


let company = game.actors.getName("BC Organization");
let days = parseInt(company.getFlag('world','days'));
let msg = '';
msg+="Adventure Day: "+days;


ChatMessage.create({
        speaker: {
            alias: 'Daily Report'
    },
        content: msg
});
