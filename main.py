import re
from pprint import pprint
import csv

with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
pprint(contacts_list)

pattern = r"(\+7|8)[\s(]*(\d{3})[)\s-]*(\d{3})[\s-]?(\d{2})[\s-]?(\d{2})?[\s]?[(]?(\доб.)?[\s-]?[\s-]?(\d{4})?[)\s-]?"
new_pattern = r"+7(\2)\3-\4-\5 \6\7"

new_contact_list=list()
for record in contacts_list:
  string = ','.join(record)
  format = re.sub(pattern, new_pattern, string)
  page_list = format.split(',')
  new_contact_list.append(page_list)
  # print(new_contact_list)

pattern2 = r"^([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]+)" \
               r"(\s*)(\,?)([А-ЯЁа-яё]*)(\,?)(\,?)(\,?)"
new_pattern2 = r"\1\3\10\4\6\9\7\8"
contacts_list = list()
for rec in new_contact_list:
  string = ','.join(rec)
  format_page = re.sub(pattern2, new_pattern2, string)
  page_list = format_page.split(',')
  if page_list not in contacts_list:
    contacts_list.append(page_list)
    print(contacts_list)

with open("phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(contacts_list)





