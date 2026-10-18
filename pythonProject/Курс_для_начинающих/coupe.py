def coupe(seat: int) -> int:
    coupe_number = (seat - 1) // 4 + 1
    return coupe_number

seat = int(input())

print(coupe(seat))