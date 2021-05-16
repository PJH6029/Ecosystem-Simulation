import random

# 맵 크기
MAP_WIDTH = 1000
MAP_HEIGHT = 1000
# 개체 증가 시 변이율
MUTATION_RATE = 0.3
# 두 개체가 만났을 때 호전성
GENTLE = 0
NORMAL = 1
HOSTILE = 2
# 맵의 상태
BARREN = 0
GRASS = 1
OCCUPIED = 2


class world:
    def __init__(self):
        self.map = [[random.randrange(0, 2) for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]
        self.time = 0
        self.lives = []


class creature:
    def __init__(self, x, y, power, velocity, intelligence, fertility, hostility):
        self.x = x
        self.y = y
        self.power = power
        self.velocity = velocity
        self.intelligence = intelligence
        self.fertility = fertility
        self.hostility = hostility
        self.energy_total = power + velocity + intelligence + fertility # 함수화 필요
        self.energy_left = self.energy_total
        self.lifespan = 100 / self.energy_total # 함수화 필요

    def age(self, world):
        self.lifespan -= 1
        if self.lifespan < 0:
            world.map[self.x][self.y] = GRASS
            world.lives.remove(self)
        # 일정 확률로 아이를 낳는다
        if random.randrange(0, int(100 / self.fertility) + 1) < 5: # 함수화 필요
            self.breed(world)

    def breed(self, world):
        power = self.power
        velocity = self.velocity
        intelligence = self.intelligence
        fertility = self.fertility
        hostility = self.hostility
        # 돌연변이
        if random.randrange(0, int(1 / MUTATION_RATE)) == 0:
            r = random.randrange(0, 5)
            if r == 0:
                power = self.power + random.randrange(-2, 3)
                if power < 1:
                    power = 1
                elif power > 10:
                    power = 10
            elif r == 1:
                velocity = self.velocity + random.randrange(-2, 3)
                if velocity < 1:
                    velocity = 1
                elif velocity > 10:
                    velocity = 10
            elif r == 2:
                intelligence = self.intelligence + random.randrange(-2, 3)
                if intelligence < 1:
                    intelligence = 1
                elif intelligence > 10:
                    intelligence = 10
            elif r == 3:
                fertility = self.fertility + random.randrange(-2, 3)
                if fertility < 1:
                    fertility = 1
                elif fertility > 10:
                    fertility = 10
            elif r == 4:
                hostility = self.hostility + random.randrange(-1, 2)
                if hostility < 0:
                    hostility = 0
                elif hostility > 2:
                    hostility = 2

        c = creature(self.x + random.randrange(0, 2), self.y + random.randrange(0, 2),
                     power, velocity, intelligence, fertility, hostility)
        world.lives.append(c)


# 월드 초기화
w = world()
# 초기 생명체 100마리
for i in range(100):
    x, y = 0, 0
    while True:
        x = random.randrange(0, MAP_WIDTH)
        y = random.randrange(0, MAP_HEIGHT)
        if w.map[x][y] != OCCUPIED:
            break
    c = creature(x, y, 1, 1, 1, 1, GENTLE)
    w.lives.append(c)
    w.map[x][y] = OCCUPIED

# 월드 시작
while w.time < 1000:
    for c in w.lives:
        c.age(w)
    w.time += 1