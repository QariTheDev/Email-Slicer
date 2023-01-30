def main():
    print("Welcome To The Email Slicer")
    print("---------------------------")
    email = input("Enter Your Email Address: ")

    (username, domain) = email.split('@')
    (domain, extension) = domain.split('.')

    print("Your Username Is: " + username)
    print("Your Domain Name Is: " + domain)
    print("Your Extension Is: " + extension)

main()