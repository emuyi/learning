# testing for 12-05
import importlib
lst = []
with open('cases.txt') as f:
    for line in f:
        if ',' in line:
            case, circle = line.split(',')
            for i in range(1, int(circle.strip())+1):
                lst.append('{0}_C{1}'.format(case.strip(), str(i)))
        else:
            lst.append('{}_null'.format(line.strip()))

for case_name in lst:
    case_id, circle = case_name.rsplit('_', maxsplit=1)
    pyfile = importlib.import_module(case_id)
    case = getattr(pyfile, case_id)()
    case.case_id = case_name.strip('_null')
    case.run()

