import google.generativeai as genai

genai.configure(api_key="AIzaSyAenNcHpDXPUpVtsPydh1upF4ZvIAMsQbQ")

for m in genai.list_models():
    print(m.name)
