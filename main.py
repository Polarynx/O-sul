#O-sul Current: Over 790+ lines, 19 functions, 44K+ Programmed Modifications, 14 scenarios, and 1 ending
#O-sul Beta: Over ---+ lines, 33 functions, ---+ Programmed Modifications, 25 scenarios, and 4 endings
import time
import sys
import os
from PIL import Image
from getpass import getpass
global Story_Speed
def Game_TXT(text):
  for char in text:
      print(char, end='')
      sys.stdout.flush() 
      time.sleep(0.02)
def Logs():
  print("\n--- Logs ---\n")
  print("0.0 - Mauá (June 31)")
  print(" - Prepped Program")
  print(" - Basic Story Planning\n")
  print("0.1 - Sorocaba (July 15)")
  print(" - Added Affiliation")
  print(" - Designated Branching\n")
  print("0.2 - Osasco (July 31)")
  print(" - Added Alone, Cabo Frio E.P., and Avenue")
  print(" - Added Game Text & Game Pause\n")
  print("0.3 - Riberão Preto (August 15)")
  print(" - Added Dockside, Plaza, and Uprise")
  print(" - Added Decision #")
  print(" - Changed Game from Statements to Functions")
  print(" - Added Testing Hub")
  print(" - Added Start Menu\n")
  print("--Long Break for School --\n")
  print("0.4 - Santo André (January 26)")
  print(" - Added Reedeemer, São Paolo Excursion, Military")
  print(" - Added Testing Caution")
  print(" - Added Developer and Player Accounts in Start Menu")
  print(" - Added Story Speed")
  print(" - Added Logs\n")
  print(" - Integrated Formatting")
  print("0.5 - São José dos Campos (February 16)")
  print(" - Added Cargo, City, Armory")
  print(" - Added Quick Test")
  print("--Short Break for SAT --\n")
  print("0.6 - São Bernardo do Campo (March 23)")
  print(" - will add Trail, Tribal, Statue")
def Narrative_Testing_hub():
  Testing_Decision = []
  Testing_Caution = True
  print("\n--- Narrative Testing Hub ---")
  print("Enter the section you want to test:")
  print("1. Alone")
  print("2. Federação")
  print("3. São_Paolo_Excursion")
  print("4. Cabo_Frio_EP")
  print("5. Dockside")
  print("6. Trail")
  print("7. Plaza")
  print("8. Redeemer")
  print("9. Anarchy")
  print("10. Uprise")
  print("11. Military")
  print("12. Cargo")
  print("13. City")
  print("14. Armory")
  Section_Test = int(input("Section #: "))
  if Section_Test == 0:
    Narrative_Testing_hub()
  Testing_Name = input("What is the testing name? ")
  Testing_Name = Testing_Name[0].upper() + Testing_Name[1:]
  Testing_Name_Dialouge = Testing_Name + ": "
  Testing_Paths = [Alone, Federação, São_Paolo_Excursion, Cabo_Frio_EP, Dockside, Trail, Plaza, Redeemer, Anarchy, Uprise, Military, Cargo, City, Armory]
  Testing_Paths_Num = 0
  Testing_Story_Speed = input("What do you want your text speed to be? (Slow/Medium/Fast): ")
  while Testing_Story_Speed.lower() not in ["slow", "medium", "fast"]:
    Testing_Story_Speed = input("Invalid Input\nPlease choose a valid option: ")
  if Testing_Story_Speed.lower() == "slow":
    Testing_Story_Speed = 2
  elif Testing_Story_Speed.lower() == "medium":
    Testing_Story_Speed = 1
  elif Testing_Story_Speed.lower() == "fast":
    Testing_Story_Speed = 0.5
  if Section_Test < 5:
    if Section_Test > 2:
      Testing_Decision = ["0"]
      for Testing_Paths_Num in range(len(Testing_Paths)):
        if Section_Test - 1 == Testing_Paths_Num:
          Testing_Paths[Testing_Paths_Num](Testing_Name, Testing_Name_Dialouge, Testing_Caution, Testing_Decision, Testing_Story_Speed)
    elif Section_Test < 3:
      for Testing_Paths_Num in range(len(Testing_Paths)):
        if Section_Test - 1 == Testing_Paths_Num:
          Testing_Paths[Testing_Paths_Num](Testing_Name, Testing_Name_Dialouge, Testing_Caution, Testing_Decision, Testing_Story_Speed)
  elif Section_Test >= 5 and Section_Test < 11:
    Test_Alone_Route = input("Enter what Route the Character would have taken? (SP/CB) ")
    if Section_Test == 5:
      if Test_Alone_Route.lower() == "sp":
        Testing_Decision = ["0", "0", "1"]
        Testing_Paths[4](Testing_Name, Testing_Name_Dialouge, Testing_Caution, Testing_Decision, Testing_Story_Speed)
      elif Test_Alone_Route.lower() == "cb":
        Testing_Decision = ["0", "1"]
        Testing_Paths[4](Testing_Name, Testing_Name_Dialouge, Testing_Caution, Test_Alone_Route, Testing_Decision, Testing_Story_Speed)
    elif Section_Test >=6:
      if Section_Test == 6:
        Testing_Decision = ["0", "1"]
        Testing_Paths[5](Testing_Name, Testing_Name_Dialouge, Testing_Caution, Testing_Decision, Testing_Story_Speed)
      elif Section_Test == 7:
        if Test_Alone_Route.lower() == "sp":
          Testing_Decision = ["0", "0", "1", "1"]
          Testing_Paths[6](Testing_Name, Testing_Name_Dialouge, Testing_Caution, Testing_Decision, Testing_Story_Speed)
        elif Test_Alone_Route.lower() == "cb":
          Testing_Decision = ["0", "1", "0"]
          Testing_Paths[6](Testing_Name, Testing_Name_Dialouge, Testing_Caution, Testing_Decision, Testing_Story_Speed)
      elif Section_Test == 8:
        if Test_Alone_Route.lower() == "sp":
          Testing_Decision = ["0", "0", "1", "1"]
          Testing_Paths[7](Testing_Name, Testing_Name_Dialouge, Testing_Caution, Testing_Decision, Testing_Story_Speed)
        elif Test_Alone_Route.lower() == "cb":
          Testing_Decision = ["0", "1", "0"]
          Testing_Paths[7](Testing_Name, Testing_Name_Dialouge, Testing_Caution, Testing_Decision, Testing_Story_Speed)
      elif Section_Test == 9:
        Test_Cargo_Route = input("Enter what Route the Character would have taken? (TR/DO) ")
        if Test_Cargo_Route.lower() == "tr":
          Testing_Decision = ["0", "0", "1", "0"]
          Testing_Paths[8](Testing_Name, Testing_Name_Dialouge, Testing_Caution, Testing_Decision, Testing_Story_Speed)
        if Test_Cargo_Route.lower() == "do":
          if Test_Alone_Route.lower() == "sp":
            Testing_Decision = ["0", "0", "1", "1", "0"]
            Testing_Paths[8](Testing_Name, Testing_Name_Dialouge, Testing_Caution, Testing_Decision, Testing_Story_Speed)
          elif Test_Alone_Route.lower() == "cb":
            Testing_Decision = ["0", "1", "0", "0"]
            Testing_Paths[8](Testing_Name, Testing_Name_Dialouge, Testing_Caution, Testing_Decision, Testing_Story_Speed)
      elif Section_Test == 10:
        if Test_Alone_Route.lower() == "sp":
          Testing_Decision = ["0", "0", "1", "1", "0"]
          Testing_Paths[9](Testing_Name, Testing_Name_Dialouge, Testing_Caution, Testing_Decision, Testing_Story_Speed)
        elif Test_Alone_Route.lower() == "cb":
          Testing_Decision = ["0", "1", "0", "0"]
          Testing_Paths[9](Testing_Name, Testing_Name_Dialouge, Testing_Caution, Testing_Decision, Testing_Story_Speed)
  elif Section_Test >= 11:
    if Section_Test == 11:
      Testing_Decision = ["0", "0"]
      Testing_Paths[10](Testing_Name, Testing_Name_Dialouge, Testing_Caution, Testing_Decision, Testing_Story_Speed)
    elif Section_Test == 12:
      Testing_Decision = ["0", "0"]
      Testing_Paths[11](Testing_Name, Testing_Name_Dialouge, Testing_Caution, Testing_Decision, Testing_Story_Speed)
    elif Section_Test == 13:
      Testing_Decision = ["0", "0", "1"]
      Testing_Paths[12](Testing_Name, Testing_Name_Dialouge, Testing_Caution, Testing_Decision, Testing_Story_Speed)
    elif Section_Test == 14:
      Testing_Decision = ["0", "0", "1", "0"]
      Testing_Paths[13](Testing_Name, Testing_Name_Dialouge, Testing_Caution, Testing_Decision, Testing_Story_Speed)
