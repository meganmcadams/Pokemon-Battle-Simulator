----- How to Compile and Run
The program was written using Visual Studio Community (VSC) 2022, Python 3.7 
(64-bit). If you have VSC 2022, I have included the file for it in the zip file, 
but it isn’t required; you can also just copy the files (minus the VSC 2022 file) 
elsewhere. 


----- Notes
A lot of features were planned with the idea that I’d have a partner in mind, 
but since I didn’t end up having a partner, a lot of features were not implemented. 
I listed below those that were implemented and those that were not. 

The main part of the project is the battle simulator, but it is very, very 
rudimentary as it only acts as a base; it can handle picking the parties, picking 
a move, picking a target, calculating/applying damage, and checking if there’s a 
winning party/calculating and applying exp and money, but it can’t do anything 
beyond that. For example, it can’t do a traditional 1v1; it’s more of a free-for-all 
turn-based battle. 

In addition, while the main part is the battle simulator, there are a lot of other 
features involved that together, make up more than the battle simulator itself. 
These include a number of handlers to help with the features (such as the level 
handler, which is completely separate from the battle simulator), the save and load 
functions, and the party/pokemon/trainer managers. 

I did implement the two classes I spoke about in the update (Pokémon and Trainers), 
but they are handled at a very low-level; the dictionaries inside of the classes are 
passed to functions, not the class itself. This is because I had already implemented 
it as a dictionary to begin with, and with as many functions and files as I have, it 
wouldn’t have been feasible to find all the times I referenced the dictionary and 
replace it with the class’s dictionary. 

Lastly, there very well may be bugs in the program. I could not test 110% of it due to 
the number of features and size of the program, but I tested every feature; the amount 
of specific case testing was very little, though. That which I listed below in “Implemented 
Features” is working and tested, but please keep in mind that it is possible that you may 
run into bugs, and I am very sorry if you do; I did my best to fix those I came across, 
but it is a very large program. 


----- Implemented Features
- Saving and loading
- On Load 
   - Check for level ups and apply, if any
- Pokémon Manager
   - Create Pokémon
   - Delete Pokémon
   - List Pokémon
   - Pokémon Center (heal all Pokémon in a party)
- Trainer Manager
   - Create Trainer
   - Delete Trainer
   - List Trainers
- Battle Simulator
   - Pick two parties
   - Pick move
   - Pick target
   - Calculate and apply damage
   - Check if won
   - Calculate and apply money and exp gained
- Party Builder
   - Create Party
   - Delete Party
   - List Parties


----- Planned But Not Implemented Features
- On load
   - Check for evolution
- Encounter Generator
   - Create Encounter
   - Delete Encounter
   - Run Encounter
   - List Encounters
- Shop
   - Create Shop
   - Delete Shop
   - Open Shop
   - Buy
   - Sell
   - List Shops
- Battle Simulator
   - Decrement and check for PP
   - Multiple targets
   - No targets
   - Non-physical moves
   - 1v1, 2v2, 3v3, etc.
