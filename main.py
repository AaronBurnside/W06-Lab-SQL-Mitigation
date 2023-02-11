def main():
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    sql_query = create_sql_query(username, password)
    print(sql_query)
    for x in range(0,3): #loop throught the tests with each of the three levels of mitigation
        Valid_Query_Test(x)
        Tautology_Attack(x)
        UnionQuery_Attack(x)
        AdditionalStatement_Attack(x)
        Comment_Attack(x)
    return
  
	
def Valid_Query_Test(Sanitize):
    usernames = ["Burn_side123", ] #TODO Add your valid Username here
    passwords = ["That_Burnside_Password45", ] #TODO Add your Valid Password Here
    for x in range [0,3]:
        if Sanitize == 0: ## no Mitigation
            sql_query = create_sql_query(usernames[x], passwords[x])
            print(sql_query)
        if Sanitize == 1: # Weak Mitigation
            usernames[x] = weak_mitigation(usernames[x])
            passwords[x] = weak_mitigation(passwords[x])
            sql_query = create_sql_query(usernames[x], passwords[x])
            print(sql_query)
        if Sanitize == 2:
            usernames[x] = strong_mitigation(usernames[x])
            passwords[x] = strong_mitigation(passwords[x])
          	
    return


def Tautology_Attack(Sanitize):
    usernames = ["Burn_side123", ] ## Add your Username here
    passwords = ["nothing' OR 'X' = 'X", ] ## Add a Tautology Attack Here
    for x in range [0,3]:
        if Sanitize == 0: ## no Mitigation
            sql_query = create_sql_query(usernames[x], passwords[x])
            print(sql_query)
        if Sanitize == 1: # Weak Mitigation
            usernames[x] = weak_mitigation(usernames[x])
            passwords[x] = weak_mitigation(passwords[x])
            sql_query = create_sql_query(usernames[x], passwords[x])
            print(sql_query)
    return

def UnionQuery_Attack(Sanitize):
    usernames = ["Burn_side123", ] ## Add your Username here
    passwords = ["nothing' UNION SELECT Password FROM Table", ] ## Add a UnionQuery Attack Here
    for x in range [0,3]:
        if Sanitize == 0: ## no Mitigation
            sql_query = create_sql_query(usernames[x], passwords[x])
            print(sql_query)
        if Sanitize == 1: # Weak Mitigation
            usernames[x] = weak_mitigation(usernames[x])
            passwords[x] = weak_mitigation(passwords[x])
            sql_query = create_sql_query(usernames[x], passwords[x])
            print(sql_query)
    return

def AdditionalStatement_Attack(Sanitize):
    usernames = ["Burn_side123",     ] ## Add your Username here
    passwords = ["nothing'; INSERT INTO Table (Username, Password) VALUES 'Fake_Account', 'Fake_Password",     ] ## Add a UnionQuery Attack Here
    for x in range [0,3]:
        if Sanitize == 0: ## no Mitigation
            sql_query = create_sql_query(usernames[x], passwords[x])
            print(sql_query)
        if Sanitize == 1: # Weak Mitigation
            usernames[x] = weak_mitigation(usernames[x])
            passwords[x] = weak_mitigation(passwords[x])
            sql_query = create_sql_query(usernames[x], passwords[x])
            print(sql_query)
    return

def Comment_Attack(Sanitize):
    usernames = ["Burn_side123'; -- ", ] ## Add a valid comment attack Username here
    passwords = ["That_Burnside_Password45", ] ## Add your inValid Password Here
    for x in range [0,3]:
        if Sanitize == 0: ## no Mitigation
            sql_query = create_sql_query(usernames[x], passwords[x])
            print(sql_query)
        if Sanitize == 1: # Weak Mitigation
            usernames[x] = weak_mitigation(usernames[x])
            passwords[x] = weak_mitigation(passwords[x])
            sql_query = create_sql_query(usernames[x], passwords[x])
            print(sql_query)
    return

def create_sql_query(username_input, password_input):
    sql = ' SELECT * FROM Table WHERE Username = '
    sql = sql + username_input
    sql = sql + ' and Password = '
    sql = sql + password_input
    return sql


def weak_mitigation(user_input):
  # block list
  translation_table = dict.fromkeys(map(ord, ";'-"), None)
  sanitized_input = user_input.translate(translation_table)
  return sanitized_input


def strong_mitigation(user_input, allowed_inputs_list):
  # allow list
  for allowed_input in allowed_inputs_list:
    if user_input == allowed_input:
      return user_input
  
  return None


main()
