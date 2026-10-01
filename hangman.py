import random
import pygame
import time

#500, 300 center of the window 

###PYGAME###
pygame.mixer.init()
pygame.init()
screen_width = 1920
screen_height = 980
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

# Colors (Red, Green, Blue)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)
purple = (128, 0, 128)
pink = (255, 192, 203)
orange = (255, 165, 0)
brown = (165, 42, 42)
cyan = (0, 255, 255)
light_blue = (173, 216, 230)
light_green = (144, 238, 144)
light_yellow = (255, 255, 224)
light_purple = (221, 160, 221)
light_pink = (255, 182, 193)
# Sets the title of the window and other properties
def setup(Difficulty, word_list, wrong_value, max_attempts, guessed_letter, word, sentence_list, list_1):
    if Difficulty is not None:
        render_text("GUESS A LETTER ", 35, black, (750, 200))
        render_text(f"Difficulty: {Difficulty}", 38, black, (370, 150))
        render_text(' '.join(word_list).upper(), 60, black, (600, 750))
        render_text(f"Guessed Letters: {', '.join(guessed_letter)}", 30, black, (50, 50))
        render_text(f'Attempts left: {max_attempts - wrong_value}', 30, black, (1600, 55))
        if wrong_value >= 3:
            render_text(sentence_list[list_1.index(word)], 30, black, (800, 350))
# DRAW HANGMAN
def draw_hangman(wrong_value):
    if wrong_value > 0:
        pygame.draw.circle(screen, black, (700, 305), 45, 5) #head
    if wrong_value > 1:
        pygame.draw.line(screen, black, (700, 350), (700, 520), 5) #body
    if wrong_value > 2:
        pygame.draw.line(screen, black, (700, 400), (740, 450), 5) #right arm
    if wrong_value > 3:
        pygame.draw.line(screen, black, (700, 400), (660, 450), 5) #left arm
    if wrong_value > 4:
        pygame.draw.line(screen, black, (700, 520), (740, 570), 5) #right leg
    if wrong_value > 5:    
        pygame.draw.line(screen, black, (700, 520), (660, 570), 5) #left leg



# HANDLE GUESSING
def handle_guess(word, word_list, wrong_value, max_attempts, guessed_letter):

    event = pygame.event.wait()
    Input = pygame.key.name(event.key)
    Correct_Answer = pygame.mixer.Sound("Correct_Ans.wav")
     
    if Input in word:
        for i in range(len(word)):
            if word[i] == Input:
                word_list[i] = Input
        print(f"Updated word_list: {word_list}")
        guessed_letter.append(Input)
        Correct_Answer.play()
        pygame.time.delay(500)
    elif Input not in word:
        wrong_value += 1
        guessed_letter.append(Input)
        pygame.mixer.music.load("wrong_ans.mp3")
        pygame.mixer.music.play()
        pygame.time.delay(500)
    return wrong_value

        

 # Render the text
def render_text(text, font_size, color, position):        
    font = pygame.font.SysFont("comicsansms", font_size)  
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(topleft=position)
    screen.blit(text_surface, text_rect)
    
