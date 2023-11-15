# Import the pygame module
import pygame
import random

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    RLEACCEL,
    K_w,
    K_s,
    K_a,
    K_d,
    K_ESCAPE,
    K_SPACE,
    K_LSHIFT,
    KEYDOWN,
    K_RETURN,
    QUIT,
)

# Define constants for the screen width and height
SCREEN_WIDTH = 256*2.5
SCREEN_HEIGHT = 224*2.1

fullscreen = True

X = 256
Y = 224

#This is the scale of the map image file, scaled to be larger for the full screen effect
map_width = 4113*4
map_height = 1598*4

#This is a variable that is used often for playing audio files
#only once instead of being looped every time the update is called

#This starts at the Menu screen
stage = 'Menu'

playerX = SCREEN_WIDTH //2
playerY = SCREEN_HEIGHT//2

display = pygame.Surface((256,224))
direction = 'Right'

#This is going to be a redefining of sprites from local files to variables within the project.
#SPRITES IN USE FOR LINK:
downAttack = "Down-Attack.png"
downStand = "Down-Standing.png"
downStand2 = "Down-Standing2.png"
downSword = "Down-Sword.png"
downSword2 = "Sword2Down.png"
downArrow="DownArrow.png"
leftAttack = "Left-Attack.png"
leftStand = "Left-Standing.png"
leftStand2 = "Left-Standing2.png"
leftSword = "Left-Sword.png"
leftSword2 = "Sword2Left.png"
leftArrow = "LeftArrow.png"
rightAttack = "Right-Attack.png"
rightStand = "Right-Standing.png"
rightStand2 = "Right-Standing2.png"
rightSword = "Right-Sword.png"
rightSword2 = "Sword2Right.png"
rightArrow="RightArrow.png"
upAttack = "Up-Attack.png"
upStand = "Up-Standing.png"
upStand2 = "Up-Standing2.png"
upSword = "Up-Sword.png"
upSword2 = "Sword2Up.png"
upArrow = "UpArrow.png"

#This helps progresss the Title screen through the list to make it a moving image for the waterfall and the flashing

menustep=1
#This is a global variable for the amount of Lives link has
#This is a global variable that changes the scale of all major sprites at once. This is very handy for quick changes

playerscale=(32,32)

#These are the colors that make the border detection work. If they need to be changed, this changes it for all sprites
green=(0,168,0,255)
brown=(200,76,12,255)
blue=(32,56,236,255)
cave=(124,8,0,255)

#These are the sprites for the Octoroc enemies

#SPRITES IN USE:
OctoRight = 'OctorocRight.png'
OctoRight2 = 'OctorocRight2.png'
OctoLeft = 'OctorocLeft.png'
OctoLeft2 = 'OctorocLeft2.png'
OctoUp = 'OctorocUp.png'
OctoUp2 = 'OctorocUp2.png'
OctoDown = 'OctorocDown.png'
OctoDown2 = 'OctorocDown2.png'
OctoDeath = 'OctorocDeath.png'
#This is the list of images for the title screen, and text screen
menuscreen=['TitleScreen1.png','TitleScreen2.png','TitleScreen3.png','TitleScreen4.png','TitleScreen5.png','TitleScreen6.png','TitleScreen7.png','TitleScreen8.png','TitleScreen9.png','TitleScreen10.png','TitleScreen11.png','TitleScreen12.png','TitleScreen13.png','TitleScreen14.png','TitleScreen15.png','TitleScreen16.png']
storyscreen=['TextScreen.png','TextScreen.png','TextScreen.png','TextScreen.png','GameOver.png']
#This is the gamehud image
gamehud='GameHud.png'
#This is the minipixel for the minimap
mini='MiniPixel.png'
#This is the hearts list for the hearts system
heart_sprites=['FullHeart.png','HalfHeart.png','NoHeart.png']
keycount_sprites=['0Keys.png','1Key.png']
keysprte='Key Sprite.png'
swordhudimgs=['SwordHud1.png','SwordHud2.png']
firepngs=['Fire1.png', 'Fire2.png']
oldman='OldMan.png'

