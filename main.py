import numpy as np
from PIL import Image


class Ant:
    def __init__(self) -> None:
        self.size: int = 1024
        self.position: list[int] = [512, 512]
        self.borders: tuple[int, int] = (0, self.size - 1)
        self.direction: int = 0
        self.field = np.zeros([self.size, self.size], dtype=int)

    def __is_direction_correct(self) -> None:
        if self.direction < 0:
            self.direction = 3
        elif self.direction > 3:
            self.direction = 0

    def __moving(self) -> None:
        match self.direction:
            case 0:  #! up
                self.position[0] -= 1
            case 1:  #! right
                self.position[1] += 1
            case 2:  #! down
                self.position[0] += 1
            case 3:  #! left
                self.position[1] -= 1

    def __change_cell(self, num: int) -> None:
        if num == 0:
            self.direction -= 1
        elif num == 1:
            self.direction += 1

        self.__is_direction_correct()
        self.field[self.position[0], self.position[1]] = num
        self.__moving()

    def _movement(self) -> None:
        while (
            self.position[0] not in self.borders
            and self.position[1] not in self.borders
        ):
            if self.field[self.position[0], self.position[1]] == 0:
                self.__change_cell(1)
            else:
                self.__change_cell(0)

    def _sum_black_cells(self) -> None:
        print(self.field.sum())

    def _save_field(self) -> None:
        image = Image.fromarray(
            ((np.ones([self.size, self.size]) - self.field) * 255).astype(np.uint8),
            mode="L",
        )
        image.save("img.png", bits=1, optimize=True)

    def resalt(self) -> None:
        self._movement()
        self._sum_black_cells()
        self._save_field()


a = Ant()
a.resalt()
