
import allure
import json 
def allure_log(text):
    with allure.step(text):
        pass

# def allure_json(text, json):
#     with allure.step(f'''{text} <pre 
#         style="background-color: black;
#         color: #ffff; padding: 10px; border-radius: 5px;
#     ">json</pre>'''):
#         pass

def allure_json(text, json_body):
    allure.attach(f'''<pre 
        style="background-color: black;
        color: #ffff; padding: 10px; border-radius: 5px;
    ">{json.dumps(json_body, indent=4)}</pre>''', name=text, attachment_type=allure.attachment_type.HTML)
  
        
