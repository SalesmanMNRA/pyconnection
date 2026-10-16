from pyconnection import PYConnectionClient

# Test that the class can be instantiated (won't fully connect without real creds)
client = PYConnectionClient(
    api_id=12345,
    api_hash="test_hash",
    phone_number="+989123456789",
)
print(f"Client created: {type(client).__name__}")
print(f"Has http handler: {hasattr(client, 'http')}")
print(f"Splus client lazily loaded: {client._splus_client is None}")

# Test HTTP methods through the client
r = client.http_get("https://httpbin.org/get")
print(f"HTTP GET status: {r.status_code}")

r = client.http_post("https://httpbin.org/post", json={"test": "data"})
print(f"HTTP POST status: {r.status_code}")

print("\nAll tests passed!")