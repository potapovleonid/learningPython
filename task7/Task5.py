class Employee:
    def __init__(self, name, seniority):
        self.name = name
        self.seniority = seniority

        self.grade = 1

    def grade_up(self):
        """Повышает уровень сотрудника"""
        self.grade += 1

    def publish_grade(self):
        """Публикация результатов аккредитации сотрудников"""
        print(f"{self.name} has grade: {self.grade}")

    def check_if_it_is_time_for_upgrade(self):
        pass


class Developer(Employee):
    def __init__(self, name, seniority):
        super().__init__(name, seniority)

    def check_if_it_is_time_for_upgrade(self):
        # для каждой аккредитации увеличиваем счетчик на 1
        # пока считаем, что все разработчики проходят аккредитацию
        self.seniority += 1

        # условие повышения сотрудника из презентации
        if self.seniority % 5 == 0:
            self.grade_up()

        # публикация результатов
        return self.publish_grade()


class Designer(Employee):

    def __init__(self, name, seniority, awards=2):
        super().__init__(name, seniority)
        self.awards = awards

    def publish_grade(self):
        print(f"{self.name} has grade: {self.grade} and also {self.awards} awards")

    def check_if_it_is_time_for_upgrade(self):
        self.seniority += 1

        if self.seniority % 7 == 0:
            self.grade_up()

        return self.publish_grade()

    def award_up(self):
        self.awards += 1


alex = Developer('Alexander', 0)
for i in range(20):
    alex.check_if_it_is_time_for_upgrade()


elena = Designer('Elena', seniority=0, awards=3)
for i in range(20):
    elena.check_if_it_is_time_for_upgrade()
    if i%5 == 0:
        elena.award_up()
