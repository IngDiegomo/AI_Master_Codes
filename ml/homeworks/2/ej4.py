def is_h_n(n,a,b,x):
  if(n == b*(b-1)/2 + a + 1):
    print(f"h{n}", a, "<=", x, "<", b)
  return n == b*(b-1)/2 + a + 1

s_x = [0, 3, 2]
limit = 20
skip_outer_loop = False
for n in range (1,limit): # para cada hipotesis (vamos a limitarlo a 20)
  for i, x in enumerate(s_x): # para cada elemento x del  conjunto de entrenamiento
    for a in range(0, x + 1): # para cada a menor o igual que x
      for b in range(x + 1, limit + 1): # para cada b mayor que x (limitado hasta 20)
        comply_with_h_n = is_h_n(n,a,b,x) # prueba si la hipotesis contiene dicho punto