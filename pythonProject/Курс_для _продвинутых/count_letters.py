def telegram_count():
    text = str(input())
    total = 0
    for f in text:
        total += 60
    
    rubles = total // 100 
    pennies = total % 100 

    print(f"{rubles} р. {pennies} коп.")

telegram_count()