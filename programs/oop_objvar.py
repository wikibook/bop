class Robot:
    """이름을 가진 로봇을 나타냅니다."""

    # 로봇의 수를 세는 클래스 변수
    population = 0

    def __init__(self, name):
        """데이터를 초기화합니다."""
        self.name = name
        print("(Initializing {})".format(self.name))

        # 이 로봇이 생성되면 로봇 수에 더해집니다.
        Robot.population += 1

    def die(self):
        """저는 죽어가고 있습니다."""
        print("{} is being destroyed!".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(
                Robot.population))

    def say_hi(self):
        """로봇이 인사합니다.

        로봇은 인사할 수 있습니다."""
        print("Greetings, my masters call me {}.".format(self.name))

    @classmethod
    def how_many(cls):
        """현재 로봇 수를 출력합니다."""
        print("We have {:d} robots.".format(cls.population))


droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()

Robot.how_many()