# Define the Player object extending pygame.sprite.Sprite
# The surface we draw on the screen is now a property of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load(downStand).convert_alpha()
        self.surf.set_colorkey((106, 106, 106), RLEACCEL)
        self.image = self.surf
        self.image_scaled = pygame.transform.scale(self.image,playerscale)
        self.surf = self.image_scaled
        Player.rect = self.surf.get_rect()
        self.LinkLives = 3.0
        Player.death=False
        Player.deathcount=0
        Player.pickedupkey = False
        Playerpickedupsword = False
        Player.direction= 'Down'
        Player.step=0
        Player.incave=False
        Player.hassword= False
        Player.swordtick=0

        if stage== 'Menu':
            self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    def checkCollision(self, sprite1, sprite2):
        col = pygame.sprite.collide_rect(sprite1, sprite2)
        if col == True and Octoroc.death==False and sprite2==rock:
            self.LinkLives-=.5
            lives1.update()
            lives2.update()
            lives3.update()
            if Octoroc.randdirection == 1:
                self.rect.y+= 40
                linkhurt.play()
            elif Octoroc.randdirection == 2:
                self.rect.y -= 40
                linkhurt.play()
            elif Octoroc.randdirection == 3:
                self.rect.x += 40
                linkhurt.play()
            elif Octoroc.randdirection == 4:
                self.rect.x -= 40
                linkhurt.play()
            pass
        elif col == True and Octoroc2.death==False and sprite2==rock2:
            self.LinkLives-=.5
            lives1.update()
            lives2.update()
            lives3.update()
            if Octoroc2.randdirection == 1:
                self.rect.y+= 40
                linkhurt.play()
            elif Octoroc2.randdirection == 2:
                self.rect.y -= 40
                linkhurt.play()
            elif Octoroc2.randdirection == 3:
                self.rect.x += 40
                linkhurt.play()
            elif Octoroc2.randdirection == 4:
                self.rect.x -= 40
                linkhurt.play()
            pass
        elif col == True and Octoroc3.death==False and sprite2==rock3:
            self.LinkLives-=.5
            lives1.update()
            lives2.update()
            lives3.update()
            if Octoroc3.randdirection == 1:
                self.rect.y+= 40
                linkhurt.play()
            elif Octoroc3.randdirection == 2:
                self.rect.y -= 40
                linkhurt.play()
            elif Octoroc3.randdirection == 3:
                self.rect.x += 40
                linkhurt.play()
            elif Octoroc3.randdirection == 4:
                self.rect.x -= 40
                linkhurt.play()
            pass
        else:
            pass
    # Move the sprite based on keypresses
    def update(self, pressed_keys):
        if stage == 'Play' and Player.step == 0:
            self.rect.center = (SCREEN_WIDTH// 2, SCREEN_HEIGHT // 2)
            Player.step = 1
        else:
            global playerX
            global playerY
            #This section moves the player across the screen if they are touching one of the edges.
            #This allows for movement across the map
            if not stage == 'Menu':
                if self.rect.left <= 16:
                    self.rect.left=SCREEN_WIDTH-72
                elif self.rect.right >= SCREEN_WIDTH-32:
                    self.rect.right = 72
                elif self.rect.top <= SCREEN_HEIGHT/4:
                    self.rect.top = SCREEN_HEIGHT - 72
                elif self.rect.bottom >= SCREEN_HEIGHT-32:
                    self.rect.bottom = (SCREEN_HEIGHT/4)+72
            elif stage == 'Menu':
                self.rect.center = (-100, -100)

            #This section is for the first step motion
            #If the step variable is odd, it moves to the first position
            if Player.death == False and Player.step % 2 == 1:
                if Player.hassword and pressed_keys[K_w] and pressed_keys[K_SPACE]:
                    self.surf = pygame.image.load(upAttack).convert_alpha()
                elif pressed_keys[K_w] and not pressed_keys[K_SPACE]:
                    Player.direction = 'Up'
                    self.surf = pygame.image.load(upStand).convert_alpha()
                    self.rect.move_ip(0, -5)
                if Player.hassword and pressed_keys[K_s] and pressed_keys[K_SPACE]:
                    self.surf = pygame.image.load(downAttack).convert_alpha()
                elif pressed_keys[K_s] and not pressed_keys[K_SPACE]:
                    Player.direction = 'Down'
                    self.surf = pygame.image.load(downStand).convert_alpha()
                    self.rect.move_ip(0, 5)
                if Player.hassword and pressed_keys[K_a] and pressed_keys[K_SPACE]:
                    self.surf = pygame.image.load(leftAttack).convert_alpha()
                elif pressed_keys[K_a] and not pressed_keys[K_SPACE]:
                    Player.direction = 'Left'
                    self.surf = pygame.image.load(leftStand).convert_alpha()
                    self.rect.move_ip(-5, 0)
                if Player.hassword and pressed_keys[K_d] and pressed_keys[K_SPACE]:
                    self.surf = pygame.image.load(rightAttack).convert_alpha()
                elif pressed_keys[K_d] and not pressed_keys[K_SPACE]:
                    Player.direction = 'Right'
                    self.surf = pygame.image.load(rightStand).convert_alpha()
                    self.rect.move_ip(5, 0)
                if Player.hassword and pressed_keys[K_SPACE]:
                    if Player.direction == 'Up':
                        self.surf = pygame.image.load(upAttack).convert_alpha()
                    elif Player.direction == 'Down':
                        self.surf = pygame.image.load(downAttack).convert_alpha()
                    elif Player.direction == 'Left':
                        self.surf = pygame.image.load(leftAttack).convert_alpha()
                    elif Player.direction == 'Right':
                        self.surf = pygame.image.load(rightAttack).convert_alpha()
                #This next section allows for the end of the attack update
                #This brings the sprite back to the original position after using the sword
                elif not pressed_keys[K_SPACE]:
                    if Player.direction == 'Up':
                        self.surf = pygame.image.load(upStand).convert_alpha()
                    elif Player.direction == 'Down':
                        self.surf = pygame.image.load(downStand).convert_alpha()
                    elif Player.direction == 'Left':
                        self.surf = pygame.image.load(leftStand).convert_alpha()
                    elif Player.direction == 'Right':
                        self.surf = pygame.image.load(rightStand).convert_alpha()
                    # Keep player on the screen
                if not (pressed_keys[K_w] or pressed_keys[K_a] or pressed_keys[K_s] or pressed_keys[K_d]):
                    pass
                else:
                    Player.step += 1


            #This section is for the second step motion
            #If the step veriable is even, it moves to the second position
            elif Player.death == False and Player.step % 2 == 0:
                if Player.hassword and pressed_keys[K_w] and pressed_keys[K_SPACE]:
                    self.surf = pygame.image.load(upAttack).convert_alpha()
                elif pressed_keys[K_w] and not pressed_keys[K_SPACE]:
                    Player.direction = 'Up'
                    self.surf = pygame.image.load(upStand2).convert_alpha()
                    self.rect.move_ip(0, -5)
                if Player.hassword and pressed_keys[K_s] and pressed_keys[K_SPACE]:
                    self.surf = pygame.image.load(downAttack).convert_alpha()
                elif pressed_keys[K_s] and not pressed_keys[K_SPACE]:
                    Player.direction = 'Down'
                    self.surf = pygame.image.load(downStand2).convert_alpha()
                    self.rect.move_ip(0, 5)
                if Player.hassword and pressed_keys[K_a] and pressed_keys[K_SPACE]:
                    self.surf = pygame.image.load(leftAttack).convert_alpha()
                elif pressed_keys[K_a] and not pressed_keys[K_SPACE]:
                    Player.direction = 'Left'
                    self.surf = pygame.image.load(leftStand2).convert_alpha()
                    self.rect.move_ip(-5, 0)
                if Player.hassword and pressed_keys[K_d] and pressed_keys[K_SPACE]:
                    self.surf = pygame.image.load(rightAttack).convert_alpha()
                elif pressed_keys[K_d] and not pressed_keys[K_SPACE]:
                    Player.direction = 'Right'
                    self.surf = pygame.image.load(rightStand2).convert_alpha()
                    self.rect.move_ip(5, 0)
                if Player.hassword and pressed_keys[K_SPACE]:
                    if Player.direction == 'Up':
                        self.surf = pygame.image.load(upAttack).convert_alpha()
                    elif Player.direction == 'Down':
                        self.surf = pygame.image.load(downAttack).convert_alpha()
                        self.image = self.surf
                        self.image_scaled = pygame.transform.scale(self.image, playerscale)
                        self.surf = self.image_scaled
                    elif Player.direction == 'Left':
                        self.surf = pygame.image.load(leftAttack).convert_alpha()
                    elif Player.direction == 'Right':
                        self.surf = pygame.image.load(rightAttack).convert_alpha()
                # This next section allows for the end of the attack update
                # This brings the sprite back to the original position after using the sword
                elif not pressed_keys[K_SPACE]:
                    if Player.direction == 'Up':
                        self.surf = pygame.image.load(upStand2).convert_alpha()
                    elif Player.direction == 'Down':
                        self.surf = pygame.image.load(downStand2).convert_alpha()
                    elif Player.direction == 'Left':
                        self.surf = pygame.image.load(leftStand2).convert_alpha()
                    elif Player.direction == 'Right':
                        self.surf = pygame.image.load(rightStand2).convert_alpha()
                if not (pressed_keys[K_w] or pressed_keys[K_a] or pressed_keys[K_s] or pressed_keys[K_d]):
                    pass
                else:
                    Player.step += 1
                if Player.step == 2000:
                    Player.step = 1

            if Player.hassword and Player.swordtick <= 20:
                self.surf = pygame.image.load("PickedupSword.png").convert_alpha()
                Player.swordtick += 1
            if Player.hassword and Player.swordtick>20:
                firstsword.kill()
                firstsword.rect.move(-10000, -10000)
            self.image = self.surf
            self.image_scaled = pygame.transform.scale(self.image, playerscale)
            self.surf = self.image_scaled
            if Player.death == False and stage == 'Play':
                ##COLLISION DETECTION
                ##uses direction to decide how to handle collision
                ##check the player's direction and decrement the player's position accordingly
                Player.upcoords = player.rect.center
                Player.downcoords = player.rect.center
                Player.leftcoords = player.rect.center
                Player.rightcoords = player.rect.center

                Player.upcoords = list(Player.upcoords)
                Player.downcoords = list(Player.downcoords)
                Player.leftcoords = list(Player.leftcoords)
                Player.rightcoords = list(Player.rightcoords)

                if Player.upcoords[1] > 16:
                    Player.upcoords[1] = int(Player.upcoords[1] - 16)
                else:
                    Player.upcoords[1] == SCREEN_HEIGHT
                if Player.downcoords[1] < (SCREEN_HEIGHT - 16):
                    Player.downcoords[1] = int(Player.downcoords[1] + 16)
                else:
                    Player.downcoords[1] == int(SCREEN_HEIGHT)
                if Player.leftcoords[0] > 16:
                    Player.leftcoords[0] = int(Player.leftcoords[0] - 16)
                else:
                    Player.leftcoords[0] == 0
                if Player.rightcoords[0] < (SCREEN_WIDTH - 16):
                    Player.rightcoords[0] = int(Player.rightcoords[0] + 16)
                else:
                    Player.rightcoords[0] == int(SCREEN_WIDTH)
                # This is the actual logic
                if (Mapbackground.rect.x != Mapbackground.startingX +(7*SCREEN_WIDTH) and Mapbackground.rect.y!=Mapbackground.startingY - (SCREEN_HEIGHT-SCREEN_HEIGHT/4)) and display_surface.get_at([player.rect.center[0],(player.rect.center[1]+12)])==(0,0,0,255) and (display_surface.get_at([player.rect.center[0]+12,(player.rect.center[1])])==(0,0,0,255) or display_surface.get_at([player.rect.center[0]-12,(player.rect.center[1])])==(0,0,0,255)):
                    Player.incave=True
                else:
                    Player.incave=False
                if pressed_keys[K_d] and ((display_surface.get_at([Player.rightcoords[0], Player.rightcoords[1] - 20]) != blue and display_surface.get_at([Player.rightcoords[0], Player.rightcoords[1] - 8]) == brown) or (display_surface.get_at([Player.rightcoords[0], Player.rightcoords[1] - 8]) == green or display_surface.get_at([Player.rightcoords[0], Player.rightcoords[1] - 8]) == blue or display_surface.get_at([Player.rightcoords[0], Player.rightcoords[1] - 8]) == cave) or (display_surface.get_at([Player.rightcoords[0], Player.rightcoords[1] - 20]) != blue and display_surface.get_at(Player.rightcoords) == brown) or (display_surface.get_at(Player.rightcoords) == green or display_surface.get_at(Player.rightcoords) == blue or display_surface.get_at(Player.rightcoords) == cave)):
                    player.rect.x = player.rect.x - 5
                    if pressed_keys[K_w]:
                        player.rect.y = player.rect.y + 5
                    elif pressed_keys[K_s]:
                        player.rect.y = player.rect.y - 5
                    elif pressed_keys[K_a]:
                        player.rect.x = player.rect.x + 5
                elif pressed_keys[K_a] and ((display_surface.get_at([Player.leftcoords[0], Player.leftcoords[1] - 20]) != blue and display_surface.get_at([Player.leftcoords[0], Player.leftcoords[1] - 8]) == brown) or (display_surface.get_at([Player.leftcoords[0], Player.leftcoords[1] - 8]) == green or display_surface.get_at([Player.leftcoords[0], Player.leftcoords[1] - 8]) == blue or display_surface.get_at([Player.leftcoords[0], Player.leftcoords[1] - 8]) == cave) or (display_surface.get_at([Player.leftcoords[0], Player.leftcoords[1] - 20]) != blue and display_surface.get_at(Player.leftcoords) == brown) or (display_surface.get_at(Player.leftcoords) == green or display_surface.get_at(Player.leftcoords) == blue or display_surface.get_at(Player.leftcoords) == cave)):
                    player.rect.x = player.rect.x + 5
                    if pressed_keys[K_w]:
                        player.rect.y = player.rect.y + 5
                    elif pressed_keys[K_s]:
                        player.rect.y = player.rect.y - 5
                    elif pressed_keys[K_d]:
                        player.rect.x = player.rect.x - 5
                elif pressed_keys[K_w] and ((display_surface.get_at([Player.upcoords[0], Player.upcoords[1] - 20]) != blue and display_surface.get_at([Player.upcoords[0] - 8, Player.upcoords[1]]) == brown) or (display_surface.get_at([Player.upcoords[0] - 8, Player.upcoords[1]]) == green or display_surface.get_at([Player.upcoords[0] - 8, Player.upcoords[1]]) == blue or display_surface.get_at([Player.upcoords[0] - 8, Player.upcoords[1]]) == cave) or (display_surface.get_at([Player.upcoords[0], Player.upcoords[1] - 20]) != blue and display_surface.get_at(Player.upcoords) == brown) or (display_surface.get_at(Player.upcoords) == green or display_surface.get_at(Player.upcoords) == blue or display_surface.get_at(Player.upcoords) == cave)):
                    player.rect.y = player.rect.y + 5
                    if pressed_keys[K_d]:
                        player.rect.x = player.rect.x - 5
                    elif pressed_keys[K_s]:
                        player.rect.y = player.rect.y - 5
                    elif pressed_keys[K_a]:
                        player.rect.x = player.rect.x + 5
                elif pressed_keys[K_s] and ((display_surface.get_at([Player.downcoords[0], Player.downcoords[1] - 20]) != blue and display_surface.get_at([Player.downcoords[0] - 3, Player.downcoords[1]]) == brown) or (display_surface.get_at([Player.downcoords[0] - 3, Player.downcoords[1]]) == green or display_surface.get_at([Player.downcoords[0] - 3, Player.downcoords[1]]) == blue or display_surface.get_at([Player.downcoords[0] - 3, Player.downcoords[1]]) == cave) or (display_surface.get_at([Player.downcoords[0], Player.downcoords[1] - 20]) != blue and display_surface.get_at(Player.downcoords) == brown) or (display_surface.get_at(Player.downcoords) == green or display_surface.get_at(Player.downcoords) == blue or display_surface.get_at(Player.downcoords) == cave)):
                    player.rect.y = player.rect.y - 5
                    if pressed_keys[K_d]:
                        player.rect.x = player.rect.x - 5
                    elif pressed_keys[K_w]:
                        player.rect.y = player.rect.y + 5
                    elif pressed_keys[K_a]:
                        player.rect.x = player.rect.x + 5
                else:
                    pass
# Define the sword object extending pygame.sprite.Sprite
# The surface we draw on the screen is now a property of 'sword'
class Sword(pygame.sprite.Sprite):
    def __init__(self):
        super(Sword, self).__init__()
        self.surf = pygame.image.load(downSword).convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.image = self.surf
        self.image_scaled = pygame.transform.scale(self.image, playerscale)
        self.surf = self.image_scaled
        Sword.rect = self.surf.get_rect()
        Sword.play_time=0
        Sword.swordscale=(8,8)
    def checkCollision(self, sprite1, sprite2):
        if not pressed_keys[K_SPACE]:
            col = pygame.sprite.collide_rect(sprite1, sprite2)
            if col == True and sprite2 == octoroc:
                Octoroc.death == True
                Octoroc.rect.move_ip(-10000, -10000)
                Rock.rect.move_ip(-10000, -10000)
            elif col == True and sprite2 == octoroc2:
                Octoroc2.death == True
                Octoroc2.rect.move_ip(-10000, -10000)
                Rock2.rect.move_ip(-10000, -10000)
            elif col == True and sprite2 == octoroc3:
                Octoroc3.death == True
                Octoroc3.rect.move_ip(-10000, -10000)
                Rock3.rect.move_ip(-10000, -10000)
        else:
            pass

    def update(self, pressed_keys):
        #This variable makes the sword audio only play once if the attack button is held down
        #These next if-else statements change the sword sprite to the correct direction
        # This is depending on the direction the player sprite is pointing
        #These statements are only run if the attack button is held
        if Swordupgrade.foundcount==0:
            if Player.hassword and Player.death == False and Player.direction == 'Up' and pressed_keys[K_SPACE] and not pressed_keys[K_LSHIFT]:
                self.surf = pygame.image.load(upSword).convert()
                if Sword.play_time == 0:
                    sword_slash.play()
                    Sword.play_time += 1
                Sword.rect.center = Player.rect.center
                Sword.rect.bottom =Player.rect.top
                Sword.swordscale = (playerscale)
            elif Player.hassword and Player.death == False and Player.direction == 'Down' and pressed_keys[K_SPACE] and not pressed_keys[K_LSHIFT]:
                self.surf = pygame.image.load(downSword).convert_alpha()
                if Sword.play_time == 0:
                    sword_slash.play()
                    Sword.play_time += 1
                Sword.rect.center = Player.rect.center
                Sword.rect.top=Player.rect.bottom
                Sword.swordscale = (playerscale)
            elif Player.hassword and Player.death == False and Player.direction == 'Left' and pressed_keys[K_SPACE] and not pressed_keys[K_LSHIFT]:
                self.surf = pygame.image.load(leftSword).convert()
                if Sword.play_time == 0:
                    sword_slash.play()
                    Sword.play_time += 1
                Sword.rect.center = Player.rect.center
                Sword.rect.right=Player.rect.left
                Sword.swordscale = (playerscale)
            elif Player.hassword and Player.death == False and Player.direction == 'Right' and pressed_keys[K_SPACE] and not pressed_keys[K_LSHIFT]:
                self.surf = pygame.image.load(rightSword).convert()
                if Sword.play_time == 0:
                    sword_slash.play()
                    Sword.play_time += 1
                Sword.rect.center = Player.rect.center
                Sword.rect.left=Player.rect.right
                Sword.swordscale=(playerscale)
            #If the attack buttons are not held, the sword just hides behind the player sprite, and the audio variable is reset
            else:
                self.surf = pygame.image.load(upSword).convert()
                self.image = self.surf
                Sword.swordscale=(8,8)
                self.image_scaled = pygame.transform.scale(self.image, Sword.swordscale)
                self.surf = self.image_scaled
                Sword.rect.center = (Player.rect.x+30, Player.rect.y+30)

                Sword.play_time = 0

            #Unlike the player sprite, the sword sprite can go off screen
            #This is because of how the motion of the sword works.
            #If it moved like the player, then
        elif Swordupgrade.foundcount>=1:
            if Player.death == False and Player.direction == 'Up' and pressed_keys[K_SPACE] and not pressed_keys[K_LSHIFT]:
                self.surf = pygame.image.load(upSword2).convert()
                if Sword.play_time == 0:
                    sword_slash.play()
                    Sword.play_time += 1
                Sword.rect.center = Player.rect.center
                Sword.rect.bottom = Player.rect.top
                Sword.swordscale = (playerscale)
            elif Player.death == False and Player.direction == 'Down' and pressed_keys[K_SPACE] and not pressed_keys[K_LSHIFT]:
                self.surf = pygame.image.load(downSword2).convert_alpha()
                if Sword.play_time == 0:
                    sword_slash.play()
                    Sword.play_time += 1
                Sword.rect.center = Player.rect.center
                Sword.rect.top = Player.rect.bottom
                Sword.swordscale = (playerscale)
            elif Player.death == False and Player.direction == 'Left' and pressed_keys[K_SPACE] and not pressed_keys[K_LSHIFT]:
                self.surf = pygame.image.load(leftSword2).convert()
                if Sword.play_time == 0:
                    sword_slash.play()
                    Sword.play_time += 1
                Sword.rect.center = Player.rect.center
                Sword.rect.right = Player.rect.left
                Sword.swordscale = (playerscale)
            elif Player.death == False and Player.direction == 'Right' and pressed_keys[K_SPACE] and not pressed_keys[K_LSHIFT]:
                self.surf = pygame.image.load(rightSword2).convert()
                if Sword.play_time == 0:
                    sword_slash.play()
                    Sword.play_time += 1
                Sword.rect.center = Player.rect.center
                Sword.rect.left = Player.rect.right
                Sword.swordscale = (playerscale)
            # If the attack buttons are not held, the sword just hides behind the player sprite, and the audio variable is reset
            else:
                self.surf = pygame.image.load(upSword2).convert()
                self.image = self.surf
                Sword.swordscale=(8,8)
                self.image_scaled = pygame.transform.scale(self.image, Sword.swordscale)
                self.surf = self.image_scaled
                Sword.rect.center = (Player.rect.x+30, Player.rect.y+30)

                Sword.play_time = 0

        self.image = self.surf
        self.image_scaled = pygame.transform.scale(self.image, Sword.swordscale)
        self.surf = self.image_scaled
        if stage == 'Menu':
            self.rect.center=(-100,-100)
class Arrow(pygame.sprite.Sprite):
    def __init__(self):
        super(Arrow, self).__init__()
        self.surf = pygame.image.load(upArrow).convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.image = self.surf
        self.image_scaled = pygame.transform.scale(self.image, (16, 16))
        self.surf = self.image_scaled
        Arrow.rect = self.surf.get_rect()
        Arrow.currentdir = ''

    def checkCollision(self, sprite1, sprite2):
        col = pygame.sprite.collide_rect(sprite1, sprite2)
        if col == True and sprite2 == octoroc:
            Octoroc.death == True
            self.rect.center = Player.rect.center
            Octoroc.rect.move_ip(-10000,-10000)
            Rock.rect.move_ip(-10000,-10000)
        elif col == True and sprite2 == octoroc2:
            Octoroc2.death==True
            self.rect.center = Player.rect.center
            Octoroc2.rect.move_ip(-10000,-10000)
            Rock2.rect.move_ip(-10000,-10000)
        elif col == True and sprite2 == octoroc3:
            Octoroc3.death == True
            self.rect.center = Player.rect.center
            Octoroc3.rect.move_ip(-10000,-10000)
            Rock3.rect.move_ip(-10000,-10000)


    def update(self, pressed_keys):
        #CURRENTDIR INDEX
        #1 = left
        #2 = Right
        #3 = Down
        #4 = Up
        if (self.rect.left <= 0) or (self.rect.right >= SCREEN_WIDTH) or (self.rect.top <= 0 ) or (self.rect.bottom >= SCREEN_HEIGHT):
            self.rect.center = Player.rect.center
            self.currentdir = ''
        else:
            if Player.death == False and (pressed_keys[K_SPACE] and pressed_keys[K_LSHIFT]) and (Player.direction == 'Up') and (self.rect.center == Player.rect.center):
                self.currentdir = 'Up'
                arrowsound.play()
                self.surf = pygame.image.load(upArrow).convert()
                self.rect.y -= 5
            elif Player.death == False and (self.currentdir == 'Up') and not (self.rect.center == Player.rect.center):
                self.rect.y -= 5

            elif Player.death == False and (pressed_keys[K_SPACE] and pressed_keys[K_LSHIFT]) and (Player.direction == 'Down') and (self.rect.center == Player.rect.center):
                self.currentdir = 'Down'
                arrowsound.play()
                self.surf = pygame.image.load(downArrow).convert()
                self.rect.y += 5
            elif Player.death == False and (self.currentdir == 'Down') and not (self.rect.center == Player.rect.center):
                self.rect.y += 5
            elif Player.death == False and (pressed_keys[K_SPACE] and pressed_keys[K_LSHIFT]) and (Player.direction == 'Left') and (self.rect.center == Player.rect.center):
                self.currentdir = 'Left'
                arrowsound.play()
                self.surf = pygame.image.load(leftArrow).convert()
                self.rect.x -= 5
            elif Player.death == False and (self.currentdir == 'Left') and not (self.rect.center == Player.rect.center):
                self.rect.x -= 5
            elif Player.death == False and (pressed_keys[K_SPACE] and pressed_keys[K_LSHIFT]) and (Player.direction == 'Right') and (self.rect.center == Player.rect.center):
                self.currentdir = 'Right'
                arrowsound.play()
                self.surf = pygame.image.load(rightArrow).convert()
                self.rect.x += 5
            elif Player.death == False and (self.currentdir == 'Right') and not (self.rect.center == Player.rect.center):
                self.rect.x += 5
            else:
                self.rect.center = Player.rect.center
                self.currentdir = ''
                pass
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.image = self.surf
        self.image_scaled = pygame.transform.scale(self.image, (16, 16))
        self.surf = self.image_scaled

class Key(pygame.sprite.Sprite):
    def __init__(self):
        super(Key, self).__init__()
        self.surf = pygame.image.load(keysprte).convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.image = self.surf
        self.image_scaled = pygame.transform.scale(self.image, (16,16))
        self.surf = self.image_scaled
        Key.rect = self.surf.get_rect()
        Key.foundcount=0

    def checkCollision(self, sprite1, sprite2):
        if not pressed_keys[K_SPACE]:
            col = pygame.sprite.collide_rect(sprite1, sprite2)
            if col == True:
                Player.pickedupkey=True
                if Key.foundcount==0:
                    keyfound.play()
                    Key.foundcount+=1

        else:
            pass

    def update(self):
        if stage == 'Menu':
            self.rect.center = (random.randint(-3,3) * SCREEN_WIDTH//2, random.randint(-3,1) * SCREEN_HEIGHT//2)
        else:
            #These next if-else statements change the sword sprite to the correct direction
            # This is depending on the direction the player sprite is pointing
            #These statements are only run if the attack button is held
            if Player.death == False and Player.direction == 'Up' and Player.pickedupkey == True:
                self.rect.center = Player.rect.center
                self.rect.left = Player.rect.right
            elif Player.death == False and Player.direction == 'Down' and Player.pickedupkey == True:
                self.rect.center = Player.rect.center
                self.rect.right=Player.rect.left
            elif Player.death == False and Player.direction == 'Left' and Player.pickedupkey == True:
                self.rect.center = Player.rect.center
                self.rect.bottom=Player.rect.top
            elif Player.death == False and direction == 'Right' and Player.pickedupkey == True:
                self.rect.center = Player.rect.center
                self.rect.top = Player.rect.bottom
            #If the attack buttons are not held, the sword just hides behind the player sprite, and the audio variable is reset

            self.image = self.surf
            self.image_scaled = pygame.transform.scale(self.image, (16,16))
            self.surf = self.image_scaled
            #Unlike the player sprite, the sword sprite can go off screen
            #This is because of how the motion of the sword works.
            #If it moved like the player, then`

class Swordupgrade(pygame.sprite.Sprite):
    def __init__(self):
        super(Swordupgrade, self).__init__()
        self.surf = pygame.image.load(upSword2).convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.image = self.surf
        self.image_scaled = pygame.transform.scale(self.image, (16,16))
        self.surf = self.image_scaled
        Swordupgrade.rect = self.surf.get_rect()
        Swordupgrade.foundcount=0

    def checkCollision(self, sprite1, sprite2):
        if not pressed_keys[K_SPACE]:
            col = pygame.sprite.collide_rect(sprite1, sprite2)
            if col == True and Player.hassword:
                Player.pickedupsword=True
                if Swordupgrade.foundcount==0:
                    keyfound.play()
                    Swordupgrade.foundcount+=1
                    self.kill()
                    self.rect.move(-10000,-10000)
        else:
            pass

    def update(self):
        if stage == 'Menu':
            self.rect.center = (random.randint(-3,3) * SCREEN_WIDTH//2, random.randint(-3,1) * SCREEN_HEIGHT//2)
            #If the attack buttons are not held, the sword just hides behind the player sprite, and the audio variable is reset
        self.image = self.surf
        self.image_scaled = pygame.transform.scale(self.image, (16,16))
        self.surf = self.image_scaled
        #Unlike the player sprite, the sword sprite can go off screen
         #This is because of how the motion of the sword works.
        #If it moved like the player, then`
class FirstSword(pygame.sprite.Sprite):
    def __init__(self):
        super(FirstSword, self).__init__()
        self.surf = pygame.image.load(upSword).convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.image = self.surf
        self.image_scaled = pygame.transform.scale(self.image, playerscale)
        self.surf = self.image_scaled
        FirstSword.rect = self.surf.get_rect()
        FirstSword.foundcount=0

    def checkCollision(self, sprite1, sprite2):
        if not pressed_keys[K_SPACE]:
            col = pygame.sprite.collide_rect(sprite1, sprite2)
            if col == True:
                Player.hassword=True
                if FirstSword.foundcount==0:
                    keyfound.play()
                    FirstSword.foundcount+=1
        else:
            pass

    def update(self):
        if Player.incave and Mapbackground.rect.x == Mapbackground.startingX and Mapbackground.rect.y == Mapbackground.startingY:
            self.rect.center = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2+100)
            #If the attack buttons are not held, the sword just hides behind the player sprite, and the audio variable is reset
        self.surf = pygame.image.load(upSword).convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.image = self.surf
        self.image_scaled = pygame.transform.scale(self.image, playerscale)
        self.surf = self.image_scaled
        #Unlike the player sprite, the sword sprite can go off screen
         #This is because of how the motion of the sword works.
        #If it moved like the player, then`
class KeyCount(pygame.sprite.Sprite):
    def __init__(self):
        super(KeyCount, self).__init__()
        self.surf = pygame.image.load(keycount_sprites[0]).convert()
        self.surf.set_colorkey((116, 116, 116), RLEACCEL)
        self.image = self.surf
        self.image_scaled = pygame.transform.scale(self.image, (63, 18))
        self.surf = self.image_scaled
        KeyCount.rect = self.surf.get_rect()

    def update(self):
        if Player.pickedupkey >= 1:
            super(KeyCount, self).__init__()
            self.surf = pygame.image.load(keycount_sprites[1]).convert()
        else:
            pass
        self.image = self.surf
        self.image_scaled = pygame.transform.scale(self.image, (63, 18))
        self.surf = self.image_scaled
    # Move the map based on player location

class Swordhud(pygame.sprite.Sprite):
    def __init__(self):
        super(Swordhud, self).__init__()
        self.surf = pygame.image.load(swordhudimgs[0]).convert()
        self.surf.set_colorkey((116, 116, 116), RLEACCEL)
        self.image = self.surf
        self.image_scaled = pygame.transform.scale(self.image, (25, 35))
        self.surf = self.image_scaled
        Swordhud.rect = self.surf.get_rect()

    def update(self):
        if stage=='Play' and Player.hassword:
            self.rect.center=(330,66)
        else:
            self.rect.center=(-1000,-1000)
        if Swordupgrade.foundcount >= 1:
            self.surf = pygame.image.load(swordhudimgs[1]).convert()
        else:
            pass
        self.surf.set_colorkey((116, 116, 116), RLEACCEL)
        self.image = self.surf
        self.image_scaled = pygame.transform.scale(self.image, (25, 35))
        self.surf = self.image_scaled
    # Move the map based on player location

class Mapbackground(pygame.sprite.Sprite):
    def __init__(self):
        super(Mapbackground, self).__init__()
        self.surf = pygame.image.load("NES - The Legend of Zelda - Overworld First Quest.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.image = self.surf
        self.image_scaled = pygame.transform.scale(self.image, (map_width/1.605, (map_height)/2.005))
        self.surf = self.image_scaled
        Mapbackground.rect = self.surf.get_rect()
        Mapbackground.startingX = 1028 - (map_width // 2)+2712
        Mapbackground.startingY = 670 - (map_height)+3367
        Mapbackground.counter=0
        Mapbackground.speed=3
        if stage == 'Menu':
            self.rect.x = Mapbackground.startingX

            self.rect.y = Mapbackground.startingY
    # Move the map based on player location
    def update(self, playerX, playerY):
        if not stage == 'Menu':
            print((Mapbackground.rect.x, Mapbackground.rect.y))
            print( ( round(Mapbackground.startingX + (7*SCREEN_WIDTH)) , Mapbackground.startingY - round(SCREEN_HEIGHT-SCREEN_HEIGHT/4)))
            if playerY <= SCREEN_HEIGHT/4:
                self.rect.move_ip(0, +(SCREEN_HEIGHT-SCREEN_HEIGHT/4)+1)
                if ((Mapbackground.rect.x, Mapbackground.rect.y) == (Mapbackground.startingX, Mapbackground.startingY)) or Player.incave == True or ((Mapbackground.rect.x,Mapbackground.rect.y) == ( round(Mapbackground.startingX + (7*SCREEN_WIDTH)) , Mapbackground.startingY - round(SCREEN_HEIGHT-SCREEN_HEIGHT/4)) ):
                    print('This is true!')
                    Octoroc.death = True
                    Octoroc2.death = True
                    Octoroc3.death = True
                    Octoroc.rect.move_ip(-10000, -10000)
                    Octoroc2.rect.move_ip(-10000, -10000)
                    Octoroc3.rect.move_ip(-10000, -10000)
                else:
                    Octoroc.death = False
                    Octoroc2.death = False
                    Octoroc3.death = False
                    Octoroc.rect.center = (random.randint(100, SCREEN_WIDTH),random.randint(int(SCREEN_HEIGHT / 4) + 100, int(SCREEN_HEIGHT - 100)))
                    Octoroc2.rect.center = (random.randint(100, SCREEN_WIDTH),random.randint(int(SCREEN_HEIGHT / 4) + 100, int(SCREEN_HEIGHT - 100)))
                    Octoroc3.rect.center = (random.randint(100, SCREEN_WIDTH),random.randint(int(SCREEN_HEIGHT / 4) + 100, int(SCREEN_HEIGHT - 100)))

                Rock.rect.move_ip(0, +(SCREEN_HEIGHT-SCREEN_HEIGHT/4))
                Rock2.rect.move_ip(0, +(SCREEN_HEIGHT - SCREEN_HEIGHT / 4))
                Rock3.rect.move_ip(0, +(SCREEN_HEIGHT - SCREEN_HEIGHT / 4))
                Key.rect.move_ip(0, +(SCREEN_HEIGHT - SCREEN_HEIGHT / 4))
                Swordupgrade.rect.move_ip(0, +(SCREEN_HEIGHT - SCREEN_HEIGHT / 4))
            elif playerY >= SCREEN_HEIGHT-64:
                if self.rect.x!=Mapbackground.startingX +(7*SCREEN_WIDTH) and self.rect.y != Mapbackground.startingY - (SCREEN_HEIGHT-SCREEN_HEIGHT/4):
                    self.rect.move_ip(0,-(SCREEN_HEIGHT-SCREEN_HEIGHT/4)-1)
                    if ((Mapbackground.rect.x, Mapbackground.rect.y) == (Mapbackground.startingX, Mapbackground.startingY)) or Player.incave == True or ((Mapbackground.rect.x,Mapbackground.rect.y) == ( round(Mapbackground.startingX + (7*SCREEN_WIDTH)) , Mapbackground.startingY - round(SCREEN_HEIGHT-SCREEN_HEIGHT/4)) ):
                        print('This is true!')
                        Octoroc.death = True
                        Octoroc2.death = True
                        Octoroc3.death = True
                        Octoroc.rect.move_ip(-10000, -10000)
                        Octoroc2.rect.move_ip(-10000, -10000)
                        Octoroc3.rect.move_ip(-10000, -10000)
                    else:
                        Octoroc.death = False
                        Octoroc2.death = False
                        Octoroc3.death = False
                        Octoroc.rect.center = (random.randint(100, SCREEN_WIDTH),random.randint(int(SCREEN_HEIGHT / 4) + 100, int(SCREEN_HEIGHT - 100)))
                        Octoroc2.rect.center = (random.randint(100, SCREEN_WIDTH),random.randint(int(SCREEN_HEIGHT / 4) + 100, int(SCREEN_HEIGHT - 100)))
                        Octoroc3.rect.center = (random.randint(100, SCREEN_WIDTH),random.randint(int(SCREEN_HEIGHT / 4) + 100, int(SCREEN_HEIGHT - 100)))
                    Rock.rect.move_ip(0, -(SCREEN_HEIGHT-SCREEN_HEIGHT/4))
                    Rock2.rect.move_ip(0, -(SCREEN_HEIGHT - SCREEN_HEIGHT / 4))
                    Rock3.rect.move_ip(0, -(SCREEN_HEIGHT - SCREEN_HEIGHT / 4))
                    Key.rect.move_ip(0, -(SCREEN_HEIGHT - SCREEN_HEIGHT / 4))
                    Swordupgrade.rect.move_ip(0, -(SCREEN_HEIGHT - SCREEN_HEIGHT / 4))
                else:
                    Mapbackground.rect.center=Mapbackground.prevcent
                    Player.rect.center=Mapbackground.prevplayer
                    FirstSword.rect.center=(-100000,-100000)
                    MiniMap.rect.move_ip(0, -10)
            elif playerX <= 16:
                self.rect.move_ip(+SCREEN_WIDTH+1, 0)
                if ((Mapbackground.rect.x, Mapbackground.rect.y) == (Mapbackground.startingX, Mapbackground.startingY)) or Player.incave == True or ((Mapbackground.rect.x,Mapbackground.rect.y) == ( round(Mapbackground.startingX + (7*SCREEN_WIDTH)) , Mapbackground.startingY - round(SCREEN_HEIGHT-SCREEN_HEIGHT/4)) ):
                    print('This is true!')
                    Octoroc.death = True
                    Octoroc2.death = True
                    Octoroc3.death = True
                    Octoroc.rect.move_ip(-10000, -10000)
                    Octoroc2.rect.move_ip(-10000, -10000)
                    Octoroc3.rect.move_ip(-10000, -10000)
                else:
                    Octoroc.death = False
                    Octoroc2.death = False
                    Octoroc3.death = False
                    Octoroc.rect.center = (random.randint(100, SCREEN_WIDTH),random.randint(int(SCREEN_HEIGHT / 4) + 100, int(SCREEN_HEIGHT - 100)))
                    Octoroc2.rect.center = (random.randint(100, SCREEN_WIDTH),random.randint(int(SCREEN_HEIGHT / 4) + 100, int(SCREEN_HEIGHT - 100)))
                    Octoroc3.rect.center = (random.randint(100, SCREEN_WIDTH),random.randint(int(SCREEN_HEIGHT / 4) + 100, int(SCREEN_HEIGHT - 100)))
                Rock.rect.move_ip(+SCREEN_WIDTH, 0)
                Rock2.rect.move_ip(+SCREEN_WIDTH, 0)
                Rock3.rect.move_ip(+SCREEN_WIDTH, 0)
                Key.rect.move_ip(+SCREEN_WIDTH, 0)
                Swordupgrade.rect.move_ip(+SCREEN_WIDTH, 0)
            elif playerX >= SCREEN_WIDTH-64:
                self.rect.move_ip(-SCREEN_WIDTH-1, 0)
                if ((Mapbackground.rect.x, Mapbackground.rect.y) == (Mapbackground.startingX, Mapbackground.startingY)) or Player.incave == True or ((Mapbackground.rect.x,Mapbackground.rect.y) == ( round(Mapbackground.startingX + (7*SCREEN_WIDTH)) , Mapbackground.startingY - round(SCREEN_HEIGHT-SCREEN_HEIGHT/4)) ):
                    print('This is true!')
                    Octoroc.death = True
                    Octoroc2.death = True
                    Octoroc3.death = True
                    Octoroc.rect.move_ip(-10000, -10000)
                    Octoroc2.rect.move_ip(-10000, -10000)
                    Octoroc3.rect.move_ip(-10000, -10000)
                else:
                    Octoroc.death = False
                    Octoroc2.death = False
                    Octoroc3.death = False
                    Octoroc.rect.center = (random.randint(100, SCREEN_WIDTH),random.randint(int(SCREEN_HEIGHT / 4) + 100, int(SCREEN_HEIGHT - 100)))
                    Octoroc2.rect.center = (random.randint(100, SCREEN_WIDTH),random.randint(int(SCREEN_HEIGHT / 4) + 100, int(SCREEN_HEIGHT - 100)))
                    Octoroc3.rect.center = (random.randint(100, SCREEN_WIDTH),random.randint(int(SCREEN_HEIGHT / 4) + 100, int(SCREEN_HEIGHT - 100)))
                Rock.rect.move_ip(-SCREEN_WIDTH, 0)
                Rock2.rect.move_ip(-SCREEN_WIDTH, 0)
                Rock3.rect.move_ip(-SCREEN_WIDTH, 0)
                Key.rect.move_ip(-SCREEN_WIDTH, 0)
                Swordupgrade.rect.move_ip(-SCREEN_WIDTH, 0)
        if Player.incave:
            Mapbackground.prevcent = Mapbackground.rect.center
            string = "IT'S DANGEROUS TO GO ALONE! TAKE THIS"
            white = (255, 255, 255, 255)
            black = (0, 0, 0, 0)
            font = pygame.font.Font('Pixel_NES.otf', 16)
            snip = font.render('', True, white)
            if Mapbackground.rect.x == Mapbackground.startingX and Mapbackground.rect.y == Mapbackground.startingY:
                while Mapbackground.counter <= Mapbackground.speed * len(string):
                    snip = font.render(string[0:Mapbackground.counter // Mapbackground.speed], True, white)
                    screen.blit(snip, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 - 50))
                    Mapbackground.counter += 1
                    pygame.time.wait(25)
                    textaudio.play()
                    pygame.display.flip()
                pygame.time.wait(50)
                Mapbackground.counter = 0
            Mapbackground.minimapcent=MiniMap.rect.center
            self.rect.x=Mapbackground.startingX +(7*SCREEN_WIDTH)
            self.rect.y=Mapbackground.startingY - (SCREEN_HEIGHT-SCREEN_HEIGHT/4)
            Mapbackground.prevplayer=(Player.rect.center[0] , Player.rect.center[1]+15)
            Player.rect.center=(SCREEN_WIDTH//2,SCREEN_HEIGHT-55)

#This creates each heart for the three lives. In the original game there were half lives. This lives system works in the same way
class Lives1(pygame.sprite.Sprite):
    def __init__(self):
        super(Lives1, self).__init__()
        self.surf = pygame.image.load(heart_sprites[0]).convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.image = self.surf
        self.image_scaled = pygame.transform.scale(self.image, (20, 17))
        self.surf = self.image_scaled
        Lives1.rect = self.surf.get_rect()

    def update(self):
        if player.LinkLives >= 1:
            super(Lives1, self).__init__()
            self.surf = pygame.image.load(heart_sprites[0]).convert()
            if player.LinkLives==1:
                linklow.play()
        elif player.LinkLives==.5:
            super(Lives1, self).__init__()
            self.surf = pygame.image.load(heart_sprites[1]).convert()
            linklow.play()
        elif player.LinkLives==0:
            linklow.stop()
            super(Lives1, self).__init__()
            self.surf = pygame.image.load(heart_sprites[2]).convert()
            Player.death=True

        self.image = self.surf
        self.image_scaled = pygame.transform.scale(self.image, (20, 17))
        self.surf = self.image_scaled
    # Move the map based on player location
class Lives2(pygame.sprite.Sprite):
    def __init__(self):
        super(Lives2, self).__init__()
        self.surf = pygame.image.load(heart_sprites[0]).convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.image = self.surf
        self.image_scaled = pygame.transform.scale(self.image, (20, 17))
        self.surf = self.image_scaled
        Lives2.rect = self.surf.get_rect()

    def update(self):
        if player.LinkLives>=2:
            super(Lives2, self).__init__()
            self.surf = pygame.image.load(heart_sprites[0]).convert()
        elif player.LinkLives==1.5:
            super(Lives2, self).__init__()
            self.surf = pygame.image.load(heart_sprites[1]).convert()
        elif player.LinkLives==1:
            super(Lives2, self).__init__()
            self.surf = pygame.image.load(heart_sprites[2]).convert()

        self.image = self.surf
        self.image_scaled = pygame.transform.scale(self.image, (20, 17))
        self.surf = self.image_scaled
    # Move the map based on player location
class Lives3(pygame.sprite.Sprite):
    def __init__(self):
        super(Lives3, self).__init__()
        self.surf = pygame.image.load(heart_sprites[0]).convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.image = self.surf
        self.image_scaled = pygame.transform.scale(self.image, (20,17))
        self.surf = self.image_scaled
        Lives3.rect = self.surf.get_rect()

    def update(self):
        if player.LinkLives==3:
            super(Lives3, self).__init__()
            self.surf = pygame.image.load(heart_sprites[0]).convert()
        elif player.LinkLives==2.5:
            super(Lives3, self).__init__()
            self.surf = pygame.image.load(heart_sprites[1]).convert()
        elif player.LinkLives==2:
            super(Lives3, self).__init__()
            self.surf = pygame.image.load(heart_sprites[2]).convert()
        self.image = self.surf
        self.image_scaled = pygame.transform.scale(self.image, (20, 17))
        self.surf = self.image_scaled
    # Move the map based on player location

#This minimap follows the player to give them an idea of where they are on the map
class MiniMap(pygame.sprite.Sprite):
    def __init__(self):
        super(MiniMap, self).__init__()
        self.surf = pygame.image.load(mini).convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.image = self.surf
        self.image_scaled = pygame.transform.scale(self.image,(10,10))
        self.surf = self.image_scaled
        MiniMap.rect = self.surf.get_rect()
        if stage == 'Play':
            self.rect.x = 100
            self.rect.y = 100
    # Move the map based on player location
    def update(self, playerX, playerY):
        if not stage == 'Menu':
            if playerY <= SCREEN_HEIGHT/4:
                self.rect.move_ip(0, -10)
            elif playerY >= SCREEN_HEIGHT-64:
                self.rect.move_ip(0,10)
            elif playerX <= 16:
                self.rect.move_ip(-10, 0)
            elif playerX >= SCREEN_WIDTH-64:
                self.rect.move_ip(10, 0)

class OldMan(pygame.sprite.Sprite):
    def __init__(self):
        super(OldMan, self).__init__()
        self.surf = pygame.image.load(oldman).convert_alpha()
        self.surf.set_colorkey((106, 106, 106), RLEACCEL)
        self.image = self.surf
        self.image_scaled = pygame.transform.scale(self.image,playerscale)
        self.surf = self.image_scaled
        OldMan.rect = self.surf.get_rect()

    # Move the sprite based on keypresses
    def update(self):
        if stage == 'Play' and Mapbackground.rect.x != Mapbackground.startingX + (7*SCREEN_WIDTH) and Mapbackground.rect.y != Mapbackground.startingY - (SCREEN_HEIGHT-SCREEN_HEIGHT/4):
            self.rect.center = (-10000,-10000)
        else:
            self.rect.center=(SCREEN_WIDTH//2,SCREEN_HEIGHT//2+30)

class Fire1(pygame.sprite.Sprite):
    def __init__(self):
        super(Fire1, self).__init__()
        self.surf = pygame.image.load(firepngs[0]).convert_alpha()
        self.surf.set_colorkey((106, 106, 106), RLEACCEL)
        self.image = self.surf
        self.image_scaled = pygame.transform.scale(self.image,playerscale)
        self.surf = self.image_scaled
        Fire1.step = 1
        Fire1.rect = self.surf.get_rect()
    # Move the sprite based on keypresses
    def update(self):
        if stage == 'Play' and Mapbackground.rect.x != Mapbackground.startingX + (7*SCREEN_WIDTH) and Mapbackground.rect.y != Mapbackground.startingY - (SCREEN_HEIGHT-SCREEN_HEIGHT/4):
            self.rect.center = (-10000,-10000)
        else:
            if Fire1.step % 2 == 0:
                self.surf = pygame.image.load(firepngs[0]).convert_alpha()
            elif Fire1.step % 2 ==1:
                self.surf = pygame.image.load(firepngs[1]).convert_alpha()
            self.surf.set_colorkey((106, 106, 106), RLEACCEL)
            self.image = self.surf
            self.image_scaled = pygame.transform.scale(self.image, playerscale)
            self.surf = self.image_scaled
            Fire1.rect = self.surf.get_rect()
            self.rect.center = (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 30)
            Fire1.step +=1

class Fire2(pygame.sprite.Sprite):
    def __init__(self):
        super(Fire2, self).__init__()
        self.surf = pygame.image.load(firepngs[0]).convert_alpha()
        self.surf.set_colorkey((106, 106, 106), RLEACCEL)
        self.image = self.surf
        self.image_scaled = pygame.transform.scale(self.image, playerscale)
        self.surf = self.image_scaled
        Fire2.step = 1
        Fire2.rect = self.surf.get_rect()

    # Move the sprite based on keypresses
    def update(self):
        if stage == 'Play' and Mapbackground.rect.x != Mapbackground.startingX + (7 * SCREEN_WIDTH) and Mapbackground.rect.y != Mapbackground.startingY - (SCREEN_HEIGHT - SCREEN_HEIGHT / 4):
            self.rect.center = (-10000, -10000)
        else:
            if Fire2.step % 2 == 0:
                self.surf = pygame.image.load(firepngs[0]).convert_alpha()
            elif Fire2.step % 2 == 1:
                self.surf = pygame.image.load(firepngs[1]).convert_alpha()
            self.surf.set_colorkey((106, 106, 106), RLEACCEL)
            self.image = self.surf
            self.image_scaled = pygame.transform.scale(self.image, playerscale)
            self.surf = self.image_scaled
            Fire2.rect = self.surf.get_rect()
            self.rect.center = (SCREEN_WIDTH // 2 + 150, SCREEN_HEIGHT // 2 + 30)
            Fire2.step += 1

#This is the first screen shown. It goes through a list of pngs that make the flashing and waterfall effect
class MenuScreen(pygame.sprite.Sprite):
    def __init__(self):
        super(MenuScreen, self).__init__()
        self.surf = pygame.image.load(menuscreen[menustep]).convert()
        self.image = self.surf
        self.image_scaled = pygame.transform.scale(self.image, (SCREEN_WIDTH, 10+SCREEN_HEIGHT))
        self.surf = self.image_scaled
        MenuScreen.rect = self.surf.get_rect()
    # Move the map based on player location

    def playstage(self, stage):
        if stage == 'Text':
            self.rect.center=(-1000,-1000)
    def update(self, menustep, stage):
        if stage == 'Menu':
            self.surf = pygame.image.load(menuscreen[menustep]).convert()
            self.image = self.surf
            self.image_scaled = pygame.transform.scale(self.image, (SCREEN_WIDTH, 10 + SCREEN_HEIGHT))
            self.surf = self.image_scaled
            pygame.time.wait(400)
        elif stage == 'Text':
            self.surf = pygame.image.load(menuscreen[menustep]).convert()
            self.image = self.surf
            self.image_scaled = pygame.transform.scale(self.image, (SCREEN_WIDTH, 10 + SCREEN_HEIGHT))
            self.surf = self.image_scaled
        else:
            pass

#This creates the text screen that goes over the story of the game
class TextScreen(pygame.sprite.Sprite):
    def __init__(self):
        super(TextScreen, self).__init__()
        self.surf = pygame.image.load(storyscreen[menustep]).convert()
        self.image = self.surf
        self.image_scaled = pygame.transform.scale(self.image, (SCREEN_WIDTH, 10+SCREEN_HEIGHT))
        self.surf = self.image_scaled
        TextScreen.rect = self.surf.get_rect()
    # Move the map based on player location

    def playstage(self, stage):
        if stage == 'Play':
            self.rect.center=(-1000,-1000)
    def update(self,menustep, stage):
        if stage == 'Text':
            self.surf = pygame.image.load(storyscreen[menustep]).convert()
            self.image = self.surf
            self.image_scaled = pygame.transform.scale(self.image, (SCREEN_WIDTH, 10 + SCREEN_HEIGHT))
            self.surf = self.image_scaled

#This creates the game hud that is the base for the minimap and lives.
class Gamehud(pygame.sprite.Sprite):
    def __init__(self):
        super(Gamehud, self).__init__()
        self.surf = pygame.image.load(gamehud).convert()
        self.image = self.surf
        self.image_scaled = pygame.transform.scale(self.image, (SCREEN_WIDTH, SCREEN_HEIGHT/3))
        self.surf = self.image_scaled
        Gamehud.rect = self.surf.get_rect()
    # Move the map based on player location

    def playstage(self, stage):
        if stage != 'Play':
            self.rect.center=(-1000,-1000)
    def update(self, stage):
        if stage == 'Play':
            self.surf = pygame.image.load(gamehud).convert()
            self.image = self.surf
            self.image_scaled = pygame.transform.scale(self.image, (SCREEN_WIDTH, SCREEN_HEIGHT/4))
            self.surf = self.image_scaled
# Define the enemy object extending pygame.sprite.Sprite
# The surface we draw on the screen is now a property of 'Octoroc'
class Octoroc(pygame.sprite.Sprite):
    def __init__(self):
        super(Octoroc, self).__init__()
        self.surf = pygame.image.load(OctoLeft).convert_alpha()
        self.surf.set_colorkey((106, 106, 106), RLEACCEL)
        self.image = self.surf
        self.image_scaled = pygame.transform.scale(self.image,playerscale)
        self.surf = self.image_scaled
        Octoroc.rect = self.surf.get_rect()
        Octoroc.death=False
        Octoroc.randdirection=5
        Octoroc.stepping=0
    def checkCollision(self, sprite1, sprite2):
        if pressed_keys[K_SPACE]:
            col = pygame.sprite.collide_rect(sprite1, sprite2)
            if col == True:
                Octoroc.death=True
                Octoroc.rect.move_ip(-10000, -10000)
                Rock.rect.move_ip(-10000, -10000)
        else:
            pass

    # Move the sprite based on keypresses
    def update(self):
        if stage == 'Play' and self.stepping == 0:
            self.stepping = 1
        elif Octoroc.death == True:
            Octoroc.rect.move(-10000, -10000)
            Rock.rect.move(-10000, -10000)
        else:
            if self.stepping %100==0:
                Octoroc.randdirection=random.randint(1,5)
            else:
                pass
            #This section moves the player across the screen if they are touching one of the edges.
            #This allows for movement across the map
            #This section is for the first step motion
            #If the step variable is odd, it moves to the first position
            if self.death == False and self.stepping % 2 == 1 and stage=='Play' and ((self.rect.x<SCREEN_WIDTH and self.rect.x>0) and (self.rect.y<SCREEN_HEIGHT and self.rect.y>0)):
                if Octoroc.randdirection==1:
                    self.surf = pygame.image.load(OctoLeft).convert_alpha()
                    if Octoroc.rect.x<75:
                        Octoroc.randdirection==2
                elif Octoroc.randdirection==2:
                    self.surf = pygame.image.load(OctoRight).convert_alpha()
                if Octoroc.randdirection==3:
                    self.surf = pygame.image.load(OctoDown).convert_alpha()
                elif Octoroc.randdirection==4:
                    self.surf = pygame.image.load(OctoUp).convert_alpha()
                elif Octoroc.randdirection == 5:
                    pass
                self.stepping += 1
            #This section is for the second step motion
            #If the step veriable is even, it moves to the second position
            elif self.death == False and self.stepping % 2 == 0 and stage=='Play' and ((self.rect.x<SCREEN_WIDTH and self.rect.x>0) and (self.rect.y<SCREEN_HEIGHT and self.rect.y>SCREEN_HEIGHT/4)):
                if Octoroc.randdirection == 1:
                    self.surf = pygame.image.load(OctoLeft2).convert_alpha()
                    self.rect.x = self.rect.x - 5
                elif Octoroc.randdirection == 2:
                    self.surf = pygame.image.load(OctoRight2).convert_alpha()
                    self.rect.x = self.rect.x + 5
                if Octoroc.randdirection == 3:
                    self.surf = pygame.image.load(OctoDown2).convert_alpha()
                    self.rect.y = self.rect.y + 5
                elif Octoroc.randdirection == 4:
                    self.surf = pygame.image.load(OctoUp2).convert_alpha()
                    self.rect.y=self.rect.y-5
                elif Octoroc.randdirection == 5:
                    pass
                self.stepping += 1
                if self.stepping == 2000:
                    self.stepping = 1
            self.image = self.surf
            self.image_scaled = pygame.transform.scale(self.image, playerscale)
            self.surf = self.image_scaled
            if stage == 'Play' and ((self.rect.x<SCREEN_WIDTH and self.rect.x>0) and (self.rect.y<SCREEN_HEIGHT and self.rect.y>(SCREEN_HEIGHT/4))):
                ##COLLISION DETECTION
                ##uses direction to decide how to handle collision
                ##check the player's direction and decrement the player's position accordingly
                Octoroc.upcoords = octoroc.rect.center
                Octoroc.downcoords = octoroc.rect.center
                Octoroc.leftcoords = octoroc.rect.center
                Octoroc.rightcoords = octoroc.rect.center

                Octoroc.upcoords = list(Octoroc.upcoords)
                Octoroc.downcoords = list(Octoroc.downcoords)
                Octoroc.leftcoords = list(Octoroc.leftcoords)
                Octoroc.rightcoords = list(Octoroc.rightcoords)

                if Octoroc.upcoords[1] > 55 + (SCREEN_HEIGHT / 4):
                    Octoroc.upcoords[1] = int(Octoroc.upcoords[1] - 35)
                else:
                    Octoroc.upcoords[1] = int(50 + (SCREEN_HEIGHT / 4))
                    self.randdirection = 3
                if Octoroc.downcoords[1] < (SCREEN_HEIGHT - 55):
                    Octoroc.downcoords[1] = int(Octoroc.downcoords[1] + 35)
                else:
                    Octoroc.downcoords[1] = int(SCREEN_HEIGHT - 50)
                    self.randdirection = 4
                if Octoroc.leftcoords[0] > 55:
                    Octoroc.leftcoords[0] = int(Octoroc.leftcoords[0] - 35)
                else:
                    Octoroc.leftcoords[0] = 50
                    self.randdirection = 2
                if Octoroc.rightcoords[0] < (SCREEN_WIDTH - 55):
                    Octoroc.rightcoords[0] = int(Octoroc.rightcoords[0] + 35)
                else:
                    Octoroc.rightcoords[0] = int(SCREEN_WIDTH - 50)
                    self.randdirection = 1

                # This is the actual logic
                try:
                    if (display_surface.get_at([Octoroc.rightcoords[0], Octoroc.rightcoords[1]-8]) == brown or display_surface.get_at([Octoroc.rightcoords[0], Octoroc.rightcoords[1]-8]) == green or display_surface.get_at([Octoroc.rightcoords[0], Octoroc.rightcoords[1]-8]) == blue or display_surface.get_at(Octoroc.rightcoords) == brown or display_surface.get_at(Octoroc.rightcoords) == green or display_surface.get_at(Octoroc.rightcoords) == blue):
                        octoroc.rect.x = octoroc.rect.x - 5
                    elif (display_surface.get_at([Octoroc.leftcoords[0], Octoroc.leftcoords[1]-8]) == brown or (display_surface.get_at([Octoroc.leftcoords[0], Octoroc.leftcoords[1]-8]) == green or display_surface.get_at([Octoroc.leftcoords[0], Octoroc.leftcoords[1]-8]) == blue) or display_surface.get_at(Octoroc.leftcoords) == brown or display_surface.get_at(Octoroc.leftcoords) == green or display_surface.get_at(Octoroc.leftcoords) == blue):
                        octoroc.rect.x = octoroc.rect.x + 5
                    elif (display_surface.get_at([Octoroc.upcoords[0]-8, Octoroc.upcoords[1]]) == brown or (display_surface.get_at([Octoroc.upcoords[0]-8, Octoroc.upcoords[1]]) == green or display_surface.get_at([Octoroc.upcoords[0]-8, Octoroc.upcoords[1]]) == blue) or display_surface.get_at(Octoroc.upcoords) == brown or display_surface.get_at(Octoroc.upcoords) == green or display_surface.get_at(Octoroc.upcoords) == blue):
                        octoroc.rect.y = octoroc.rect.y + 5
                    elif (display_surface.get_at([Octoroc.downcoords[0]-8, Octoroc.downcoords[1]]) == brown or (display_surface.get_at([Octoroc.downcoords[0]-8, Octoroc.downcoords[1]]) == green or display_surface.get_at([Octoroc.downcoords[0]-8, Octoroc.downcoords[1]]) == blue) or display_surface.get_at(Octoroc.downcoords) == brown or display_surface.get_at(Octoroc.downcoords) == green or display_surface.get_at(Octoroc.downcoords) == blue):
                        octoroc.rect.y = octoroc.rect.y - 5
                except IndexError:
                    if Octoroc.upcoords[0] > (SCREEN_WIDTH - 55):
                        Octoroc.upcoords[0] = SCREEN_WIDTH - 55
                        Octoroc.rect.x = SCREEN_WIDTH - 55
                        Octoroc.randdirection=1
                    elif Octoroc.upcoords[0] < 55:
                        Octoroc.upcoords[0] = 55
                        Octoroc.rect.x = 55
                        Octoroc.randdirection = 2
                    elif Octoroc.downcoords[0] > (SCREEN_WIDTH - 55):
                        Octoroc.downcoords[0] = SCREEN_WIDTH - 55
                        Octoroc.rect.x = SCREEN_WIDTH - 55
                        Octoroc.randdirection = 1
                    elif Octoroc.downcoords[0] < 55:
                        Octoroc.downcoords[0] = 55
                        Octoroc.rect.x = 55
                        Octoroc.randdirection = 2
                    elif Octoroc.leftcoords[1] > (SCREEN_HEIGHT - 55):
                        Octoroc.leftcoords[1] = SCREEN_HEIGHT - 55
                        Octoroc.rect.y = SCREEN_HEIGHT - 55
                        Octoroc.randdirection = 4
                    elif Octoroc.leftcoords[1] < int(SCREEN_HEIGHT / 4 + 55):
                        Octoroc.leftcoords[1] = int(SCREEN_HEIGHT / 4 + 55)
                        Octoroc.rect.y=SCREEN_HEIGHT / 4 + 55
                        Octoroc.randdirection = 3
                    elif Octoroc.rightcoords[1] > (SCREEN_HEIGHT - 55):
                        Octoroc.rightcoords[1] = SCREEN_HEIGHT - 55
                        Octoroc.rect.y = SCREEN_HEIGHT - 55
                        Octoroc.randdirection = 4
                    elif Octoroc.rightcoords[1] > (SCREEN_HEIGHT / 4 + 55):
                        Octoroc.rightcoords[1] = int(SCREEN_HEIGHT / 4 + 55)
                        Octoroc.rect.y = int(SCREEN_HEIGHT / 4 + 55)
                        Octoroc.randdirection = 3
                    octoroc.update()
                    pass

# Define the projectile object extending pygame.sprite.Sprite
# The surface we draw on the screen is now a property of 'Rock'
class Rock(pygame.sprite.Sprite):
    def __init__(self):
        super(Rock, self).__init__()
        self.surf = pygame.image.load("Rock.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.image = self.surf
        self.image_scaled = pygame.transform.scale(self.image, (16, 16))
        self.surf = self.image_scaled
        Rock.rect = self.surf.get_rect()
        Rock.currentdir=1

    def checkCollision(self, sprite1, sprite2):
        if pressed_keys[K_SPACE]:
            col = pygame.sprite.collide_rect(sprite1, sprite2)
            if col == True and sprite2 == player:
                self.rect.center=octoroc.rect.center
            elif col==True and sprite2==sword:
                self.rect.center=octoroc.rect.center
        else:
            pass
    def update(self):
        #CURRENTDIR INDEX
        #1 = left
        #2 = Right
        #3 = Down
        #4 = Up
        if (self.rect.left <= 0) or (self.rect.right >= SCREEN_WIDTH) or (self.rect.top <= 0 ) or (self.rect.bottom >= SCREEN_HEIGHT) and ((Octoroc.rect.x<SCREEN_WIDTH or Octoroc.rect.x>0) or (Octoroc.rect.y<SCREEN_HEIGHT or Octoroc.rect.y>0)):
            self.rect.center = Octoroc.rect.center
            self.currentdir=Octoroc.randdirection
        else:
            if Octoroc.death==False and (Octoroc.randdirection == 1 or Octoroc.randdirection == 2) and (Octoroc.rect.y-10 < Player.rect.y < Octoroc.rect.y+10) and (self.rect.center == Octoroc.rect.center):
                if Player.rect.x < Octoroc.rect.x and Octoroc.randdirection == 1:
                    self.currentdir = 1
                    self.rect.x = self.rect.x - 5
                elif Player.rect.x > Octoroc.rect.x and Octoroc.randdirection == 2:
                    self.currentdir = 2
                    self.rect.x = self.rect.x + 5
                else:
                    pass
            elif Octoroc.death==False and (self.currentdir == 1 or self.currentdir == 2) and not (self.rect.center == Octoroc.rect.center):
                if self.currentdir == 1:
                    self.rect.x = self.rect.x - 5
                elif self.currentdir == 2:
                    self.rect.x = self.rect.x + 5
                else:
                    pass
            elif Octoroc.death==False and (Octoroc.randdirection == 3 or Octoroc.randdirection == 4) and (Octoroc.rect.x-10 < Player.rect.x < Octoroc.rect.x+10) and (self.rect.center == Octoroc.rect.center):
                if Player.rect.y < Octoroc.rect.y and Octoroc.randdirection==4:
                    self.currentdir = 4
                    self.rect.y = self.rect.y - 5
                elif Player.rect.y > Octoroc.rect.y and Octoroc.randdirection==3:
                    self.currentdir = 3
                    self.rect.y = self.rect.y + 5
                else:
                    pass
            elif Octoroc.death==False and (self.currentdir == 3 or self.currentdir == 4) and not (self.rect.center == Octoroc.rect.center):
                if self.currentdir==4:
                    self.rect.y = self.rect.y - 5
                elif self.currentdir==3:
                    self.rect.y = self.rect.y + 5
                else:
                    pass
            else:
                self.rect.center = Octoroc.rect.center
                pass

#This is a duplicate of the original Octoroc and rock class, made for more enemies.
#For every enemy added, most of the code stays the same, making copies very quick to  make
class Octoroc2(pygame.sprite.Sprite):
    def __init__(self):
        super(Octoroc2, self).__init__()
        self.surf = pygame.image.load(OctoLeft).convert_alpha()
        self.surf.set_colorkey((106, 106, 106), RLEACCEL)
        self.image = self.surf
        self.image_scaled = pygame.transform.scale(self.image,playerscale)
        self.surf = self.image_scaled
        Octoroc2.rect = self.surf.get_rect()
        Octoroc2.death=False
        Octoroc2.randdirection=1
        Octoroc2.stepping=0
    def checkCollision(self, sprite1, sprite2):
        if pressed_keys[K_SPACE]:
            col = pygame.sprite.collide_rect(sprite1, sprite2)
            if col == True:
                Octoroc2.death = True
                Octoroc2.rect.move_ip(-10000, -10000)
                Rock2.rect.move_ip(-10000, -10000)
        else:
            pass

    # Move the sprite based on keypresses
    def update(self):
        if stage == 'Play' and self.stepping == 0:
            self.stepping = 1
        elif self.death==True:
            Octoroc2.rect.move(-10000, -10000)
            Rock2.rect.move(-10000, -10000)
        else:
            if self.stepping %100==0:
                Octoroc2.randdirection=random.randint(1,5)
            else:
                pass
            #This section moves the player across the screen if they are touching one of the edges.
            #This allows for movement across the map
            #This section is for the first step motion
            #If the step variable is odd, it moves to the first position
            if self.death == False and self.stepping % 2 == 1 and stage=='Play' and ((self.rect.x<SCREEN_WIDTH and self.rect.x>0) and (self.rect.y<SCREEN_HEIGHT and self.rect.y>0)):
                if Octoroc2.randdirection==1:
                    self.surf = pygame.image.load(OctoLeft).convert_alpha()
                elif Octoroc2.randdirection==2:
                    self.surf = pygame.image.load(OctoRight).convert_alpha()
                if Octoroc2.randdirection==3:
                    self.surf = pygame.image.load(OctoDown).convert_alpha()
                elif Octoroc2.randdirection==4:
                    self.surf = pygame.image.load(OctoUp).convert_alpha()
                elif Octoroc2.randdirection == 5:
                    pass
                self.stepping+=1
            #This section is for the second step motion
            #If the step veriable is even, it moves to the second position
            elif self.death == False and self.stepping % 2 == 0 and stage=='Play' and ((self.rect.x<SCREEN_WIDTH and self.rect.x>0) and (self.rect.y<SCREEN_HEIGHT and self.rect.y>SCREEN_HEIGHT/4)):
                if Octoroc2.randdirection == 1:
                    self.surf = pygame.image.load(OctoLeft2).convert_alpha()
                    self.rect.x = self.rect.x - 5
                elif Octoroc2.randdirection == 2:
                    self.surf = pygame.image.load(OctoRight2).convert_alpha()
                    self.rect.x = self.rect.x + 5
                if Octoroc2.randdirection == 3:
                    self.surf = pygame.image.load(OctoDown2).convert_alpha()
                    self.rect.y = self.rect.y + 5
                elif Octoroc2.randdirection == 4:
                    self.surf = pygame.image.load(OctoUp2).convert_alpha()
                    self.rect.y=self.rect.y-5
                elif Octoroc2.randdirection == 5:
                    pass
                self.stepping+=1

                if self.stepping == 2000:
                    self.stepping = 1
            self.image = self.surf
            self.image_scaled = pygame.transform.scale(self.image, playerscale)
            self.surf = self.image_scaled

            if stage == 'Play' and ((self.rect.x<SCREEN_WIDTH and self.rect.x>0) and (self.rect.y<SCREEN_HEIGHT and self.rect.y>(SCREEN_HEIGHT/4))):
                ##COLLISION DETECTION
                ##uses direction to decide how to handle collision
                ##check the player's direction and decrement the player's position accordingly
                Octoroc2.upcoords = octoroc2.rect.center
                Octoroc2.downcoords = octoroc2.rect.center
                Octoroc2.leftcoords = octoroc2.rect.center
                Octoroc2.rightcoords = octoroc2.rect.center

                Octoroc2.upcoords = list(Octoroc2.upcoords)
                Octoroc2.downcoords = list(Octoroc2.downcoords)
                Octoroc2.leftcoords = list(Octoroc2.leftcoords)
                Octoroc2.rightcoords = list(Octoroc2.rightcoords)
                if Octoroc2.upcoords[1] > 55+(SCREEN_HEIGHT/4):
                    Octoroc2.upcoords[1] = int(Octoroc2.upcoords[1] - 35)
                else:
                    Octoroc2.upcoords[1] = int(50+(SCREEN_HEIGHT/4))
                    self.randdirection=3
                if Octoroc2.downcoords[1] < (SCREEN_HEIGHT - 55):
                    Octoroc2.downcoords[1] = int(Octoroc2.downcoords[1] + 35)
                else:
                    Octoroc2.downcoords[1] = int(SCREEN_HEIGHT-50)
                    self.randdirection=4
                if Octoroc2.leftcoords[0] > 55:
                    Octoroc2.leftcoords[0] = int(Octoroc2.leftcoords[0] - 35)
                else:
                    Octoroc2.leftcoords[0] = 50
                    self.randdirection=2
                if Octoroc2.rightcoords[0] < (SCREEN_WIDTH - 55):
                    Octoroc2.rightcoords[0] = int(Octoroc2.rightcoords[0] + 35)
                else:
                    Octoroc2.rightcoords[0] = int(SCREEN_WIDTH-50)
                    self.randdirection=1
                # This is the actual logic
                try:
                    if (display_surface.get_at([Octoroc2.rightcoords[0], Octoroc2.rightcoords[1]-8]) == brown or display_surface.get_at([Octoroc2.rightcoords[0], Octoroc2.rightcoords[1]-8]) == green or display_surface.get_at([Octoroc2.rightcoords[0], Octoroc2.rightcoords[1]-8]) == blue or display_surface.get_at(Octoroc2.rightcoords) == brown or display_surface.get_at(Octoroc2.rightcoords) == green or display_surface.get_at(Octoroc2.rightcoords) == blue):
                        octoroc2.rect.x = octoroc2.rect.x - 5
                        self.randdirection = random.randint(1, 5)
                    elif (display_surface.get_at([Octoroc2.leftcoords[0], Octoroc2.leftcoords[1]-8]) == brown or (display_surface.get_at([Octoroc2.leftcoords[0], Octoroc2.leftcoords[1]-8]) == green or display_surface.get_at([Octoroc2.leftcoords[0], Octoroc2.leftcoords[1]-8]) == blue) or display_surface.get_at(Octoroc2.leftcoords) == brown or display_surface.get_at(Octoroc2.leftcoords) == green or display_surface.get_at(Octoroc2.leftcoords) == blue):
                        octoroc2.rect.x = octoroc2.rect.x + 5
                        self.randdirection = random.randint(1, 5)
                    elif (display_surface.get_at([Octoroc2.upcoords[0]-8, Octoroc2.upcoords[1]]) == brown or (display_surface.get_at([Octoroc2.upcoords[0]-8, Octoroc2.upcoords[1]]) == green or display_surface.get_at([Octoroc2.upcoords[0]-8, Octoroc2.upcoords[1]]) == blue) or display_surface.get_at(Octoroc2.upcoords) == brown or display_surface.get_at(Octoroc2.upcoords) == green or display_surface.get_at(Octoroc2.upcoords) == blue):
                        octoroc2.rect.y = octoroc2.rect.y + 5
                        self.randdirection = random.randint(1, 5)
                    elif (display_surface.get_at([Octoroc2.downcoords[0]-8, Octoroc2.downcoords[1]]) == brown or (display_surface.get_at([Octoroc2.downcoords[0]-8, Octoroc2.downcoords[1]]) == green or display_surface.get_at([Octoroc2.downcoords[0]-8, Octoroc2.downcoords[1]]) == blue) or display_surface.get_at(Octoroc2.downcoords) == brown or display_surface.get_at(Octoroc2.downcoords) == green or display_surface.get_at(Octoroc2.downcoords) == blue):
                        octoroc2.rect.y = octoroc2.rect.y - 5
                        self.randdirection = random.randint(1, 5)
                except IndexError:
                    if Octoroc2.upcoords[0] > (SCREEN_WIDTH - 55):
                        Octoroc2.upcoords[0] = SCREEN_WIDTH - 55
                        Octoroc2.rect.x = SCREEN_WIDTH - 55
                        Octoroc2.randdirection=1
                    elif Octoroc2.upcoords[0] < 55:
                        Octoroc2.upcoords[0] = 55
                        Octoroc2.rect.x = 55
                        Octoroc2.randdirection = 2
                    elif Octoroc2.downcoords[0] > (SCREEN_WIDTH - 55):
                        Octoroc2.downcoords[0] = SCREEN_WIDTH - 55
                        Octoroc2.rect.x = SCREEN_WIDTH - 55
                        Octoroc2.randdirection = 1
                    elif Octoroc2.downcoords[0] < 55:
                        Octoroc2.downcoords[0] = 55
                        Octoroc2.rect.x = 55
                        Octoroc2.randdirection = 2
                    elif Octoroc2.leftcoords[1] > (SCREEN_HEIGHT - 55):
                        Octoroc2.leftcoords[1] = SCREEN_HEIGHT - 55
                        Octoroc2.rect.y = SCREEN_HEIGHT - 55
                        Octoroc2.randdirection = 4
                    elif Octoroc2.leftcoords[1] < int(SCREEN_HEIGHT / 4 + 55):
                        Octoroc2.leftcoords[1] = int(SCREEN_HEIGHT / 4 + 55)
                        Octoroc2.rect.y=SCREEN_HEIGHT / 4 + 55
                        Octoroc2.randdirection = 3
                    elif Octoroc2.rightcoords[1] > (SCREEN_HEIGHT - 55):
                        Octoroc2.rightcoords[1] = SCREEN_HEIGHT - 55
                        Octoroc2.rect.y = SCREEN_HEIGHT - 55
                        Octoroc2.randdirection = 4
                    elif Octoroc2.rightcoords[1] > (SCREEN_HEIGHT / 4 + 55):
                        Octoroc2.rightcoords[1] = int(SCREEN_HEIGHT / 4 + 55)
                        Octoroc2.rect.y = int(SCREEN_HEIGHT / 4 + 55)
                        Octoroc2.randdirection = 3
                    octoroc2.update()
                    pass
class Rock2(pygame.sprite.Sprite):
    def __init__(self):
        super(Rock2, self).__init__()
        self.surf = pygame.image.load("Rock.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.image = self.surf
        self.image_scaled = pygame.transform.scale(self.image, (16, 16))
        self.surf = self.image_scaled
        Rock2.rect = self.surf.get_rect()
        Rock2.currentdir=1

    def checkCollision(self, sprite1, sprite2):
        if pressed_keys[K_SPACE]:
            col = pygame.sprite.collide_rect(sprite1, sprite2)
            if col == True and sprite2 == player:
                self.rect.center=octoroc2.rect.center
            elif col==True and sprite2==sword:
                self.rect.center=octoroc2.rect.center
        else:
            pass

    def update(self):
        #CURRENTDIR INDEX
        #1 = left
        #2 = Right
        #3 = Down
        #4 = Up
        if (self.rect.left <= 0) or (self.rect.right >= SCREEN_WIDTH) or (self.rect.top <= 0 ) or (self.rect.bottom >= SCREEN_HEIGHT) and ((Octoroc2.rect.x<SCREEN_WIDTH or Octoroc2.rect.x>0) or (Octoroc2.rect.y<SCREEN_HEIGHT or Octoroc2.rect.y>0)):
            self.rect.center = Octoroc2.rect.center
            self.currentdir=Octoroc2.randdirection
        else:
            if Octoroc2.death==False and (Octoroc2.randdirection == 1 or Octoroc2.randdirection == 2) and (Octoroc2.rect.y-10 < Player.rect.y < Octoroc2.rect.y+10) and (self.rect.center == Octoroc2.rect.center):
                if Player.rect.x < Octoroc2.rect.x and Octoroc2.randdirection == 1:
                    self.currentdir = 1
                    self.rect.x = self.rect.x - 5
                elif Player.rect.x > Octoroc2.rect.x and Octoroc2.randdirection == 2:
                    self.currentdir = 2
                    self.rect.x = self.rect.x + 5
                else:
                    pass
            elif Octoroc2.death==False and (self.currentdir == 1 or self.currentdir == 2) and not (self.rect.center == Octoroc2.rect.center):
                if self.currentdir == 1:
                    self.rect.x = self.rect.x - 5
                elif self.currentdir == 2:
                    self.rect.x = self.rect.x + 5
                else:
                    pass
            elif Octoroc2.death==False and (Octoroc2.randdirection == 3 or Octoroc2.randdirection == 4) and (Octoroc2.rect.x-10 < Player.rect.x < Octoroc2.rect.x+10) and (self.rect.center == Octoroc2.rect.center):
                if Player.rect.y < Octoroc2.rect.y and Octoroc2.randdirection==4:
                    self.currentdir = 4
                    self.rect.y = self.rect.y - 5
                elif Player.rect.y > Octoroc2.rect.y and Octoroc2.randdirection==3:
                    self.currentdir = 3
                    self.rect.y = self.rect.y + 5
                else:
                    pass
            elif Octoroc2.death==False and (self.currentdir == 3 or self.currentdir == 4) and not (self.rect.center == Octoroc2.rect.center):
                if self.currentdir ==4:
                    self.rect.y = self.rect.y - 5
                elif self.currentdir ==3:
                    self.rect.y = self.rect.y + 5
                else:
                    pass
            else:
                self.rect.center = Octoroc2.rect.center
                pass
class Octoroc3(pygame.sprite.Sprite):
    def __init__(self):
        super(Octoroc3, self).__init__()
        self.surf = pygame.image.load(OctoLeft).convert_alpha()
        self.surf.set_colorkey((106, 106, 106), RLEACCEL)
        self.image = self.surf
        self.image_scaled = pygame.transform.scale(self.image,playerscale)
        self.surf = self.image_scaled
        Octoroc3.rect = self.surf.get_rect()
        Octoroc3.death=False
        Octoroc3.randdirection=1
        Octoroc3.stepping=0
    def checkCollision(self, sprite1, sprite2):
        if pressed_keys[K_SPACE]:
            col = pygame.sprite.collide_rect(sprite1, sprite2)
            if col == True:
                Octoroc3.death = True
                Octoroc3.rect.move_ip(-10000,-10000)
                Rock3.rect.move_ip(-10000, -10000)
        else:
            pass
    # Move the sprite based on keypresses
    def update(self):
        if stage == 'Play' and self.stepping == 0:
            self.stepping= 1
        elif Octoroc3.death==True:
            Octoroc3.rect.move(-10000, -10000)
            Rock3.rect.move(-10000, -10000)
        else:
            if self.stepping %100==0:
                Octoroc3.randdirection=random.randint(1,5)
            else:
                pass
            #This section moves the player across the screen if they are touching one of the edges.
            #This allows for movement across the map
            #This section is for the first step motion
            #If the step variable is odd, it moves to the first position
            if self.death == False and self.stepping % 2 == 1 and stage=='Play' and ((self.rect.x<SCREEN_WIDTH or self.rect.x>0) or (self.rect.y<SCREEN_HEIGHT or self.rect.y>0)):
                if Octoroc3.randdirection==1:
                    self.surf = pygame.image.load(OctoLeft).convert_alpha()
                elif Octoroc3.randdirection==2:
                    self.surf = pygame.image.load(OctoRight).convert_alpha()
                if Octoroc3.randdirection==3:
                    self.surf = pygame.image.load(OctoDown).convert_alpha()
                elif Octoroc3.randdirection==4:
                    self.surf = pygame.image.load(OctoUp).convert_alpha()
                elif Octoroc3.randdirection == 5:
                    pass
                self.stepping+=1
            #This section is for the second step motion
            #If the step veriable is even, it moves to the second position
            elif Octoroc3.death == False and self.stepping % 2 == 0 and stage=='Play' and ((self.rect.x<SCREEN_WIDTH and self.rect.x>0) and (self.rect.y<SCREEN_HEIGHT and self.rect.y>SCREEN_HEIGHT/4)):
                if Octoroc3.randdirection == 1:
                    self.surf = pygame.image.load(OctoLeft2).convert_alpha()
                    self.rect.x = self.rect.x - 5
                elif Octoroc3.randdirection == 2:
                    self.surf = pygame.image.load(OctoRight2).convert_alpha()
                    self.rect.x = self.rect.x + 5
                elif Octoroc3.randdirection == 3:
                    self.surf = pygame.image.load(OctoDown2).convert_alpha()
                    self.rect.y = self.rect.y + 5
                elif Octoroc3.randdirection == 4:
                    self.surf = pygame.image.load(OctoUp2).convert_alpha()
                    self.rect.y=self.rect.y-5
                elif Octoroc3.randdirection == 5:
                    pass
                self.stepping +=1
                if self.stepping == 2000:
                    self.stepping = 1
            self.image = self.surf
            self.image_scaled = pygame.transform.scale(self.image, playerscale)
            self.surf = self.image_scaled

            if stage == 'Play' and ((self.rect.x<SCREEN_WIDTH and self.rect.x>0) and (self.rect.y<SCREEN_HEIGHT and self.rect.y>(SCREEN_HEIGHT/4))):
                ##COLLISION DETECTION
                ##uses direction to decide how to handle collision
                ##check the player's direction and decrement the player's position accordingly
                Octoroc3.upcoords = octoroc3.rect.center
                Octoroc3.downcoords = octoroc3.rect.center
                Octoroc3.leftcoords = octoroc3.rect.center
                Octoroc3.rightcoords = octoroc3.rect.center

                Octoroc3.upcoords = list(Octoroc3.upcoords)
                Octoroc3.downcoords = list(Octoroc3.downcoords)
                Octoroc3.leftcoords = list(Octoroc3.leftcoords)
                Octoroc3.rightcoords = list(Octoroc3.rightcoords)
                if Octoroc3.upcoords[1] > 55 + (SCREEN_HEIGHT / 4):
                    Octoroc3.upcoords[1] = int(Octoroc3.upcoords[1] - 35)
                else:
                    Octoroc3.upcoords[1] = int(50 + (SCREEN_HEIGHT / 4))
                    self.randdirection = 3
                if Octoroc3.downcoords[1] < (SCREEN_HEIGHT - 55):
                    Octoroc3.downcoords[1] = int(Octoroc3.downcoords[1] + 35)
                else:
                    Octoroc3.downcoords[1] = int(SCREEN_HEIGHT - 50)
                    self.randdirection = 4
                if Octoroc3.leftcoords[0] > 55:
                    Octoroc3.leftcoords[0] = int(Octoroc3.leftcoords[0] - 35)
                else:
                    Octoroc3.leftcoords[0] = 50
                    self.randdirection = 2
                if Octoroc3.rightcoords[0] < (SCREEN_WIDTH - 55):
                    Octoroc3.rightcoords[0] = int(Octoroc3.rightcoords[0] + 35)
                else:
                    Octoroc3.rightcoords[0] = int(SCREEN_WIDTH - 50)
                    self.randdirection = 1
                # This is the actual logic
                try:
                    if (display_surface.get_at([Octoroc3.rightcoords[0], Octoroc3.rightcoords[1]-8]) == brown or display_surface.get_at([Octoroc3.rightcoords[0], Octoroc3.rightcoords[1]-8]) == green or display_surface.get_at([Octoroc3.rightcoords[0], Octoroc3.rightcoords[1]-8]) == blue or display_surface.get_at(Octoroc3.rightcoords) == brown or display_surface.get_at(Octoroc3.rightcoords) == green or display_surface.get_at(Octoroc3.rightcoords) == blue):
                        octoroc3.rect.x -= 5
                        Octoroc3.randdirection = random.randint(1, 5)
                    elif (display_surface.get_at([Octoroc3.leftcoords[0], Octoroc3.leftcoords[1]-8]) == brown or (display_surface.get_at([Octoroc3.leftcoords[0], Octoroc3.leftcoords[1]-8]) == green or display_surface.get_at([Octoroc3.leftcoords[0], Octoroc3.leftcoords[1]-8]) == blue) or display_surface.get_at(Octoroc3.leftcoords) == brown or display_surface.get_at(Octoroc3.leftcoords) == green or display_surface.get_at(Octoroc3.leftcoords) == blue):
                        octoroc3.rect.x += 5
                        Octoroc3.randdirection = random.randint(1, 5)
                    elif (display_surface.get_at([Octoroc3.upcoords[0]-8, Octoroc3.upcoords[1]]) == brown or (display_surface.get_at([Octoroc3.upcoords[0]-8, Octoroc3.upcoords[1]]) == green or display_surface.get_at([Octoroc3.upcoords[0]-8, Octoroc3.upcoords[1]]) == blue) or display_surface.get_at(Octoroc3.upcoords) == brown or display_surface.get_at(Octoroc3.upcoords) == green or display_surface.get_at(Octoroc3.upcoords) == blue):
                        octoroc3.rect.y += 5
                        Octoroc3.randdirection = random.randint(1, 5)
                    elif (display_surface.get_at([Octoroc3.downcoords[0]-8, Octoroc3.downcoords[1]]) == brown or (display_surface.get_at([Octoroc3.downcoords[0]-8, Octoroc3.downcoords[1]]) == green or display_surface.get_at([Octoroc3.downcoords[0]-8, Octoroc3.downcoords[1]]) == blue) or display_surface.get_at(Octoroc3.downcoords) == brown or display_surface.get_at(Octoroc3.downcoords) == green or display_surface.get_at(Octoroc3.downcoords) == blue):
                        octoroc3.rect.y -= 5
                        Octoroc3.randdirection = random.randint(1, 5)
                except IndexError:
                    if Octoroc3.upcoords[0] > (SCREEN_WIDTH - 55):
                        Octoroc3.upcoords[0] = SCREEN_WIDTH - 55
                        Octoroc3.rect.x = SCREEN_WIDTH - 55
                        Octoroc3.randdirection=1
                    elif Octoroc3.upcoords[0] < 55:
                        Octoroc3.upcoords[0] = 55
                        Octoroc3.rect.x = 55
                        Octoroc3.randdirection = 2
                    elif Octoroc3.downcoords[0] > (SCREEN_WIDTH - 55):
                        Octoroc3.downcoords[0] = SCREEN_WIDTH - 55
                        Octoroc3.rect.x = SCREEN_WIDTH - 55
                        Octoroc3.randdirection = 1
                    elif Octoroc3.downcoords[0] < 55:
                        Octoroc3.downcoords[0] = 55
                        Octoroc3.rect.x = 55
                        Octoroc3.randdirection = 2
                    elif Octoroc3.leftcoords[1] > (SCREEN_HEIGHT - 55):
                        Octoroc3.leftcoords[1] = SCREEN_HEIGHT - 55
                        Octoroc3.rect.y = SCREEN_HEIGHT - 55
                        Octoroc3.randdirection = 4
                    elif Octoroc3.leftcoords[1] < int(SCREEN_HEIGHT / 4 + 55):
                        Octoroc3.leftcoords[1] = int(SCREEN_HEIGHT / 4 + 55)
                        Octoroc3.rect.y=SCREEN_HEIGHT / 4 + 55
                        Octoroc3.randdirection = 3
                    elif Octoroc3.rightcoords[1] > (SCREEN_HEIGHT - 55):
                        Octoroc3.rightcoords[1] = SCREEN_HEIGHT - 55
                        Octoroc3.rect.y = SCREEN_HEIGHT - 55
                        Octoroc3.randdirection = 4
                    elif Octoroc3.rightcoords[1] > (SCREEN_HEIGHT / 4 + 55):
                        Octoroc3.rightcoords[1] = int(SCREEN_HEIGHT / 4 + 55)
                        Octoroc3.rect.y = int(SCREEN_HEIGHT / 4 + 55)
                        Octoroc3.randdirection = 3
                    octoroc3.update()
                    pass
class Rock3(pygame.sprite.Sprite):
    def __init__(self):
        super(Rock3, self).__init__()
        self.surf = pygame.image.load("Rock.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.image = self.surf
        self.image_scaled = pygame.transform.scale(self.image, (16, 16))
        self.surf = self.image_scaled
        Rock3.rect = self.surf.get_rect()
        Rock3.currentdir=1

    def checkCollision(self, sprite1, sprite2):
        if pressed_keys[K_SPACE]:
            col = pygame.sprite.collide_rect(sprite1, sprite2)
            if col == True and sprite2 == player:
                self.rect.center=octoroc3.rect.center
            elif col==True and sprite2==sword:
                self.rect.center=octoroc3.rect.center
        else:
            pass

    def update(self):
        #CURRENTDIR INDEX
        #1 = left
        #2 = Right
        #3 = Down
        #4 = Up
        if (self.rect.left <= 0) or (self.rect.right >= SCREEN_WIDTH) or (self.rect.top <= 0 ) or (self.rect.bottom >= SCREEN_HEIGHT) and ((Octoroc3.rect.x<SCREEN_WIDTH or Octoroc3.rect.x>0) or (Octoroc3.rect.y<SCREEN_HEIGHT or Octoroc3.rect.y>0)):
            self.rect.center = Octoroc3.rect.center
            self.currentdir=Octoroc3.randdirection
        else:
            if Octoroc3.death==False and (Octoroc3.randdirection == 1 or Octoroc3.randdirection == 2) and (Octoroc3.rect.y-10 < Player.rect.y < Octoroc3.rect.y+10) and (self.rect.center == Octoroc3.rect.center):
                if Player.rect.x < Octoroc3.rect.x and Octoroc3.randdirection == 1:
                    self.currentdir = 1
                    self.rect.x = self.rect.x - 5
                elif Player.rect.x > Octoroc3.rect.x and Octoroc3.randdirection == 2:
                    self.currentdir = 2
                    self.rect.x = self.rect.x + 5
                else:
                    pass
            elif Octoroc3.death==False and (self.currentdir == 1 or self.currentdir == 2) and not (self.rect.center == Octoroc3.rect.center):
                if self.currentdir == 1:
                    self.rect.x = self.rect.x - 5
                elif self.currentdir == 2:
                    self.rect.x = self.rect.x + 5
                else:
                    pass
            elif Octoroc3.death==False and (Octoroc3.randdirection == 3 or Octoroc3.randdirection == 4) and (Octoroc3.rect.x-10 < Player.rect.x < Octoroc3.rect.x+10) and (self.rect.center == Octoroc3.rect.center):
                if Player.rect.y < Octoroc2.rect.y and Octoroc3.randdirection==4:
                    self.currentdir = 4
                    self.rect.y = self.rect.y - 5
                elif Player.rect.y > Octoroc3.rect.y and Octoroc3.randdirection==3:
                    self.currentdir = 3
                    self.rect.y = self.rect.y + 5
                else:
                    pass
            elif Octoroc3.death==False and (self.currentdir == 3 or self.currentdir == 4) and not (self.rect.center == Octoroc3.rect.center):
                if self.currentdir ==4:
                    self.rect.y = self.rect.y - 5
                elif self.currentdir ==3:
                    self.rect.y = self.rect.y + 5
                else:
                    pass
            else:
                self.rect.center = Octoroc3.rect.center
                pass

#Setup the clock for a decent framerate
clock = pygame.time.Clock()

#this starts the music system
pygame.mixer.init()

# Initialize pygame
pygame.init()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((X, Y), pygame.FULLSCREEN)

#This is all of the music files in the game
pygame.mixer.music.load("01 Title BGM.mp3")
pygame.mixer.music.play(loops=-1)
sword_slash = pygame.mixer.Sound("Sword_Slash.mp3")
start_game = pygame.mixer.Sound("07 Catch Treasure Fanfare.mp3")
linkdead=pygame.mixer.Sound("LOZ_Link_Die.wav")
keyfound=pygame.mixer.Sound("LOZ_Key_Appear.wav")
arrowsound=pygame.mixer.Sound("LOZ_Arrow_Boomerang.wav")
linkhurt=pygame.mixer.Sound("LOZ_Link_Hurt.wav")
linklow=pygame.mixer.Sound("LOZ_LowHealth.wav")
textaudio=pygame.mixer.Sound("LOZ_Text.wav")

# Create our 'player' and all other classes
sword = Sword()
arrow=Arrow()
player = Player()
key=Key()
keycount=KeyCount()
swordhud=Swordhud()
swordupgrade=Swordupgrade()

#These are all of the classes that are tied to the cave system throughout the map
firstsword=FirstSword()
oldMan=OldMan()
fire1= Fire1()
fire2=Fire2()

mapbackground = Mapbackground()

octoroc=Octoroc()
octoroc2=Octoroc2()
octoroc3=Octoroc3()
rock=Rock()
rock2=Rock2()
rock3=Rock3()

menu=MenuScreen()
textscreen=TextScreen()
hud=Gamehud()
minimap=MiniMap()
lives1=Lives1()
lives2=Lives2()
lives3=Lives3()

#This moves any sprites to their proper position at the start of the game
player.rect.move(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
menu.rect.center=(SCREEN_WIDTH//2,5+SCREEN_HEIGHT//2)
minimap.rect.center=(125,96)
lives1.rect.center=(440,74)
lives2.rect.center=(470,75)
lives3.rect.center=(490,75)

keycount.rect.center=(270,76)

# - all_sprites is used for rendering
all_sprites = pygame.sprite.Group()
all_sprites.add(mapbackground, sword, arrow, rock, rock2, rock3, octoroc, octoroc2, octoroc3, oldMan, fire1, fire2, key,swordupgrade, firstsword, player, hud,minimap, lives1, lives2, lives3, keycount, swordhud, textscreen, menu)

# Variable to keep our main loop running
running = True
# Our main loop
screen.fill((0,0,0))
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)

#This is the game loop
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop
            if event.key == K_ESCAPE:
                running = False
        # Did the user click the window close button? If so, stop the loop
        elif event.type == QUIT:
            running = False

    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    arrow.update(pressed_keys)
    octoroc.update()
    octoroc2.update()
    octoroc3.update()
    rock.update()
    rock2.update()
    rock3.update()
    key.update()
    keycount.update()
    swordhud.update()
    swordupgrade.update()
    firstsword.update()

    oldMan.update()
    fire1.update()
    fire2.update()

    hud.update(stage)
    screen.fill((0, 0, 0))
    if Player.death and Player.deathcount ==0:
        white = (255, 255, 255, 255)
        black = (0, 0, 0, 0)
        font = pygame.font.Font('Pixel_NES.otf', 32)
        # create a text surface object,
        # on which text is drawn on it.
        text = font.render('Game Over', True, white, black)
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        screen.blit(text, textRect)

        player.kill()
        octoroc.kill()
        octoroc2.kill()
        rock.kill()
        rock2.kill()
        mapbackground.kill()
        sword.kill()
        arrow.kill()
        key.kill()
        pygame.mixer.music.unload()
        pygame.mixer.music.stop()
        linkdead.play()

        Player.deathcount+=1
    elif Player.death and Player.deathcount > 0:
        white = (255, 255, 255, 255)
        black = (0, 0, 0, 0)
        font = pygame.font.Font('Pixel_NES.otf', 32)

        # create a text surface object,
        # on which text is drawn on it.
        text = font.render('Game Over', True, white, black)

        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        screen.blit(text,textRect)

    if stage == 'Play':
        sword.update(pressed_keys)
        arrow.update(pressed_keys)
        playerX=Player.rect.x
        playerY=Player.rect.y
        mapbackground.update(playerX, playerY)
        minimap.update(playerX,playerY)

        Octoroc.checkCollision(octoroc, octoroc, sword)
        Octoroc2.checkCollision(octoroc2, octoroc2, sword)
        Octoroc3.checkCollision(octoroc3, octoroc3, sword)
        Swordupgrade.checkCollision(swordupgrade,swordupgrade,player)
        FirstSword.checkCollision(firstsword, firstsword, player)
        if Octoroc.death == False:
            Player.checkCollision(player,player,rock)
        else:
            Rock.rect.move(-10000,-10000)
        if Octoroc2.death == False:
            Player.checkCollision(player, player, rock2)
        else:
            Rock2.rect.move(-10000, -10000)
        if Octoroc3.death == False:
            Player.checkCollision(player,player,rock3)
        else:
            Rock3.rect.move(-10000, -10000)

        Sword.checkCollision(sword,sword,rock)
        Sword.checkCollision(sword, sword, rock2)
        Sword.checkCollision(sword, sword, rock3)

        Arrow.checkCollision(arrow, arrow, octoroc)
        Arrow.checkCollision(arrow, arrow, octoroc2)
        Arrow.checkCollision(arrow, arrow, octoroc3)

        Rock.checkCollision(rock, rock, sword)
        if Octoroc.death==False:
            Rock.checkCollision(rock, rock, player)

        Rock2.checkCollision(rock2, rock2, sword)
        if Octoroc2.death == False:
            Rock2.checkCollision(rock2, rock2, player)

        Rock3.checkCollision(rock3, rock3, sword)
        if Octoroc3.death == False:
            Rock3.checkCollision(rock3, rock3, player)

        lives1.update()
        lives2.update()
        lives3.update()
        lives1.rect.center = (450, 75)
        lives2.rect.center = (470, 75)
        lives3.rect.center = (490, 75)

        Key.checkCollision(key, key, player)
        if pressed_keys[K_RETURN]:
            stage = 'Pause'
        if Player.death:
            stage == 'Death'

    if stage == 'Pause':
        if pressed_keys[K_RETURN]:
            stage='Play'

    # Update the position of our enemies
    if stage == 'Menu':
        timetick = 0
        if menustep > 15:
            menustep = 0
        MenuScreen.update(MenuScreen, menustep,stage)
        screen.blit(MenuScreen.surf, MenuScreen.rect)
        pygame.display.flip()
        menustep+=1
        #display_surface.blit(MenuScreen, MenuScreen.rect)
        if pressed_keys[K_RETURN]:
            menustep=0
            stage ='Text'
    elif stage == 'Text':
        if menustep > 3:
            menustep = 0
        MenuScreen.playstage(MenuScreen, stage)
        TextScreen.update(TextScreen,menustep, stage)
        screen.blit(TextScreen.surf, TextScreen.rect)
        pygame.display.flip()
        menustep+=1
        if pressed_keys[K_RETURN]:
            pygame.mixer.music.pause()
            pygame.mixer.music.unload()
            start_game.play()
            timetick=0
            killdeath = 0
            stage ='Play'

    elif stage == 'Play' and timetick==0:
        screen.fill((0, 0, 0))
        TextScreen.playstage(TextScreen, stage)
        pygame.mixer.music.load("Overworld_Music.mp3")
        pygame.mixer.music.play(loops=-1)
        timetick=1
        pygame.mixer.music.unpause()

    # Draw all our sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    # Flip everything to the display
    pygame.display.set_caption("The Legend of Zelda")
    pygame.display.flip()
    # Ensure program maintains a rate of 30 frames per second
    clock.tick(30)
#This ends the game when the while loop ends
pygame.mixer.quit()
