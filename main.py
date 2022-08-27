import re
from pprint import pprint
import csv

with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
  # pprint(contacts_list)

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
# pprint(contacts_list)

new_list = [contacts_list [0]]
contacts_list.pop(0)
contacts_list.sort()
new_list.append(contacts_list[0])
i = 1
for rec in contacts_list:
  if rec[0] == new_list[i][0] and rec[1] == new_list[i][1]:
    if rec[2] != '':
      new_list[i][2] = rec[2]
    if rec[3] != '':
      new_list[i][3] = rec[3]
    if rec[4] != '':
      new_list[i][4] = rec[4]
    if rec[5] != '':
      new_list[i][5] = rec[5]
    if rec[6] != '':
      new_list[i][6] = rec[6]
  else:
    new_list.append(rec)
    i = i+1

  # temp_voc = {}
  # voc={}
  # for record in list:
  #   temp_voc[record[0], record[1]] = (record[2], record[3], record[4], record[5], record[6])
  #
  # for fio, data in temp_voc.items():
  #   if data [0] == 0:
  #     voc[fio] = data
  # pprint(voc)


with open("phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(new_list)


