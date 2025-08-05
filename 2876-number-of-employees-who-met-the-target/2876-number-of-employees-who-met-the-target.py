from typing import List

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        """
        Count how many employees have worked at least `target` hours.

        Parameters
        ----------
        hours : List[int]
            A list where each element represents the number of hours an employee has worked.
        target : int
            The minimum required number of hours for an employee to be considered as having met the target.

        Returns
        -------
        int
            The count of employees whose worked hours are greater than or equal to `target`.
        """
        # Using a simple list comprehension and len() is concise,
        # but a loop can be slightly faster for very large lists.
        return sum(1 for h in hours if h >= target)

