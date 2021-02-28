c = 3e8
time_light = 1.0
distance = c*time_light

v_car = 1.2e5/3.6e3
time_car = 3e8/v_car
timeh_car = time_car/(24*3600)

print('For a light second a car needs',time_car,'seconds'
      '\nThat\'s',timeh_car,'days')
