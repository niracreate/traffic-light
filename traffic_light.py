import pygame
import time
pygame.init()

display_width = 800
display_height = 600
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Traffic Light and Car")

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
grey = (128, 128, 128)

# car
car_width = 80
car_height = 40

# traffic light
light_r = 50
light_pos_x = 700
light_pos_y = 150
clock = pygame.time.Clock()


def main():

    car_pos_x = -car_width
    car_pos_y = display_height / 2 - car_height / 2
    car_speed = 5
    light_color = red
    last_color_change_time = time.time()

    # loop
    game_exit = False
    while not game_exit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

        # update color
        elapsed_time = time.time() - last_color_change_time
        if elapsed_time > 1:
            if light_color == red:
                light_color = yellow
            elif light_color == yellow:
                light_color = green
            else:
                light_color = red
            last_color_change_time = time.time()

        game_display.fill(black)

        # draw traffic light
        pygame.draw.circle(game_display, black, (light_pos_x, light_pos_y - light_r * 2), light_r)
        if light_color == red:
            pygame.draw.circle(game_display, red, (light_pos_x, light_pos_y - light_r * 2), light_r // 2)
        elif light_color == yellow:
            pygame.draw.circle(game_display, yellow, (light_pos_x, light_pos_y - light_r * 2), light_r // 2)
        else:
            pygame.draw.circle(game_display, green, (light_pos_x, light_pos_y - light_r * 2), light_r // 2)

        # move car if light is green
        if light_color == green:
            if car_pos_x < display_width:
                car_pos_x += car_speed
            else:
                car_pos_x = -car_width

        pygame.draw.rect(game_display, white, (car_pos_x, car_pos_y, car_width, car_height))
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()


if __name__ == '__main__':
    main()
