from euler.lib.mem import memoize


@memoize()
def A_recursive(m, n):
    if m == 0:
        return n + 1
    if n == 0:
        return A_recursive(m - 1, 1)
    return A_recursive(m - 1, A_recursive(m, n - 1))


def A(m, n):
    next = [0] * (m + 1)
    goal = [1] * (m + 1)
    goal[-1] = -1
    while True:
        value = next[0] + 1
        transferring = True
        m_current = 0
        while transferring:
            if next[m_current] == goal[m_current]:
                goal[m_current] = value
            else:
                transferring = False
            next[m_current] += 1
            m_current += 1
        if next[m] == n + 1:
            return value


def test():
    for m in xrange(0, 4 + 1):
        for n in xrange(0, 13 + 1):
            print 'A(%d, %d) = %s' % (m, n, A(m, n))


if __name__ == '__main__':
    test()