def Affiliation():
  Testing_Caution = False
  Decision_Num = []
  Game_TXT("\n\nVersion 0.6.0 - São Bernardo do Campo - Trail\n")
  Game_TXT("Version São Bernardo do Campo Release Date: 3/23/24")
  Game_TXT("\nThis is the world you live in, can you survive in it, or will you fall like everyone else?")
  Game_TXT("\nDo you want to survive?\n")
  START_GAME = input("")
  if START_GAME.lower() == "yes":
    Game_TXT("How fast do you want your story to be? (Slow/Medium/Fast): \n")
    Story_Speed = input("")
    while Story_Speed.lower() not in ["slow", "medium", "fast"]:
        Game_TXT("Invalid Input\nPlease choose a valid option: \n")
        Story_Speed = input("")
    if Story_Speed.lower() == "slow":
        Story_Speed = 2.0
    elif Story_Speed.lower() == "medium":
        Story_Speed = 1.0
    elif Story_Speed.lower() == "fast":
        Story_Speed = 0.5
    else:
        Story_Speed = 1.0
    Game_TXT("Let's survive then.\n|Welcome to the DYSTOPIAN WORLD: O-sul|")
    time.sleep(2* Story_Speed)
    Game_TXT("\nWe will see who will rule O-sul, who are you? \n")
    Player_Name = input("")
    Player_Name = Player_Name[0].upper() + Player_Name[1:]
    Player_Name_Dialouge = Player_Name + ": "
    Game_TXT("\nHello ")
    Game_TXT(Player_Name) 
    Game_TXT(", You will decide your PATH, and maybe, it will lead to LIFE or maybe DEATH? You will forge your PATH...")
    Game_TXT("\n\nSTORY: O-sul has fallen to the caos, a group of devout worshippers of the great god of chaos, Tau. You were once an elite soldier in the Special Operations Command, born and raised Río de Jainero; you must free it of the caos. A Federação do Neo-Brasil wants your help to take them down, will you fight in the war for O-sul alone or with A Federação do Neo-Brasil. (Alone/Neo-Brasil) \n")
    Affiliation_Choice = input("")
    time.sleep(3 * Story_Speed)
    if Affiliation_Choice.lower() == "alone":
      Alone(Player_Name, Player_Name_Dialouge, Testing_Caution, Decision_Num, Story_Speed)
    elif Affiliation_Choice.lower() == "neo-brasil":
      Federação(Player_Name, Player_Name_Dialouge, Testing_Caution, Decision_Num, Story_Speed)
def Alone(Player_Name, Player_Name_Dialouge, Testing_Caution, Decision_Num, Story_Speed):
  Game_TXT("\n")
  Decision_Num.append("0")
  Game_TXT(Player_Name) 
  Game_TXT(" refuses the offer made by the Brazilian Government and returns to their base, and starts to trying to crack down on the government and what they know, so ")
  Game_TXT(Player_Name) 
  Game_TXT(" can occupy O-sul.")
  time.sleep(4* Story_Speed)
  Game_TXT("\n\ndEcrYpTInG...")
  time.sleep(1* Story_Speed)
  Game_TXT("DeCRyPtiNg...")
  time.sleep(1* Story_Speed)
  Game_TXT("DeCRyptiNG")
  time.sleep(3* Story_Speed)
  Game_TXT("\nDecryption SUCCESFUL! Converse.1311 activated, PLAY NOW!")
  Game_TXT("\n\nConverse.1311:\nPessoa 1: Comandante Cacau, o caos tomou O-sul, não podemos fazer nada. Nossa melhor opção para levar O-sul de volta é sequestrar seus trens de suprimentos, entrar furtivamente na cidade e tentar eliminar os líderes de dentro.")
  time.sleep(5* Story_Speed)
  Game_TXT("\n\n")
  Game_TXT(Player_Name_Dialouge + "I can't understand anything *turns on translation-mod")
  time.sleep(3* Story_Speed)
  Game_TXT("\n\nCoNFIguRiNg...")
  time.sleep(1* Story_Speed)
  Game_TXT("cOnfiGUrInG...")
  time.sleep(1* Story_Speed)
  Game_TXT("coNFiguRINg")
  time.sleep(2* Story_Speed)
  Game_TXT("\n\nPerson 1: Commander Cacau, the chaos have occupied O-sul, we can't do anything. Our best option to take O-sul back is to hijack their supply trains, and sneak into the city and try to take out the leaders from the inside.")
  time.sleep(6* Story_Speed)
  Game_TXT("\n\nPerson 2: Vice-Commander David, Which supply trains?")
  time.sleep(3* Story_Speed)
  Game_TXT("\n\nPerson 1: The ones from São Paulo, it should suffice for our troops to take over from the inside.")
  time.sleep(3* Story_Speed)
  Game_TXT("\n\nRecording END...")
  if Testing_Caution == False:
    pass
  else:
    Testing_Notion = input("\nIf you want to continue testing, input \"C\", If you want to stop testing and return to testing hub, input \"T\", or If you want to stop the program entirely, input \"S\": ")
    if Testing_Notion == "C":
      pass
    elif Testing_Notion == "T":
      Narrative_Testing_hub()
    else:
      exit()
  time.sleep(2* Story_Speed)
  Game_TXT("\n" + Player_Name)
  Game_TXT(" must decide whether to go from São Paulo in the south or from the east to Cabo Frio.(S/E)\n ")
  Infiltration = input("")
  if Infiltration.lower() == "e":
    Cabo_Frio_EP(Player_Name, Player_Name_Dialouge, Testing_Caution, Decision_Num, Story_Speed)
  elif Infiltration.lower() == "s":
    São_Paolo_Excursion(Player_Name, Player_Name_Dialouge, Testing_Caution, Decision_Num, Story_Speed)
