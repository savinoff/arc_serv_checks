from classes.arcserv import ArcServ
from classes.testresult import TestResult

def check_period(arcserv: ArcServ) -> TestResult:
    res = TestResult()
    allowed_periods = ['Q1_2021', 'Q12021', 'Q2_2021', 'Q22021', 'Q3_2021', 'Q32021', 'Q4_2021', 'Q42021']
    if arcserv.period in allowed_periods:
        res = TestResult('OK', f'{arcserv.period} в списке разрешённых периодов')
    else:
        res.result_code = 'Error'
        res.result_description = f'{arcserv.period} не в списке разрешённых периодов'
    return res

