class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        path = path.split('/')
        real = []
        for p in path:
            if p=='.' or p=='':
                continue
            elif p=='..':
                if real:
                    del real[-1]
            else:
                real.append(p)
        return '/'+('/'.join(real))
