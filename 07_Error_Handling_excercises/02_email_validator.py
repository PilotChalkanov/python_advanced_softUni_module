from errors import NameTooShortError,InvalidDomainError,MustContainAtSymbolError,InvalidDomainNameError

valid_domain = {'com', 'bg', 'org', 'net'}
line = input()
while line != 'End':
    email_parts = line.split('@')
    if len(email_parts) == 1:
        raise MustContainAtSymbolError('Email must contain @')
    name,domain_name = email_parts

    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    domain_name_parts = domain_name.split('.')
    if len(domain_name_parts)<2 or not all([len(x)>1 for x in domain_name_parts[0:len(domain_name_parts)-1]]) :
        raise InvalidDomainNameError("Invalid domain name")

    domain = domain_name_parts[-1]
    if domain not in valid_domain:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    print("Email is valid")
    line = input()
