def main():
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    sql_query = create_sql_query(username, password)
    print(sql_query)
  

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
    if user_input = allowed_input:
      return user_input
  
  return None


main()