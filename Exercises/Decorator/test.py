a_string = "This is a global variable"
def foo():
     a_string = "test" # 1
     print locals()
foo()
#The out put of locals() is {'This is a_string': 'test'}
