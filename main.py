import pygame
import sys

pygame.init()
width,height=500,490
screen=pygame.display.set_mode((width,height))
FPS=pygame.time.Clock()
text=pygame.font.SysFont('comicsans',40)
bg=(0,0,0)
white=(255,255,255)
black=(0,0,0)


def draw_squares():
    global first,second,third,fourth,fifth,sixth,seventh,eigth,ninth
    first=pygame.draw.rect(screen,white,(50,50,100,100))
    second=pygame.draw.rect(screen,white,(200,50,100,100))
    third=pygame.draw.rect(screen,white,(350,50,100,100))

    fourth=pygame.draw.rect(screen,white,(50,200,100,100))
    fifth=pygame.draw.rect(screen,white,(200,200,100,100))
    sixth=pygame.draw.rect(screen,white,(350,200,100,100))

    seventh=pygame.draw.rect(screen,white,(50,350,100,100))
    eigth=pygame.draw.rect(screen,white,(200,350,100,100))
    ninth=pygame.draw.rect(screen,white,(350,350,100,100))

draw_squares()

class squares:
    def __init__(self,square,state):
        self.square=square
        self.state=state

first_open=squares(first,'')
second_open=squares(second,'')
third_open=squares(third,'')
fourth_open=squares(fourth,'')
fifth_open=squares(fifth,'')
sixth_open=squares(sixth,'')
seventh_open=squares(seventh,'')
eigth_open=squares(eigth,'')
ninth_open=squares(ninth,'')

squares_lst=[first_open,second_open,third_open,fourth_open,fifth_open,sixth_open,seventh_open,eigth_open,ninth_open]


def win_screen(player):
    current_player=text.render(f"{player}" ,1,(255,255,255))
    screen.blit(current_player,(width//2-current_player.get_width()//2,height-current_player.get_height()))
    pygame.display.update()
    pygame.time.delay(2000)
    pygame.draw.rect(screen,black,(0,height-50,width,height))
    draw_squares()
    for i in squares_lst:
        i.state=''
    main()

    


def main():
    player1=True
    player1_points=0
    player2_points=0
    pygame.draw.rect(screen,black,(0,0,width,50))
    pygame.display.update()
    current_player='X'
    current_player=text.render(f"{current_player} turn" ,1,(255,255,255))
    screen.blit(current_player,(10,2))

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type==pygame.MOUSEBUTTONUP:
                pos=pygame.mouse.get_pos()
                if player1==True:
                    for i in squares_lst:
                        if i.square.collidepoint(pos):
                            pygame.draw.line(screen,(255,0,0),(i.square[0]+5,i.square[1]+5),(i.square[0]+i.square[2]-5,i.square[1]+i.square[2]-5),8)
                            pygame.draw.line(screen,(255,0,0),(i.square[0]+i.square[2]-5,i.square[1]+5),(i.square[0]+5,i.square[1]+i.square[2]-5),8)
                            i.state='Player1'



            if event.type==pygame.MOUSEBUTTONUP:
                pos=pygame.mouse.get_pos()
                if player1==False:
                    for i in squares_lst:
                        if i.square.collidepoint(pos):
                            pygame.draw.circle(screen,(0,0,255),(i.square[0]+i.square[2]/2,i.square[1]+i.square[2]/2),50,8)
                            i.state='Player2'
                            

            if event.type==pygame.MOUSEBUTTONUP:
                if player1==False:
                    player1=True
                    pygame.draw.rect(screen,black,(0,0,width,50))
                    pygame.display.update()
                    
                    current_player='X'
                    current_player=text.render(f"{current_player} turn" ,1,(255,255,255))
                    screen.blit(current_player,(10,2))
                    player1_points+=1


                else:
                    player1=False
                    pygame.draw.rect(screen,black,(0,0,width,50))
                    pygame.display.update()
                    
                    current_player='O'
                    current_player=text.render(f"{current_player} turn" ,1,(255,255,255))
                    screen.blit(current_player,(10,2))
                    player2_points+=1

                
        ##check for player 1 win
        if first_open.state=='Player1' and second_open.state=='Player1' and third_open.state=='Player1':
            win_screen('Player 1 wins')


        elif fourth_open.state=='Player1' and fifth_open.state=='Player1' and sixth_open.state=='Player1':
            win_screen('Player 1 wins')

        elif seventh_open.state=='Player1' and eigth_open.state=='Player1' and ninth_open.state=='Player1':
            win_screen('Player 1 wins')

        elif first_open.state=='Player1' and fourth_open.state=='Player1' and seventh_open.state=='Player1':
            win_screen('Player 1 wins')

        elif second_open.state=='Player1' and fifth_open.state=='Player1' and eigth_open.state=='Player1':
            win_screen('Player 1 wins')

        elif third_open.state=='Player1' and sixth_open.state=='Player1' and ninth_open.state=='Player1':
            win_screen('Player 1 wins')

        elif first_open.state=='Player1' and fifth_open.state=='Player1' and ninth_open.state=='Player1':
            win_screen('Player 1 wins')

        elif third_open.state=='Player1' and fifth_open.state=='Player1' and seventh_open.state=='Player1':
            win_screen('Player 1 wins')

        


        ##Check for player 2 win
        elif first_open.state=='Player2' and second_open.state=='Player2' and third_open.state=='Player2':
            win_screen('Player 2 wins')

        elif fourth_open.state=='Player2' and fifth_open.state=='Player2' and sixth_open.state=='Player2':
            win_screen('Player 2 wins')

        elif seventh_open.state=='Player2' and eigth_open.state=='Player2' and ninth_open.state=='Player2':
            win_screen('Player 2 wins')

        elif first_open.state=='Player2' and fourth_open.state=='Player2' and seventh_open.state=='Player2':
            win_screen('Player 2 wins')

        elif second_open.state=='Player2' and fifth_open.state=='Player2' and eigth_open.state=='Player2':
            win_screen('Player 2 wins')

        elif third_open.state=='Player2' and sixth_open.state=='Player2' and ninth_open.state=='Player2':
            win_screen('Player 2 wins')

        elif first_open.state=='Player2' and fifth_open.state=='Player2' and ninth_open.state=='Player2':
            win_screen('Player 2 wins')

        elif third_open.state=='Player2' and fifth_open.state=='Player2' and seventh_open.state=='Player2':
            win_screen('Player 2 wins')

        elif player1_points==4 and player2_points==5:
            win_screen('Draw')

        pygame.display.update()
        FPS.tick(120)


if __name__=='__main__':
    main()
