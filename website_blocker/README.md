Website Blocker Python Script
Project Background
This project is a simple Python script designed to block specific websites by modifying the system's hosts file. This is achieved by redirecting the website's URL to the local machine (127.0.0.1), effectively preventing access to the site. In this case, the script blocks the website www.fnp.com.

Blocking websites can be useful for various reasons, such as restricting access to distracting sites, protecting children from inappropriate content, or preventing access to harmful sites on shared or public computers.

How to Run the Code
Step 1: Prerequisites
Python: Make sure you have Python installed on your system. You can download it from the official Python website.
PyCharm: This example uses PyCharm as the Integrated Development Environment (IDE). You can download it from the official JetBrains website.
Step 2: Set Up the Project
Create a New Project:

Open PyCharm and create a new Python project.
Name your project (e.g., WebsiteBlocker).
Create a Python File:

Right-click on the project directory, select New > Python File.
Name the file block_website.py.
Copy the Code:

Paste the following code into your block_website.py file:
python
Copy code
def block_website(website):
    hosts_path = "C:\\Windows\\System32\\drivers\\etc\\hosts"  # Use /etc/hosts for macOS/Linux.
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
Step 3: Run the Script
Run PyCharm as Administrator:

Windows: Right-click on the PyCharm shortcut and select Run as administrator.
macOS/Linux: Run PyCharm with sudo or as root to ensure the script has the necessary permissions to modify the hosts file.
Execute the Script:

Click the green play button in PyCharm to run the script.
The script will block the website www.fnp.com.
Step 4: Verify the Block
Open Your Web Browser:
Navigate to www.fnp.com.
You should see a message that the site cannot be reached, indicating that it has been successfully blocked.
Step 5: Unblock the Website (Optional)
To unblock the website, manually edit the hosts file and remove the line containing 127.0.0.1 www.fnp.com.
Post-Run Example Screenshots with Commentary
Screenshot 1: Website Block Confirmation
Description: This screenshot shows the successful execution of the script in PyCharm. The output confirms that the website www.fnp.com has been blocked.
![Screenshot 2024-08-28 215912](https://github.com/user-attachments/assets/2d9c4d6c-2737-4e42-8d1d-f8f6d2cb46b4)

Screenshot 2: Blocked Website in Browser
Description: This screenshot shows the result when trying to access www.fnp.com in a web browser after running the script. The website is inaccessible, confirming the block is effective.
![Screenshot 2024-08-28 215647](https://github.com/user-attachments/assets/809aebf1-761d-4d53-8cd6-a93108a8d6ca)

Conclusion
This project demonstrates a simple yet effective way to block websites using Python. It’s a great starting point for learning about system-level modifications with Python and can be extended to include more sophisticated blocking mechanisms or user interfaces.

