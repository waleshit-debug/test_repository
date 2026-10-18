path = '/Users/mike/Documents/Notes/tasks.md	'
if '/' in path:
   word = path.split('/')[-1]
elif "\\" in path:
    word = path.split('\\')[-1]

length = len(path)-len(word)
print(path[:length])

# def strip_filename(path):
#     if len(path) < 2: return path
#     splitters = ['\\', '/']
#     for splitter in splitters:
#         if splitter in path:
#             file_part = path.split(splitter)[-1]
#             return path[:-len(file_part)]
#     return path
#
#
# user_path = input()
# print(strip_filename(user_path))