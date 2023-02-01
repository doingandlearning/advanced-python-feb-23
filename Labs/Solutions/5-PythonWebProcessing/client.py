from requests import get

result = get("http://localhost:8001/fib")
print(result.content)

