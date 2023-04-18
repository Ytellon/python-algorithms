speed = 61
place_car = 90

radar_1 = 60
place_1 = 100
radar_range = 1


if speed > radar_1:
    print(f'Você foi multado em R$ {place_car}')

if place_car >= (place_1 - radar_range) and \
        place_car <= (place_1 + radar_range):
    print(f'Você foi multado em R$ {place_car * radar_range}')