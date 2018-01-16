import os
import time
batteryimg="""
╔══════════════════════╗
║╔════════════════════╗╚╗
║║████████████████████╚╗╚╗
║║███████Full Battery  ║║║
║║████████████████████╔╝╔╝
║╚════════════════════╝╔╝
╚══════════════════════╝"""
sfpercent="""
╔══════════════════════╗
║╔════════════════════╗╚╗
║║████████████████\\\\\\\\╚╗╚╗
║║█████75% Battery     ║║║
║║████████████████\\\\\\\\╔╝╔╝
║╚════════════════════╝╔╝
╚══════════════════════╝"""
x = 0
playerHealth = 100
batteryCharge = 100
trycount = 0
while x == 0:
	os.system('cls')
	answer = input("  How do you feel about car batteries? \n1.Strangely excited \n2.Fuck you\n>")
	options = ["You are seated on a hard chair, a table is in front of you.", "Straighten up and fly right or you gonna get got boy, 3 chances total\n"]
	try: 
		int(answer)
	except ValueError:
		print("That's not a number ya dingus")
		break
		os.system('cls')

	if int(answer) == 1 and trycount != 2:
		os.system('cls')
		print(options[0])
		print("\nOn the table is a shining fork, it calls for you. You can feel it throbbing with creative energy")
		answer = input("1.Jab it in your eye\n>")
		try: 
			int(answer)
		except ValueError:
			print("That's not a number ya dingus")
			time.sleep(2)
			break
			
		if int(answer)==1:
			playerHealth=75
			os.system('cls')
			print("Your vision darkens, everything is black for a time")
			time.sleep(2)
			os.system('cls')
			print("Suddenly you come to, the fork in your hand is gone, you feel empty, drained")
			time.sleep(4)
			os.system('cls')
			print("The feeling of emptiness vanishes as you realize that on the table in front of you is a battery")
			print(batteryimg)
			time.sleep(2)
			print("A thought occurs to you... What if you were to fulfil your darkest, sauciest desire?")
			print("you've always wanted to try it, but your dad was always very adamant that nipples were only for looking nice and pointing places when it was cold out")
			answer = input("\nDo you taste of the forbidden fruit?\n1.fry them badbois\n2.No it is not of god\n>")
			try: 
				int(answer)
			except ValueError:
				print("That's not a number ya dingus")
				break
			time.sleep(2)
			
			if int(answer) == 1:
				os.system('cls')
				print("You cannot resist, it's not like there's anyone here to judge you anyway, and plus since Jonathon left your juice hasn't been able to flow")
				time.sleep(7)
				os.system('cls')
				print("Your hands shake, your temples throb, you've wanted this for so long but now that the time is here... Are you ready?")
				time.sleep(5)
				print("You cannot wait any longer, you surrender yourself to your passions")
				time.sleep(5)
				print("You grab the battery, you thrust one terminal to each nipple and suddenly...")
				time.sleep(3)
				os.system('cls')
				print("B")
				time.sleep(1)
				print("A")
				time.sleep(1)
				print("N")
				time.sleep(1)
				print("G")
				time.sleep(5)
				os.system('cls')
				print("Everything is white, so white it's like a family christmas, you're on the floor")
				playerHealth=75
				time.sleep(7)
				os.system('cls')
				print("You stand up, your vision clears")
				time.sleep(3)
				os.system('cls')
				print("You feel a comforting pressure in your hand, you look down and see the battery, clutched tightly in your palm")
				time.sleep(3)
				print("You open your teacher's fist and bring the battery to your eyes to get a clear look")
				print(sfpercent)
				print("Huh, you say, as you realize you feel back to perfect health... If with very mixed emotions")
				time.sleep(3)
				os.system('cls')
				print("Suddenly you hear a cough and look up")
				time.sleep(5)
				print("God is standing there")
				time.sleep(3)
				print("\"What the fuck man?\" he asks")
				time.sleep(10)
			elif int(answer) == 2:
				print("Purity must be kept intact, you will sit in this room, and marinate in your feelings of self satisfaction")
				time.sleep(10)
				print("Well? Are you happy? the timer gets longer between each message")
				time.sleep(15)
				print("Man, sometimes I wish I could just be an avalanche, you know? Crushing stuff, going fast")
				time.sleep(20)
		else:
			print("Just enter 1 mane")
			trycount+=1
			
	elif int(trycount) <= 1:
		trycount+=1
		print(options[1])
		time.sleep(2.5)
		os.system('cls')
		
	elif int(trycount) >= 2:
		os.system('cls')
		print ("Right, that's it, it's bees for you")
		for i in range(0,20):
			print ("BEES")
			x+=1
		time.sleep(2)
		for i in range(0,20):
			print ("BEES")
	