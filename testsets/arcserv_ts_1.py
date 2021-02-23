

from classes.arctest import ArcTestList, ArcTest
from testsets.testfunctions.arcservtestfunctions import check_period


testset = ArcTestList('TS_1', 'Список тестов 1 по архитектуре сервиса')


# TODO: Перенести функцию в параметры создания теста
test1 = ArcTest('T1', 'Проверка на период')
test1.test_function = check_period

testset.append(test1)
