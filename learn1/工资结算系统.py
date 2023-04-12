from abc import ABCMeta, abstractmethod


class Employee(metaclass=ABCMeta):
    """员工类"""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        """结算月薪（抽象方法）"""
        pass


class Manager(Employee):
    """部门经理"""

    def get_salary(self):
        return 15000.0


class Programmmer(Employee):
    """程序员"""

    def __init__(self, name, work_hour=0):
        self.work_hour = work_hour
        super().__init__(name)

    def get_salary(self):
        return 200.0 * self.work_hour


class Salesman(Employee):
    """销售员"""

    def __init__(self, name, sales=0.0):
        self.sales = sales
        super().__init__(name)

    def get_salary(self):
        return 1800.0 + self.sales * 0.05


class EmployeeFactory:
    """创造员工的工厂"""

    @staticmethod
    def create(emp_type, *args):
        """创建员工"""
        all_emp_types = {'M': Manager, 'P': Programmmer, 'S': Salesman}
        cls = all_emp_types[emp_type.upper()]
        return cls(*args) if cls else None


def main():
    """主函数"""
    emps = [
        EmployeeFactory.create('M', '曹操'),
        EmployeeFactory.create('P', '荀彧', 120),
        EmployeeFactory.create('P', '郭嘉', 85),
        EmployeeFactory.create('S', '典韦', 123000),
    ]
    for emp in emps:
        print(f'{emp.name}:{emp.get_salary():.2f}元')
        print(emp)


if __name__ == '__main__':
    main()