def Federação(Player_Name, Player_Name_Dialouge, Testing_Caution, Decision_Num, Story_Speed):
  Game_TXT("\n")
  Decision_Num.append("1")
  print("Undetermined.")
  if Testing_Caution == False:
    pass
  else:
    Testing_Notion = input("\nIf you want to continue testing, input \"C\", If you want to stop testing and return to testing hub, input \"T\", or If you want to stop the program entirely, input \"S\": ")
    if Testing_Notion == "C":
      pass
    elif Testing_Notion == "T":
     Narrative_Testing_hub()
    else:
      exit()
def São_Paolo_Excursion(Player_Name, Player_Name_Dialouge, Testing_Caution, Decision_Num, Story_Speed):
  Game_TXT("\n")
  Decision_Num.append("0")
  Game_TXT("\n\nSão Paulo from the south, Let's go...")
  time.sleep(1*Story_Speed)
  Game_TXT("\nTravelling to São Paulo...")
  time.sleep(1* Story_Speed)
  Game_TXT("\nTravelling to São Paulo...")
  time.sleep(1* Story_Speed)
  Game_TXT("\nTravelling to São Paulo")
  time.sleep(1* Story_Speed)
  Game_TXT("\nEven São Paulo is desolate, as soon as the Caos took over the bustling region, they vacated the city and now all of their forces are in O-sul")
  time.sleep(4)
  Game_TXT("\nNo one dares to come into the region of Tau, in these streets, only Tau traders lurk")
  time.sleep(3)
  Game_TXT("\nYou hear a bustling ship horn as Tau traders head to a port as you sneak into an alleyway")
  time.sleep(3)
  Game_TXT("\nThey get into a ship, it looks like a cargo ship as the ship captain announces to the Tau traders in Guaraní *you turn on your translator")
  time.sleep(3)
  Game_TXT("\nShip Captain: Tau Traders, this ship is heading north, friends. If you wish to get on, proceed to do so before we leave in 15 minutes.")
  time.sleep(3)
  Game_TXT("\nThe ravagous Tau get on, as you head the opposite way...")
  time.sleep(2)
  Game_TXT("\n\nYou suddenly hear whispers after sneaking in the alleyway")
  time.sleep(2)
  Game_TXT("\nUnknown: atacaremos O-sul, soldados. Prepare suas armas. *turns on translation. We will attack O-sul, soldiers. Ready your weapons.")
  time.sleep(3)
  Game_TXT("\FNB Commander: The Federação will attack O-sul, we will make sure Río will once again fluorish, soldiers.")
  time.sleep(2)
  Game_TXT("\n{} now faces a choices, should {} join the Federação's Military operation or go to the Cargo? (M/C)".format(Player_Name, Player_Name))
  if Testing_Caution == False:
    pass
  else:
    Testing_Notion = input("\nIf you want to continue testing, input \"C\", If you want to stop testing and return to testing hub, input \"T\", or If you want to stop the program entirely, input \"S\": \n")
    if Testing_Notion == "C":
      pass
    elif Testing_Notion == "T":
     Narrative_Testing_hub()
    else:
      exit()
    São_Paolo_Excursion = input("")
    if São_Paolo_Excursion.lower() == "m":
      Military(Player_Name, Player_Name_Dialouge, Testing_Caution, Decision_Num, Story_Speed)
    elif São_Paolo_Excursion.lower() == "c":
      Cargo(Player_Name, Player_Name_Dialouge, Testing_Caution, Decision_Num, Story_Speed)
def Cabo_Frio_EP(Player_Name, Player_Name_Dialouge, Testing_Caution, Decision_Num, Story_Speed):
  Game_TXT("\n")
  Decision_Num.append("1")
  Alone_Route = "CB" 
  Game_TXT("\n\nI guess I have to go to O-sul from the east, Time to go to Cabo Frio...")
  time.sleep(2* Story_Speed)
  Game_TXT("\nTravelling to Cabo Frio...")
  time.sleep(1* Story_Speed)
  Game_TXT("Travelling to Cabo Frio...")
  time.sleep(1* Story_Speed)
  Game_TXT("Travelling to Cabo Frio")
  time.sleep(1* Story_Speed)
  Game_TXT("\n\n\nYou have arrived at Cabo Frio, the closest city to O-sul without being in O-sul. "+ Player_Name+ " sees a map.")
  print("\n<------------MAP")
  img = Image.open("ssamblu.gif")
  img.show("ssamblu.gif")
  time.sleep(10* Story_Speed)
  Game_TXT(Player_Name_Dialouge + "The new Union really took over the bustling sectors of Brazil, they only have Manaus, Salvador, and Belem left. And the War for the South did not help them, they have no allies. Rio de Janeiro no longer exists, only O-sul.")
  time.sleep(4* Story_Speed)
  Game_TXT("\nBrazil has fallen.")
  time.sleep(1* Story_Speed)
  Game_TXT("\nThis is their chance, the chance to take back their Rio, currently O-sul.")
  if Testing_Caution == False:
    pass
  else:
    Testing_Notion = input("\nIf you want to continue testing, input \"C\", If you want to stop testing and return to testing hub, input \"T\", or If you want to stop the program entirely, input \"S\": ")
    if Testing_Notion == "C":
      pass
    elif Testing_Notion == "T":
     Narrative_Testing_hub()
    else:
      exit()
  time.sleep(1* Story_Speed)
  Game_TXT("\n" + Player_Name + " encounters a pathway, one leading to an avenue and another to a trail, (A/T) \n")
  Cabo_Frio_EP = input("")
  if Cabo_Frio_EP.lower() == "a":
    Dockside(Player_Name, Player_Name_Dialouge, Testing_Caution, Alone_Route, Decision_Num, Story_Speed)
  elif Cabo_Frio_EP.lower() == "t":
    Trail(Player_Name, Player_Name_Dialouge, Testing_Caution, Alone_Route, Decision_Num, Story_Speed)
