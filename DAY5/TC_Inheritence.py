class Animal:
    def sound(self):
        print('animal sounds')


class dog(Animal):  
        def bark(self):
            print('dog barks')
 
class cat(Animal):
     def meow(self):
          print('cat meows')

s = dog()
s.sound()
s.bark()            

p = cat()
p.meow()