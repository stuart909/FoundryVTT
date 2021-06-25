# FoundryVTT
Foundry VTT Macros
This repo was created and written by Stuart Anderson
All code and works are under a GNU license.  Please refer to the license for questions about redistribution, modification, or redistribution of your changes.

Description: Foundry VTT is a virtual table top client that allows people to connect via web browser to a common gaming table and share assets with a host, 
typically the "game master".  This application allows for users to write all sort of scripts and personal software to plugin to the main framework to perform
advanced calculations, market simulations, character movements, or even combat actions.  Anything a programmer can dream us using Javascript and Node.js is
a possibility with enough effort.

This repository contains the works that I have written that I use in my own game hosting with my players.  In it contains banking simulation, industry simulation,
time advancement, and even a websocket to allow the game client to communicate with another server that calculates data in Python, my preferred language.
In fact, the key selling point of this repo is the node.js websocket that will send and receive data to a python server, and a working example of said Python
server processing and returning actual data that I use day to day in my own games.

How it works:

The websock.py is a python program that starts a local websocket server that listens for input on port 8089.  You start this application with a Python runtime environment
before running any other macro / script in this repos.  The endday.js file is a script that I run via macro on my hotbar to end the game day.  This macro contains a 
websocket that will send the appropriate data to my Python server for processing.  The Python server receives that data and parses it into a sort of data table, then
runs it through a multitude of functions and checks to determine various things, like the daily market economy or production and sale of resources.  I also
calculate the actual calendar year in my game world and return all information that I need back to the game client.  The game client then receives the response and 
parses it into the appropriate function calls to store into the game token, which effectively saves the data on disk.  The game client now has updated market info
and calendar day.

With this example, you can see that we are able to simulate kingdoms, populations, wars, battles, monster movements, important events, and in depth roll tables
outside of the node.js game client and return the required information to the main application so we can have a complex and truly dynamic adventure with the push of a
button.

Why am I simply not coding these events in the game application?
  To put it bluntly, I hate javascript.  To be more blunt, I don't like how Foundry is structured. I have an easier time just writing code and storing and retrieving
  what I need outside of the game client.
  
What is on the table for the future?
  Python SQLite connector with a CLI interface that a macro or script can send and retrieve SQL data from
    - I have many SQLite connectors already
    - I have many CLI programs already
    - Just need to marry the 3 concepts
  Kingdom simulation, resource simulation, and population frameworks
    - I have various utilities and programs that simulate various factors, I just need to design and implement something that works for my game.
  Complex roll table framework.
    - Foundry roll tables suck.  I need to be able to have roll tables inside of roll tables, and complex selection logic for my needs.