def Military(Player_Name, Player_Name_Dialouge, Testing_Caution, Decision_Num, Story_Speed):
  Game_TXT("\n")
  Decision_Num.append("0")
  Game_TXT("\n{}I gotta go with the Federação, It will provide me with backup.".format(Player_Name_Dialouge))
  time.sleep(2* Story_Speed)
  Game_TXT("\nYou start to take a step out of the shadows to go to them when the unknown person alerts that someone lurks")
  time.sleep(3* Story_Speed)
  Game_TXT("\nFNB Commander: Soldiers, get the crawler.")
  time.sleep(1* Story_Speed)
  Game_TXT("\n\nTwo soldiers drag you by your shoulders and bring you in front of the commander")
  time.sleep(2* Story_Speed)
  Game_TXT("\n{}I am friendly, I want O-sul back as well, I can join your mission.".format(Player_Name_Dialouge))
  time.sleep(2* Story_Speed)
  Game_TXT("\nFNB Commander: Aren't you the ex-SOC soldier, {}?".format(Player_Name))
  time.sleep(2* Story_Speed)
  Game_TXT("\n{}Yes, I wish to accept your command, I shouldn't have walked away last time".format(Player_Name_Dialouge))
  time.sleep(3*Story_Speed)
  Game_TXT("\nFNB Commander: You were a brave soldier, I remember your stories while I was a lowly soldier, but....")
  time.sleep(5*Story_Speed)
  Game_TXT("\n\nDO YOU REALLY TAKE THE FEDERAÇÃO AS A GOVERNMENT THAT IS FOOLISH!!! First you deny our request, now you want back, what if you want out by betraying us?")
  time.sleep(5*Story_Speed)
  Game_TXT("\n{}I won't, trust me.".format(Player_Name_Dialouge))
  time.sleep(1*Story_Speed)
  Game_TXT("\nFNB Commander: We would have gained trust if you had joined us the first time, sorry {}".format(Player_Name))
  time.sleep(3*Story_Speed)
  Game_TXT("\n\nAs the Commander rose his gun, you tried to escape but the soldiers held you tightly")
  time.sleep(3*Story_Speed)
  Game_TXT("\nFNB Commander: Viva a Federação do Neo-Brasil")
  time.sleep(2*Story_Speed)
  Game_TXT("\nThe Trigger was pulled.................................BANG!")
  time.sleep(5*Story_Speed)
  Game_TXT("\n\n\nThe military's hope and trust died with your life.")
  time.sleep(2*Story_Speed)
  Game_TXT("\nYou haven't completed the story, your choices led you here, make some different ones to survive...\n")
  time.sleep(3* Story_Speed)
  for x in Decision_Num:
    print(x, end='')
  if Testing_Caution == False:
    pass
  else:
    Testing_Notion = input("\nIf you want to continue testing, input \"C\", If you want to stop testing and return to testing hub, input \"T\", or If you want to stop the program entirely, input \"S\": ")
    if Testing_Notion == "C":
      pass
    elif Testing_Notion == "T":
     Narrative_Testing_hub()
    else:
      exit()
def Cargo(Player_Name, Player_Name_Dialouge, Testing_Caution, Decision_Num, Story_Speed):
  Game_TXT("\n")
  Decision_Num.append("1")
  Alone_Route = "SP"
  Game_TXT("{} slowly creeps onto the cargo boat as the captain announces to the harbor and the crewmates\n".format(Player_Name))
  time.sleep(3*Story_Speed)
  Game_TXT("The captain: Caos, We are heading north, friends. Be seated for harbor departure.\n")
  time.sleep(2*Story_Speed)
  Game_TXT("As {} snuck onto the boat, he hid in one of the unoccupied boiler rooms.\n")
  time.sleep(2*Story_Speed)
  Game_TXT("{} inspected the boiler rooms, finding manafactured engines with the name of the forgotten Brazil, all scratched out and replaced with the writing of the Caos.\n".format(Player_Name))
  time.sleep(5*Story_Speed)
  Game_TXT("{}These are not made by the Caos, these are everyday ferries remade as ships, the caos have no industrial capability, the factories are just getting built.\n".format(Player_Name_Dialouge))
  time.sleep(5*Story_Speed)
  Game_TXT("Suddenly, {} heard a big boom, and the captain commanded the ferryman in the speakers.\n".format(Player_Name))
  time.sleep(2*Story_Speed)
  Game_TXT("Captain: Caos, we are being attacked, our inspectors inform that it is the pesky Federacão, we have no weapons, we have to flee for now, brace yourselves\n")
  time.sleep(5*Story_Speed)
  Game_TXT("The boat started to speed up and the boiler rooms started to get hotter and hotter, {} had to escape, {} climbed slowly to main level.\n\n".format(Player_Name, Player_Name))
  time.sleep(4*Story_Speed)
  Game_TXT("{} snuck onto the main level, as he saw the caos crewman gather on the back of the ship, looking at the Federacão ship getting out of reach\n".format(Player_Name))
  time.sleep(4*Story_Speed)
  Game_TXT("As {} was trying to go away from the window, {} realized one tribesman turn back and was squinting at {}, panicked, {} ran to one of the unoccupied rooms\n".format(Player_Name, Player_Name, Player_Name, Player_Name))
  time.sleep(5*Story_Speed)
  Game_TXT("Alarmed by the encounter, {} went into a mode of doubt, \"Had he seen me?\"\n\n".format(Player_Name))
  time.sleep(2*Story_Speed)
  Game_TXT("Considering the situation, {} must decide whether to jump ship to avoid risking them attacking or relying on luck and staying on the ship(J/L)\n".format(Player_Name))
  if Testing_Caution == False:
    pass
  else:
    Testing_Notion = input("\nIf you want to continue testing, input \"C\", If you want to stop testing and return to testing hub, input \"T\", or If you want to stop the program entirely, input \"S\": \n")
    if Testing_Notion == "C":
      pass
    elif Testing_Notion == "T":
      Narrative_Testing_hub()
    else:
      exit()
  time.sleep(4*Story_Speed)
  Cargo_Choice = input("")
  if Cargo_Choice.lower() == "l":
    Dockside(Player_Name, Player_Name_Dialouge, Testing_Caution, Alone_Route, Decision_Num, Story_Speed)
  elif Cargo_Choice.lower() == "j":
    City(Player_Name, Player_Name_Dialouge, Testing_Caution, Decision_Num, Story_Speed)
