class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l_one, r_one = 0, len(matrix) - 1
        l_two, r_two = 0, len(matrix[0]) - 1

        while l_one <= r_one:
            m_one = l_one + (r_one - l_one) // 2

            if matrix[m_one][0] <= target and matrix[m_one][-1] >= target:
                while l_two <= r_two:
                    m_two = l_two + (r_two - l_two) // 2

                    if matrix[m_one][m_two] == target: 
                        return True
                    elif matrix[m_one][m_two] < target: 
                        l_two = m_two + 1
                    elif matrix[m_one][m_two] > target: 
                        r_two = m_two - 1
                return False

            elif matrix[m_one][-1] < target:
                l_one = m_one + 1
            elif matrix[m_one][-1] > target:
                r_one = m_one - 1
        return False
                
