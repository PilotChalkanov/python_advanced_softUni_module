    def find_user(company:dict, user: str):
        for user_list in company.values():
            if user in user_list:
                return True
        return False
    def remove_user(company: dict, user:str):
        for side, force_users in company.items():
            if user in force_users:
                company[side].remove(user)
    line = input()
    company = {}
    while not line == 'Lumpawaroo':
        if '|' in line:
            force_side, force_user = line.split(' | ')
            if force_side not in company:
                company[force_side]= set()
                company[force_side].add(force_user)
            company[force_side].add(force_user)

        elif "->" in line:
            force_user, force_side = line.split(' -> ')
            if not find_user(company, force_user) and force_side not in company:
                company[force_side] = set()
                company[force_side].add(force_user)
                print(f"{force_user} joins the {force_side} side!" )
            elif force_side not in company and find_user(company, force_user):
                company[force_side] = force_user
                remove_user(company, force_user)
                print(f"{force_user} joins the {force_side} side!")
            elif force_side in company and not find_user(company, force_user):
                company[force_side].add(force_user)
                print(f"{force_user} joins the {force_side} side!")
            elif force_side in company and find_user(company, force_user) and force_user not in company[force_side]:
                remove_user(company, force_user)
                company[force_side].add(force_user)

                print(f"{force_user} joins the {force_side} side!")

        line = input()

    sorted_company = sorted(company.items(), key=lambda x: (-len(x[1]), x[0]))
    for k,v in sorted_company:
        if len(v)>0:
            print(f"Side: {k}, Members: {len(v)}")
            for el in sorted(v):
                print(f"! {el}")

