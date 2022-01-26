




def create_list():
    list = []
    while True:
        item = input('Tell me what you want to add to your shopping list. ')
        if item.isalpha():
            list.append(item)
            print(f'{item} has been added to the list.')
            print(f'Here is your current list: {list}')
        else:
            print('invalid input, try again')
            continue
        
        active = True
        while active:
            decision = input('Enter 1 to add more items, 0 to delete an item, or quit to exit. ').lower()
            if decision == '1':
                break
            elif decision == '0':
                deleted = input(f'Please tell me the item you want to delete: {list} ')
                if deleted in list:
                    list.remove(deleted)
                    print(f'{deleted} has been deleted from your list. Here is your current list: {list}')
                else:
                    print(f'{deleted} not found in list.')
            elif decision == 'quit':
                print(f'Here is your final list: {list}')
                return
            else:
                print('invalid entry')


create_list()