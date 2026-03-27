import json

# Given JSON string
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

# Step 1: Load JSON string into Python dictionary
data = json.loads(sampleJson)

# Step 2: Access the nested "salary" key
salary = data["company"]["employee"]["payable"]["salary"]
print("Salary:", salary)

# Step 3: Add "birth_date" key to employee
data["company"]["employee"]["birth_date"] = "1995-06-15"

# Step 4: Save modified JSON to a file
with open("modified_data.json", "w") as file:
    json.dump(data, file, indent=4)

print("Modified JSON saved to 'modified_data.json'")