from db.run_sql import run_sql

def fetch_content(description):
    sql = 'SELECT * FROM cover_letter_data WHERE description = %s'
    values = [description]
    results = run_sql(sql, values)[0][2]
    print(results)
    return results

def build_content(arr):
    content = ''
    for item in arr:
        content = content + str(fetch_content(item)) + '\n \n'
    return content
    

def write_cover_letter():
    save_as = input('Enter the name of the file to save as:\n')
    company_name = input('Enter the name of the company:\n')
    position = input('Enter the position you are applying for:\n')
    languages_frameworks = input('Enter the languages and frameworks you are familiar with in the form of a sentance (eg. \'JavaScript, Python and Java\'):\n')
    terms = input('Enter the languages/frameworks you want to search for: ').lower().split()
    your_name = input('Enter your name: ')

    with open(f'letters/{save_as}.txt', 'w') as f:
        f.write('Hello \n \n')
        f.write(f'I am writing to apply for the {position} position at {company_name}. \n \n')
        f.write(f'I have experience with {languages_frameworks} and I am confident that I can make a valuable contribution to your team. \n \n')
        f.write(f'{build_content(terms)}\n \n')
        f.write(f'I look forward to hearing from you. \n')
        f.write(f'Kind regards, \n')
        f.write(f'{your_name}')

def add_content():
    description = input('Enter the name of the content: ')
    data = input('Enter the content: ')
    sql = 'INSERT INTO cover_letter_data (description, data) VALUES (%s, %s)'
    values = [description, data]
    run_sql(sql, values)
    
while True:
    choice = input('Would you like to build a cover letter or add content for a new one? (b/a) ')
    if choice == 'b':
        write_cover_letter()
    elif choice == 'a':
        add_content()
    elif choice == 'q':
        break
    else:
        print('Invalid input. Please try again.')