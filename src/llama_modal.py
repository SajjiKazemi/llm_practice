import modal
from llama import app, generate

with modal.enable_output():
    with app.run():
        #result = generate.local("Life is a mystery, everyone must stand alone, I hear")
        result = generate.remote("Life is a mystery, everyone must stand alone, I hear")
print(result)