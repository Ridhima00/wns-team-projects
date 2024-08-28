def block_website(website):
    hosts_path = "C:\\Windows\\System32\\drivers\\etc\\hosts"  # Use "C:\\Windows\\System32\\drivers\\etc\\hosts" for Windows.
    redirect_ip = "127.0.0.1"

    with open(hosts_path, 'r+') as file:
        content = file.read()
        if website not in content:
            file.write(redirect_ip + " " + website + "\n")
            print(f"{website} has been blocked.")
        else:
            print(f"{website} is already blocked.")

if __name__ == "__main__":
    website_to_block = "www.fnp.com"
    block_website(website_to_block)


