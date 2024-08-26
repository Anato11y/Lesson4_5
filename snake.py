import pygame  # Импортируем библиотеку Pygame для создания игры
import time  # Импортируем библиотеку time для управления временем (не используется в коде)
import random  # Импортируем библиотеку random для генерации случайных значений

pygame.init()  # Инициализируем все модули Pygame

# Определение цветов
white = (255, 255, 255)  # Белый цвет для текста
yellow = (255, 255, 102)  # Желтый цвет (не используется)
black = (0, 0, 0)  # Черный цвет для фона
red = (213, 50, 80)  # Красный цвет для сообщения о проигрыше
green = (0, 255, 0)  # Зеленый цвет для змейки
blue = (50, 153, 213)  # Синий цвет для еды

# Размеры экрана
dis_width = 600  # Ширина игрового окна
dis_height = 400  # Высота игрового окна

# Создание экрана
icon = pygame.image.load('pngwing.png')  # Загрузка изображения иконки
pygame.display.set_icon(icon)   # Установка иконки окна

dis = pygame.display.set_mode((dis_width, dis_height))  # Устанавливаем размеры игрового окна
pygame.display.set_caption('Змейка')  # Устанавливаем заголовок окна

clock = pygame.time.Clock()  # Создаем объект clock для управления частотой кадров
snake_block = 10  # Размер одного блока змейки
snake_speed = 15  # Скорость движения змейки

# Шрифты для отображения текста
font_style = pygame.font.SysFont(None, 50)  # Шрифт для вывода сообщений
score_font = pygame.font.SysFont(None, 35)  # Шрифт для вывода счета

# Функция для отображения счета
def your_score(score):
    value = score_font.render("Ваш счёт: " + str(score), True, white)  # Создаем текст для отображения счета
    dis.blit(value, [0, 0])  # Отображаем текст в верхнем левом углу экрана

# Функция для отрисовки змейки
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])  # Рисуем каждый блок змейки

# Функция для отображения сообщения о проигрыше в несколько строк
def message(msg1, msg2, msg3, color):
    mesg1 = font_style.render(msg1, True, color)  # Создаем первую строку сообщения
    mesg2 = font_style.render(msg2, True, color)  # Создаем вторую строку сообщения
    mesg3 = font_style.render(msg3, True, color)  # Создаем третью строку сообщения
    dis.blit(mesg1, [dis_width / 6, dis_height / 3])  # Отображаем первую строку на экране
    dis.blit(mesg2, [dis_width / 6, dis_height / 3 + 40])  # Отображаем вторую строку на экране с отступом
    dis.blit(mesg3, [dis_width / 6, dis_height / 3 + 80])  # Отображаем третью строку на экране с отступом

# Основной игровой цикл
def gameLoop():
    game_over = False  # Переменная для проверки окончания игры
    game_close = False  # Переменная для проверки состояния проигрыша

    x1 = dis_width / 2  # Начальная позиция змейки по оси X
    y1 = dis_height / 2  # Начальная позиция змейки по оси Y

    x1_change = 0  # Изменение позиции змейки по оси X (вначале не движется)
    y1_change = 0  # Изменение позиции змейки по оси Y (вначале не движется)

    snake_List = []  # Список для хранения блоков змейки
    Length_of_snake = 1  # Начальная длина змейки

    # Позиция еды
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0  # Случайное положение еды по X
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0  # Случайное положение еды по Y

    while not game_over:

        while game_close == True:  # Если игра окончена, отображаем сообщение
            dis.fill(black)  # Заполняем экран черным цветом
            message("Вы проиграли!", "Нажмите Q для выхода", "или C для новой игры", red)  # Сообщение о проигрыше
            your_score(Length_of_snake - 1)  # Отображаем текущий счет
            pygame.display.update()  # Обновляем экран

            for event in pygame.event.get():  # Обрабатываем события
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:  # Если нажата клавиша Q, выходим из игры
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:  # Если нажата клавиша C, запускаем игру заново
                        gameLoop()

        for event in pygame.event.get():  # Обработка событий во время игры
            if event.type == pygame.QUIT:  # Если закрываем окно, завершаем игру
                game_over = True
            if event.type == pygame.KEYDOWN:  # Если нажата клавиша
                if event.key == pygame.K_LEFT:  # Движение змейки влево
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:  # Движение змейки вправо
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:  # Движение змейки вверх
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:  # Движение змейки вниз
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:  # Проверка на столкновение с границей экрана
            game_close = True
        x1 += x1_change  # Обновляем позицию змейки по X
        y1 += y1_change  # Обновляем позицию змейки по Y
        dis.fill(black)  # Очищаем экран
        pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])  # Рисуем еду
        snake_Head = []  # Создаем голову змейки
        snake_Head.append(x1)  # Добавляем позицию головы по X
        snake_Head.append(y1)  # Добавляем позицию головы по Y
        snake_List.append(snake_Head)  # Добавляем голову змейки в список

        if len(snake_List) > Length_of_snake:  # Если змейка длиннее нужной длины, удаляем последний блок
            del snake_List[0]

        for x in snake_List[:-1]:  # Проверка на столкновение змейки с самой собой
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)  # Рисуем всю змейку
        your_score(Length_of_snake - 1)  # Отображаем текущий счет

        pygame.display.update()  # Обновляем экран

        if x1 == foodx and y1 == foody:  # Если змейка съела еду
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0  # Новая позиция еды по X
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0  # Новая позиция еды по Y
            Length_of_snake += 1  # Увеличиваем длину змейки

        clock.tick(snake_speed)  # Устанавливаем скорость игры

    pygame.quit()  # Завершаем работу Pygame
    quit()  # Выход из программы

gameLoop()  # Запуск игрового цикла
