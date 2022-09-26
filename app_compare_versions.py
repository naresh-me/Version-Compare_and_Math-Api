from sys import exit
import time


class CompareVersions:
    def compare(self, ver1, ver2):
        ver1 = [int(n) for n in ver1.split(".")]
        ver2 = [int(n) for n in ver2.split(".")]
        for i in range(max(len(ver1), len(ver2))):
            v1 = ver1[i] if i < len(ver1) else 0
            v2 = ver2[i] if i < len(ver2) else 0
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        return 0


print(CompareVersions().compare("1.2.9.9.9.9", "1.2.9.9.8.9"))
time.sleep(5)
exit()
