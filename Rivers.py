Rivers = {'nile':'egypt',
          'amazon':'brazil',
          'mekong':'china',
          }
for river, country in Rivers.items():
    print(f'The {river.title()} runs through {country.title()}\n' )

print('These are the Countries in this data set\n')
for river in Rivers:
    print(f'{river.title()}\n')
print('These are the Rivers in this data set\n')
for country in Rivers.values():
    print(f'{country.title()}\n')
