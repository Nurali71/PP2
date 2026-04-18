import pygame

class MusicPlayer:
    def __init__(self, playlist):
        self.playlist = playlist
        self.index = 0
        pygame.mixer.init()

    def play(self):
        # Загружаем текущий файл из списка по индексу
        pygame.mixer.music.load(self.playlist[self.index])
        pygame.mixer.music.play()

    def stop(self):
        pygame.mixer.music.stop()

    def next(self):
        # Переходим к следующему треку (остаток от деления для круга)
        self.index = (self.index + 1) % len(self.playlist)
        self.play()

    def prev(self):
        # Переходим к предыдущему треку
        self.index = (self.index - 1) % len(self.playlist)
        self.play()

    def current_track_name(self):
        # Возвращаем имя файла
        return self.playlist[self.index]