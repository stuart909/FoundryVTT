//Written by Stuart Anderson
//This is a simple program that messages a slightly decorated, but still somewhat sloppy text message to the players
//You can see I used many variables to break up a report from a mission that I made on a Rifts adventure for our game
//Feel free to change the lines up or modify this as you wish.  This is handy for printing out contracts or quest completion stuff.
//If you place keywords or search keys, it makes it easier for the GM to find this stuff later.


let title = 'Naruni Enterprises URGENT Notice';
let p1 = 'TO: Black Cat Free Company';
let p2 = 'SUBJECT: Gobli Kingdom Sales Promotion';
let p3 = 'CONFIDENTIAL: Urgent matters have come to our attention and we wish to meet with your leadership in person.  A shuttle is currently inbound to discuss the dire situation.';
let p4 = 'As such, the Naruni Enterprises has considered your efforts and has been most pleased with your sales boosting efforts.  However, we do not believe the current contract is relevant to the current mission parameters and we are cancelling the remainder of your mission.';
let p5 = 'By intergalactic law, you are entitled to full compensation for your efforts, thus, 30,000,000ISC has been transferred to your corporate account.  It is our hope to make better use of your time, and we will be sure to admonish those that devalued the corporation and wasted your valuable time.';



ChatMessage.create({
        speaker: {
            alias: title
    },
        content: p1+'<br><br>'+p2+'<br><br>'+p3+'<br><br>'+p4+',<br>'+p5
});
