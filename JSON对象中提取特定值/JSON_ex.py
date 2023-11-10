import json  
  
try:  
    # 从txt文件中读取JSON数据  
    with open('poc.txt', 'r', encoding='utf-8') as file:  
        json_string = file.read()  
      
    # 由于所有的JSON对象在同一行，先将其分开  
    json_objects = json.loads("[" + json_string.replace('}{', '}, {') + "]")  
      
    # 提取processInstanceId  
    process_instance_ids = [obj['processInstanceId'] for obj in json_objects if 'processInstanceId' in obj]  
      
    # 将processInstanceId写入到一个新的txt文件  
    with open('output.txt', 'w', encoding='utf-8') as output_file:  
        for process_instance_id in process_instance_ids:  
            output_file.write(f"{process_instance_id}\n")  
      
    print("processInstanceIds have been written to 'output.txt'.")  
  
except FileNotFoundError:  
    print("The file 'poc.txt' was not found.")  
except json.JSONDecodeError:  
    print("There was an error decoding the JSON data.")  
except KeyError:  
    print("The key 'processInstanceId' was not found in one or more JSON objects.")  
except Exception as e:  
    print(f"An unexpected error occurred: {e}")