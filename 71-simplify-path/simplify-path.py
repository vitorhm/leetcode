class Solution:
    def simplifyPath(self, path: str) -> str:
        dir_list = []

        for s in path.split('/'):
            if not s or s == '.': continue
            if s == '..':
                if dir_list:
                    dir_list.pop()
            else:
                dir_list.append(s)

        return '/' + '/'.join(dir_list)