def City(Player_Name, Player_Name_Dialouge, Testing_Caution, Decision_Num, Story_Speed):
  Game_TXT("\n")
  Decision_Num.append("1")
  Game_TXT("{} carefully moved to the outside of the ship, {} could see O-sul with its fiery ligthing, {} needed to escape, {} jumped ship\n".format(Player_Name, Player_Name, Player_Name, Player_Name))
  time.sleep(3*Story_Speed)
  Game_TXT("The waves were huge, {} remembered surfing in these same wave of Copacabana. Not anymore as that beach and anything Brazillian, was wiped of the map by the caos\n".format(Player_Name))
  time.sleep(4*Story_Speed)
  Game_TXT("After swimming, {} reached the shoreline, there were no guards or any natives protecting the shoreline, {} moved with haste.\n\n".format(Player_Name, Player_Name))
  time.sleep(3*Story_Speed)
  Game_TXT("{} investigated the streets, and noticed a huge tower looming ahead, what once was the Rio Sul Tower, was now, etched in fire, was Tower O-sul\n".format(Player_Name))
  time.sleep(3*Story_Speed)
  Game_TXT("As {} stick to the allys, {} hears feet rustling, quickly turning around and hiding behind a dumpster, some natives ran past with flashlights checking for intruders\n".format(Player_Name, Player_Name))
  time.sleep(4*Story_Speed)
  Game_TXT("Luckily for {}, he stuck close to the ground so that the natives could not see him, as they cleard, {} slowly got up but something pressured the back of {}\'s head, as {} heard.\n".format(Player_Name, Player_Name, Player_Name, Player_Name))
  time.sleep(5*Story_Speed)
  Game_TXT("Unknown Man: Don't look back, or I will shoot you. Who are you?\n")
  time.sleep(2*Story_Speed)
  Game_TXT("Considering the man's portugese, {} deduced the man was either a rebel or an agent of the Federacão\n".format(Player_Name))
  time.sleep(3*Story_Speed)
  Game_TXT("{}I am {}, I have come to take the natives down as well, believe me.\n".format(Player_Name_Dialouge, Player_Name))
  time.sleep(2*Story_Speed)
  Game_TXT("Unknown Man: I only trust you because I recognize you, you were once an elite soldier, you would be of help.\n")
  time.sleep(3*Story_Speed)
  Game_TXT("Unknown Man: Get up, I am one of the scouts of the rebels, we are planning an attack on their Tau statue tonight, they will get here.\n")
  time.sleep(3*Story_Speed)
  Game_TXT("The man explained his plan, wanting {} to help in one way\n".format(Player_Name))
  time.sleep(2*Story_Speed)
  Game_TXT("Rebel: We have enough rebels at the attack at Tau, we want you to get rid of the leaders while we stage this rebellion, go to the Tower O-sul, once you hear the sound of the Tau falling\n\n")
  time.sleep(5*Story_Speed)
  Game_TXT("The two rebels parted ways as {} narrowly snuck to the Tower, as {} was about to climb the Tower to reach the upper areas, {} heard a loud bang and saw the statue of Tau collapsing\n".format(Player_Name, Player_Name, Player_Name))
  time.sleep(5*Story_Speed)
  Game_TXT("{} quickly ran to the streetside, peeking at the running natives, ready for a battle at the statue.\n".format(Player_Name))
  time.sleep(3*Story_Speed)
  Game_TXT("{} needed to find a way into the building another way, climbing would no longer be an option because too many natives were outside now.\n\n".format(Player_Name))
  if Testing_Caution == False:
    pass
  else:
    Testing_Notion = input("\nIf you want to continue testing, input \"C\", If you want to stop testing and return to testing hub, input \"T\", or If you want to stop the program entirely, input \"S\": ")
    if Testing_Notion == "C":
      pass
    elif Testing_Notion == "T":
     Narrative_Testing_hub()
    else:
      exit()
  Game_TXT("{} needed to decide a pathway to get into the building, {} could go through the armory or the main entrance(A/M)\n".format(Player_Name, Player_Name))
  time.sleep(3*Story_Speed)
  City = input("")
  if City.lower == "a":
    Armory(Player_Name, Player_Name_Dialouge, Testing_Caution, Decision_Num, Story_Speed)
  elif City.lower == "m":
    Anarchy(Player_Name, Player_Name_Dialouge, Testing_Caution, Decision_Num, Story_Speed)
def Armory(Player_Name, Player_Name_Dialouge, Testing_Caution, Decision_Num, Story_Speed):
  Game_TXT("\n")
  Decision_Num.append("1")
  Game_TXT("{} crept in the armory, most of the weapons were gone, probably taken by the fighting natives.\n".format(Player_Name))
  time.sleep(3*Story_Speed)
  Game_TXT("{} grabbed a spear and headed up the stairs\n".format(Player_Name))
  time.sleep(2*Story_Speed)
  Game_TXT("Creeping slowly up the stairs, he saw the final door leading to a hall, {} inspected both sides of the walls before heading inside, {} was in Tower O-sul\n".format(Player_Name, Player_Name))
  time.sleep(4*Story_Speed)
  Game_TXT("As {} was walking down the hall...............................TWANG!!!\n\n".format(Player_Name))
  time.sleep(3*Story_Speed)
  Game_TXT("Three arrows flew at {} from the walls, piercing their body\n".format(Player_Name))
  time.sleep(2*Story_Speed)
  Game_TXT("The elite soldier coudln't notice the trap, it was so particularly designed to look like a normal wall, but it was a trap\n")
  time.sleep(4*Story_Speed)
  Game_TXT("Natives started running out and picked up the wounded soldier, {} tried to fight back, but alas no strenght was found\n".format(Player_Name))
  time.sleep(4*Story_Speed)
  Game_TXT("{} faintly saw as the natives talked of an intruder, getting confirmation for execution\n".format(Player_Name))
  time.sleep(3*Story_Speed)
  Game_TXT("{} tried to fight back, but {} was dragged to the room and arrows prepped for fire\n\n".format(Player_Name,Player_Name))
  time.sleep(3*Story_Speed)
  Game_TXT("The execution ended the rebel's life.\n")
  time.sleep(2* Story_Speed)
  Game_TXT("You haven't completed the story, your choices led you here, make some different ones to survive...\n")
  time.sleep(3* Story_Speed)
