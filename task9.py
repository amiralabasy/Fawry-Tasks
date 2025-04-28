import ssl
import socket
from datetime import datetime

def get_ssl_expiry_date(hostname, port=443):
    context = ssl.create_default_context()
    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert()
            expiry_date_str = cert['notAfter']
            expiry_date = datetime.strptime(expiry_date_str, '%b %d %H:%M:%S %Y %Z')
            return expiry_date

# جرب على أي موقع
hostname = 'google.com'
try:
    expiry_date = get_ssl_expiry_date(hostname)
    print(f"The SSL certificate for {hostname} expires on {expiry_date}")
except Exception as e:
    print(f"Error: {e}")

