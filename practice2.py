# class Solution:
#     def HighestOccurence(self, logLines):
#         s = []
#         for log in logLines:
#             if "Error" in log:
#                 try:
#                     if int(log.split()[1]):
#                         s.append(log.split()[1])
#                 except ValueError:
#                     pass

#         return max(s, key=s.count)


# solution = Solution()
# print(solution.HighestOccurence(
#     ["Error 204 Message", "Error abc Message", "Error 204 message", "Error 104 Message", "Warning 203 message", "Info abc Message", "Warning 203 message", "Error 104 Message",  "Error 404 message", "Error 500 message",  "Error 204 message"]))
print(int("-2"))
