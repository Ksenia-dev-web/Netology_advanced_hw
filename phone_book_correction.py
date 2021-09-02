# поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname соответственно.
# В записной книжке изначально может быть Ф + ИО, ФИО, а может быть сразу правильно: Ф+И+О;
# привести все телефоны в формат +7(999)999-99-99.
# Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999;
# объединить все дублирующиеся записи о человеке в одну.

from pprint import pprint
import csv
import re


def phonenumber_correction(phonenumber_line):
    pattern = r'(8|\+7)\s*\(?(\d\d\d)\)?\s*-*(\d\d\d)-*(\d\d)-*(\d\d)\s*\(?(доб.)*\s*(\d*)\)?'
    if 'доб.' not in phonenumber_line:
        sub = r'+7(\2)-\3-\4-\5'
    else:
        sub = r'+7(\2)-\3-\4-\5 \6\7'
    phonenumber_line[5] = re.sub(pattern, sub, phonenumber_line[5])
    return phonenumber_line


# читаем адресную книгу в формате CSV в список contacts_list

def main():
    with open("phonebook_raw.csv", encoding='UTF-8') as f:
        rows1 = csv.reader(f, delimiter=",")
        contacts_list = list(rows1)
        # pprint(contacts_list)

    # TODO 1: выполните пункты 1-3 ДЗ
    for info_line in contacts_list:
      fio = info_line[0] + ' ' + info_line[1] + ' ' + info_line[2]
      fio = re.split(' ', fio)
      for i in range(3):
         info_line[i] = fio[i]
         phonenumber_correction(info_line)

    corrected_contacts_list = []
    for i in range(len(contacts_list)):
        for j in range(len(contacts_list)):
            if contacts_list[i][0] == contacts_list[j][0]:
                contacts_list[i] = [x or y for x, y in zip(contacts_list[i], contacts_list[j])]
        if contacts_list[i] not in corrected_contacts_list:
            corrected_contacts_list.append(contacts_list[i])

    # TODO 2: сохраните получившиеся данные в другой файл
    # код для записи файла в формате CSV
    with open("phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        # Вместо contacts_list подставьте свой список
        datawriter.writerows(corrected_contacts_list)
    pprint(corrected_contacts_list)

if __name__ == "__main__":
    main()
