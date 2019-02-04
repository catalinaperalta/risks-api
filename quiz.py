from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABcTyknen0uRuE6ZF-VYlTNGXpYLlL0gwZhWQN18j7DSx0XUTPgb-Hhq58-yu5-yTkhhwUf2LWOc52M0dvsLQRF3YPsdh0nNNf9lF3poWxo5TjQSC0ahU5fRwHzGXDIDZnyo7mClO9c8p36jmMCzxThz2atg0fi5eUYpH7Gak5CM1tkWM4='

def main():
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    main()