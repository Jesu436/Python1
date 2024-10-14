def main():
    try:
        configuration = open ( 'config.txt')
    except FileNotFoundError:
        print("Couldn`t fint the config.txt file!")
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn`t read it")
    except Exception as e:
        print(type(e))
    except PermissionError as e:
        print(e)

main()
