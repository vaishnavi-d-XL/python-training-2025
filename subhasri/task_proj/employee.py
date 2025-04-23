import json
# with open('employee.json','r') as f:
#     data=json.load(f) #read
#     print(data)


# json_str='{"name":"abi","dept":"ca","dept_id":"3"}'
# data=json.loads(json_str)  #in loads , s - refers string
# json_out=json.dumps(data)
# print(json_out)

def load_json(filename):
    with open(filename,'r') as f:
        return json.load(f)
    
def filter_by_dept(data,department):
    filtered=([emp for emp in data if emp.get("department")==department])
    return filtered

db=load_json("employee.json")
filtered_emp=filter_by_dept(db,"HR")
print(filtered_emp)


def avg_salary(data):
    sal=([emp.get("salary") for emp in data])
    avg=sum(sal)/len(data)
    return avg
print(avg_salary(db))

def assign_level(data):
    for emp in data:
        salary=emp.get("salary",0)
        if salary>100000:
            emp["level"]="Senior"
        else:
            emp["level"]="Junior"
    return data
print(assign_level(db))

def save_json(data,filename):
    with open(filename,"w") as f:
        json.dump(data,f,indent=4)
save_json(db,"employee.json")
