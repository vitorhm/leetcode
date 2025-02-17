class Solution:
    def simplifyPath(self, path: str) -> str:
        dir_list = []
        dir_s = []

        for i in range(1, len(path) + 1):
            cur = '/' 
            if i < len(path):
                cur = path[i]

            if cur == '/':
                if dir_s:
                    dir_str = ''.join(dir_s) 
                    if dir_str == '..':
                        if dir_list:
                            dir_list.pop()
                    elif dir_str != '.':
                        dir_list.append(dir_str)
                
                dir_s = []
            else:
                dir_s.append(cur)

        return '/' + '/'.join(dir_list)
