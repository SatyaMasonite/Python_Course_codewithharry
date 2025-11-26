def multi_table(table):
        #  print(f"{table}*{i}={i*table}")
        table2=''
        for i in range(1,11):
            
            table2 += (f"{table}*{i} = {i*table}\n") 
        with open(f"{table}_table","w") as f:
              f.write(table2)


multi_table(3)
