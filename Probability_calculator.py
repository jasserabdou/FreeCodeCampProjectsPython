import random
import copy


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        drawn_balls = []
        if num_balls >= len(self.contents):
            drawn_balls = self.contents
            self.contents = []
        else:
            for _ in range(num_balls):
                random_index = random.randint(0, len(self.contents) - 1)
                drawn_balls.append(self.contents.pop(random_index))
        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        drawn_balls_dict = {}
        for ball in drawn_balls:
            drawn_balls_dict[ball] = drawn_balls_dict.get(ball, 0) + 1

        success = True
        for color, count in expected_balls.items():
            if color not in drawn_balls_dict or drawn_balls_dict[color] < count:
                success = False
                break

        if success:
            success_count += 1

    return success_count / num_experiments


if __name__ == '__main__':
    hat = Hat(black=6, red=4, green=3)
    probability = experiment(hat=hat, expected_balls={
                             "red": 2, "green": 1}, num_balls_drawn=5, num_experiments=2000)
    print("Probability:", probability)
