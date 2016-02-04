def difference():
   n= input("Enter the value of n?")
   squ_sum = (n * (n + 1) / 2) ** 2
   sum_squ = n * (n + 1)*(2 * n + 1) / 6
   diff= squ_sum - sum_squ
   print diff
difference()
