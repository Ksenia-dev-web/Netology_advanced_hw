import json


class GetCountries:
    def __init__(self, json_file):
        with open(json_file, 'r') as f:
            self.get_countries = json.load(f)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.get_countries:
            raise StopIteration
        name_ = self.get_countries.pop().get('name').get('common')
        link_ = 'https://en.wikipedia.org/wiki/' + name_.replace(' ','-')
        return name_, link_


countries_link = GetCountries('countries.json')

with open('links_list.txt', 'w') as output_f:
    for name, link in countries_link:
        line_ = name + ' - ' + link + '\n'
        output_f.write(line_)
