class Employee:
    def __init__(self, id, name, *args):
        self.id = id
        self.name = name

    def get_info(self):
        print(F'Имя сотрудника: {self.name} его id: {self.id}')


class Manager(Employee):
    def __init__(self, id, name, department, project_name, *args):
        super().__init__(id, name, *args)
        self.project_name = project_name
        self.department = department

    def manage_project(self, new_project_name):
        self.project_name = new_project_name
        print(f'Сейчас сотрудник: {self.name} перенаправлен на проект {self.project_name}')


class Technician(Employee):
    def __init__(self, id, name, specialization, activity, *args):
        super().__init__(id, name, *args)
        self.activity = activity
        self.specialization = specialization

    def perform_maintenance(self, progress):
        self.activity = progress
        print(f'Сейчас статус проекта сотрудника: {self.name} = {self.activity}')


class TechManager(Manager, Technician):
    def __init__(self, id, name, department, project_name, specialization, activity, *args):
        # self.id = id
        # self.name = name
        # self.department = department
        # self.project_name = project_name
        # self.specialization = specialization
        # self.activity = activity
        super().__init__(id, name, department, project_name, specialization, activity, *args)

    def add_employee(name, department, project_name, specialization, activity):
        id = str("{:04}".format(int(employs[-1].id) + 1))
        employs.append(TechManager(id, name, department, project_name, specialization, activity))

    def get_team_info():
        for i in employs:
            print(
                f'сотрудник №{i.id} | имя: {i.name} | отдел: {i.department} | специализация: {i.specialization} | проект: {i.project_name} | ход выполнения: {i.activity}')


TechManagerVovan = TechManager('0001', 'vladimir', 'IT', 'AI calculator', 'Python dev', 'in progress')
TechManagerBura = TechManager('0002', 'yuriy', 'IT', 'labs', 'Python dev', 'in progress')
TechManagerSveta = TechManager('0003', 'svetlana', 'crasivosti', 'UI for AI calculator', 'designer', 'in progress')
TechManagerBalbes = TechManager('0004', 'evgeniy', 'experts', 'nothing', 'sofa_expert', 'done')
employs = [TechManagerVovan, TechManagerBura, TechManagerSveta, TechManagerBalbes]

TechManager.get_team_info()
TechManager.add_employee('kolya', 'cars', 'V8 boost', 'car mechanic', 're-stitching')
print()
TechManager.get_team_info()
print()
TechManagerBura.get_info()
TechManagerBalbes.perform_maintenance('done')
TechManagerVovan.manage_project('sleep')

print(TechManager.mro())