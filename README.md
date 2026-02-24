# About
These files is a summary of all what I learned in python.

## Common
This folder contains tools for later use.
More details can be found in the file comments.
Short description:
1. FileService - includes one class named FileService, that operates on files, with methods allowing to easly edit any file.
2. TableFormat - includes two classes named TableService and TableColumn. This tool is used for show data in table format.

## Encode
Starting with encode, this is something I heard in shool, about cipher method that was used years ago.
Cipher method is called "Cezar Cipher" or "Shift Cipher", meaning that each letter is assigned to another letter located a specified number of places later in the alphabet. I wanted to recreate this method in code.

## [Messages](https://github.com/Az0xV/Python/tree/main/Messages)
Messages contains 2 scripts that are connected by socket library witch uses internet connection and open ports to communicate with each other. This is how to make it work in 5 steps:
1. Make sure you have python and socket library installed
2. Open first messagesServer.py in console
3. Then second messagesClient.py in console
4. In the second console, the application asks for an IP address. If you do it locally, type: "127.0.0.0" (without quotes)
5. Type your username in second console, it can be anything.

And you done!
Now these scripts can talk to each other.
Open Third and Fourth messagesClient.py in console, connect them to the same network and test it as you want.

## Network
GetWifiPasswords.py creates a file named passwords.txt, which contains data about SSID appropriately matched to password, stored on computer.

## Pygame
These are my python files with Pygame library. I remade some games to learn how it works.

block.py - It works like Timberman game, but with no graphics.

flappy.py - This is classical game, flappy bird remade in python.

plains.py - There all squares are green at start, but when you click with right button, it turns red, if with left - turns blue. Red cant stand with too much blue squares.

Tabela.py - It creates random path with looks like stain. Click space to repeat.

TabelaTick.py - Exacly like Tabela.py, but the creation process is slower, and shows every square being place in real-time.

tic-tac-toe.py - name tells all

[...]

## SQL
The script connects to local database, and can execute commands on it, showing all data. This is the best script to know how to start with databases in python.
