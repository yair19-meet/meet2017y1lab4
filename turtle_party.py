strawberries = int(input("Enter a strawberries number"))
is_weekend = bool(input("Enter a boolean: "))

       
   
if is_weekend:
    if strawberries > 39:
            print('Fun!')
    else:
            print('Not Fun!')

else:
    if strawberries > 39 and strawberries < 61:
            print('Fun')
    else:
        print('Not Fun')
              
