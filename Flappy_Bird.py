import pygame
import random
import sys
import os

def resource_path(file_name):
    if hasattr(sys,'_MEIPASS'):
        return os.path.join(sys._MEIPASS, file_name)
    else:
        return filename
    
pygame.init()

screen = pygame.display.set_mode([1500,1500])
pygame.display.set_caption('Flappy Birds')
running = True
player = pygame.image.load(resource_path("bird.png"))
Player = pygame.transform.scale(player,(50,50))
top_pipe = pygame.image.load(resource_path("pipe_top.png"))
Top_pipe_1 = pygame.transform.scale(top_pipe,(150,600))
Top_pipe_2 = pygame.transform.scale(top_pipe,(150,650))
Top_pipe_3 = pygame.transform.scale(top_pipe,(150,700))
Top_pipe_4 = pygame.transform.scale(top_pipe,(150,750))
Top_pipe_5 = pygame.transform.scale(top_pipe,(150,800))
bottom_pipe = pygame.image.load(resource_path("pipe_bottom.png"))
Bottom_pipe_1 = pygame.transform.scale(bottom_pipe,(150,600))
Bottom_pipe_2 = pygame.transform.scale(bottom_pipe,(150,650))
Bottom_pipe_3 = pygame.transform.scale(bottom_pipe,(150,700))
Bottom_pipe_4 = pygame.transform.scale(bottom_pipe,(150,750))
Bottom_pipe_5 = pygame.transform.scale(bottom_pipe,(150,800))

width = 1500
height = 1500

TOP_PIPES = [Top_pipe_1,Top_pipe_2,Top_pipe_3,Top_pipe_4,Top_pipe_5]
BOTTOM_PIPES = [Bottom_pipe_1,Bottom_pipe_2,Bottom_pipe_3,Bottom_pipe_4,Bottom_pipe_5]
    
score = 0
ding = pygame.mixer.music.load(resource_path("ding.mp3"))

font = pygame.font.Font(pygame.font.get_default_font(),25)
Score_text = font.render('Score: '+str(score),True,pygame.Color(255,255,255),pygame.Color(0,0,0))
screen.blit(Score_text,(width/2.0,0))
    
pipe_x_loc = random.randint(int(width/2.0),width)
passed = False

BP = random.choice(BOTTOM_PIPES)
TP = random.choice(TOP_PIPES)

pipe_speed = [1,2,3,4,5]

screen.fill("blue")
screen.blit(Player,(width/2.0,height/2.0))
screen.blit(TP,(pipe_x_loc,0))
screen.blit(BP,(pipe_x_loc,height/2.0))
y = height/2.0

while running:
    y = y + 2
    pipe_x_loc = pipe_x_loc - random.choice(pipe_speed)
    screen.fill("blue")
    font = pygame.font.Font(pygame.font.get_default_font(),25)
    Score_text = font.render('Score: '+str(score),True,pygame.Color(255,255,255),pygame.Color(0,0,0))
    screen.blit(Score_text,(width/2.0,0))
    screen.blit(Player,(width/2.0,y))
    screen.blit(TP,(pipe_x_loc,0))
    screen.blit(BP,(pipe_x_loc,height/2.0))
    if pipe_x_loc <= 0:
        pipe_x_loc = random.randint(int(width/2.0),width)
        BP = random.choice(BOTTOM_PIPES)
        TP = random.choice(TOP_PIPES)
        screen.blit(TP,(pipe_x_loc,0))
        screen.blit(BP,(pipe_x_loc,height/2.0))
        passed = False
    if (pipe_x_loc <= 1.1*width/2.0 and pipe_x_loc >= 0.9*width/2.0 and y <= 0.8*TP.get_height()) or (pipe_x_loc <= 1.1*width/2.0 and pipe_x_loc >= 0.9*width/2.0 and y >= 1.2*BP.get_height()):
        quit()
    if pipe_x_loc <= 0.9*width/2.0 and not passed:
        score = score + 1
        passed = True
        pygame.mixer.music.play()
        font = pygame.font.Font(pygame.font.get_default_font(),25)
        Score_text = font.render('Score: '+str(score),True,pygame.Color(255,255,255),pygame.Color(0,0,0))
        screen.blit(Score_text,(width/2.0,0))
        
    if y >= 53*height/80:
        quit()
        
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                y = y - 100
                screen.fill("blue")
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()
