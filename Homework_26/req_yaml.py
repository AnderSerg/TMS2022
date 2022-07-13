import yaml
from pprint import pprint

with open('order.yaml') as f:
    templates = yaml.safe_load(f)

pprint(templates)

# yaml.dump_all(templates)

print(templates['invoice'])

print(templates['bill-to']["address"])