def Dockside(Player_Name, Player_Name_Dialouge, Testing_Caution, Alone_Route, Decision_Num, Story_Speed):
  Game_TXT("\n")
  if(Alone_Route.lower() == "cb"):
    Decision_Num.append("0")
  elif(Alone_Route.lower() == "sp"):
    Decision_Num.append("1")
  Game_TXT(Player_Name + " enters the broken avenue.\n")
  time.sleep(1* Story_Speed)
  Game_TXT("Even though this wasn't under the jurusdiction of the caos, Cabo Frio was a town of anarchy, no one dared to come.\n\n")
  time.sleep(3* Story_Speed)
  Game_TXT(Player_Name + " walks along the broken road, broken lamplights, and broken hearts.\n\n")
  time.sleep(2* Story_Speed)
  Game_TXT(Player_Name_Dialouge + "It leads to a Dock, hopefully this dock leads to O-sul.\n\n")
  time.sleep(2* Story_Speed)
  Game_TXT(Player_Name + " seeks a boat and finds one adressing to O-sul as cargo, " + Player_Name + " creeps onto the boat and quickly hides as murmuring is heard.\n\n")
  time.sleep(4* Story_Speed)
  Game_TXT("Unknown: Make sure to take arms as soon as we reach the Redeemer, this is where we could free O-sul from its opressors and make it return to our Rio de Jainero.\n")
  time.sleep(3* Story_Speed)
  Game_TXT("The Redeemer is no longer the savior you think of that stood by Rio for over 150 years, The Caos destroyed the world wonder and replaced it with the monument of their god, Tau. ")
  if Testing_Caution == False:
    pass
  else:
    Testing_Notion = input("\nIf you want to continue testing, input \"C\", If you want to stop testing and return to testing hub, input \"T\", or If you want to stop the program entirely, input \"S\": ")
    if Testing_Notion == "C":
      pass
    elif Testing_Notion == "T":
     Narrative_Testing_hub()
    else:
      exit()
  time.sleep(4* Story_Speed)
  Game_TXT("\n" + Player_Name + " didn't know whether to take alliance with these rebels, it was neccesary needed to either work with them or stay silent. What was " + Player_Name + "'s descision, to take arms together or seprate? (T/S)")
  Rebel_Affiliation = input(" ")
  if Rebel_Affiliation.lower() == "t":
    Redeemer(Player_Name, Player_Name_Dialouge, Testing_Caution, Decision_Num, Story_Speed)
  elif Rebel_Affiliation.lower() == "s":
    Plaza(Player_Name, Player_Name_Dialouge, Testing_Caution, Decision_Num, Story_Speed)
def Trail(Player_Name, Player_Name_Dialouge, Testing_Caution, Alone_Route, Decision_Num, Story_Speed):
  Game_TXT("\n")
  Decision_Num.append("1")
  print("\nThe Trail pathway will be added in version 0.6 - São Bernardo do Campo\nVersion São Bernardo do Campo Release Date: 2/23/24")
  if Testing_Caution == False:
    pass
  else:
    Testing_Notion = input("\nIf you want to continue testing, input \"C\", If you want to stop testing and return to testing hub, input \"T\", or If you want to stop the program entirely, input \"S\": ")
    if Testing_Notion == "C":
      pass
    elif Testing_Notion == "T":
     Narrative_Testing_hub()
    else:
      exit()
def Plaza(Player_Name, Player_Name_Dialouge, Testing_Caution, Decision_Num, Story_Speed):
  Game_TXT("\n")
  Decision_Num.append("0")
  Game_TXT("Deciding to go solo, " + Player_Name + " hides in the cargo hold of the chaos's hijacked trade ship, blending in with the cargo to avoid detection.\n")
  time.sleep(3* Story_Speed)
  Game_TXT("\nAs the ship sails towards O-sul, the chaos's crew members are busy discussing their plans.\n\n")
  time.sleep(2* Story_Speed)
  Game_TXT("Their voices carry through the ship, and you listen attentively without revealing yourself.\n\n")
  time.sleep(2* Story_Speed)
  Game_TXT(Player_Name + " learns that the chaos's forces have taken control of key areas in O-sul.\n\n")
  time.sleep(2* Story_Speed)
  Game_TXT("The rebels on board are planning to launch a surprise attack on the Redeemer to weaken the chaos's grip on the city.\n")
  time.sleep(6* Story_Speed)
  Game_TXT("\nWhile you maintain your silence, the rebels have a heated conversation.\n\n")
  time.sleep(2* Story_Speed)
  Game_TXT("Unknown Rebel: Are we sure the Redeemer is the right target? It is a important monument for the Caos, if we take out the structure of their god, they will go beserk, Alpha.\n\n")
  Game_TXT("Alpha: Yes, taking down the Redeemer will send a powerful message to the rebels, they have toppled our diety, we will topple theirs.\n\n")
  Game_TXT("Alpha: Once we've secured O-sul, the rest of the territory will fall in line, and I don't have a care of what I will do to get back my home.\n")
  time.sleep(6* Story_Speed)
  Game_TXT("\nAs the ship approaches O-sul's port, the chaos's crew readies for the upcoming battle.\n\n")
  time.sleep(3* Story_Speed)
  Game_TXT(Player_Name + " seizes the opportunity to slip away unnoticed, staying true to their solo mission.\n")
  time.sleep(2* Story_Speed)
  Game_TXT("\n" + Player_Name + " makes their way through the abandoned streets of O-sul, finally reaching the desolate Plaza.\n\n")
  time.sleep(2* Story_Speed)
  Game_TXT("The Plaza, once vibrant with life, now stands in stark contrast as a reminder of the chaos's tyranny.\n\n")
  time.sleep(2* Story_Speed)
  Game_TXT("With determination, " + Player_Name + " begins searching for valuable information.\n\n")
  time.sleep(3* Story_Speed)
  Game_TXT("\n\nSearching...")
  time.sleep(1* Story_Speed)
  Game_TXT("Searching...")
  time.sleep(1* Story_Speed)
  Game_TXT("Searching\n")
  time.sleep(5* Story_Speed)
  Game_TXT("BOOOOOM!!\n\n")
  time.sleep(1* Story_Speed)
  Game_TXT("Sirens roared as I hid behind the closed stalls as Speakers across O-sul grew loud and spoke.\n\n")
  time.sleep(3* Story_Speed)
  Game_TXT("Speakers: Ha'e ndaha'etama haguã....!!*" + Player_Name + " turns on translation devices\n")
  time.sleep(0.5* Story_Speed)
  Game_TXT("...ur great statue of Tau has been toppled by outsiders, the REBELS OF O-SUL. WHAT GREAT DEFIANCE THEY HAVE, Caos, rise up and defend your true homeland from colonizers. Defend the great Tau!!!!!\n\n")
  time.sleep(5* Story_Speed)
  Game_TXT(Player_Name_Dialouge + "This is a troubling situation, but I can use this against the Caos, I just need to do something while they are weak? What do I doooo!")
  time.sleep(4* Story_Speed)
  if Testing_Caution == False:
    pass
  else:
    Testing_Notion = input("\nIf you want to continue testing, input \"C\", If you want to stop testing and return to testing hub, input \"T\", or If you want to stop the program entirely, input \"S\": ")
    if Testing_Notion == "C":
      pass
    elif Testing_Notion == "T":
     Narrative_Testing_hub()
    else:
      exit()
  Game_TXT(Player_Name + " got an idea, I can either ignite the workers while all the tribal members have gone to fight the rebels, or I could go inside the Core parts of O-sul to take down their leaders? (W/C) ")
  time.sleep(6* Story_Speed)
  Uprise_or_Anarchy = input(" ")
  if Uprise_or_Anarchy.lower() == "w":
    Uprise(Player_Name, Player_Name_Dialouge, Testing_Caution, Decision_Num, Story_Speed)
  elif Uprise_or_Anarchy.lower() == "c":
    Anarchy(Player_Name, Player_Name_Dialouge, Testing_Caution, Decision_Num, Story_Speed)
