from datetime import date

def main():
    print("")
    print('--------------------------')
    print('HELLO WORLD!!!')
    print('ISS135 | UES | 2024')
    print(get_textual_date())
    print('--------------------------')
    print("")
    
def get_textual_date():
    return date.today().strftime("%B %d, %Y")
    
    
main()
