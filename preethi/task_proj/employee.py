import json
def load_json(filename):
    with open(filename,'r') as f:
        return json.load(f) 
def filter_by_department(data,department):
    filtered=([employee for employee in data if employee.get("department")==department])
    return filtered
db=load_json("employee.json")
#filtered_employees=filter_by_department(db,'Engineering')
#print(filtered_employees)
def avg_salary(data):
    ls=([emp.get("salary") for emp in data])
    avg=sum(ls)/len(data)
    return avg
#total=avg_salary(db)
#print(total)
def level(data):
    for emp in data:
        salary=emp.get("salary",0)
        if salary>100000:
            emp["level"]='senior'
        else:
            emp["level"]='mid'
    return data
new_data=level(db)
print(new_data)
def save_json(data,filename):
    with open(filename,'w') as f:
        json.dump(data,f,indent=4)
save_json(db,'employee.json')
