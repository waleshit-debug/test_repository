def mass_index():
    height = float(input())
    weight = float(input())
    index_calculations = weight/height**2 
    if index_calculations > 25:
        print("Избыточная масса")
    elif index_calculations <= 25 and index_calculations >= 18:
         print("Оптимальная масса")
    else:
        print("Недостаточная масса")
        
mass_index()
