import os

# Optional: Terminal beep for fun effect (works on most systems)
os.system('echo \a')  # Beep when game starts

print(r"""
╔════════════════════════════════════════════╗
║  🌟 THE MYSTERIOUS DOOR IN YOUR CLOSET 🌟  ║
╚════════════════════════════════════════════╝
""")

intro_para = """One lazy afternoon, you're cleaning your room when you notice something strange:
A small wooden door has appeared at the back of your closet.
You swear it wasn't there yesterday.
A glowing note pinned to the door reads:
“Only the brave may enter. Choose wisely.”
You gulp. Your heart races.
What do you do?
"""
print(intro_para)

first_choices = """🧭 FIRST CHOICE:
A. Open the door and step inside
B. Call your best friend to come over and investigate
C. Close the closet and pretend it’s not there
"""
print(first_choices)

choice1 = input("What did you do? (A/B/C): ").strip().upper()

if choice1 == "A":
    print("\n" + """A. You open the door and step inside…
You crawl through the door, which opens into a long tunnel made of swirling colors. It feels like you're falling upward. Suddenly, you land gently on grass.
You're in a magical forest, filled with floating lanterns, talking animals, and trees that whisper in rhyme.
A fox wearing spectacles walks up to you and says:
"You must choose your quest. Do you wish to seek the Crystal Banana 🍌 or tame the Sky Whale 🐳?"
Choose:
A1. Seek the Crystal Banana
A2. Tame the Sky Whale
""")
    choiceA = input("What do you choose? (A1/A2): ").strip().upper()
    if choiceA == "A1":
        print("\n" + """A1. You seek the Crystal Banana…
The fox hands you a map, which leads you through a jungle of bouncing mushrooms and river rafts made of vines.
You finally reach a giant stone banana pedestal. But it’s guarded by…
a tribe of monkeys wearing capes!
They challenge you to a banana pun contest.

You clear your throat and deliver your best pun:
"I find this whole thing… a-peeling."

The monkeys erupt in laughter and begin clapping with their feet.

Their leader says, “You may take the Crystal Banana! But first, choose your reward:”
1. 🍕 A never-ending pizza fountain
2. 🐾 The ability to talk to animals
3. 🔁 Return and try a different path
""")

        reward = input("Choose your reward (1/2/3): ").strip()
        if reward == "1":
            print("You now live in a pizza-powered castle. Pizza falls like waterfalls. Life is saucy and full of cheese!")
        elif reward == "2":
            print("You can now talk to animals! You become a global ambassador for human-animal peace treaties. Your pet starts giving you sass.")
        elif reward == "3":
            print("Suddenly, you’re whisked back to the fork in the forest. The fox blinks and says, 'Deja vu? Let's try again.'")
        else:
            print("The monkeys tilt their heads. 'That’s not a choice, banana-brain!' They send you home with banana confetti.")

    elif choiceA == "A2":
        print("\n" + """A2. You try to tame the Sky Whale…
The fox hands you a magical flute.
“Climb the Cloud Staircase and play this,” he says.
You scale the clouds until you see the enormous, floating Sky Whale — gliding through the sky with stars on its back.
You play the tune… and it works! The whale bows its head.
You now soar across the skies as Captain of the Clouds, eating ice cream with sky pirates and living among stardust.""")
    else:
        print("Oops! That wasn't a valid quest.")

elif choice1 == "B":
    print("\n" + """B. You call your best friend to investigate…
Your friend rushes over and says, “No way. Is this Narnia 2.0?”
You both step through the door together and land in a board game world.
Each square on the ground is a new challenge.
A talking dice bounces over and shouts:
“Roll me to begin your quest!”
You roll a 6. The dice cheers, and you're teleported to…
Choose:
B1. A lava parkour obstacle course
B2. A quiz game hosted by a penguin in a tuxedo
B3. A dance battle against a disco robot
""")
    choiceB = input("Which challenge do you face? (B1/B2/B3): ").strip().upper()
    if choiceB == "B1":
        print("\n" + """B1. Lava Parkour
You and your friend leap across floating rocks as lava bubbles beneath you.
You both just barely make it, earning shoes that let you fly for 10 seconds.
You use the shoes to fly out of the game and back into your room.
You high-five each other. That was wild.""")
    elif choiceB == "B2":
        print("\n" + """B2. Quiz Game
The penguin says:
“Get three questions right, and you may leave with treasure!”
You ace the quiz thanks to your friend's random obsession with trivia.
You win a glowing snow globe that can show you the future for 10 seconds per shake.
You both stare into it and see…
You acing your final exams and eating cake the size of a car.""")
    elif choiceB == "B3":
        print("\n" + """B3. Dance Battle
The disco robot spins, breakdances, and moonwalks to funky music. Lasers shoot from its chest in sync with the beat.
Your friend goes first, doing the worm and a double spin.
Now it’s your turn…

You break into The Electric Slide followed by the Griddy, then finish with a mid-air backflip!
The crowd of NPCs goes wild.

The robot claps and ejects a glittery golden record from its chest.

“This grants you the power to teleport to **any concert in history**,” it says.

Where do you go?
1. 🎤 Queen Live at Wembley Stadium
2. 🎧 A Billie Eilish secret show
3. 🎼 Beethoven’s first piano symphony
""")
        concert = input("Choose your concert (1/2/3): ").strip()
        if concert == "1":
            print("You’re in the front row, screaming 'We Will Rock You' with 72,000 fans. Freddie Mercury winks at you mid-song.")
        elif concert == "2":
            print("You appear in a neon-lit underground stage. Billie notices your entrance and shouts, 'Special guest in the house!'")
        elif concert == "3":
            print("You're sitting next to Mozart, who whispers, 'This dude’s got potential.' You nod in awe as Beethoven begins playing.")
        else:
            print("The robot scratches its head. 'No groove detected in that choice.' It sends you to a silent disco instead.")
    else:
        print("Oops! That wasn't a valid challenge.")

elif choice1 == "C":
    print("\n" + """C. You close the closet and pretend it’s not there…
You go back to scrolling on your phone.
But that night, you hear whispering from the closet.
You open it again — the door is gone.
You missed your chance.
Or did you?
You go to sleep. But when you wake up…
There’s a trapdoor under your bed.
And this time, the note says:
"Second chances are rare. You’re lucky."
✨ The End…? ✨""")

else:
    print("Invalid choice. Please restart the game.")
