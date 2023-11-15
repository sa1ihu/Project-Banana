def res(ans):
    if ans < 18.5:
        return 'Underweight'
    elif ans >= 18.5 and ans <= 24.9:
        return 'Normal'
    elif ans >= 25 and ans <= 29.9:
        return 'Overweight'
    else:
        return 'Obese'


while True:
    try:
        wt = float(input('Enter your weight in Kilograms: '))
        ht = float(input('Enter your height in Meters: '))
        ans = wt/(ht)** 2
        x = res(ans)
        print(f"{ans}: {x}")
        break
    except (ValueError, TypeError) as e:
        print(f"An error occured: {e}")

