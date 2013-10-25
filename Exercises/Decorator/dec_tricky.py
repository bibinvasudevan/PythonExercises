def B(z):
  def C(a):
    def D(*args):
      return z * a(*args);
    return D
  return C

@B(2)
def A(x, y):
  return x + y;

print A(2, 3)
