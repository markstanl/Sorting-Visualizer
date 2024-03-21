import pygame
import random
import math
from BubbleSort import BubbleSort

pygame.init()


class DrawingInformation:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    RED = 255, 0, 0
    GREEN = 0, 255, 0
    BLUE = 0, 0, 255
    GREY = 128, 128, 128
    BACKGROUND_COLOR = WHITE

    GRADIENTS = [
        GREY,
        (160, 160, 160),
        (192, 192, 192),
    ]

    FONT = pygame.font.SysFont('InputSans-Medium.ttf', 30)
    LARGE_FONT = pygame.font.SysFont('InputSans-Medium.ttf', 40)

    SIDE_PAD = 100
    TOP_PAD = 150

    def __init__(self, width, height, lst):
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        self.set_list(lst)

    def set_list(self, lst):
        self.lst = lst
        self.min_value = min(lst)
        self.max_value = max(lst)

        self.bar_width = round((self.width - self.SIDE_PAD) / len(lst))
        self.block_height = math.floor((self.height - self.TOP_PAD) / (self.max_value - self.min_value))
        self.start_x = self.SIDE_PAD // 2


def draw(draw_info):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)

    controls = draw_info.FONT.render(
        "R - Reset | SPACE - Start Sorting", 1,
        draw_info.BLACK)
    draw_info.window.blit(controls, (draw_info.width/2 - controls.get_width()/2, 10))
    sorting = draw_info.FONT.render(
        "C - Change Sorting Algorithm", 1,
        draw_info.BLACK)
    draw_info.window.blit(sorting, (draw_info.width/2 - sorting.get_width()/2, 40))

    draw_list(draw_info)
    pygame.display.update()


def draw_list(draw_info, color_positions={}, clear_bg=False):
    lst = draw_info.lst

    if clear_bg:
        clear_rect = (draw_info.SIDE_PAD // 2, draw_info.TOP_PAD,
                      draw_info.width - draw_info.SIDE_PAD, draw_info.height - draw_info.TOP_PAD)
        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOR, clear_rect)

    for i, value in enumerate(lst):
        x = draw_info.start_x + i * draw_info.bar_width
        y = draw_info.height - (value - draw_info.min_value) * draw_info.block_height

        color = draw_info.GRADIENTS[i % 3]
        if i in color_positions:
            color = color_positions[i]

        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.bar_width, value * draw_info.block_height))

    if clear_bg:
        pygame.display.update()

def bubble_sort(draw_info):
    lst = draw_info.lst
    bubble_sort = BubbleSort(draw_info)
    green_index = 0
    while True:
        try:
            lst_copy = lst.copy()
            lst = next(bubble_sort)
            for i in range(len(lst)):
                if lst[i] != lst_copy[i]:
                    green_index = i
                    break
            draw_list(draw_info, {green_index: draw_info.GREEN, green_index + 1: draw_info.RED}, True)
            yield True
        except StopIteration:
            break

    return lst



def generate_starting_list(n):
    return random.sample(range(n), n)


def main():
    run = True
    clock = pygame.time.Clock()

    n = 50

    lst = generate_starting_list(n)
    draw_info = DrawingInformation(800, 600, lst=lst)
    sorting = False

    sorting_algorithm = bubble_sort
    sorting_algo_name = "Bubble Sort"
    sorting_algo_generator = None

    while run:
        clock.tick(60)

        if sorting:
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
                sorting = False
        else:
            draw(draw_info)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    lst = generate_starting_list(n)
                    draw_info.set_list(lst)
                    sorting = False
                elif event.key == pygame.K_SPACE and not sorting:
                    sorting = True
                    sorting_algorithm_generator = sorting_algorithm(draw_info)

        pygame.display.update()


if __name__ == "__main__":
    main()


