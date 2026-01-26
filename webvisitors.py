monday = {101, 102, 103, 104}
tuesday = {102, 104, 105, 106}
wednesday = {101, 106, 107}
unique_visitors = monday.union(tuesday).union(wednesday)
print("Unique visitors in 3 days:", unique_visitors)
print("Total unique visitors:", len(unique_visitors))