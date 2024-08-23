rows=[]
columns=[]
data_type=[]
file_path=input("Enter file path: ")
with open(file_path,"r") as reading:
    for line in reading:
        columns=line.strip().split(",")
        break
    for line in reading:
        values=line.strip().split(",")
        entry={}
        for i in range(len(columns)):
           entry[columns[i]]=values[i]
        rows.append(entry)

table_name=input("Enter the table name: ")
location=input("Enter the desired location: ")
location=location.replace("\\","//")
location+=("//"+table_name+".sql")
with open(location,"w") as writing:
    table="CREATE TABLE "
    table+=(table_name+"(")
    for i in range(len(columns)):
        type=" TEXT"
        if i!=len(columns)-1:
            type+=","
        table+=(columns[i]+type)
    table+=");\n"
    writing.write(table)


    for entries in rows:
        insert="INSERT INTO "+table_name+" VALUES("
        for i in range(len(columns)):
            data=columns[i]
            insert+=('"'+entries[data]+'"')
            if i!=len(columns)-1:
                insert+=","
        insert+=(");\n")
        writing.write(insert)