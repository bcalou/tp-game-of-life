import pygame
from game_of_life.constants import SCREEN_SIZE, INITIAL_STATE, \
    UPDATES_PER_SECOND
from game_of_life.game import update, get_next_state

screen: pygame.surface.Surface = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

done: bool = False
state: list[list[int]] = INITIAL_STATE

# Game loops until it's over
while not done:

    # Listen for all events
    for event in pygame.event.get():

        # Quit the infinite loop when the user presses the close button
        if event.type == pygame.QUIT:
            done = True

    update(screen, state)
    state = get_next_state(state)
    clock.tick(UPDATES_PER_SECOND)

pygame.quit()
