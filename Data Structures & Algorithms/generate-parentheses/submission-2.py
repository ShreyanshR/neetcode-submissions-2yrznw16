class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = []
        openp = 0
        closep = 0

        def dfs(openp, closep):
            if openp == n and closep == n:
                res.append("".join(cur))
                return

            if openp < n:
                cur.append("(")
                dfs(openp + 1, closep)
                cur.pop()

            if closep < openp:
                cur.append(")")
                dfs(openp, closep + 1)
                cur.pop()

        dfs(openp, closep)

        return res
