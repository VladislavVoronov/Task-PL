import json


def parse(test, values):
    for t in test:
        if not ((t.get('id') is None) or (t.get('value') is None)):
            t['value'] = values.get(t.get('id'))
        if not (t.get('values') is None):
            parse(t['values'], values)


print('Путь к файлу tests:')
tests_fn = input()
print('Путь к файлу values:')
values_fn = input()
print('Путь к файлу report:')
report_fn = input()

# tests_fn = 'tests.json'
# values_fn = 'values.json'
# report_fn = 'report.json'

with open(tests_fn, 'r') as f:
    test = json.load(f)
with open(values_fn, 'r') as f:
    values = json.load(f)

nvalues = {}
for v in values['values']:
    nvalues[v['id']] = v['value']

parse(test['tests'], nvalues)

with open(report_fn, "w") as f:
    json.dump(test, f, indent=4)


