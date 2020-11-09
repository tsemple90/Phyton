class lion(object):#lion
  def __init__(self,*args):#lion1
    if len(args) > 1:#if
    #takes two return types
      self._name = args[0]
      self._color = args[1]
      self._size = 5
      self._height = 1
      self._food = "corn"

    elif len(args) == 1:#else if
    # take 1 type
      self._name = args[0]
      self._color = "brown"
      self._size = 7
      self._height = 2
      self._food = "tacos"

    

  @property
  def size(self):#get size
    return self._size
  @property
  def name(self):#get name
    return self._name
  @property
  def color(self):#get color
    return self._color
  @property
  def height(self):#get height
    return self._height
  @property
  def food(self):#get food
    return self._food
  @size.setter
  def size(self,x):#set size
    self._size = x
  @name.setter
  def name(self,x):#set name
    self._name = x
  @color.setter
  def color(self,x):#set color
    self._color = x
  @height.setter
  def height(self,x):#set height
    self._height = x
  @food.setter
  def food(self,x):#set food
    self._food = x


  def show(self):
    print(str(self._name) +" the mountain lion is "+str(self._color)+ ". The mountain lion is "+ str(self._size) +" cm big and it is "+str(self._height) +" cm long. His favorite food to eat is "+ str(self._food)+".\n")#sentence

lion1 = lion("Tyler", "blue")#first lion
lion1.show()#print
lion2= lion("Bob")#second lion
lion2.show()#print

#using setters and getters
lion1.size = 5
lion1.height = 30
lion1.food= "beef"
lion1.show()#print new sentence with new inputs

#using setters and getters
lion2.name="Hanana"
lion2.color="Pink"
lion2.size = 300
lion2.height = 3
lion2.food= "carrots"
lion2.show()#print new sentence with new inputs
