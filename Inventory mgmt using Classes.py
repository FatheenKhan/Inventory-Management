import json

class inventory:

    def __init__(self) -> None:
        pass

    def enter():
        id = input("Enter product Id")
        name = input("enter the product name")
        brand = input("enter the product brand")
        price = input("enter the product price")
        y = {
            'Name': name, 
            'Brand': brand, 
            'Price': price
            }
        I.write(y,id ) 
    
    def write(new_data, key, filename = 'learnjson3.json'):
        print(new_data)
        print(key)
        with open(filename, 'r+') as f:
            file_data = json.load(f)
            file_data[key] = new_data
            f.seek(0)
            json.dump(file_data, f, indent= 0)
    
    def chek( filename = 'learnjson3.json'): 
        id = input("enter the product id for which you want to change")
        with open(filename, 'r+') as f:
            file_data = json.load(f)
            print(file_data)
            for key in file_data.keys():
                if key == id:
                    name = input("enter the product name")
                    brand = input("enter the product brand")
                    price = input("enter the product price")
                    y =  {'Name': name, 
                        'Brand': brand, 
                        'Price': price
                        }
                    I.write(y,id ) 
    
    def display(filename = 'learnjson3.json'):
        with open(filename, 'r+') as f:
            file_data = json.load(f)
            print(file_data)
    
    def delete(filename = 'learnjson3.json'):
        id = input("enter the product id for which you want to delete")   
        with open(filename, 'r+') as f:
            file_data = json.load(f)
            del file_data[id]                           #With this command we delete the dictionary from te json file
            with open(filename, 'r+') as f:
                json.dump(file_data, f, indent= 0)
                I.display()
        

    

I = inventory
t = True
while t == True:
    a = input("Enter the Action \n Click 1 to display all contents \n Click 2 to add product \n Click 3 to alter product \n Click 4 to delete a product")
    if a == "1":
        I.display()
    elif a == "2":
        I.enter()
    elif a == "3":
        I.chek()
    elif a =="4":
        I.delete()
    else:
        t = False



