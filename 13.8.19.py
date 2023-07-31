vsego_biletov = int(input('Введите количество билетов: '))
vozrast_ychastnikov = []
for i in range(0, vsego_biletov):
    input_value = int(input(f'Введите возраст участника №{i + 1}:\n'))
    vozrast_ychastnikov.append(input_value)
    def tsena(age):
        if age < 18:
            return 0
        elif 18 <= age < 25:
            return 990
        else:
            return 1390

    stoimost_biletov = sum(map(tsena, vozrast_ychastnikov))

stoimpst_biletov_so_skidkoi = int(stoimost_biletov * 0.9)
if vsego_biletov > 3:
    print('Стоимость всех билетов со скидкой: ', stoimpst_biletov_so_skidkoi, "рублей")
else:
    print('Стоимость всех билетов: ', stoimost_biletov, "рублей")
