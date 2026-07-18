def read_csv_safe(filepath):
    try:
        with open(filepath, 'r') as f:
            return f.readlines()
    except FileNotFoundError:
        print(f'File not found: {filepath}')
        return []
    except PermissionError:
        print('Access denied.')
        return []
    except Exception as e:
        print(f'Unexpected: {e}')
        return []