import os


def clear_clutter(directory, extension):
    '''    files = os.listdir(directory)
    print(files)
    filtered_files = list(filter(lambda x: x[-4:] == extension, files))
    print(filtered_files)
    counter = 101
    for elem in filtered_files:
        source = f'{directory}\\{elem}'
        destination = f'{directory}\\{counter}.png'
        os.rename(source, destination)
        counter += 1
    print("Operation Successful")
    return'''
    files = os.listdir(directory)
    print(files)
    counter = 1101
    for elem in files:
        if elem.endswith('.png'):
            source = f'{directory}\\{elem}'
            destination = f'{directory}\\{counter}.png'
            os.rename(source, destination)
            counter += 1
    print("Operation Successful")
    return


clear_clutter("D:\AWS\Cloud Practitioner Certification", '.png')
print(os.listdir("D:\AWS\Cloud Practitioner Certification"))
