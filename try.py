

strs = ["asdf", "sdf", "asdfgg", "sdf"]


def longestCommonPrefix(self, strs):

    if len(strs) == 0:
        return ""

    prefix = strs[0]

    for i in range(1, len(strs)-1, 1):
        res = self.get_index(i, strs, prefix)
        while res != 0:
            prefix = prefix[:len(prefix)-1]
            res = self.get_index(i, strs, prefix)
            if prefix == "":
                return ""
    return prefix


res = longestCommonPrefix(strs)
print(res)


def get_index(self, i, strs, prefix):
    try:
        res = strs[i].index(prefix)
    except Exception as e:
        res -= 1

    return res