# Game loop
def graphics():
    guessed_letter = []
    sentence_list = []
    list_1 = []
    word_list = []
    word = ''
    wrong_value = 0
    max_attempts = 6
    running = True
    Difficulty = ''
    while running:
        screen.fill(light_blue)
        render_text('HANGMAN', 50, black, (800, 45))
        render_text('Choose a difficulty level (1, 2, or 3)', 30, black, (750, 95))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if Difficulty == '':
                    ###DIFFICULTY###

                    ###EASY###
                    if event.key == pygame.K_1:
                        Difficulty = 'EASY'
                        list_1 = ["apple", "banana", "pencil", "rabbit", "flower", "turtle", "cookie", "soccer", "puzzle", "crayon"]
                        word = random.choice(list_1)
                        
                        ###PRONUNCIATION###
                        pronunciation = [
                        'AP-uhl',
                        'buh-NAN-uh',
                        'PEN-suhl',
                        'RAB-it',
                        'FLOW-er',
                        'TUR-tuhl',
                        'KOO-kee',
                        'SOK-er',
                        'PUH-zuhl',
                        'KRAY-uhn',
                        ]
                        ###SENTENCE###
                        sentence_list = [
                        "I ate a juicy _____.",
                        "She peeled a _____.",
                        "Please use a _____ to write your name.",
                        "The fluffy ______ hopped across the field.",
                        "The red _____ smelled very sweet.",
                        "A slow ____ walked on the beach.",
                        "I want a yummy _____ after dinner.",
                        "We played _____ at the park.",
                        "The _____ was fun to solve.",
                        "I drew a rainbow with my _____."
                        ]
                        ###DEFINITION###
                        definitions = [
                            'A red fruit',       
                            'A yellow fruit', 
                            'A writing tool', 
                            'A small animal', 
                            'A blooming plant', 
                            'A slow-moving and hard shell reptile', 
                            'A sweet baked good', 
                            'A sport played with a ball', 
                            'A game with pieces to fit together', 
                            'A colored wax stick for drawing'
                        ]

                        word_list = ["_"] * len(word)

                    ###MEDIUM###
                    elif event.key == pygame.K_2:
                        Difficulty = 'MEDIUM'
                        list_1 = ["library", "mountain", "computer", "adventure", "instrument", "celebrate", "challenge", "knowledge", "structure", "community"]
                        word = random.choice(list_1)
                        Difficulty = 'MEDIUM'
                        ###PRONUNCIATION###
                        pronunciation = [
                            "lie-brer-ee", 
                            "moun-tin", 
                            "com-pyoo-ter", 
                            "ad-ven-chur", 
                            "in-struh-ment", 
                            "sel-uh-brayt", 
                            "chal-lenj", 
                            "nol-ij", 
                            "struk-chur", 
                            "com-myoo-nih-tee"
                            ]

                        ###DEFINITION###
                        definitions = [
                            'A place with books', 
                            'A high landform', 
                            'An electronic device', 
                            'An exciting experience', 
                            'A musical tool', 
                            'To mark a special occasion', 
                            'A test of skill or ability', 
                            'Information and understanding', 
                            'A physical construction', 
                            'A group of people living together'
                        ]
                        ###PRONUNCIATION###
                        pronunciation = [
                        "LIE-brer-ee",
                        "MOUN-tin",
                        "kum-PYOO-ter",
                        "ad-VEN-cher",
                        "IN-struh-ment",
                        "SEL-uh-brayt",
                        "CHAL-enj",
                        "NOL-ij",
                        "STRUK-cher",
                        "kum-MYOO-ni-tee"
                        ]
                            ###SENTENCE###
                        sentence_list = [
                        "I went to the _______ to find books.",
                        "We climbed up the _____ to see the view.",
                        "I use the _____ to play video games.",
                        "Let's go on an ______ to the park.",
                        "She used the _____ to make music.",
                        "We will _______ with cake and balloons.",
                        "The puzzle is a ______ to solve.",
                        "Reading gives you ______ about the world.",
                        "The bridge is a tall _________ to cross.",
                        "Our _________ had a fun picnic."
                        ]

                        word_list = ["_"] * len(word)
                    
                    ###HARD###
                    elif event.key == pygame.K_3:
                        list_1 = ["algorithm", "hypothesis", "photosynthesis", "jurisdiction", "ambivalence", "metamorphosis", "extraterrestrial", "consequential", "discrepancy", "paradoxical"]
                        word = random.choice(list_1)
                        Difficulty = 'HARD'
                            ###DEFINITION###
                        definitions = [
                            'Step-by-step problem solving',
                            'Proposed explanation',
                            'Plant food making using sunlight',
                            'Official legal power',
                            'Mixed, conflicting feelings',
                            'Immature to adult transformation',
                            'From beyond Earth',
                            'Logical result',
                            'Difference, inconsistency',
                            'Related to self-contradictory truth'
                        ]
                        
                        ###PRONUNCIATION###
                        pronunciation = [
                            "AL-guh-ri-thum",
                            "hy-PAH-thuh-sis",
                            "foh-tuh-SIN-thuh-sis",
                            "jur-is-DIK-shun",
                            "am-BIV-uh-lents",
                            "met-uh-MOR-fuh-sis",
                            "eks-truh-tuh-RES-tree-ul",
                            "kon-si-KWEN-shul",
                            "dis-KREP-un-see",
                            "par-uh-DOKS-i-kul"
                        ]
                        ###SENTENCE###
                        sentence_list = [
                        "The _________ helps the robot move.",  
                        "My _________ was about the plant's growth.",
                        "______________ helps the tree make food.",
                        "The court has __________ over the town.",
                        "He felt ____________ about which toy to choose.",
                        "The bug's _________ changed it into a butterfly.",
                        "Is there ________________ life in space?",
                        "His actions were ____________ for his friends.",
                        "There was __________ in the number of cookies.",
                        "That's a _________ idea, like a square circle.",
                        ]

                        word_list = ["_"] * len(word)  
                    else:
                        render_text("Please choose a valid difficulty level (1, 2, or 3)", 30, red, (750, 150))
                        pygame.time.delay(2000)
                elif Difficulty != '' and "_" in word_list and wrong_value < max_attempts:
                    wrong_value = handle_guess(word, word_list, wrong_value, max_attempts, guessed_letter)

        # Draw a line (screen, color, start_pos, end_pos, width)
        pygame.draw.line(screen, black, (225, 800), (515, 800), 5)  # Base
        pygame.draw.line(screen, black, (370, 800), (370, 200), 5)  # Vertical pole
        pygame.draw.line(screen, black, (370, 200), (700, 200), 5)  # Horizontal pole
        pygame.draw.line(screen, black, (700, 200), (700, 260), 5)  # Rope
        pygame.draw.line(screen, black, (370, 250), (420, 200), 10)  # Diagonal support
        draw_hangman(wrong_value)  # Draw the hangman based on wrong_value
       
        setup(Difficulty, word_list, wrong_value, max_attempts, guessed_letter, word, sentence_list, list_1)

        if "_" not in word_list and Difficulty != '':
            render_text("You won!", 50, green, (750, 150))
            render_text(f"Definition:{definitions[list_1.index(word)]}", 20, black, (1500, 400))
            render_text(f"Pronunciation: {pronunciation[list_1.index(word)]}", 20, black, (1500, 430))
            pygame.display.flip()
            pygame.mixer.music.load("win_sound.mp3")
            pygame.mixer.music.play()
            pygame.time.delay(10000)
            
            running = False
        
        elif wrong_value >= max_attempts:
            render_text("You lost!", 50, red, (750, 150))
            render_text(f"The word was: {word}", 30, black, (800, 520))
            render_text(f"Definition: {definitions[list_1.index(word)]}", 20, black, (1500, 400))
            render_text(f"Pronunciation: {pronunciation[list_1.index(word)]}", 20, black, (1500, 430))
            pygame.display.flip()
            pygame.mixer.music.load("lose_sound.mp3")
            pygame.mixer.music.play()
            pygame.time.delay(10000)
            running = False
            

        # Update the display
        clock.tick(60)  # Limit the frame rate to 60 FPS
        pygame.display.flip()

    pygame.quit()    
   
graphics()