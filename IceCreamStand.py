import resturant

tamberma = resturant.Resturant('Tamberma', 'African')
tamberma.describe_resturant()
tamberma.open_resturant()
print('\n')
coldstone = resturant.IceCreamStand('Cold Stone Creamery')
coldstone.flavors = ['vanilla','chocolate','strawberry','mint']
coldstone.describe_resturant()
coldstone.available_flavors()