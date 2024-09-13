class EmployeeManager: 
    employees = {}

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        EmployeeManager.employees[self.name] = self.salary 
        # employees = {}에 저장되어 있는 직원들의 이름을 Key, 그에 해당하는 월급의 액수를 value로 하여 Dict 구성

    @classmethod
    def calculate_average_salary(cls):
        if not cls.employees:
            return 0 # 직원이 없을 때는 0을 반환 

        total_salary = sum(cls.employees.values()) # 값에 저장된 월급을 전부 더 함
        personnel = len(cls.employees.keys()) # 직원의 수 구하기 
        average_salary = total_salary / personnel # 평균 급여 계산
        print(f'직원 평균 급여: {average_salary}원')
        return average_salary

# 사용 예시
if __name__ == "__main__":
    emp1 = EmployeeManager("홍길동", 50000)
    emp2 = EmployeeManager("김철수", 60000)

    EmployeeManager.calculate_average_salary()
