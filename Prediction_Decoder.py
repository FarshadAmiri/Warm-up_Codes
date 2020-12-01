def Prediction_decoder(p,n,first_variable,second_variable):
  # p = Prediction (Model Output)
  # n = Second variable starting indice (count from zero)
  # first_variable  = you should enter the column (ex. train_df.color) -  doesn't matter test or train
  # second_variable = you should enter the column (ex. train_df.marker) - doesn't matter test or train

  first = p[0][:n]
  second = p[0][n:]

  c1 = first_variable.unique() 
  c2 = second_variable.unique()
  c1.sort()
  c2.sort()

  d_first,d_second = {},{}
  n_first,n_second = 0,0

  for i in c1:
    d_first[n_first]= i
    n_first += 1
  for i in c2:
    d_second[n_second]= i
    n_second += 1
  for i in range(len(first)):
    if first [i] == 1:
      print(d_first[i])
  for i in range(len(second)):
    if second[i] == 1:
      print(d_second[i])

