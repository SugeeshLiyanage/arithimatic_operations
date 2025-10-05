amount = int(input("enter the amonut you wan't to withdraw"))
note1 = amount // 100
note2 = (amount%100) // 50
note3 = ((amount%100)%50) // 10
print("note 100 is",note1)
print("note 50 is",note2)
print("note 10 is",note3)