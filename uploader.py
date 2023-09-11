import json
import requests
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from bs4 import BeautifulSoup
# Считываем данные из JSON файла
with open('C:/Users/user/Desktop/swgoh_bot/data_swgoh_332.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

wb = Workbook()

# Удаляем начальную страницу (по умолчанию sheet)
default_sheet = wb['Sheet']
wb.remove(default_sheet)

roles_url = 'https://swgoh.gg/g/Z0kME2OMScC4ipNLpCpeSw/'

# Отправляем GET-запрос и создаем объект BeautifulSoup
roles_response = requests.get(roles_url)
roles_soup = BeautifulSoup(roles_response.text, 'html.parser')

player_roles = {}


# Проходим по данным из JSON файла и записываем их в файл Excel
for player_id, player_data in data.items():
    # Получаем имя игрока с сайта
    player_url = f'https://swgoh.gg/p/{player_id}/'
    response = requests.get(player_url)
    #role = player_roles.get(player_name, '')
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        player_name = soup.find('h5').text.strip()
        galactic_power_element = soup.select_one('html > body > div:nth-of-type(3) > div:nth-of-type(1) > div:nth-of-type(2) > ul > li:nth-of-type(8) > div > div:nth-of-type(1) > span:nth-of-type(2) > strong')
        galactic_power = galactic_power_element.text
        lvl = soup.select_one('body > div.container.p-t-md > div.content-container > div.content-container-aside > div.panel.panel-default.panel-profile.m-b-sm > div.panel-body > ul > li:nth-child(3) > h5').text.strip()
        # Удалите запятые и конвертируйте в число
        galactic_power = int(galactic_power.replace(',', ''))
    else:
        player_name = 'Unknown'
        galactic_power = 0  # По умолчанию

    # Добавляем имя игрока и галактическую мощь в JSON данные
    player_data['player_name'] = player_name
    player_data['galactic_power'] = galactic_power

    # Создаем новый лист с именем недели
    progress_in_week = player_data.get('progress_in_week', {})
    for week, week_data in progress_in_week.items():
        avg_energy = week_data.get('avg_energy', '')
        activ_gild_war = week_data.get('activ_gild_war', '')
        activ_battles = week_data.get('activ_battles', '')

        # Создаем новый лист с именем недели
        ws = wb.create_sheet(title=week)

        # Записываем заголовки столбцов
        headers = ["Player Name", "Galactic Power", "Player ID", "Level", "Role", "Average Energy", "Active Guild War", "Active Battles", "Plan"]
        ws.append(headers)
        # Записываем данные в файл Excel
        row = [player_name, galactic_power, player_id, lvl, player_data.get('role', ''), avg_energy, activ_gild_war, activ_battles, player_data.get('plan', '')]
        ws.append(row)

# Обновляем исходный JSON файл с добавленными данными
with open('your_json_file.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

# Сохраняем файл Excel
wb.save('output.xlsx')

#/html/body/div[3]/div[1]/div[2]/ul/li[2]/div/table/tbody/tr[1]
#/html/body/div[3]/div[1]/div[2]/ul/li[2]/div/table/tbody/tr[2]

print("Данные успешно записаны в файл Excel и обновлены в исходном JSON файле.")