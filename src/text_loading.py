import pygame
import random
from helper import get_asset_path

pygame.init()
main_font = get_asset_path("assets/font.ttf")
bold_font = get_asset_path("assets/fontbold.ttf")
facts_for_game = [
    "At least 1,000 sea turtles die each year due to plastic. Thats more than 1 turtle every 9 hours!",
    "By 2050, there will be more plastic than fish in the ocean!",
    "More than 100,000 marine animals die each year due to plastic."
    ]
fact_on_menu = str(random.choice(facts_for_game))
question_font = pygame.font.Font(main_font, 30)
question_font2 = pygame.font.Font(main_font, 20)
submit_text = question_font.render("Press Enter to Submit", True, (0,0,0))
math_questions = ["If there are 12 dolphins swimming in the ocean, and 9 more join them, how many dolphins are there now?", "A fisherman catches 25 fish in the morning and 14 in the afternoon. How many fish did he catch in total?",
                  "If there are 8 turtles on a beach and each turtle lays 5 eggs, how many eggs are laid in total?", "A group of 36 starfish is divided equally into 6 groups. How many starfish are in each group?",
                  "The coral reef has 1,247 colorful fish. What is the value of the digit 2 in the number 1,247?", "A seashell costs $3, and you have $15. How many seashells can you buy?",
                  "You see 8 whales swimming in the ocean. 3 of them dive deep. What fraction of the whales dived deep?","If a boat takes 45 minutes to reach the island and it leaves at 2:30 PM, what time will it arrive?",
                  "A group of fish is swimming in a repeating pattern: 3 yellow fish, 2 blue fish, 1 red fish. How many fish will be in the pattern after 5 full cycles?",
                  "The beach is shaped like a rectangle with a length of 10 meters and a width of 4 meters. What is the area of the beach?", "A square pond on the beach has a side length of 6 meters. What is the perimeter of the pond?",
                  "A seahorse swims at a speed of 2 miles per hour. How far will it swim in 3 hours?", "A fishing boat catches 125 fish each day. How many fish will it catch in 7 days?",
                  "There are 120 crabs on the beach. If each group of crabs contains 8 crabs, how many groups of crabs are there?", "A giant clam weighs 15 kilograms. How much would 4 giant clams weigh together?",
                  "A school of 256 fish swims past a boat, and 378 more fish follow them. How many fish are there in total?", "You have $25 to spend at an aquarium. You buy 2 tickets at $6 each and a stuffed animal for $7. How much money do you have left?",
                  "A beach has 12 seashells. 4 of them are pink, 3 are blue, and the rest are white. What fraction of the seashells are white?", "An octopus has 8 arms. How many arms do 12 octopuses have in total?",
                  "The ocean has a depth of 3,500 meters in one area and 4,200 meters in another area. Which area is deeper, and by how many meters?"]
math_answers = ["21","39","40","6","200","5","3/8","3:15 PM","30","40","24","6","875","15","60","634","$6","5/12","96","700"]
marine_questions = ["How does plastic pollution affect marine ecosystems?", "What are microplastics?", 
                    "How do microplastics enter the ocean?", "Which source contributes most to ocean plastic pollution?",
                    "What is a major plastic accumulation zone in the ocean?", "How does plastic pollution contribute to climate change?",
                    "What is a potential health risk of microplastics in seafood?", "Which policy helps combat ocean plastic pollution?",
                    "What is a solution to plastic pollution?"
                    ]
marine_mc = [
    "a) It provides shelter for marine life b) It harms animals through ingestion and entanglement c) It improves water quality d) It increases oxygen levels",
    "a) Tiny plastic particles under 5mm b) Large plastic debris in the oceanc) A type of biodegradable plastic d) Plastics that dissolve in water",
    "a) Through wastewater and runoff b) Only from plastic bottles c) Released by deep-sea organisms d) Created naturally by ocean currents",
    "a) It stays in one place b) It sinks immediately c) Carried by ocean currents d) Absorbed by marine organisms",
    "a) Mariana Trench b) The Great Pacific Garbage Patch c) Bermuda Triangle d) Arctic Ocean",
    "a) It increases CO₂ emissions during production b) It releases greenhouse gases as it degrades c) It harms ecosystems that store carbon d) All of the above",
    "a) They contain harmful toxins b) They improve digestion c) They provide extra nutrients d) They boost metabolism",
    "a) UN Global Plastic Treaty b) Open Ocean Dumping Initiative c) Plastic Promotion Act d) The Deep-Sea Disposal Program",
    "a) Using biodegradable plastics b) Banning plastic bags c) Ocean cleanup projects d) All of the above"
    ]
