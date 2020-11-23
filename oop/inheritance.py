# inheriting object class as of pre 2.2 version

class BaseX(object):
    def __init__(self): # you must have to pass self whether you use it or not
        print("BaseX created")   

# POP = BaseX()

# note: after 2.2 version release we dont need to explicitly write something


# inheriting class

class A:
    def __init__(self):
        print("class A") # -> class A on call class A

class B(A):
    def __init__(self):
        print("class B") # -> class A on call class A

# a = A()

# b = B()

# note there is a notable difference in constructor calling from anyother languages like java, dart etc.
# if we make an object of child class that will not automatically call parent class


# super constructor

class Father:
    def __init__(self, fname):
        self.fname = fname
        print("triggered")

class Son(Father):
    def __init__(self, sname, careof):
        self.sname = sname
        super().__init__(careof)    # when we called super().init only then the parent constructor invoked/trigerred

jim = Son("jim", "jolly")

print(jim.fname)
print(jim.sname)

