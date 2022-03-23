my_str = '''Lorem ipsum dolor sit amet, consectetur adipiscing
elit. Mauris vulputate lacus id eros consequat tempus.
Nam viverra velit sit amet lorem lobortis, at tincidunt
nunc ultricies. Duis facilisis ultrices lacus, id
tiger123@email.cz auctor massa molestie at. Nunc tristique
fringilla congue. Donec ante diam cnn@info.com, dapibus
lacinia vulputate vitae, ullamcorper in justo. Maecenas
massa purus, ultricies a dictum ut, dapibus vitae massa.
Cras abc@gmail.com vel libero felis. In augue elit, porttitor
nec molestie quis, auctor a quam. Quisque b2b@money.fr
pretium dolor et tempor feugiat. Morbi libero lectus,
porttitor eu mi sed, luctus lacinia risus. Maecenas posuere
leo sit amet spam@info.cz. elit tincidunt maximus. Aliquam
erat volutpat. Donec eleifend felis at leo ullamcorper cursus.
Pellentesque id dui viverra, auctor enim ut, fringilla est.
Maecenas gravida turpis nec ultrices aliquet.
'''

def collect_emails(text):
    emails = []
    for i in text.split():
        if "@" in i:
            emails.append(i)
    return emails

def select_num_emails(emails):
    num_emails = []
    for email in emails:
        for character in email[:email.find("@")]:
            if character.isdigit():
                num_emails.append(email)
                break
    return num_emails

def extract_domains(emails):
    extract_domains = []
    for email in emails :
        extract_domains.append(email[email.find("@")+1:])
    return extract_domains


print(collect_emails(my_str))
print(select_num_emails(collect_emails(my_str)))
print(extract_domains(collect_emails(my_str)))