marine_answers = ["b", "a", "a", "c", "c", "b", "d", "a", "a", "d"]

main_title_font = pygame.font.Font(bold_font, 65)
main_title_text = main_title_font.render("Save The Turtles", True, (0, 0, 0))
subtitle_font = pygame.font.Font(main_font, 55)
subtitle_text = subtitle_font.render("GASTC Project by Jayden Wu", True, (0, 0, 0))
facts_title_font = pygame.font.Font(bold_font, 40)
facts_title_text = facts_title_font.render("Real Facts:", True, (0, 0, 0))
facts_font = pygame.font.Font(main_font, 25)
facts_text = facts_font.render(str(fact_on_menu), True, (0, 0, 0))
settings_font = pygame.font.Font(main_font, 50)
about_font = pygame.font.Font(main_font, 40)
about_text1 = about_font.render("Save The Turtles - a game by Jayden Wu. In this game, you will navigate a turtle", True, (0, 0, 0))
about_text2 = about_font.render("through multiple plastic obstacles. If you hit plastic, you will lose some health.", True, (0, 0, 0))
about_text3 = about_font.render("Every once in a while, the player is asked a question about a subject of their liking", True, (0, 0, 0))
about_text4 = about_font.render("and if they get it wrong, they will lose points and if they get it right they won't", True, (0, 0, 0))
about_text5 = about_font.render("lose any.", True, (0, 0, 0))
about_text6 = about_font.render("This game is targeted to the younger age group (late elementary) to empower the", True, (0, 0, 0))
about_text7 = about_font.render("earlier generation. The sooner people know, the better.", True, (0, 0, 0))
how_to_play_font = pygame.font.Font(main_font, 40)
how_to_play_text1 = how_to_play_font.render("Use WASD or arrow keys to navigate your turtle! You start with 100 health and each", True, (0, 0, 0))
how_to_play_text2 = how_to_play_font.render("time you hit an obstacle, for example a plastic bag or bottle, you will lose 10 health", True, (0, 0, 0))
how_to_play_text3 = how_to_play_font.render("and slow down a little.", True, (0, 0, 0))
how_to_play_text4 = how_to_play_font.render("Each time you eat a fish, you gain 1 point and each 5 fish you eat you grow a bit.", True, (0,0,0))
how_to_play_text5 = how_to_play_font.render("If you hit a squid, you will lose 15 health and have obscured vision for a short time", True, (0, 0, 0))
how_to_play_text6 = how_to_play_font.render("and also slown down. Survive as long as you can!", True, (0, 0, 0))
display_caps_font = pygame.font.Font(bold_font, 25)
version_text = display_caps_font.render("v. 5.81  mobile is not supported ", True, (0, 0, 0))
challenge_question_font = pygame.font.Font(main_font, 60)
challenge_question_text = challenge_question_font.render("Challenge Question:", True, (0,0,0))

#labels
labels_font = pygame.font.Font(main_font, 30)
play_label_text = labels_font.render("^ Play ^", True, (0, 0, 0))
settings_label_text = labels_font.render("^ Settings ^", True, (0, 0, 0))
about_label_text = labels_font.render("^ About ^", True, (0, 0, 0))
how_to_play_label_text = labels_font.render("^ How To Play ^", True, (0, 0, 0))
quit_label_text = labels_font.render("^ Quit ^", True, (0, 0, 0))

#game labels
game_labels_font = pygame.font.Font(main_font, 25)
game_title_text = game_labels_font.render("Save the Turtles by Jayden Wu", True, (0, 0, 0))
you_lost_font1 = pygame.font.Font(main_font, 80)
you_lost_font2 = pygame.font.Font(main_font, 45)
you_lost_text1 = you_lost_font1.render("You Lost!", True, (0, 0, 0))
you_lost_text2 = you_lost_font2.render("Thousands of turtles and marine animalshave died due to plastic like you", True, (0, 0, 0))
you_lost_text3 = you_lost_font2.render("just did. However, we can put a stop to this. Donating to fundraising", True, (0, 0, 0))
you_lost_text4 = you_lost_font2.render("campaigns that want to stop ocean pollution, for example #TeamSeas, is a", True, (0, 0, 0))
you_lost_text5 = you_lost_font2.render("great way to help. Press R to Restart, or press the exit button to go back to", True, (0, 0, 0))
you_lost_text6 = you_lost_font2.render("the menu.", True, (0, 0, 0))
