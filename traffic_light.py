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
car_width = 40
car_height = 80

# traffic light
light_r = 50
light_pos_x = 100
light_pos_y = display_height // 2 - light_r // 2
circle_vertical_distance = light_r * 1.5
clock = pygame.time.Clock()

# Font settings
font = pygame.font.Font(None, 36)


def main():
    car_pos_x = display_width // 2 - car_width // 2
    car_pos_y = display_height - car_height
    car_speed = 5
    light_colors = ["Green", "Red", "Yellow"]
    current_light_index = 0
    last_color_change_time = time.time()

    # Loop
    game_exit = False
    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

        # Update color
        elapsed_time = time.time() - last_color_change_time
        if elapsed_time > 2:
            current_light_index = (current_light_index + 1) % 3
            last_color_change_time = time.time()

        game_display.fill(black)

        # Draw road
        road_width = 200  # Increased road width
        road_x = display_width // 2 - road_width // 2  # Centered horizontally
        pygame.draw.rect(game_display, grey, (road_x, 0, road_width, display_height))

        # Draw traffic light
        for i in range(3):
            light_y = light_pos_y + i * circle_vertical_distance
            pygame.draw.circle(game_display, black, (light_pos_x, light_y), light_r)

            # Draw the current active light in color, others in gray
            if i == current_light_index:
                pygame.draw.circle(game_display, light_colors[i], (light_pos_x, light_y), light_r // 2)
            else:
                pygame.draw.circle(game_display, grey, (light_pos_x, light_y), light_r // 2)

        # Move car if light is green
        if current_light_index == 0:  # Green light
            if car_pos_y > -car_height:
                car_pos_y -= car_speed
            else:
                car_pos_y = display_height

        pygame.draw.rect(game_display, white, (car_pos_x, car_pos_y, car_width, car_height))

        # Display text indicating which light is glowing
        text = "Light: " + light_colors[current_light_index]
        text_render = font.render(text, True, white)
        game_display.blit(text_render, (10, 10))

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()


if __name__ == '__main__':
    main()