def Redeemer(Player_Name, Player_Name_Dialouge, Testing_Caution, Decision_Num, Story_Speed):
  Game_TXT("\n")
  Decision_Num.append("1")
  Game_TXT("\nAs {} steps into the moonlight, the shadows cling to them like a cloak. {} is ready.".format(Player_Name, Player_Name))
  time.sleep(3* Story_Speed)
  Game_TXT("\nThe rebels, caught off guard, turn with surprise as they point their pulsars in {}'s direction.".format(Player_Name))
  time.sleep(3* Story_Speed)
  Game_TXT("\nUnknown: Who are you? What are you doing here? He must be with the Caos! Hands up if you wanna live!")
  time.sleep(3* Story_Speed)
  Game_TXT("\n{} calmly raises their hands, pulsars pointed at them. The tension in the air is palpable.\n".format(Player_Name))
  time.sleep(3* Story_Speed)
  Game_TXT("\nUnknown: Speak! Why should we trust you?\n")
  time.sleep(2* Story_Speed)
  Game_TXT("{}I am not with the Caos, trust me. I want O-sul to return back to Río. Do whatever you want to ensure your safety.".format(Player_Name_Dialouge))
  time.sleep(3* Story_Speed)
  Game_TXT("\nTheir leader signals one of the men, they attach something to {}\n".format(Player_Name))
  time.sleep(2* Story_Speed)
  Game_TXT("\nUnknown: We attached something to you that can't be opened without a passcode\n")
  time.sleep(2* Story_Speed)
  Game_TXT("Unknown: We'll give ya the passcode after you have proven your loyalty, but if ya even think about decievin' us, that attachment will explode with ya, ¡Entende!\n")
  time.sleep(5* Story_Speed)
  Game_TXT("{}Yes I understand, I will do anything for Río, now tell me what's our plan?\n".format(Player_Name_Dialouge))
  time.sleep(2* Story_Speed)
  Game_TXT("Unknown: Ok, let's get to it, I'm Alpha, leader of the rebels, and we are heading to the Reedemer.\n")
  time.sleep(3* Story_Speed)
  Game_TXT("Alpha: The reedemer was what stood before that hideous god, Tau, we will topple their diety like they have toppled ours, Rebels!!! We will take back our Río!!!!!!\n")
  time.sleep(5* Story_Speed)
  Game_TXT("The daring speech brought everybody power, and as they reached the shore of O-sul. They readied their weapons to fight.\n\n")
  time.sleep(4* Story_Speed)
  Game_TXT("The rebels with {} got to the reedemer, {} ran to the foot of Tau and realized the rebels weren't with him, but behind him, about 50 feet away.\n".format(Player_Name, Player_Name))
  time.sleep(5* Story_Speed)
  Game_TXT("A rebel threw a grenade at your feet, it released a solution that binded your feet to the ground\n")
  time.sleep(3* Story_Speed)
  Game_TXT("{}What is this? I can't move. Unbind me, we're part of the same team.\n")
  time.sleep(2* Story_Speed)
  Game_TXT("Alpha: We are, but you will help us acheive this goal of toppling Tau, that attached device never had a passcode\n")
  time.sleep(3* Story_Speed)
  Game_TXT("Alpha: We can't risk ya running with any information, consider this a great help to the rebellion, I'm sorry {}, this is the only way.".format(Player_Name))
  time.sleep(4* Story_Speed)
  Game_TXT("\n{} closed their eyes, and waited for something................................................BOOM!!!\n\n".format(Player_Name))
  time.sleep(4* Story_Speed)
  Game_TXT("The statue fell with your life.\n")
  time.sleep(2* Story_Speed)
  Game_TXT("You haven't completed the story, your choices led you here, make some different ones to survive...\n")
  time.sleep(3* Story_Speed)
  for x in Decision_Num:
    print(x, end='')
  if Testing_Caution == False:
    pass
  else:
    Testing_Notion = input("\nIf you want to continue testing, input \"C\", If you want to stop testing and return to testing hub, input \"T\", or If you want to stop the program entirely, input \"S\": ")
    if Testing_Notion == "C":
      pass
    elif Testing_Notion == "T":
     Narrative_Testing_hub()
    else:
      exit()
def Anarchy(Player_Name, Player_Name_Dialouge, Testing_Caution, Decision_Num, Story_Speed):
  print("\n")
  Decision_Num.append("0")
  print("\nThe Anarchy ending will be added in version 0.9 - São Paolo\nVersion São Paolo Release Date: 4/13/24")
