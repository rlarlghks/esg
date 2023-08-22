import requests

# import random
# print(random.randrange(1,10))
def main():
    # print('main function')
    response = requests.get("http://www.google.com/random-address/")
    # print("Status Code: ", response.status_code)
    # print(response)
    print(response.text)
    print(response.url)

if __name__ == "__main__":
    main()


