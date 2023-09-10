from rembg import remove



input_path = 'C://Users//Dell//Desktop//לימודים//python//remove-background-from-photo/logoTest.jpg'
output_path = 'C://Users//Dell//Desktop//לימודים//python//remove-background-from-photo/logoTest2.jpg'
with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        input = i.read()
        output = remove(input)
        o.write(output)