def Uprise(Player_Name, Player_Name_Dialouge, Testing_Caution, Decision_Num, Story_Speed):
  Game_TXT("\n\n")
  Decision_Num.append("1")
  Game_TXT("\nAs chaos spreads across O-sul and the great statue of Tau is toppled, " + Player_Name + " embarks on a daring mission.\n\n")
  time.sleep(3* Story_Speed)
  Game_TXT(Player_Name_Dialouge + "To reclaim O-sul, I need a strong force by my side.\n")
  time.sleep(3* Story_Speed)
  Game_TXT("\n" + Player_Name + " sneaks through the darkened streets and hidden alleys, searching for the oppressed workers and slaves.\n\n")
  time.sleep(4* Story_Speed)
  Game_TXT("In the shadow of the looming factories, " + Player_Name + " finds groups of workers and slaves held captive by the Caos.\n\n")
  time.sleep(5* Story_Speed)
  Game_TXT(Player_Name_Dialouge + "My fellow brothers and sisters, today is the day we break free from the chains that bind us.\n\n")
  time.sleep(4* Story_Speed)
  Game_TXT(Player_Name_Dialouge + "The Caos may have tried to oppress us, but together, we have the power to defy them!\n\n")
  time.sleep(4* Story_Speed)
  Game_TXT("\nThe workers and slaves, fueled by " + Player_Name + "'s words, rise with newfound determination.\n\n")
  time.sleep(4* Story_Speed)
  Game_TXT("They grab whatever tools they can find, turning them into makeshift weapons to fight for their freedom.\n\n")
  time.sleep(5* Story_Speed)
  Game_TXT(Player_Name_Dialouge + "Today, we stand united against the Caos, for a future where we determine our own destiny!\n")
  time.sleep(4* Story_Speed)
  Game_TXT("\nWith a united force, " + Player_Name + " leads the workers and slaves towards the heart of the city - the Redeemer statue.\n\n")
  time.sleep(5* Story_Speed)
  Game_TXT("The sound of battle draws near as they approach the epicenter of the conflict.\n\n")
  time.sleep(4* Story_Speed)
  Game_TXT(Player_Name_Dialouge + "We will make our stand here! Together, we fight for the liberation of O-sul!\n\n\n")
  time.sleep(4* Story_Speed)
  Game_TXT("\n*** The Battle of O-sul Unfolds ***\n\n")
  time.sleep(3* Story_Speed)
  Game_TXT("The original rebels clash fiercely with the natives, but they are outnumbered and face a challenging fight.\n\n")
  time.sleep(5* Story_Speed)
  Game_TXT("Just when it seems like all hope is lost, the unexpected alliance of workers and slaves enters the fray.\n\n")
  time.sleep(6* Story_Speed)
  Game_TXT("The natives are caught by surprise as the workers and slaves unleash their determination and power.\n\n")
  time.sleep(5* Story_Speed)
  Game_TXT("With newfound strength, the workers overwhelm the natives and force them to surrender.\n\n")
  time.sleep(5* Story_Speed)
  Game_TXT("The victory belongs to the workers and slaves of O-sul, who have fought valiantly for their freedom.\n\n")
  time.sleep(5* Story_Speed)
  Game_TXT(Player_Name_Dialouge + "Today, we have achieved the impossible. O-sul is now free from tyranny!\n\n\n")
  time.sleep(4* Story_Speed)
  Game_TXT("\n*** O-sul Transforms into a Worker's-State ***\n\n")
  time.sleep(4* Story_Speed)
  Game_TXT("In the aftermath of the battle, O-sul undergoes a transformation.\n\n")
  time.sleep(4* Story_Speed)
  Game_TXT("The workers and slaves join forces and establish a worker's-state, governed by their own people.\n\n")
  time.sleep(5* Story_Speed)
  Game_TXT("This will be a land of equality and freedom for all its citizens.\n\n")
  time.sleep(4* Story_Speed)
  Game_TXT("Thus, The Proletariat State of South-East Brazil was born, it forged friendly relations with the Federation of Neo-Brazil and ceded back their capital district.\n\n")
  time.sleep(6* Story_Speed)
  Game_TXT(Player_Name + " had accomplished his task, what would await for " + Player_Name + " next...\n\n")
  time.sleep(3* Story_Speed)
  Game_TXT("You have completed the story, find more endings and more scenarios, the world will change at your decisions...\n")
  time.sleep(2* Story_Speed)
  for x in Decision_Num:
    print(x, end='')
def Start():
    Selection = input("Are you a player or a dev? ")
    if Selection.lower() == "dev":
        Credentials_log = {"Polaris": "Semper.Nos", "Alpha": "Star.Dream"}
        Credentials_num = [17081779, 223687638973]
        Attempts = 3
        while Attempts > 0:
            Credentials_type = input("What Credentials do you wish to input to gain gateway into the developer testing hub: (User/Num) ")
            if Credentials_type.lower() == "user":
                Username = input("Developer Username: ")
                Password = getpass("Developer Password: ")
                if Username in Credentials_log and Password == Credentials_log[Username]:
                    print("Authorization granted.")
                    print("Welcome", Username)
                    Test_Type = input("What do you want to access? (Logs/Story Testing) ")
                    while not (Test_Type.lower().startswith("log") or Test_Type.lower().startswith("sto")):
                     Test_Type = input("Invalid input, please try again: (Logs/Story Testing) ")
                    if (Test_Type.lower()).startswith("log"):
                     Logs()
                     break
                    elif (Test_Type.lower()).startswith("sto"):
                     Narrative_Testing_hub()
                     break
                else:
                    print("Invalid Username or Password.")
                    Attempts -= 1
                    print("Attempts remaining:", Attempts)
            elif Credentials_type.lower() == "num":
                Numerical_safety = int(getpass("Developer Number:  "))
                if Numerical_safety in Credentials_num:
                    print("Numerical safety code accepted.")
                    print("Authorization granted.")
                    print("Welcome Developer " + str(Numerical_safety))
                    Test_Type = input("What do you want to access? (Logs/Story Testing) ")
                    while not (Test_Type.lower().startswith("log") or Test_Type.lower().startswith("sto")):
                     Test_Type = input("Invalid input, please try again: (Logs/Story Testing) ")
                    if (Test_Type.lower()).startswith("log"):
                     Logs()
                     break
                    elif (Test_Type.lower()).startswith("sto"):
                     Narrative_Testing_hub()
                     break
                else:
                    print("Invalid Numerical Safety Code.")
                    Attempts -= 1
                    print("Attempts remaining:", Attempts)
            else:
                print("Invalid Credentials type.")
                Attempts -= 1
                print("Attempts remaining:", Attempts)
        if Attempts == 0:
            print("Redirecting to Game.")
            os.system('clear')
            Affiliation()
    else:
        print("Welcome Player.")
        print("\n\n")
        Affiliation()
Start()