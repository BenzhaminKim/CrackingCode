def urlFy(url):
    url_arr = url.split()
    
    return "%20".join(url_arr)

if __name__ == "__main__":
    print(urlFy('hi my name is Ben'))